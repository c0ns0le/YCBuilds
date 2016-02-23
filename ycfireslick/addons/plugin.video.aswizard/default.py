import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,shutil,urllib2,urllib,re,extract,downloader,time,socket,net
net             = net.Net()
addon_id        = 'plugin.video.aswizard'
ADDON           = xbmcaddon.Addon(id=addon_id)
selfAddon       = xbmcaddon.Addon(id=addon_id)
datapath        = xbmc.translatePath(selfAddon.getAddonInfo('profile'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.jpg'))
addonspath      = xbmc.translatePath(os.path.join('special://home/addons/', ''))
udpath          = xbmc.translatePath(os.path.join('special://home/userdata/', ''))
dialog          = xbmcgui.Dialog()

def CATEGORIES():
    link = net.http_GET('http://wookiespmc.com/Updates/wizard_txt/wookie.txt').content.replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    name = '';iconimage = '';fanart = '';description = ''   
    for name,url,iconimage,fanart,description in match:
        name = '[COLOR red]'+name+'[/COLOR]'
        if 'Section' in name:
            if not 'Build' in name:
                addDir(name,url,1,iconimage,fanart,description)
        else:
            addLink(name,url,1,iconimage,fanart,description)
    addDir('[COLOR red]Community Builds[/COLOR]','url',2,'http://wookiespmc.com/Updates/images/communitybuilds.jpg',fanart,description)
    xbmc.executebuiltin('Container.SetViewMode(500)')

def WIZARD(name,url,description):
            ret = dialog.yesno('[COLOR red]Wookie[/COLOR]', 'For A Successful Update','Ensure You Have Cleared Data First','Do You Wish To Continue?','Cancel','Continue')
            if ret == 1:
                name = name.replace('[COLOR red]','').replace('[/COLOR]','')
                path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
                dp = xbmcgui.DialogProgress()
                dp.create("[COLOR red]Wookie[/COLOR]","Wookie is creating your custom view",'', 'Please Wait')
                lib=os.path.join(path, name+'.zip')
                try:
                   os.remove(lib)
                except:
                   pass
                downloader.download(url, lib, dp)
                addonfolder = xbmc.translatePath(os.path.join('special://','home'))
                dp.update(0,"", "[COLOR red]Applying Wookie View[/COLOR]")
                extract.all(lib,addonfolder,dp)
                try:
                   os.remove(lib)
                except:
                   pass
                FORCECLOSE()
            else:quit()
    
def COMMUNITY():
    addDir('[COLOR red]xbmckodiaddons.com Builds[/COLOR]','url',4,'http://wookiespmc.com/Updates/images/xbmckodiaddons.jpg',fanart,description)
    addDir('[COLOR red]Other 3rd Party Builds[/COLOR]','http://wookiespmc.com/Updates/wizard_txt/3rdPartyBuilds(notforum).txt',3,'http://wookiespmc.com/Updates/images/communitybuilds.jpg',fanart,description)
    xbmc.executebuiltin('Container.SetViewMode(500)')

def GET3RDPARTY(url):
    link = net.http_GET(url).content.replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    name = '';iconimage = '';fanart = '';description = ''   
    for name,url,iconimage,fanart,description in match:
        name = '[COLOR red]'+name+'[/COLOR]'
        addLink(name,url,1,iconimage,fanart,description)
    xbmcplugin.addSortMethod(int(sys.argv[1]), 1)
    xbmc.executebuiltin('Container.SetViewMode(500)')

def GETFORUMBUILDS():
    response = net.http_GET('http://www.xbmckodiaddons.com/?forum=468019')
    link = cleanHex(response.content)
    match = re.compile('<a href="(.+?)" title=".+?" class="thread_title">(.+?)</a>').findall(link)
    for url,name in match:
      try:
        if '[Release]' in name:
            print name
            name = name.replace("[Release]","")
            url='http://www.xbmckodiaddons.com'+url
            response = net.http_GET(url).content
            thumb = 'http://wookiespmc.com/Updates/images/xbmckodiaddons.png'
            url = re.compile('url="(.+?)"').findall(response)[0]
            url = url.replace('amp;','')
            thumb = re.compile('img="(.+?)"').findall(response)[0]
            thumb = thumb.replace('amp;','')
            addLink(name,url,1,thumb,fanart,name)
      except:pass  
    xbmc.executebuiltin('Container.SetViewMode(500)')

def GRABFORUMBUILDS(url,name):
    response = net.http_GET(url)
    link = cleanHex(response.content)
    buildzip = re.compile('url="(.+?)"').findall(link)[0]
    WIZARD(name,buildzip,'')

def FORCECLOSE():
    FoundPlatform = PLATFORMQUERY()
    if FoundPlatform == 'osx':
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR red]Wookie[/COLOR]", "Wookie configuration prepared", "[COLOR red]PLEASE DISCONNECT THE POWER FROM YOUR DEVICE[/COLOR]")
    elif FoundPlatform == 'linux':
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR red]Wookie[/COLOR]", "Wookie configuration prepared", "[COLOR red]PLEASE DISCONNECT THE POWER FROM YOUR DEVICE[/COLOR]")
    elif FoundPlatform == 'android':
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass
        try: os.system('adb shell am force-stop com.semperpax.spmc')
        except: pass
        dialog.ok("[COLOR red]Wookie[/COLOR]", "Wookie configuration prepared", "[COLOR red]PLEASE DISCONNECT THE POWER FROM YOUR DEVICE[/COLOR]")
    elif FoundPlatform == 'windows':
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR red]Wookie[/COLOR]", "Wookie configuration prepared", "[COLOR red]PLEASE DISCONNECT THE POWER FROM YOUR DEVICE[/COLOR]")
    else: #ATV
        try: os.system('killall AppleTV')
        except: pass
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR red]Wookie[/COLOR]", "Wookie configuration prepared", "[COLOR red]PLEASE DISCONNECT THE POWER FROM YOUR DEVICE[/COLOR]")

def PLATFORMQUERY():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

def addLink(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def addDir(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))
        
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
                            
params=get_params();url=None;name=None;mode=None;iconimage=None;description=None
try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:iconimage=urllib.unquote_plus(params["iconimage"])
except:pass
try:mode=int(params["mode"])
except:pass
try:description=urllib.unquote_plus(params["description"])
except:pass

if mode==None or url==None or len(url)<1:CATEGORIES()
elif mode==1:WIZARD(name,url,description)
elif mode==2:COMMUNITY()
elif mode==3:GET3RDPARTY(url)
elif mode==4:GETFORUMBUILDS()
elif mode==5:GRABFORUMBUILDS(url,name)
elif mode==100:FORCECLOSE()
xbmcplugin.endOfDirectory(int(sys.argv[1]))

