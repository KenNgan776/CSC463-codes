import requests
from bs4 import BeautifulSoup
import time  


# Function to crawl a website and extract links
def crawl(url):
    print(f"Crawling: {url}")
    time.sleep(20)  # Add a delay of 20 seconds so that you can see job running in dashboard
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if link.startswith('http'):
            links.add(link)
    return links


# List of URLs to crawl
urls_to_crawl = [
    "https://spotify.com", 
    "https://bofa.com", 
    "https://google.com", 
    "https://facebook.com", 
    "https://amazon.com", 
    "https://netflix.com", 
    "https://chase.com", 
    "https://wikipedia.org", 
    "https://github.com", 
    "https://apple.com"
]

# Crawl each URL sequentially
results = [crawl(url) for url in urls_to_crawl]


# Collect all unique links from the results
all_links = set()
for result in results:
    all_links.update(result)

# Print the final list of all crawled links
print(f"All crawled links: {all_links}")
