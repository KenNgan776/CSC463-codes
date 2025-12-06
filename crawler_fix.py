import requests
from bs4 import BeautifulSoup
import time
import ray

ray.init(ignore_reinit_error=True, runtime_env={"pip": ["beautifulsoup4","requests"]})


# Function to crawl a website and extract links
@ray.remote
def crawl(url):
    print(f"Crawling: {url}")
    time.sleep(20)  # Add a delay of 20 seconds so that you can see job running in dashboard
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            if link.startswith('http'):
                links.add(link)
        return links
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return set()

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

futures = [crawl.remote(url) for url in urls_to_crawl]

# Crawl each URL sequentially
results = ray.get(futures)


# Collect all unique links from the results
all_links = set()
for result in results:
    all_links.update(result)

# Print the final list of all crawled links
print(f"All crawled links ({len(all_links)}):")
for link in all_links:
    print(link)
