#!/usr/bin/env python3
"""
Tribot JavaDoc Scraper

This script scrapes JavaDoc pages from the Tribot API documentation
and converts them to well-formatted markdown for LLM consumption.
"""

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import time
import re
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Optional
import json
from pathlib import Path


class TribotDocScraper:
    def __init__(self, base_url: str = "https://runeautomation.com/docs/sdk/javadocs/"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.delay = 1  # Delay between requests to be respectful
        
    def scrape_page(self, url: str) -> Dict[str, str]:
        """
        Scrape a single JavaDoc page and return structured content.
        
        Args:
            url: The URL to scrape
            
        Returns:
            Dictionary containing the scraped content and metadata
        """
        try:
            print(f"Scraping: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract the main content
            content = self._extract_content(soup)
            
            # Extract metadata
            metadata = self._extract_metadata(soup, url)
            
            return {
                'url': url,
                'content': content,
                'metadata': metadata,
                'success': True
            }
            
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return {
                'url': url,
                'content': '',
                'metadata': {},
                'success': False,
                'error': str(e)
            }
    
    def _extract_content(self, soup: BeautifulSoup) -> str:
        """Extract the main content from the JavaDoc page."""
        
        # Remove navigation and header elements
        for element in soup.find_all(['nav', 'header', 'footer']):
            element.decompose()
            
        # Remove script and style elements
        for element in soup.find_all(['script', 'style']):
            element.decompose()
            
        # Find the main content area
        main_content = soup.find('div', class_='contentContainer') or soup.find('div', class_='mainContent')
        
        if not main_content:
            # Fallback to body if no specific content container found
            main_content = soup.find('body')
            
        if not main_content:
            return "No content found"
            
        # Clean up the content
        self._clean_content(main_content)
        
        # Convert to markdown
        markdown_content = md(str(main_content), heading_style="ATX")
        
        # Post-process the markdown for better formatting
        markdown_content = self._post_process_markdown(markdown_content)
        
        return markdown_content
    
    def _clean_content(self, element):
        """Clean up HTML content before conversion."""
        # Remove empty paragraphs
        for p in element.find_all('p'):
            if not p.get_text(strip=True):
                p.decompose()
                
        # Clean up class names and IDs that might clutter the output
        for tag in element.find_all():
            # Remove class and id attributes that are just for styling
            if 'class' in tag.attrs:
                classes = tag.attrs['class']
                # Keep only meaningful classes
                meaningful_classes = [cls for cls in classes if cls not in ['clear', 'spacer', 'skipNav']]
                if meaningful_classes:
                    tag.attrs['class'] = meaningful_classes
                else:
                    del tag.attrs['class']
                    
            if 'id' in tag.attrs and tag.attrs['id'].startswith('skip'):
                del tag.attrs['id']
    
    def _post_process_markdown(self, markdown: str) -> str:
        """Post-process markdown for better readability."""
        lines = markdown.split('\n')
        processed_lines = []
        
        for line in lines:
            # Remove excessive whitespace
            line = re.sub(r'\s+', ' ', line.strip())
            
            # Fix code blocks
            if line.startswith('```') and not line.endswith('```'):
                line = line + '```'
                
            # Clean up empty lines
            if line or (processed_lines and processed_lines[-1]):
                processed_lines.append(line)
        
        # Join lines and clean up
        result = '\n'.join(processed_lines)
        
        # Remove multiple consecutive empty lines
        result = re.sub(r'\n\s*\n\s*\n', '\n\n', result)
        
        return result.strip()
    
    def _extract_metadata(self, soup: BeautifulSoup, url: str) -> Dict[str, str]:
        """Extract metadata from the page."""
        metadata = {
            'title': '',
            'class_name': '',
            'package': '',
            'description': ''
        }
        
        # Extract title
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = title_tag.get_text(strip=True)
            
        # Extract class name from URL
        path = urlparse(url).path
        class_name = Path(path).stem
        metadata['class_name'] = class_name
        
        # Extract package information
        package_tag = soup.find('div', class_='subTitle')
        if package_tag:
            metadata['package'] = package_tag.get_text(strip=True)
            
        # Extract description (first paragraph in content)
        content_div = soup.find('div', class_='contentContainer')
        if content_div:
            first_p = content_div.find('p')
            if first_p:
                metadata['description'] = first_p.get_text(strip=True)[:200] + "..."
        
        return metadata
    
    def scrape_multiple_pages(self, urls: List[str]) -> List[Dict[str, str]]:
        """
        Scrape multiple pages with rate limiting.
        
        Args:
            urls: List of URLs to scrape
            
        Returns:
            List of scraped content dictionaries
        """
        results = []
        
        for i, url in enumerate(urls):
            result = self.scrape_page(url)
            results.append(result)
            
            # Rate limiting
            if i < len(urls) - 1:  # Don't delay after the last request
                time.sleep(self.delay)
                
        return results
    
    def save_results(self, results: List[Dict[str, str]], output_dir: str = "scraped_docs"):
        """Save scraped results to files."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Save individual files
        successful_results = []
        for result in results:
            if not result['success']:
                continue
                
            class_name = result['metadata'].get('class_name', 'unknown')
            filename = f"{class_name}.md"
            filepath = output_path / filename
            
            # Create markdown content
            content = f"# {result['metadata'].get('title', class_name)}\n\n"
            content += f"**URL:** {result['url']}\n\n"
            content += f"**Package:** {result['metadata'].get('package', 'N/A')}\n\n"
            
            if result['metadata'].get('description'):
                content += f"**Description:** {result['metadata']['description']}\n\n"
            
            content += "---\n\n"
            content += result['content']
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            successful_results.append(result)
        
        # Create consolidated file with all pages
        if successful_results:
            consolidated_content = self._create_consolidated_file(successful_results)
            consolidated_path = output_path / "ALL_TRIBOT_DOCS.md"
            with open(consolidated_path, 'w', encoding='utf-8') as f:
                f.write(consolidated_content)
            print(f"Consolidated file created: {consolidated_path}")
                
        # Save summary
        summary = {
            'total_urls': len(results),
            'successful': len([r for r in results if r['success']]),
            'failed': len([r for r in results if not r['success']]),
            'results': results
        }
        
        with open(output_path / 'scraping_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
            
        print(f"Results saved to {output_path}")
        print(f"Individual files: {len(successful_results)}")
        print(f"Consolidated file: ALL_TRIBOT_DOCS.md")
    
    def _create_consolidated_file(self, results: List[Dict[str, str]]) -> str:
        """Create a single consolidated file with all scraped content."""
        consolidated = []
        
        # Add header
        consolidated.append("# Tribot API Documentation - Complete Reference")
        consolidated.append("")
        consolidated.append("This file contains all scraped Tribot API documentation pages.")
        consolidated.append(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        consolidated.append(f"Total pages: {len(results)}")
        consolidated.append("")
        consolidated.append("---")
        consolidated.append("")
        
        # Add table of contents
        consolidated.append("## Table of Contents")
        consolidated.append("")
        for i, result in enumerate(results, 1):
            class_name = result['metadata'].get('class_name', 'unknown')
            title = result['metadata'].get('title', class_name)
            consolidated.append(f"{i}. [{class_name}](#{class_name.lower()}) - {title}")
        consolidated.append("")
        consolidated.append("---")
        consolidated.append("")
        
        # Add each page's content
        for result in results:
            class_name = result['metadata'].get('class_name', 'unknown')
            title = result['metadata'].get('title', class_name)
            
            # Add page separator and header
            consolidated.append(f"## {class_name}")
            consolidated.append("")
            consolidated.append(f"**Full Title:** {title}")
            consolidated.append("")
            consolidated.append(f"**URL:** {result['url']}")
            consolidated.append("")
            consolidated.append(f"**Package:** {result['metadata'].get('package', 'N/A')}")
            consolidated.append("")
            
            if result['metadata'].get('description'):
                consolidated.append(f"**Description:** {result['metadata']['description']}")
                consolidated.append("")
            
            consolidated.append("---")
            consolidated.append("")
            
            # Add the main content
            consolidated.append(result['content'])
            consolidated.append("")
            consolidated.append("---")
            consolidated.append("")
        
        return "\n".join(consolidated)


def main():
    """Main function to run the scraper."""
    from urls import TRIBOT_URLS
    
    scraper = TribotDocScraper()
    
    print(f"🚀 Starting to scrape all {len(TRIBOT_URLS)} Tribot API URLs...")
    print("This will take several minutes due to rate limiting...")
    print("")
    
    # Scrape all URLs
    results = scraper.scrape_multiple_pages(TRIBOT_URLS)
    
    # Save all results
    scraper.save_results(results, "scraped_docs")
    
    # Print summary
    successful = len([r for r in results if r['success']])
    failed = len([r for r in results if not r['success']])
    
    print(f"\n📊 Scraping Summary:")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Individual files saved to: scraped_docs/")
    print(f"📄 Consolidated file: scraped_docs/ALL_TRIBOT_DOCS.md")
    
    if failed > 0:
        print(f"\n❌ Failed URLs:")
        for result in results:
            if not result['success']:
                print(f"  - {result['url']}: {result.get('error', 'Unknown error')}")


if __name__ == "__main__":
    main()
