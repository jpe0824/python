import re
import requests
import pprint
from urllib.parse import urljoin

class HayStack:
    def __init__(self, url, depth=3):
        self.url = url
        self.depth = depth
        self.index = {}
        self.graph = {}
        self.ranks = {}
        self.crawl(url)
        self.compute_ranks(self.graph)

    def crawl(self, url, depth=0):
        if depth == self.depth:
            return
        content = requests.get(url, headers={"User-Agent": "XY"}).text
        found_urls = re.findall('<a href="(.*?)"', content)
        words = re.findall(r'\b\w+\b', re.sub('<[^<]+?>', '', content))

        for word in words:
            word = word.lower()
            if word.isdigit() and len(word) == 1 or word == '':
                continue  # Skip single-digit numbers and empty strings
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(url)

        for found_url in found_urls:
            if not found_url.startswith('http'):
                absolute_url = urljoin(url, found_url)
            else:
                absolute_url = found_url
            if url not in self.graph:
                self.graph[url] = set()
            self.graph[url].add(absolute_url)
            self.crawl(absolute_url, depth + 1)

    def compute_ranks(self, graph):
        d = 0.85     # probability that surfer will bail
        numloops = 10

        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages

        for _ in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for url in graph:
                    if page in graph[url]:  # this url links to page
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        self.ranks = ranks

    def lookup(self, keyword):
        keyword = keyword.lower()
        if keyword in self.index:
            return sorted(self.index[keyword], key=lambda url: self.ranks[url], reverse=True)
        return []

if __name__ == '__main__':
    engine = HayStack('http://roversgame.net/cs3270/page1.html',4)
    for w in ['pages','links','you','have','I']:
        print(w)
        pprint.pprint(engine.lookup(w))
    print()
    print('index:')
    pprint.pprint(engine.index)
    print()
    print('graph:')
    pprint.pprint(engine.graph)
    print()
    print('ranks:')
    pprint.pprint({page:round(rank,4) for page,rank in engine.ranks.items()})