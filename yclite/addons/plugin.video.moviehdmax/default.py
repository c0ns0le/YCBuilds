import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse
from t0mm0.common.addon import Addon
from metahandler import metahandlers

from resources.lib.libraries import client
from resources.lib.resolvers import googleplus

addon_id = 'plugin.video.moviehdmax'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
icon4 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/latest.png'))
icon5 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/genres.png'))
icon3 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/latestshows.png'))
icon2 = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'art/search.png'))
addon = Addon(addon_id, sys.argv)

def CATEGORIES():
        addDir2('[COLOR red]>>> Search Movies <<<[/COLOR]','http://moviehdmax.com/',3,icon2,fanart)

        addDir2('> Latest Movies','http://moviehdmax.com/',111,icon4,fanart)
        addDir2('> Latest TV Episodes','http://fulltvepisodes.net/series-index/',11,icon3,fanart)

        addDir2('Action','http://moviehdmax.com/search/genre/action?page=1#genre',1,icon5,fanart)
        addDir2('Crime','http://moviehdmax.com/search/genre/crime?page=1#genre',1,icon5,fanart)
        addDir2('Romance','http://moviehdmax.com/search/genre/romance?page=1#genre',1,icon5,fanart)
        addDir2('Biography','http://moviehdmax.com/search/genre/biography?page=1#genre',1,icon5,fanart)
        addDir2('Sci-Fi','http://moviehdmax.com/search/genre/sci-fi?page=1#genre',1,icon5,fanart)
        addDir2('Documentary','http://moviehdmax.com/search/genre/documentary?page=1#genre',1,icon5,fanart)
        addDir2('Drama','http://moviehdmax.com/search/genre/drama?page=1#genre',1,icon5,fanart)
        addDir2('Comedy','http://moviehdmax.com/search/genre/comedy?page=1#genre',1,icon5,fanart)
        addDir2('Fantasy','http://moviehdmax.com/search/genre/fantasy?page=1#genre',1,icon5,fanart)
        addDir2('History','http://moviehdmax.com/search/genre/history?page=1#genre',1,icon5,fanart)
        addDir2('Horror','http://moviehdmax.com/search/genre/horror?page=1#genre',1,icon5,fanart)
        addDir2('Adventure','http://moviehdmax.com/search/genre/adventure?page=1#genre',1,icon5,fanart)
        addDir2('Mystery','http://moviehdmax.com/search/genre/mystery?page=1#genre',1,icon5,fanart)
        addDir2('Animation','http://moviehdmax.com/search/genre/animation?page=1#genre',1,icon5,fanart)
        addDir2('Family','http://moviehdmax.com/search/genre/family?page=1#genre',1,icon5,fanart)
        addDir2('Sport','http://moviehdmax.com/search/genre/sport?page=1#genre',1,icon5,fanart)
        addDir2('Music','http://moviehdmax.com/search/genre/music?page=1#genre',1,icon5,fanart)
        addDir2('Game-show','http://moviehdmax.com/search/genre/game-show?page=1#genre',1,icon5,fanart)
        addDir2('Thriller','http://moviehdmax.com/search/genre/thriller?page=1#genre',1,icon5,fanart)
        addDir2('War','http://moviehdmax.com/search/genre/war?page=1#genre',1,icon5,fanart)
        addDir2('Western','http://moviehdmax.com/search/genre/western?page=1#genre',1,icon5,fanart)




# --------------------------------- FULLTV EPISODES -----------------------------		
def GETTV(url,name):
        link = open_url(url)
        match=re.compile('<a href="(.+?)">(.+?)</a></div>').findall(link)
        for url,name in match:
			name=cleanHex(name)
			name=re.sub('Full Movie Watch Online','',name)
                        try:
                                addDir2(name,url,12,icon,fanart)
                        except:pass

def GETTVEPISODES(url,name):
        link = open_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)"><span>.+?</span>').findall(link)
        for url,name in match:
			name=cleanHex(name)
			name=re.sub('Full Movie Watch Online','',name)
  
                        try:
                                addDir2(name,url,13,icon,fanart)
                        except:pass


def GETTVLINKS(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('<a target=".+?" rel=".+?" href="(.+?)">.+?</a>').findall(link)
        for url in match:
                
                if urlresolver.HostedMediaFile(url).valid_url():
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(host,url,102,iconimage,fanart)	

def PLAYLINKMAZE(name,url,iconimage):
        name=selfAddon.getSetting('namestore')
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(stream_url)
	addLink("Press Back to exit",url,'',iconimage,fanart)       
def GETMOVIES(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass
        metaset = selfAddon.getSetting('enable_meta')
        link = open_url(url)
        match=re.compile('<a href="../..(.+?)"> <img data-original=".+?" alt="(.+?)" class=".+?">').findall(link)
        for url,name in match:
			name=cleanHex(name)
			name=re.sub('Full Movie Watch Online','',name)
			name=re.sub('watch','',name)
			name=re.sub('online','',name)
			name=re.sub('free','',name)
			name=re.sub('putlocker','',name)
			name=re.sub('xmovie8','',name)
			name=re.sub('xmovies8','',name)
			url= 'http://moviehdmax.com' + url
                        try:
                               addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						
def GETMOVIESNEW(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass
        link = open_url(url)
        match=re.compile('<a href="(.+?)">(.+?)<span class="hblank">').findall(link)[:30]
        for url,name in match:
			name=cleanHex(name)
			name=re.sub('Full Movie Watch Online','',name)
			name=re.sub('watch','',name)
			name=re.sub('online','',name)
			name=re.sub('free','',name)
			name=re.sub('putlocker','',name)
			name=re.sub('xmovie8','',name)
			name=re.sub('xmovies8','',name)
				
			url= 'http://moviehdmax.com/' + url

                        try:
                                addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						

def GETSEARCH(url,name):
	try:
			actualpage = str(url)
			actualpage = re.sub('#genre','',actualpage)
			pagenum = actualpage.split('?page=')
			
			curpage = int(pagenum[1])
			nextpage = curpage + 1
			nextpageurl = pagenum[0]+'?page='+str(nextpage)+'#genre'
	except:pass

        link = open_url(url)
        match=re.compile('<p class=".+?">\s*<a href="../(.+?)">(.+?)</a>').findall(link)
        for url,name in match:
			name=cleanHex(name)
			name=re.sub('Full Movie Watch Online','',name)
			name=re.sub('watch','',name)
			name=re.sub('online','',name)
			name=re.sub('free','',name)
			name=re.sub('putlocker','',name)
			name=re.sub('xmovie8','',name)
			name=re.sub('xmovies8','',name)
			name=re.sub('Genres','',name)
			name=re.sub('Contacts','',name)
			name=re.sub('Full TV Series','',name)
			name=re.sub('<strong>','',name)
			name=re.sub('</strong>','',name)
			name=re.sub('<span>','',name)
			name=re.sub('</span>','',name)

			url= 'http://moviehdmax.com/' + url

                        try:
                                addDir(name,url,2,icon,len(match),isFolder=True)
                        except:pass
	try:
               
					addLink('NEXT >>',nextpageurl,1,icon,'')
					
	except: pass						


def GETLINKS(url,name,iconimage):
        selfAddon.setSetting('namestore',name)
        link = open_url(url)
        match=re.compile('''<source src="(.+?)" type='.+?' data-res="(.+?)"/>''').findall(link)
		
        for url, name in match:
                
                
                        host=url.split('/')[2].replace('www.','').capitalize()
                        addLink(name+'p',url,100,iconimage,fanart)


	# ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH --------------------------------------------------------
 # ------------------------------------------------------- MEGA SEARCH -------------------------------------------------------- 
def SEARCH():
    search_entered =''
    keyboard = xbmc.Keyboard(search_entered, 'Search Movies')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText().replace(' ','+')
    if len(search_entered)>1:
  
    	url = 'http://moviehdmax.com/search/result?s=' + search_entered + '&selected=false'
        GETSEARCH(url,name)
 		
def PLAYLINK(name,url,iconimage):
        name=selfAddon.getSetting('namestore')
        resp = urllib2.urlopen(url)
        url2 = resp.geturl()
        stream_url = urlresolver.HostedMediaFile(url2).resolve()
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url2,listitem=liz)
        xbmc.Player ().play(stream_url)
	addLink("Press Back to exit",url,'',iconimage,fanart)
        
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

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

def addDir2(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        liz.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
        try:
          if not 'COLOR' in name:
            splitName=name.partition('(')
            simplename=""
            simpleyear=""
            if len(splitName)>0:
                simplename=splitName[0]
                simpleyear=splitName[2].partition(')')
            if len(simpleyear)>0:
                simpleyear=simpleyear[0]
            mg = metahandlers.MetaData()
          
            meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
            liz.setInfo( type="Video", infoLabels= meta )
            liz.setProperty("IsPlayable","true")
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=True)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
            else: liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
            return ok


		   
        except:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            liz.setProperty("IsPlayable","true")
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
    if selfAddon.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )

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
elif mode==40: MOVIESINDEX()
elif mode==1: GETMOVIES(url,name)
elif mode==111: GETMOVIESNEW(url,name)

elif mode==4: GETSEARCH(url,name)
elif mode==2: GETLINKS(url,name,iconimage)

elif mode==3: SEARCH()


elif mode==11: GETTV(url,name)
elif mode==13: GETTVLINKS(url,name,iconimage)

elif mode==12: GETTVEPISODES(url,name)
# elif mode==15: GETUPTOBOX_BASE(url,name,iconimage)
# elif mode==18: GETLINKSMOVIEWATCHER(url,name,iconimage)
# elif mode==20: ONLINEMOVIESIS()
# elif mode==21: GETONLINEMOVIESIS(url,name)
# elif mode==23: GETHDMOVIES14(url,name)
# elif mode==22: GETONLINEMOVIESLINKS(url,name,iconimage)
# elif mode==24: XMOVIES8()
# elif mode==25: GETXMOVIES8(url,name)
# elif mode==26: GETYEARSXMOVIES(url,name)
# elif mode==27: GETGENRESXMOVIES(url,name)
# elif mode==28: GETLINKS132(url,name,iconimage)
# elif mode==29: GETLINKS10(url,name,iconimage)
# elif mode==30: SEARCHTV()
# elif mode==31: GetLinks_base(url,name,iconimage)
# elif mode==32: GETSERIESCRAVING(url,name)
# elif mode==33: GETSERIESCRAVING_EP(url,name)
# elif mode==34: GETLINKS_SCRAVING(url,name,iconimage)
# elif mode==35: GETMOVIESDB(url,name)
# elif mode==36: GETLINKSDB(url,name,iconimage)
# elif mode==37: AFDAH()
# elif mode==38: GETMOVIESAFDAH(url,name)
# elif mode==39: GETMOVIES2K(url,name)
elif mode==100: PLAYLINK(name,url,iconimage)
# elif mode==101: PLAYLINKFREEFULLMOVIES(name,url,iconimage)
elif mode==102: PLAYLINKMAZE(name,url,iconimage)
# elif mode==103: PLAYLINKMOVIEWATCHER(name,url,iconimage)
# elif mode==104: PLAYLINKXMOVIES(name,url,iconimage)
# elif mode==105: PLAYLINKAFDAH(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

