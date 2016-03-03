import xbmc, xbmcaddon, xbmcgui, xbmcplugin, urllib, urllib2, os, re, sys, urlresolver, random
from resources.libs.common_addon import Addon
from metahandler import metahandlers

addon_id        = 'plugin.video.marvin'
selfAddon       = xbmcaddon.Addon(id=addon_id)
addon           = Addon(addon_id, sys.argv)
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
baseurl         = 'http://thebeastkodi.uk/addon/marvintest.txt'
iconimage       = addon.queries.get('iconimage', '')
metaset         = selfAddon.getSetting('enable_meta')
ytapi1 = 'https://www.googleapis.com/youtube/v3/search?q='
ytapi2 = '&regionCode=US&part=snippet&hl=en_US&key=AIzaSyA7v1QOHz8Q4my5J8uGSpr0zRrntRjnMmk&type=video&maxResults=50'
ytpl   = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
ytpl2  = '&maxResults=50&key=AIzaSyBAdxZCHbeJwnQ7dDZQJNfcaF46MdqJ24E'

def Index():
    link = open_url(baseurl)
    match = re.compile('name="(.+?)".+?url="(.+?)".+?img="(.+?)"', re.DOTALL).findall(link)
    for name, url, iconimage in match:
        addDir(name, url, 1, iconimage, fanart)
    xbmc.executebuiltin('Container.SetViewMode(500)')

def GetChannels(url):
    if 'Index' in url:
        CatIndex(url)
    if 'movies' in url:
        channels = GetList(url)
        cnt = len(channels)
        for channel in channels:
            addLinkMeta(channel["name"], channel["url"], 3, iconimage, cnt, isFolder=False)
        setView('movies', 'MAIN')
        if 'Index' in url:
            xbmc.executebuiltin('Container.SetViewMode(50)')
    else:
        burl = url
        channels = GetList(url)
        for channel in channels:
            if 'youtube.com/results?search_query=' in channel["url"]:
                addDir(channel["name"], channel["url"], 3, iconimage, fanart)
            elif 'youtube.com/playlist?list=' in channel["url"]:
                addDir(channel["name"], channel["url"], 3, iconimage, fanart)
            else:
                if 'txt' in channel["url"]:
                    addDir(channel["name"], channel["url"], 3, iconimage, fanart)
                else:
                    addLink(channel["name"], channel["url"], 3, iconimage, fanart)
        xbmc.executebuiltin('Container.SetViewMode(50)')

def CatIndex(url):
    link = open_url(url)
    match = re.compile('name="(.+?)".+?url="(.+?)".+?img="(.+?)"', re.DOTALL).findall(link)
    for name, url, iconimage in match:
        if 'youtube.com/playlist?list=' in url:
            addDir(name, url, 3, iconimage, fanart)
        elif 'youtube.com/results?search_query=' in url:
            addDir(name, url, 3, iconimage, fanart)
        else:
            addDir(name, url, 1, iconimage, fanart)
    xbmc.executebuiltin('Container.SetViewMode(50)')

def GetList(url):
    link = open_url(url)
    matches = re.compile('^#.+?:-?[0-9]*(.*?),(.*?)\n(.*?)$', re.I + re.M + re.U + re.S).findall(link)
    li = []
    for params, name, url in matches:
        item_data = {"params": params, "name": name, "url": url}
        li.append(item_data)
    list = []
    for channel in li:
        item_data = {"name": channel["name"], "url": channel["url"]}
        matches = re.compile(' (.+?)="(.+?)"', re.I + re.M + re.U + re.S).findall(channel["params"])
        for field, value in matches:
            item_data[field.strip().lower().replace('-', '_')] = value.strip()
        list.append(item_data)
    return list

# start of toxic function: #

def PlayLink(url,name):
        print url
        if 'txt' in url:
            GetChannels(url)
        else:
            if 'youtube.com/results?search_query=' in url:
				print 'Youtube Search'
				searchterm = url.split('search_query=')[1]
				ytapi = ytapi1 + searchterm + ytapi2
				req = urllib2.Request(ytapi)
				req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				link = link.replace('\r','').replace('\n','').replace('  ','')
				match=re.compile('"videoId": "(.+?)".+?"title": "(.+?)"',re.DOTALL).findall(link)
				print match
				for ytid,name in match:
					url = 'https://www.youtube.com/watch?v='+ytid
					addLink(name,url,3,iconimage,fanart)
            elif 'youtube.com/playlist?list=' in url:
				print 'Youtube Playlist'
				searchterm = url.split('playlist?list=')[1]
				ytapi = ytpl + searchterm + ytpl2
				req = urllib2.Request(ytapi)
				req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				link = link.replace('\r','').replace('\n','').replace('  ','')
				match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
				for name,ytid in match:
					url = 'https://www.youtube.com/watch?v='+ytid
					addLink(name,url,3,iconimage,fanart)
            else:
				print '--> Playing Direct Stream <--'
				if urlresolver.HostedMediaFile(url).valid_url():
					streamurl = urlresolver.HostedMediaFile(url).resolve()
				else: streamurl=url
				ok=True
				liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
				ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=streamurl,listitem=liz)
				try:
					xbmc.Player().play(streamurl, liz, False)
					return ok
				except:
					pass

# :end of toxic function #

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass

def open_url(url):
    url += '?%d=%d' % (random.randint(1, 10000), random.randint(1, 10000))
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    link = link.replace('\r', '').replace('\t', '').replace('&nbsp;', '').replace('\'', '')
    response.close()
    return link

def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    
    return param

def addDir(name, url, mode, iconimage, fanart, description = ''):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&description=" + urllib.quote_plus(description)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})
    liz.setProperty('fanart_image', fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def addLink(name, url, mode, iconimage, fanart, description=''):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&description=" + urllib.quote_plus(description)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})
    liz.setProperty('fanart_image', fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok

def addLinkMeta(name, url, mode, iconimage, itemcount, isFolder=False):
    if metaset == 'true':
        if not 'COLOR' in name:
            splitName = name.partition('(')
            simplename = ""
            simpleyear = ""
        if len(splitName) > 0:
            simplename = splitName[0]
            simpleyear = splitName[2].partition(')')
        if len(simpleyear) > 0:
            simpleyear = simpleyear[0]
            mg = metahandlers.MetaData()
            meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
            u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&site=" + str(site) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
            ok = True
            liz = xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=iconimage)
            liz.setInfo(type="Video", infoLabels=meta)
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else:
            liz.setProperty('fanart_image', fanart)
            ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder, totalItems=itemcount)
            return ok
    else:
        u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&site=" + str(site) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
        ok = True
        liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        liz.setInfo(type="Video", infoLabels={"Title": name})
        liz.setProperty('fanart_image', fanart)
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
        return ok

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if selfAddon.getSetting('auto_view') == 'true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType))

params = get_params(); url=None; name=None; mode=None; site=None; iconimage=None

try: site = urllib.unquote_plus(params["site"])
except: pass
try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass
try: iconimage = urllib.unquote_plus(params["iconimage"])
except: pass

if mode == None or url == None or len(url) < 1: Index()
elif mode == 1:GetChannels(url)
elif mode == 3:PlayLink(url, name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))