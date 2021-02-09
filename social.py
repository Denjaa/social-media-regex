"""
The main idea of this code is to extract all the social media URL's
that brand or company is registered on and have re-location to
"""

import re
import requests
import io

webs = ['https://deepfriedpeanut.com','https://acajunlife.com', 'https://padronflooring.com/', 'https://www.adappersandlapper.com/', 'https://adozencousins.com/', 'https://agood.com/', 'https://ahouselikethis.com']

class GetSocialMedia:

    def __init__(self, webs):
        self.fOut = dict()
        self.webs = webs
        self.pattern = re.compile(r'http(s)?://(www)?[.]?(facebook|instagram|pinterest|twitter|youtube)\.(com|ca)\/(user|chanel|channel|in)?([^plugins][^tr][^0-9]{4})[/]?\w*', re.IGNORECASE)
        self.setter = set()

    def main(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
        self.headers = { 'User-Agent' : self.user_agent }

        for web in self.webs:
            self.temporary = []
            self.response = requests.get(web, headers = self.headers)
            self.content = str(self.response.text)
            self.matches = self.pattern.finditer(self.content)

            for match in self.matches:
                if match[0] not in self.temporary:
                    self.temporary.append(match[0])
            self.fOut[web] = self.temporary

        for k, v in self.fOut.items():
            print ('\n')
            if v != []:
                print (k, ' >> ', v)
                print ('-' * 50)

GetSocialMedia(webs = webs).main()
