'''
    Ice Channel
    buzzfilms.co
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment.xgoogle.search import GoogleSearch

class watch(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "Watch1080p"
    display_name = "Watch1080p"
    base_url = 'watch1080p.com'
    
    source_enabled_by_default = 'true'

    
    def GetFileHosts(self, url, list, lock, message_queue, season, episode,type,year):

        from entertainment.net import Net
        import re
        net = Net(cached=False)

      
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        html = net.http_GET(url,headers=headers).content
        
        new_url=re.compile('href="(.+?)">Watch Now<').findall(html)[0]
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':url}
        
        LINK = net.http_GET(new_url,headers=headers).content
        
        if type == 'tv_episodes':
            try:
                TITLESPLIT = re.compile('class="svname">(.+?)</span>').findall(LINK)
                for TITLE in TITLESPLIT:
                    LINKED=LINK.split(TITLE)
                    for p in LINKED:
                        br=p.split('<br>')[0]
                        match = re.compile('<a id=".+?" href="(.+?)">(.+?)<').findall(br)
                        for FINAL_URL , EPISODE in match:
                            EPISODE=EPISODE.replace(' ','')
                            if episode ==EPISODE:
                                self.AddFileHost(list, '1080P', FINAL_URL,host=TITLE)
            except:pass                                
        else:
            match = re.compile('class="svname">(.+?)</span><span class="svep"><a id=".+?" href="(.+?)">(.+?)<').findall(LINK)

            for TITLE,FINAL_URL , res in match:
                res=res.replace('Quality','').replace(' ','')
                
                     
                self.AddFileHost(list, res, FINAL_URL,host=TITLE)                    

                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net

        from entertainment import bing
        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)
        #print ':::::::::::::::::::::::::::::::::'

        if type == 'tv_episodes':
            search_term ='%s Season %s' %(name,season)
            RESULT_TERM = 'Watch %s - Season %s'%(name,season)
            try:GOOGLED = self.GoogleSearch('watch1080p.com', search_term)
            except:GOOGLED = bing.Search('watch1080p.com', search_term)            
                      
           
        else:
            search_term = name + ' '+year
            RESULT_TERM = 'Watch %s (%s)'%(name,year)          
            try:GOOGLED = self.GoogleSearch('watch1080p.com', search_term)
            except:GOOGLED = bing.Search('watch1080p.com', search_term) 
            
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']
            if RESULT_TERM.lower() in TITLE.lower():
                if type == 'tv_episodes':
                    if movie_url not in uniques:
                        
                        uniques.append(movie_url)
                        
                        self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                        break
                else:
                    if movie_url not in uniques:
                        uniques.append(movie_url)
                        
                        self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                        break

    def Resolve(self, url):
        from entertainment.net import Net

        import re,urllib,base64

        
        
        net = Net()
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':url}
        html = net.http_GET(url,headers=headers).content                
        URL=re.compile('src="(.+?)" style').findall(html)[0]

        link = net.http_GET(URL,headers=headers).content

        try:
                stream=re.compile("window.atob\('(.+?)'\)\)").findall(link)[0]
                data=base64.b64decode(stream)
                data=base64.b64decode(data)
                stream=re.compile("<source src='(.+?)'").findall(data)[0]
        
        except:
                from entertainment import istream
                
                stream=re.compile('src="(.+?)"').findall(link)[0]
                stream=istream.ResolveUrl(stream)
        return stream
            
                
                
