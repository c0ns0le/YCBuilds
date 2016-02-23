'''
    Istream
    Oneclickwatch
    Copyright (C) 2013 Coolwave

    version 0.1

'''


from entertainment.plugnplay import Plugin
from entertainment import common

from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.xgoogle.search import GoogleSearch


class freetvserieshd(TVShowSource):
    implements = [TVShowSource]
	
    #unique name of the source
    name = "freetvserieshd"
    source_enabled_by_default = 'true'
    #display name of the source
    display_name = "FreeTvSeriesHD"
    
    #base url of the source website
    base_url = 'http://freetvserieshd.com/'
    
    def GetFileHosts(self, url, list, lock, message_queue,referer):
        import re

        from entertainment.net import Net
        net = Net(cached=False)

        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36','referer':referer}
        
       
        content = net.http_GET(url,headers=headers).content
        match=re.compile('"file":"(.+?)".+?"label":"(.+?)"',re.DOTALL).findall(content)
        for url , res in match:            
               
                res =res.upper().replace('hd','').replace('HD','')
                if not 'p' in res.lower():
                    res=res+'P'                
                if '480' in res:
                    res='HD'

                url=url+'|'+res
                            
                self.AddFileHost(list, res, url)



    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):

        import urllib2
        import re
        from entertainment.net import Net

        from entertainment import bing
        net = Net(cached=False)
        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)


        search_term ='%s Season %s Episode %s' %(name,season,episode)
        
        try:GOOGLED = self.GoogleSearch('freetvserieshd.com', search_term)
        except:GOOGLED = bing.Search('freetvserieshd.com', search_term)
        
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']
            if movie_url not in uniques:
                uniques.append(movie_url)
                if search_term.lower() in TITLE.lower():      
                    content = net.http_GET(movie_url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}).content 

                    try:URL=re.compile('data-lazy-src="(.+?)"').findall(content)[0]
                    except:
                        r='%s"' %movie_url
                        URL=re.compile(r).findall(content)[0]
                    referer =re.compile('<link rel="canonical" href="(.+?)"').findall(content)[0]

           

            
                    self.GetFileHosts(URL, list, lock, message_queue,referer)
                    break


    def Resolve(self, url):
        
        url=url.split('|')[0]
        if 'redirector.googlevideo' in url:
            import urllib
            url=urllib.urlopen(url).geturl()
            
        return url
