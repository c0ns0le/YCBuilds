'''
    Ice Channel
    buzzfilms.co
'''

from entertainment.plugnplay.interfaces import MovieSource
from entertainment.plugnplay.interfaces import TVShowSource
from entertainment.plugnplay import Plugin
from entertainment.xgoogle.search import GoogleSearch

class hdmovie(MovieSource,TVShowSource):
    implements = [MovieSource,TVShowSource]
    
    name = "HDMovie"
    display_name = "HDMovie"
    base_url = 'http://hdmovie14.net'
    
    source_enabled_by_default = 'true'

    
    def GetFileHosts(self, url, list, lock, message_queue, season, episode,type,year):

        from entertainment.net import Net
        import re
        net = Net(cached=False)

      

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        html = net.http_GET(url,headers=headers).content
        
        player='http://hdmovie14.net/player/' + re.compile('src="/player/(.+?)"').findall(html)[0]
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Referer':url}
        
        LINK = net.http_GET(player,headers=headers).content
        match = re.compile('src":"(.+?)".+?res":(.+?),').findall(LINK)

        for FINAL_URL , res in match:
            
                 
            self.AddFileHost(list, res+'P', FINAL_URL)                    

                
    def GetFileHostsForContent(self, title, name, year, season, episode, type, list, lock, message_queue):  
    
        from entertainment.net import Net

        from entertainment import bing
        
        net = Net(cached=False)        
        title = self.CleanTextForSearch(title) 
        name = self.CleanTextForSearch(name)
        #print ':::::::::::::::::::::::::::::::::'

        if type == 'tv_episodes':
            search_term ='%s Season %s' %(name,season)
            try:GOOGLED = self.GoogleSearch('hdmovie14.net', search_term)
            except:GOOGLED = bing.Search('hdmovie14.net', search_term)            
                      
           
        else:
            search_term = name + ' '+year
            RESULT_TERM = name.lower()           
            try:GOOGLED = self.GoogleSearch('hdmovie14.net', search_term)
            except:GOOGLED = bing.Search('hdmovie14.net', search_term) 
            
        uniques =[]
        for result in GOOGLED:          
            movie_url= result['url']
            TITLE = result['title']

            if type == 'tv_episodes':
                if not '/tag/' in movie_url.lower():
  
                    if 'hdmovie14.net' in movie_url.lower():

                        if name.lower() in TITLE.lower():
 
                            if 'season '+season in TITLE.lower():
                                if movie_url not in uniques:
                                    
                                    uniques.append(movie_url)
                                    movie_url=movie_url+'/'+episode
                                    self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                                    break
            else:
                if not '/tag/' in movie_url.lower():                
                    if 'hdmovie14.net' in movie_url.lower():
                        if name.lower() in TITLE.lower():
                           
                            if year in TITLE.lower():
                                if movie_url not in uniques:
                                    uniques.append(movie_url)
                                    
                                    self.GetFileHosts(movie_url, list, lock, message_queue,season, episode,type,year)
                                    break
            
    def Resolve(self, url):
                
        return url
            
                
                
