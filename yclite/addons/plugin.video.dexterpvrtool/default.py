import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse
from t0mm0.common.addon import Addon



addon_id = 'plugin.video.dexterpvrtool'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
ADDON2=xbmcaddon.Addon(id='plugin.video.dexterpvrtool')
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
epg = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/pvr.iptvsimple', 'settings.xml'))
epgdir    =  xbmc.translatePath(os.path.join('special://home/userdata/profiles/',''))
dialog = xbmcgui.Dialog()
def CATEGORIES():
		addDir2('COPY YOUR DEXTER SETTINGS','http://www.dexteriptv.com',1,icon,'',fanart)


def EPGTOOL():
	import shutil
	dir_entered = 'LiveTV & On Demand'
	
	keyboard = xbmc.Keyboard(dir_entered, 'Input profile name')
	dialog.ok("DEXTER PVR HELP TOOL", "IMPORTANT: Please input the correct profile name in the next window or your settings will not be applied", '','')
	keyboard.doModal()
	if keyboard.isConfirmed(): dir_entered = keyboard.getText()


	if not os.path.exists(epgdir):
		os.makedirs(epgdir)	
	profiledir    =  xbmc.translatePath(os.path.join(epgdir + dir_entered + '/addon_data/pvr.iptvsimple','settings.xml'))
	try:
		shutil.copy2(epg, profiledir)
		dialog.ok("DEXTER Pro", "DEXTER PVR Settings ported to the selected Profile.... Please restart Kodi to make it effective...", '','')
	except: dialog.ok("ERROR: CANNOT COPY SETTINGS", "DEXTER PVR Settings cannot be ported to the selected profile.... Run Dexter Pro before using this tool and be sure to input the correct profile name...", '','')
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






		
def addDir2(name,url,mode,iconimage,description,fanart):
        xbmc.executebuiltin('Container.SetViewMode(50)')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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
elif mode==1: EPGTOOL()


xbmcplugin.endOfDirectory(int(sys.argv[1]))

