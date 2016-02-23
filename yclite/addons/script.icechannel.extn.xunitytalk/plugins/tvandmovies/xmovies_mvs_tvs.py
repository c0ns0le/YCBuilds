'''
    Ice Channel
    buzzfilms.co
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment.xgoogle.search import GoogleSearch

class xmovies(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "XMovies8"
    display_name = "XMovies8"
    base_url = 'http://xmovies8.tv'
    
    source_enabled_by_default = 'true'

    
    def GetFileHosts(self, url, list, lock, message_queue, season, episode,type,year):

        from entertainment.net import Net
        import re
        net = Net(cached=False)
  
        URL = url.split('xmovies8.tv/movie/')[1]
        URL = URL.split('/')[0]
        
        if type == 'tv_episodes':
            isseries='1'
        else:
            isseries='2'

        data={'mx':URL,
              'isseries':isseries,
              'part':'0'}
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        html = net.http_POST('http://xmovies8.tv/lib/picasa.php',data,headers=headers).content
        
        if type == 'tv_episodes':
            match=re.compile('part_id=(.+?)">(.+?)</a>').findall(html)
            for partid , ep in match:
                if episode ==ep:
                                            
                    data={'mx':URL,
                          'isseries':isseries,
                          'part':partid}
                    HTML = net.http_POST('http://xmovies8.tv/lib/picasa.php',data,headers=headers).content
                    FINAL_URL = re.compile('<a href="(.+?)" target="_blank" rel="nofollow">.+?</a>').findall(HTML)[-1]
                    
                    self.AddFileHost(list, '720P', FINAL_URL,host='XMOVIES8')
        else:
            
            FINAL_URL = re.compile('<a href="(.+?)" target="_blank" rel="nofollow">.+?</a>').findall(html)[-1]
                 
            self.AddFileHost(list, '720P', FINAL_URL,host='XMOVIES8')                    

                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net
        from entertainment import bing


        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)
        #print ':::::::::::::::::::::::::::::::::'

        if type == 'tv_episodes':
            search_term ='%s Season %s' %(name,season)
            try:GOOGLED = self.GoogleSearch('xmovies8.tv', search_term)
            except:GOOGLED = bing.Search('xmovies8.tv', search_term)        
           
        else:
            search_term = name + ' '+year
            RESULT_TERM = name.lower()           
            try:GOOGLED = self.GoogleSearch('xmovies8.tv', search_term)
            except:GOOGLED = bing.Search('xmovies8.tv', search_term)            
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']

            if type == 'tv_episodes':
                if 'xmovies8.tv' in movie_url.lower():
                    if name.lower() in TITLE.lower():
                        if 'season '+season in TITLE.lower():
                            if movie_url not in uniques:
                                uniques.append(movie_url)               
                                self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                                break
            else:
                if 'xmovies8.tv' in movie_url.lower():
                    if name.lower() in TITLE.lower():
                       
                        if year in TITLE.lower():
                            if movie_url not in uniques:
                                uniques.append(movie_url)
                 
                                self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                                break
            
    def Resolve(self, url):
                
        return url
            
                
                
