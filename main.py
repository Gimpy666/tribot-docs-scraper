#!/usr/bin/env python3
"""
Main script to run the Tribot JavaDoc scraper
"""

import argparse
import sys
import io
from scraper import TribotDocScraper
from urls import TEST_URL, TRIBOT_URLS
from tqdm import tqdm

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Scrape Tribot JavaDoc pages')
    parser.add_argument('--test', action='store_true', 
                       help='Run test with single URL only')
    parser.add_argument('--all', action='store_true', 
                       help='Scrape all Tribot API URLs (default behavior)')
    parser.add_argument('--output', default='scraped_docs',
                       help='Output directory for scraped content')
    parser.add_argument('--delay', type=float, default=1.0,
                       help='Delay between requests in seconds')
    
    args = parser.parse_args()
    
    # Default to --all if no arguments provided
    if not args.test and not args.all:
        args.all = True
    
    scraper = TribotDocScraper()
    scraper.delay = args.delay
    
    if args.test:
        print("🧪 Running test with ActionableQuery page...")
        result = scraper.scrape_page(TEST_URL)
        
        if result['success']:
            print("✅ Test successful!")
            print(f"Title: {result['metadata'].get('title', 'N/A')}")
            print(f"Class: {result['metadata'].get('class_name', 'N/A')}")
            print(f"Package: {result['metadata'].get('package', 'N/A')}")
            print(f"Content length: {len(result['content'])} characters")
            
            scraper.save_results([result], args.output)
            print(f"Test result saved to {args.output}/")
        else:
            print(f"❌ Test failed: {result.get('error', 'Unknown error')}")
    
    else:  # args.all or default
        print(f"🚀 Scraping all {len(TRIBOT_URLS)} Tribot API URLs...")
        print(f"Output directory: {args.output}")
        print(f"Delay between requests: {args.delay}s")
        print("This will create both individual files and a consolidated file.")
        print("")
        
        results = []
        for url in tqdm(TRIBOT_URLS, desc="Scraping pages"):
            result = scraper.scrape_page(url)
            results.append(result)
        
        # Save all results
        scraper.save_results(results, args.output)
        
        # Print summary
        successful = len([r for r in results if r['success']])
        failed = len([r for r in results if not r['success']])
        
        print(f"\n📊 Scraping Summary:")
        print(f"✅ Successful: {successful}")
        print(f"❌ Failed: {failed}")
        print(f"📁 Individual files saved to: {args.output}/")
        print(f"📄 Consolidated file: {args.output}/ALL_TRIBOT_DOCS.md")
        
        if failed > 0:
            print(f"\n❌ Failed URLs:")
            for result in results:
                if not result['success']:
                    print(f"  - {result['url']}: {result.get('error', 'Unknown error')}")


if __name__ == "__main__":
    main()
