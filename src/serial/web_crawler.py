# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        host = self.extractHost(startUrl)
        visit = set()
        self.traverse(startUrl, host, htmlParser, visit)
        return list(visit)

    def traverse(self, url, host, htmlParser, visit):
        if host != self.extractHost(url) or url in visit:
            return
        visit.add(url)
        children = htmlParser.getUrls(url)
        for child in children:
            self.traverse(child, host, htmlParser, visit)
    
    def extractHost(self, url):
        
        if url.startswith('https://'):
            pos = 8
        else:
            pos = 7
        host = []
        while pos < len(url) and url[pos] not in {':', '/'}:
            host.append(url[pos])
            pos += 1
        return ''.join(host)
