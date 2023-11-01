import requests
import re
import pprint
class HayStack:
    def __init__(self, url, depth = 3):
        self.depth = depth
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'XY'})
        self.word_re = re.compile(r'[A-z|\']+')
        self.url_re = re.compile(r'href *= *"[^"]*"')
        self.index = {}
        self.graph = {}
        self.ranks = {}
        self.crawl(url)
        self.compute_ranks(self.graph)

    def lookup(self, word):
        word = word.lower()
        result = []
        if word in self.index:
            url_rank_pairs = [(url, self.ranks[url]) for url in self.index[word]]
            url_rank_pairs.sort(key=lambda pair: pair[1], reverse=True)
            result = [pair[0] for pair in url_rank_pairs]
        return result

    def crawl(self, url, depth=0):
        if depth == self.depth:
            return

        content = self.session.get(url).text

        text = re.sub(r'<[^>]*>|\t|\n|&[a-z]*;', ' ', content)
        words = self.word_re.findall(text)
        for word in words:
            word = word.lower()
            if word not in self.index:
                self.index[word] = [url]
            elif url not in self.index[word]:
                self.index[word].append(url)

        found_urls = self.url_re.findall(content)
        page_urls = set()
        for item in found_urls:
            new_url = item.split('"')[1]
            if new_url not in page_urls:
                page_urls.add(new_url)
        self.graph[url] = page_urls

        for item in page_urls:
            if item not in self.graph:
                self.crawl(item, depth - 1)

    def compute_ranks(self, graph):
        d = 0.85 # probability that surfer will bail
        numloops = 10
        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages
        for i in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for url in graph:
                    if page in graph[url]: # this url links to page
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        self.ranks = ranks

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