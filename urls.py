"""
URL list for RuneLite JavaDoc scraping
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL for RuneLite API docs
BASE_URL = "https://static.runelite.net/runelite-api/apidocs/"

# Test URL - Client class
TEST_URL = "https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Client.html"

# Index URL for discovering all classes
OVERVIEW_TREE_URL = "https://static.runelite.net/runelite-api/apidocs/overview-tree.html"


def discover_runelite_urls():
    """
    Discover all RuneLite API class URLs from the overview-tree.html page.
    
    Returns:
        List of URLs to RuneLite API class documentation pages
    """
    print("Discovering RuneLite API URLs from overview-tree.html...")
    
    try:
        response = requests.get(OVERVIEW_TREE_URL, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links that point to class documentation
        # Exclude navigation links, package links, and other non-class pages
        excluded_patterns = [
            'index', 'overview', 'deprecated', 'help-doc', 'package-',
            'stylesheet', 'script', 'jquery', 'allclasses', 'tree'
        ]
        
        urls = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Skip excluded patterns
            if any(pattern in href for pattern in excluded_patterns):
                continue
            
            # Only include .html files that look like class documentation
            # (they should have a path structure like net/runelite/api/ClassName.html)
            if href.endswith('.html') and '/' in href and not href.startswith('http'):
                full_url = urljoin(BASE_URL, href)
                urls.append(full_url)
        
        # Remove duplicates and sort
        urls = sorted(list(set(urls)))
        
        print(f"Discovered {len(urls)} RuneLite API URLs")
        return urls
        
    except Exception as e:
        print(f"Error discovering URLs: {str(e)}")
        print("Warning: Falling back to empty list. You may need to manually populate RUNELITE_URLS.")
        return []


# Discover URLs automatically
# This will be populated when the module is imported
RUNELITE_URLS = discover_runelite_urls()

# If discovery fails or returns empty, you can manually add URLs here
# Example:
# RUNELITE_URLS = [
#     "https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Client.html",
#     "https://static.runelite.net/runelite-api/apidocs/net/runelite/api/Player.html",
#     # ... more URLs
# ]
