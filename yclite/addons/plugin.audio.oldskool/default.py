import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
from t0mm0.common.addon import Addon

#Old Skool - By Mucky Duck (10/05/2015)

addon_id = 'plugin.audio.oldskool'
plugin = xbmcaddon.Addon(id=addon_id)
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
baseurl1 = 'http://artmeetsscience.co.uk/tapes/'
baseurl2 = 'http://djmzone.info/mixes/mp3/'
baseurl3 = 'http://hardcorenation.co.uk/downloads2015/Mixed%20Hardcore%20MP3%27s/'
baseurl4 = 'http://naientertainment.com/rave/'
baseurl5 = 'http://www.rockabillyhq.com/EPM/'
baseurl6 = 'http://www.djplex.net/mix/'
baseurl7 = 'http://www.deephousepage.com/mixes/'
baseurl8 = 'http://www.raveolution.com/music/techno/'
baseurl9 = 'http://www.djflipside.com/mixes/'
baseurl10 = 'http://music.lomaximoproductions.com/music/'
baseurl11 = 'http://djmarat.rubyx.eu/mixmp3/'
baseurl12 = 'http://www.alldjshere.com/songs/'
baseurl13 = 'http://elvis87.com/playlist/'
baseurl14 = 'http://www.aufect.com/mixes/'
baseurl15 = 'http://trance.flygroup.st/'
baseurl16 = 'http://gystcorp.com/beezo/'
baseurl17 = 'http://www.unrec.com/mixes/'
baseurl18 = 'http://www.sirmixalot.com/songs/'
baseurl19 = 'http://www.oldskoolanthemz.com/media/Tune%20Archive/'
baseurl20 = 'http://delivery.stpb.net/dan/Music/Reggae/'


#baseurl200 = 'http://floatingworldweb.com/MUSIC/'
#baseurl201 = 'http://klav.ma3x.org/Music/'
#baseurl202 = 'http://www.jeffgreenbank.net/songs/Charts/'
#baseurl203 = 'http://sound.offlinemode.org/~firmament/Guest%20Mixes/'
#baseurl204 = 'http://www.allmylove.org/audio/demos/'
#baseurl205 = 'http://www.protoman.com/Music/Music/'
#baseurl206 = 'http://www.ivanos.nl/mp3/Vinyl%20Rips/'
#baseurl207 = 'https://faculty.unlv.edu/kkemtes/Stuff/80s/80s%20Mixes/'
#baseurl208 = 'http://spandyandy.com/wp-content/uploads/2009/music/
#baseurl209 = 'http://ftp.icm.edu.pl/packages/mp3/'   1563
#baseurl210 = 'http://floorripper.com/downloads/'
#baseurl211 = 'http://www.djcodec.net/music/djtriskyl/'
#baseurl212 = 'http://www.shanti.ru/old-music/RadioSets/'
#baseurl213 = 'https://lsd-25.ru/uploads/'
#baseurl214 = 'http://djcotts.net/extern/'
#baseurl215 = 'http://www.808state.com/sounds/'
#baseurl216 = 'http://mindfulinnovations.com/files/Mixes/' trance
#baseurl217 = 'http://muteam.fm/dl/VA%20-%20Progressive%20Psy%20Trance%20Picks%20Vol.18%20%282014%29/'
#baseurl218 = 'http://www.oldschoolgogo.com/mp3s/'






def INDEX():
        addDir('[B][COLOR yellow]alldjshere.com[/COLOR][/B]',baseurl12,55,icon,fanart)
        addDir('[B][COLOR yellow]artmeetsscience.co.uk[/COLOR][/B]',baseurl1,1,icon,fanart)
        addDir('[B][COLOR yellow]aufect.com[/COLOR][/B]',baseurl14,65,icon,fanart)
        addDir('[B][COLOR yellow]deephousepage.com[/COLOR][/B]',baseurl7,30,icon,fanart)
        addDir('[B][COLOR yellow]delivery.stpb.net (reggae,dancehall)[/COLOR][/B]',baseurl20,95,icon,fanart)
        addDir('[B][COLOR yellow]djflipside.com[/COLOR][/B]',baseurl9,40,icon,fanart)
        addDir('[B][COLOR yellow]djmarat.rubyx.eu[/COLOR][/B]',baseurl11,50,icon,fanart)
        addDir('[B][COLOR yellow]djmzone.info[/COLOR][/B]',baseurl2,5,icon,fanart)
        addDir('[B][COLOR yellow]djplex.net[/COLOR][/B]',baseurl6,25,icon,fanart)
        addDir('[B][COLOR yellow]elvis87.com (dance/club)[/COLOR][/B]',baseurl13,60,icon,fanart)
        addDir('[B][COLOR yellow]gystcorp.com/beezo (house,trance,electro,dubstep)[/COLOR][/B]',baseurl16,75,icon,fanart)
        addDir('[B][COLOR yellow]hardcorenation.co.uk (new)[/COLOR][/B]',baseurl3,75,icon,fanart)
        addDir('[B][COLOR yellow]lomaximoproductions.com[/COLOR][/B]',baseurl10,45,icon,fanart)
        addDir('[B][COLOR yellow]naientertainment.com (reggae,dancehall,hiphop)[/COLOR][/B]',baseurl4,15,icon,fanart)
        addDir('[B][COLOR yellow]oldskoolanthemz.com[/COLOR][/B]',baseurl19,90,icon,fanart)
        addDir('[B][COLOR yellow]sirmixalot.com[/COLOR][/B]',baseurl18,85,icon,fanart)
        addDir('[B][COLOR yellow]trance.flygroup.st[/COLOR][/B]',baseurl15,70,icon,fanart)
        addDir('[B][COLOR yellow]unrec.com (house,dnb,techno,jungle,hardcore)[/COLOR][/B]',baseurl17,80,icon,fanart)
        addDir('[B][COLOR yellow]raveolution.com (techno)[/COLOR][/B]',baseurl8,35,icon,fanart)
        addDir('[B][COLOR yellow]rockabillyhq.com/EPM (mixes)[/COLOR][/B]',baseurl5,20,icon,fanart)
        

############################################################################################################################
#####################                             artmeetsscience                                          #################
############################################################################################################################
def BASE1(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>.+?\n').findall(link)
        for url1,name in match:
                nono = ['Name','\r\r    Sign Up\r    Lo..&gt;']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('..&gt;','')
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,1,icon,fanart)
                
                        
def LINKS(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>.+?\n').findall(link)
        for url1,name in match:
                nono = ['Name', '\r\r    Sign Up\r    Lo..&gt;']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('..&gt;','')
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,2,icon,fanart)

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                 djmzone                                              #################
############################################################################################################################

def BASE2(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ['/mixes/', ' Parent Directory', ' 0.jpg', ' 04.jpg', ' 1Mzone.jpg', ' DJ M-Zone - Old Skool _ Rave profile.pdf', ' natz mzone warehouse.wma', ' mzone motivator.wma', ' m_c40d71e7a7e799d090259894f1fd1d23.jpg', ' m-zone mix classics.wma', 'm-zone 7-2-98 doncaster warehouse night.wma', ' l_357d9e3534443d1b81acee56c2409230.jpg', ' WAREHOUSE______________pictures/']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('..&gt;','')
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,5,icon,fanart)
                        
############################################################################################################################
#####################                                   end                                                #################
############################################################################################################################
############################################################################################################################
#####################                              hardcorenation                                          #################
############################################################################################################################

def BASE3(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = [' Parent Directory']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,10,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                         naientertainment.com                                         #################
############################################################################################################################

def BASE4(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = [' Parent Directory',' customizer.html',' getid3/',' rave.asp',' rave.js',' rave.php',' rave.swf',' rave_fullscreen.html',' rave_popout.html',' rave_share.html',' rave_share_example.html',' skins/']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,15,icon,fanart)

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                       www.rockabillyhq.com/EPM/                                      #################
############################################################################################################################

def BASE5(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,20,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                  djplex                                              #################
############################################################################################################################

def BASE6(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,25,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                               deephousepage                                          #################
############################################################################################################################

def BASE7(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for url1,name in match:
                nono = ['Name','Last modified','Size','Description','Parent Directory','1080943_10151782406976252_2056972906_n.jpg']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,30,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                               raveolution                                            #################
############################################################################################################################

def BASE8(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,35,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                djflipside                                            #################
############################################################################################################################

def BASE9(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = [' Parent Directory',' Dj_flipside_logo.jpg',' Dj_flipside_logo_144.jpg',' flipside1400.png',' flipsidePODCAST1400.jpg',' podcast.xml']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,40,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                               lomaximoproductions                                    #################
############################################################################################################################

def BASE10(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for url1,name in match:
                nono = '../'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('..&gt;','')
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,45,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                 djmarat                                              #################
############################################################################################################################

def BASE11(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,50,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                alldjshere                                            #################
############################################################################################################################

def BASE12(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = [' Parent Directory',' BODY &amp; SOUL Vol. 5_1399140399.zip',' BODY &amp; SOUL Vol. 5_1399318004.zip',' BeastSeller_1399244793.zip',' Beautiful Deep Vol.5 2014_1399354751.zip',' Beautiful Deep Vol.5 2014_1399354789.zip',' Beautiful Deep Vol.5 2014_1399460785.zip',' Beautiful Deep Vol.6 2014_1399302399.zip',' Beautiful Life (feat. Cindy Alma).mp3',' DJ Artur Black mix-20.02.2014-February promo Vol.2_1399066459.zip',' Progressive House_1398712524.zip',' Progressive House_1399397267.zip',' Progressive House_1399397311.zip',' ROTANOV - 014 - Best of Deep House 02_1398824725.zip',' ROTANOV - 016 - Progressive Revolution 01_1399017091.zip',' Radio Session 1_1399025815.zip',' Radio Session 1_1399035608.zip',' Radio Session 4_1399236085.zip',' Radio Session 5_1399246593.zip',' Radio Session 5_1399246644.zip',' Radio Session 9_1398815394.zip',' Radio Session 9_1398815409.zip',' Tracks_1398712976.zip',' Tracks_1399012645.zip',' Vocalist Day - Beauty s Sessions 141 Part 1 - Dubstep_1399295159.zip',' Vocalist Day - Beauty s Sessions 141 Part 1 - Dubstep_1399408156.zip',' Vocalist Day - Beauty s Sessions 141 Part 1 - Dubstep_1399408190.zip',' favicon.ico']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,55,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                elvis87.com                                           #################
############################################################################################################################

def BASE13(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,60,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                aufect.com                                            #################
############################################################################################################################

def BASE14(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,65,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                           trance.flygroup.st                                         #################
############################################################################################################################

def BASE15(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for url1,name in match:
                nono = 'Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('..&gt;','')
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,70,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                               gystcorp.com/beezo                                     #################
############################################################################################################################

def BASE16(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for url1,name in match:
                nono = ['Name','Last modified','Size','Description','Parent Directory','Screen Shot 2014-07-31 at 3.25.35 AM.png']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,75,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                unrec                                                 #################
############################################################################################################################

def BASE17(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for url1,name in match:
                nono = ['Name','Last modified','Size','Description','Parent Directory','error_log','m3u/','misc/','mkm3u.php','video/']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,80,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                sirmixalot.com                                        #################
############################################################################################################################

def BASE18(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,85,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                           oldskoolanthemz.com                                        #################
############################################################################################################################

def BASE19(url):
        link = OPEN_URL(url)
        match=re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(link)
        for url1,name in match:
                nono = ' Parent Directory'
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,90,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                           delivery.stpb.net/dan                                      #################
############################################################################################################################

def BASE20(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="(.+?)">(.+?)</a>').findall(link)
        for url1,name in match:
                nono = ['Name','Last modified','Size','Description','Parent Directory']
                ok = '.mp3'
                if name  not in nono:
                        name = name.replace('&amp;','&')
                        url1 = url+url1
                        url1 = url1.replace('&amp;','&')
                        if ok in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,100,icon,fanart)
                        if ok not in url1:
                                addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url1,95,icon,fanart)
                                
############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################
############################################################################################################################
#####################                                                                                      #################
############################################################################################################################

############################################################################################################################
#####################                                  end                                                 #################
############################################################################################################################

                                

                                

def PLAY(name,url):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'audio')
        li = xbmcgui.ListItem('[COLOR green]PLAY[/COLOR] [COLOR yellow]%s[/COLOR]' %name, iconImage=icon, thumbnailImage=icon)
        li.setProperty('fanart_image', fanart)
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)



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


def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Magic Browser")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link



def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultAudio.png", thumbnailImage=iconimage)
        liz.setInfo( type="Audio", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok


def addDir(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultAudio.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        liz.setInfo( type="Audio", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

        
              
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
########################################
if mode==None or url==None or len(url)<1:
        print ""
        INDEX()

elif mode==1:
        print ""+url
        BASE1(url)
        
elif mode==2:
        print ""+url
        LINKS(url)

elif mode==5:
        print ""+url
        BASE2(url)

elif mode==10:
        print ""+url
        BASE3(url)

elif mode==15:
        print ""+url
        BASE4(url)

elif mode==20:
        print ""+url
        BASE5(url)

elif mode==25:
        print ""+url
        BASE6(url)

elif mode==30:
        print ""+url
        BASE7(url)

elif mode==35:
        print ""+url
        BASE8(url)

elif mode==40:
        print ""+url
        BASE9(url)

elif mode==45:
        print ""+url
        BASE10(url)

elif mode==50:
        print ""+url
        BASE11(url)

elif mode==55:
        print ""+url
        BASE12(url)

elif mode==60:
        print ""+url
        BASE13(url)

elif mode==65:
        print ""+url
        BASE14(url)

elif mode==70:
        print ""+url
        BASE15(url)

elif mode==75:
        print ""+url
        BASE16(url)

elif mode==80:
        print ""+url
        BASE17(url)

elif mode==85:
        print ""+url
        BASE18(url)

elif mode==90:
        print ""+url
        BASE19(url)

elif mode==95:
        print ""+url
        BASE20(url)

elif mode==105:
        print ""+url
        BASE21(url)

elif mode==110:
        print ""+url
        BASE22(url)

elif mode==115:
        print ""+url
        BASE23(url)

elif mode==120:
        print ""+url
        BASE24(url)

elif mode==125:
        print ""+url
        BASE25(url)

elif mode==130:
        print ""+url
        BASE26(url)

elif mode==135:
        print ""+url
        BASE27(url)

elif mode==140:
        print ""+url
        BASE28(url)
        
elif mode==100:
        print ""+url
        PLAY(name,url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
