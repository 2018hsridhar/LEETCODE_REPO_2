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
'''
URL = https://leetcode.com/problems/web-crawler/
1236. Web Crawler
{ protocol, hostname, port, route }

Intuition and Approach :
- crawl all links under same hostname ( startUrl ) 
- crawler returns any order :-)
- each webpage has a set of URLs ( think wikipedia )
- the trailing "/" URL edge case
- most web crawlers are std graph algos in the hiding
- good applied question :-)

Complexity
V = #-nodes
E = #-edges
T = O(V + E)
S = O(V) ( Implicit ) O(V) ( Explicit ) 
'''
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        crawlerResults = set()
        # hostname = self.getHostnameFromUrl(startUrl)
        # print(hostname)
        crawlerResults.add(startUrl)
        self.executeWebCrawlerDFS(startUrl, htmlParser, crawlerResults)
        ans = list(crawlerResults)
        return ans

    def executeWebCrawlerDFS(self, parentURL:str, htmlParser: 'HtmlParser', results:set()) -> None:
        urlsOnPage = htmlParser.getUrls(parentURL)
        parentHostname = self.getHostnameFromUrl(parentURL)
        for childURL in urlsOnPage:
            if(childURL not in results):
                childHostname = self.getHostnameFromUrl(childURL)
                if(parentHostname == childHostname):
                    results.add(childURL)
                    self.executeWebCrawlerDFS(childURL, htmlParser, results)

    def getHostnameFromUrl(self, url:str) -> str:
        hostname = ""
        protocol = "http://"
        notProtocol = url[len(protocol):]
        delimeter = "/"
        # avoid ValueError : use -1
        firstDelimIndex = notProtocol.find(delimeter)
        hostname = notProtocol
        if(firstDelimIndex != -1):
            hostname = notProtocol[:firstDelimIndex]
        return hostname



        
