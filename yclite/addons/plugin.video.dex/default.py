# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,base64,xbmcaddon,os,requests
PLUGIN='plugin.video.dex'
ADDON = xbmcaddon.Addon(id=PLUGIN)
username = ADDON.getSetting('user')
password = ADDON.getSetting('pass')
loggedin = ADDON.getSetting('loggedin')
first = ADDON.getSetting('first')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
_addon = xbmcaddon.Addon()
_path = _addon.getAddonInfo("path")
addonDir = ADDON.getAddonInfo('path').decode("utf-8")
BASE = 'http://185.115.32.12:8000/'
def start_menu():
        addDir('Configure Dexter TV','1',3,'')
        addDir('Generate INI[I] For Use With Renegades Ivue Or TV guide[/I]','1',6,'')
def createini():
    dialog = xbmcgui.Dialog()
    with open(addonDir+"/dexter.ini", "w") as f:
        url = ('http://185.115.32.12:8000/panel_api.php?username=%s&password=%s'%(username,password))
        r = requests.get(url)
        match=re.compile('"name":"(.+?)".+?stream_id":"(.+?)"').findall(r.content)
        f.write('[plugin.video.dex]\n')
        for name,stream in match:
            f.write(name+'=plugin://plugin.video.dex/?url='+stream+'&mode=55\n')
        f.close()
        dialog.ok('All Done','Created INI In The addons/plugin.video.dex/')
def inifile(url):
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Featching Your Video','g')
        dp.close()
        play.play('http://185.115.32.12:8000/live/%s/%s/%s.m3u8'%(username,password,url))
def do_configure():
                dialog = xbmcgui.Dialog()
                tecleado = keyboard_input(username,'username')
                set_setting('user',tecleado)
                tecleado2 = keyboard_input(password,'password')
                set_setting('pass',tecleado2)
                r = requests.get(BASE+'panel_api.php?'+'&username='+tecleado+'&password='+tecleado2)
                step1 = (BASE+'get.php?'+'username='+tecleado+'&password='+tecleado2+'&type=m3u&output=hls')
                match=re.compile('auth":(.+?)').findall(r.content)
                for auth in match:
                    if auth == '1':
                        dialog.ok('You Are Now Logged in', 'THANK YOU !')
                        set_setting('loggedin','1')
                        file_path_settings = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'userdata', 'addon_data', 'pvr.iptvsimple', 'settings.xml')
                        folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'userdata', 'addon_data', 'pvr.iptvsimple')
                        tecleado2 = keyboard_input('1','TimeShift In Hours')
                        timeshift=tecleado2

                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                            
                        file = open(file_path_settings, 'w')
                        file.write('<settings>\n')
                        file.write('<setting id="epgCache" value="true" />\n')
                        file.write('<setting id="epgPath" value="" />\n')
                        file.write('<setting id="epgPathType" value="1" />\n')
                        file.write('<setting id="epgTSOverride" value="true" />\n')
                        file.write('<setting id="epgTimeShift" value="%s.000000" />\n'%timeshift)
                        file.write('<setting id="epgUrl" value="http://50.7.136.90/epg/epg1.php" />\n')
                        file.write('<setting id="logoBaseUrl" value="" />\n')
                        file.write('<setting id="logoFromEpg" value="2" />\n')
                        file.write('<setting id="logoPath" value="" />\n')
                        file.write('<setting id="logoPathType" value="1" />\n')
                        file.write('<setting id="m3uCache" value="true" />\n')
                        file.write('<setting id="m3uPath" value="" />\n')
                        file.write('<setting id="m3uPathType" value="1" />\n')
                        file.write('<setting id="m3uUrl" value="%s" />\n'%step1)
                        file.write('<setting id="sep1" value="" />\n')
                        file.write('<setting id="sep2" value="" />\n')
                        file.write('<setting id="sep3" value="" />\n')
                        file.write('<setting id="startNum" value="1" />\n')
                        file.write('</settings>\n')
                        file.close()

                        dialog = xbmcgui.Dialog()
                        dialog.ok('Configuration of PVR is Successful', 'The PVR Simple Client of you KODI has been successfully configured. Please restart Kodi for the changes to take effect.')
                    else:
                        dialog.ok('error','Incorrect User/password')

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Status...","Downloading Content",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60) 
            dp.update(percent, mbs, e)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close()
import zipfile

def all(_in, _out, dp=None):
    if dp:
        return allWithProgress(_in, _out, dp)

    return allNoProgress(_in, _out)
        

def allNoProgress(_in, _out):
    try:
        zin = zipfile.ZipFile(_in, 'r')
        zin.extractall(_out)
    
    except Exception, e:
        print str(e)
        return False

    return True


def allWithProgress(_in, _out, dp):
    zin    = zipfile.ZipFile(_in,  'r')
    nFiles = float(len(zin.infolist()))
    count  = 0

    try:
        for item in zin.infolist():
            count += 1
            update = count / nFiles * 100
            dp.update(int(update))
            try:
                zin.extract(item, _out)
            except Exception, e:
                print str(e)

    
    except Exception, e:
        print str(e)
        return False

    return True



def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0:
        try:
            os.remove(filename)
            breakn
        except:
            tries -= 1

        else:
            return
    time.sleep(1)		
   
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True
def set_setting(name,value):
    ADDON.setSetting(name,value )

def keyboard_input(default_text="", title="", hidden=False):
    keyboard = xbmc.Keyboard(default_text,title,hidden)
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        tecleado = keyboard.getText()
    else:
        tecleado = ""
    return tecleado

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok


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

 
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        start_menu()
elif mode==3:
        do_configure()
elif mode==55:
        inifile(url)
elif mode==6:
        createini()


xbmcplugin.endOfDirectory(int(sys.argv[1]))

 