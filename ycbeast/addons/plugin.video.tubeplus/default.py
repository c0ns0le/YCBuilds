import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse
from t0mm0.common.addon import Addon



addon_id = 'plugin.video.tubeplus'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
ADDON2=xbmcaddon.Addon(id='plugin.video.tubeplus')
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))

base = 'http://www.tubeplus.is'
def CATEGORIES():
		addDir2('[COLOR lime]Search[/COLOR]','http://www.tubeplus.is/search/',3,icon,'',fanart)

		addDir2('[COLOR yellow]Latest Shows [/COLOR]','http://www.tubeplus.is/browse/tv-shows/Last/ALL/',6,icon,'',fanart)
		addDir2('Action','http://www.tubeplus.is/browse/tv-shows/Action/ALL/',6,icon,'',fanart)
		addDir2('Adventure','http://www.tubeplus.is/browse/tv-shows/Adventure/ALL/',6,icon,'',fanart)
		addDir2('Animation','http://www.tubeplus.is/browse/tv-shows/Animation/ALL/',6,icon,'',fanart)
		addDir2('Biography','http://www.tubeplus.is/browse/tv-shows/Biography/ALL/',6,icon,'',fanart)
		addDir2('Comedy','http://www.tubeplus.is/browse/tv-shows/Comedy/ALL/',6,icon,'',fanart)
		addDir2('Crime','http://www.tubeplus.is/browse/tv-shows/Crime/ALL/',6,icon,'',fanart)
		addDir2('Drama','http://www.tubeplus.is/browse/tv-shows/Drama/ALL/',6,icon,'',fanart)
		addDir2('Family','http://www.tubeplus.is/browse/tv-shows/Family/ALL/',6,icon,'',fanart)
		addDir2('Fantasy','http://www.tubeplus.is/browse/tv-shows/Fantasy/ALL/',6,icon,'',fanart)
		addDir2('History','http://www.tubeplus.is/browse/tv-shows/History/ALL/',6,icon,'',fanart)
		addDir2('Horror','http://www.tubeplus.is/browse/tv-shows/Horror/ALL/',6,icon,'',fanart)
		addDir2('Mystery','http://www.tubeplus.is/browse/tv-shows/Mystery/ALL/',6,icon,'',fanart)
		addDir2('Romance','http://www.tubeplus.is/browse/tv-shows/Romance/ALL/',6,icon,'',fanart)
		addDir2('Sci-Fi','http://www.tubeplus.is/browse/tv-shows/Sci-Fi/ALL/',6,icon,'',fanart)
		addDir2('Thriller','http://www.tubeplus.is/browse/tv-shows/Thriller/ALL/',6,icon,'',fanart)
		addDir2('War','http://www.tubeplus.is/browse/tv-shows/War/ALL/',6,icon,'',fanart)
		addDir2('Western','http://www.tubeplus.is/browse/tv-shows/Western/ALL/',6,icon,'',fanart)

	

		
def GETFILMS(url,name):
        
        
        link = open_url(url)
        
        match=re.compile('<a target=".+?" title="(.+?)" href="(.+?)"><img border="0" alt=".+?" src="(.+?)">').findall(link)
		
        for name,url,img in match:
                        name=cleanHex(name)
                
                        name=re.sub('Streaming','', name)
                        name=re.sub('Watch online:','', name)
                        name=re.sub('-','', name)
                        url='http://www.tubeplus.is/' + url
                        img='http://www.tubeplus.is/' + img
                        addDir2(name,url,10,img,'',fanart)
                
        try:
               
                match=re.compile('<a class="nextpostslink" rel="next" href="(.+?)">').findall(link)
                
                url= match[0]
                addDir2('[COLOR yellow]Next Page >>[/COLOR]',url,6,icon,'',fanart)
        except: pass
def GETLINK(url,name):
        
        
        link = open_url(url)
        
        match=re.compile('href=/player/(.+?)"').findall(link)
        match1=re.compile('<iframe src="(.+?)" scrolling=".+?" frameborder=".+?"').findall(link)
        for url in match:
                         url='http://www.tubeplus.is/player/' + url
                         hostname=url.split('/')[6].replace('www.','').capitalize()
                         hostname2=url.split('/')[7].replace('www.','').capitalize()
                         hostname3=url.split('/')[8].replace('www.','').capitalize()
                         season= hostname + " - " + hostname2 + " - " + hostname3
                         season=re.sub("_"," ",season)
                         addDir2(season,url,8,icon,'',fanart)  


def GETLINKS_SERIES(url,name):
        hostname=name
       
        link = open_url(url)
       
        match=re.compile('<a href="(.+?)" onclick="(.+?)" ').findall(link)
        match1=re.compile('<iframe src="(.+?)" scrolling=".+?" frameborder=".+?"').findall(link)
        for base,host in match:
                         host = host.split("'")
                         host=host[1]
                         base = base.split("'")
                         base=base[5]
                         playlink="http://" + base + "/" + host + ".html"
                         # hostname=playlink.split('/')[2].replace('www.','').capitalize()
                         addLink(hostname + " [COLOR yellow]   Play >>>[/COLOR]",playlink,11,icon,'',fanart)  


					 
	
def PLAYLINKMOVIEWATCHER(name,url,iconimage):
        name=re.sub("Play >>>", "", name)
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(stream_url, liz, False)

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))


def SEARCHMOVIES():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search TV Show')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','_')
    if len(search_entered)>1:
        url = 'http://www.tubeplus.is/search/tv-shows/'+ search_entered
        link = open_url(url)
        GETFILMS(url,name)



def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def addLink(name,url,mode,iconimage,description,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

		




		
def addDir2(name,url,mode,iconimage,description,fanart):
        xbmc.executebuiltin('Container.SetViewMode(50)')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=iconImage, thumbnailImage=img)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
            return ok
        
def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON2.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON2.getSetting(viewType) )

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
print params

if mode==None or url==None or len(url)<1: CATEGORIES()
elif mode==3: SEARCHMOVIES()
elif mode==6: GETFILMS(url,name)

elif mode==8: GETLINKS_SERIES(url,name)
elif mode==10: GETLINK(url,name)
elif mode==11: PLAYLINKMOVIEWATCHER(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

