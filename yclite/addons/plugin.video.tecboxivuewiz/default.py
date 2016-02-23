import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import shutil
import urllib2,urllib
import re
import extract
import downloader
import time
from addon.common.addon import Addon
from addon.common.net import Net
###THANK YOU TO THOSE THAT MADE THE BASE OF THIS WIZARD GREAT WORK###Based on Muckyducks wizard ###


USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon_id = 'plugin.video.tecboxivuewiz'
ADDON = xbmcaddon.Addon(id=addon_id)
AddonTitle="Tecbox Ivue Wizard" 
net = Net()
U = ADDON.getSetting('User')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
VERSION = "0.0.1"
DBPATH = xbmc.translatePath('special://database')
TNPATH = xbmc.translatePath('special://thumbnails');
PATH = "Tecbox Ivue Wizard"            
BASEURL = "http://tecbox.tv/repo/teciptvguide"
H = 'http://'

def INDEX():
    addDir('IVUE TOOLS',BASEURL,2,ART+'ivuewizard.png',FANART,'')
    addDir('MAINTENANCE',BASEURL,3,ART+'MAINTENANCE.png',FANART,'')
    setView('movies', 'MAIN')

def CUSTOMIVUE():
    addDir('INSTALL IVUE TV GUIDE',BASEURL+'/wizard/ivue/ivuetvguide.zip',5,ART+'ivueinstall.jpg',FANART,'')
    addDir('INSTALL IVUE RECOMENDED SETTINGS',BASEURL+'/wizard/ivue/settings.xml',17,ART+'settings.jpg',FANART,'')
    addDir('RESET IVUE TV GUIDE DATABASE','url',18,ART+'reset.jpg',FANART,'')
    addDir('INSTALL Latest addon file',BASEURL+'/wizard/ivue/addons.ini',19,ART+'addon.jpg',FANART,'')
    addDir('INSTALL SKINS TV GUIDE',BASEURL+'/wizard/ivue/skins.zip',6,ART+'skins.jpg',FANART,'')    
    setView('movies', 'MAIN')
	
def MAINTENANCE():
    addDir('DELETE CACHE','url',4,ART+'deletecache.png',FANART,'')
    addDir('FORCE REFRESH','url',10,ART+'repoupdate.png',FANART,'Force Refresh All Repos')
    setView('movies', 'MAIN')
	
################################
###    FIX REPOS&ADDONS      ###
################################

def UPDATEREPO():
    xbmc.executebuiltin( 'UpdateLocalAddons' )
    xbmc.executebuiltin( 'UpdateAddonRepos' )
    dialog = xbmcgui.Dialog()
    dialog.ok("Ivue Wizard", '','                                 REFRESH SUCCESSFUL :)', "                          [COLOR gold]Brought To You By Ivue Wizard[/COLOR]")
    return
    
#################################
###  Tecbox Ivue  Maintenance ###
#################################

def CUSTOMSET(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Tecbox Ivue Wizard", '                               Install Recomended Settings'):
        print '###'+AddonTitle+' - CUSTOM IVUE SETTINGS###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.tvguidetecbox',''))
        advance=os.path.join(path, 'settings.xml')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== Tecbox Ivue Wizard - WRITING RECOMENDED    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "                               Done Adding RECOMENDED Settings")  
    return
	
#################################
###addon Move File to guide ###
#################################

def CUSTOMSET1(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Move File to guide data", ' Install Latest addon.ini'):
        print '###'+AddonTitle+' - iptv SETTINGS###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.tvguidetecbox',''))
        advance=os.path.join(path, 'addons.ini')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== Tecbox Ivue Wizard - WRITING RECOMENDED    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "Done Adding latest addon file")  
    return

#################################
###  Tecbox delete database ###
#################################

def DELETEIVUEDB():
    ivue_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/script.tvguidetecbox/'), '')
    if os.path.exists(ivue_cache_path)==True:    
        for root, dirs, files in os.walk(ivue_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete IVUE database Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
				

    dialog = xbmcgui.Dialog()
    dialog.ok("Ivue Maintenance", "       All Cache Files Removed", "          [COLOR yellow]Brought To You By Ivue using Xunity Maintenance wizard[/COLOR]")

#################################
###  Tecbox Ivue install  ###
#################################

def WIZARD(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Tecbox Ivue Wizard","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("Tecbox Ivue Wizard", "Please restart kodi//xbmc for changes To Take Effect","[COLOR yellow]Brought To You By Tecbox Ivue TV[/COLOR]")

#################################
###  Ivue Skins install  ###
#################################
	
def WIZARD1(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons/script.tvguidetecbox/resources',''))
    dp = xbmcgui.DialogProgress()
    dp.create("Tecbox Ivue Wizard","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home/addons/script.tvguidetecbox/resources',''))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("Tecbox Ivue Wizard", "Please restart kodi//xbmc for changes To Take Effect","[COLOR yellow]Brought To You By Tecbox Ivue TV[/COLOR]")

    ############################################################        STANDARD CACHE          ###############################################################  
	
def deletecachefiles(url):
    print '############################################################       DELETING STANDARD CACHE             ###############################################################'
    xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
    if os.path.exists(xbmc_cache_path)==True:    
        for root, dirs, files in os.walk(xbmc_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete XBMC Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
              # Set path to Cydia Archives cache files
                             

    # Set path to What th Furk cache files
    wtf_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.whatthefurk/cache'), '')
    if os.path.exists(wtf_cache_path)==True:    
        for root, dirs, files in os.walk(wtf_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete WTF Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                # Set path to 4oD cache files
    channel4_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.4od/cache'), '')
    if os.path.exists(channel4_cache_path)==True:    
        for root, dirs, files in os.walk(channel4_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete 4oD Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                # Set path to BBC iPlayer cache files
    iplayer_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache'), '')
    if os.path.exists(iplayer_cache_path)==True:    
        for root, dirs, files in os.walk(iplayer_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete BBC iPlayer Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                
                # Set path to Simple Downloader cache files
    downloader_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/script.module.simple.downloader'), '')
    if os.path.exists(downloader_cache_path)==True:    
        for root, dirs, files in os.walk(downloader_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Simple Downloader Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                # Set path to ITV cache files
    itv_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.itv/Images'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(itv_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ITV Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
				
                # Set path to temp cache files
    temp_cache_path = os.path.join(xbmc.translatePath('special://home/temp'), '')
    if os.path.exists(temp_cache_path)==True:    
        for root, dirs, files in os.walk(temp_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete TEMP dir Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
				

    dialog = xbmcgui.Dialog()
    dialog.ok("Ivue Maintenance", "       All Cache Files Removed", "          [COLOR yellow]Brought To You By Ivue wizard[/COLOR]")
 
        
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
          
        
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

N = base64.decodestring('')
T = base64.decodestring('L2FkZG9ucy50eHQ=')
B = base64.decodestring('')
F = base64.decodestring('')
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
        
if mode==None or url==None or len(url)<1:
        INDEX()

elif mode==1:
        REPOMAINTENANCE()

elif mode==2:
        CUSTOMIVUE()

elif mode==3:
        MAINTENANCE()
		
elif mode==4:
        deletecachefiles(url)
		
elif mode==5:
        WIZARD(name,url,description)

elif mode==6:
        WIZARD1(name,url,description)
		
elif mode==10:
        UPDATEREPO()
		
elif mode==17:
        CUSTOMSET(url,name)

elif mode==18:
        DELETEIVUEDB()
		
elif mode==19:
        CUSTOMSET1(url,name)
elif mode==20:
        CUSTOMSET2(url,name)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
