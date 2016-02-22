import sys,urllib,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,json
import requests
from addon.common.addon import Addon
from addon.common.net import Net
from metahandler import metahandlers

#izle Add-on Created By Mucky Duck (2/2016)

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.mdizle'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.png'))
metaset = selfAddon.getSetting('enable_meta')
metaget = metahandlers.MetaData()
baseurl = 'http://izlemeyedeger.com'
net = Net()




def CAT():
        addDir('[B][COLOR white]Latest Added[/COLOR][/B]',baseurl+'/film-arsivi?genre=&year=&country=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Most Viewed[/COLOR][/B]',baseurl+'/film-arsivi?genre=&year=&country=&sort=view',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Most Liked[/COLOR][/B]',baseurl+'/film-arsivi?genre=&year=&country=&sort=like',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Worst IMDB[/COLOR][/B]',baseurl+'/film-arsivi?genre=&year=&country=&sort=imdb&orderby=ASC',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Top IMDB[/COLOR][/B]',baseurl+'/film-arsivi?genre=&year=&country=&sort=imdb&orderby=DESC',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Country[/COLOR][/B]',baseurl+'/film-arsivi',7,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',4,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Genre[/COLOR][/B]',baseurl+'/film-arsivi',5,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Year[/COLOR][/B]',baseurl+'/film-arsivi',6,art+'icon2.png',fanart,'')




def INDEX(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, '<div class="section">', '</ul>')
        all_videos = regex_get_all(str(all_links), '<li>', '</li>')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, 'title">', '                            <').replace("&amp;","&").replace("\\r\\n","").replace("\\n","").replace("                                ","").replace('&#39;',"'").replace('&quot;','"').replace('&#039;',"'")
                name = addon.unescape(name)
                url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
                thumb = regex_from_to(a, 'src="', '"')
                rat = regex_from_to(a, '<p>', '<')
                year = regex_from_to(a, 'year">', '<').replace(' ','').replace("\\r\\n","").replace("\\n","")
                print year
                if metaset=='true':
                        addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,3,thumb,items)
                else:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,3,thumb,fanart,'')
        try:
                match = re.compile('<li class=""><a href="(.*?)">(.*?)</a>').findall(link)
                for url, pn in match:
                        addDir('[I][B][COLOR red]Page %s >>>[/COLOR][/B][/I]' %pn,url,1,icon,fanart,'')
        except: pass
        setView('movies', 'movie-view')




def LINK(url):
        link = OPEN_URL(url)
        link = re.findall(r'<if.*?rc="(.*?)" .*?>', link, re.I|re.DOTALL)[0]
        link = OPEN_URL(link)
        try:
                url = re.compile('file: "(.*?)"').findall(link)[-1]
        except:
                url = re.compile('file: "(.*?)"').findall(link)[0]
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={'Title':description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(str(url))
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)




def SEARCH():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = baseurl+'/arama?q='+search
                INDEX(url)




def GENRE(url):
        addDir('[B][COLOR white]All[/COLOR][/B]',baseurl+'/film-arsivi?genre=&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Family[/COLOR][/B]',baseurl+'/film-arsivi?genre=28&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Action[/COLOR][/B]',baseurl+'/film-arsivi?genre=20&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Animation[/COLOR][/B]',baseurl+'/film-arsivi?genre=22&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Documentary[/COLOR][/B]',baseurl+'/film-arsivi?genre=26&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Science fiction[/COLOR][/B]',baseurl+'/film-arsivi?genre=35&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Biography[/COLOR][/B]',baseurl+'/film-arsivi?genre=23&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Drama[/COLOR][/B]',baseurl+'/film-arsivi?genre=27&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Fantasy[/COLOR][/B]',baseurl+'/film-arsivi?genre=29&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Thriller[/COLOR][/B]',baseurl+'/film-arsivi?genre=37&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Mystery[/COLOR][/B]',baseurl+'/film-arsivi?genre=33&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Comedy[/COLOR][/B]',baseurl+'/film-arsivi?genre=24&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Horror[/COLOR][/B]',baseurl+'/film-arsivi?genre=31&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Adventure[/COLOR][/B]',baseurl+'/film-arsivi?genre=21&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Musical[/COLOR][/B]',baseurl+'/film-arsivi?genre=32&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Romantic[/COLOR][/B]',baseurl+'/film-arsivi?genre=34&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]War[/COLOR][/B]',baseurl+'/film-arsivi?genre=38&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Sport[/COLOR][/B]',baseurl+'/film-arsivi?genre=36&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Crime[/COLOR][/B]',baseurl+'/film-arsivi?genre=25&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]History[/COLOR][/B]',baseurl+'/film-arsivi?genre=30&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Far East[/COLOR][/B]',baseurl+'/film-arsivi?genre=40&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        addDir('[B][COLOR white]Western[/COLOR][/B]',baseurl+'/film-arsivi?genre=39&year=&country=&sort=&orderby=',1,art+'icon2.png',fanart,'')
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_TITLE )



def COUNTRY(url):
        headers = {}
        headers['User-Agent'] = User_Agent
        link = requests.get(url, headers=headers).content
        link = addon.unescape(link)
        match=re.compile('<a href="http://www.izlemeyedeger.com/film-arsivi\?genre=\&year=\&country=(.*?)\&sort=\&orderby=" class="gender">').findall(link) 
        for country in match:
                url = 'http://www.izlemeyedeger.com/film-arsivi?genre=&year=&country='+country+'&sort=&orderby='
                country = country.replace('Almanya','Germany').replace('Amerika','America').replace('\xc4\xb0ngiltere','Britain').replace('\xc4\xb0ran','Iranian').replace('S\xc4\xb1rbistan','Serbia')
                country = country.replace('Arjantin','Argentina').replace('Avustralya','Australia').replace('\xc4\xb0rlanda','Ireland').replace('\xc4\xb0spanya','Spain').replace('T\xc3\xbcrkiye','Turkey')
                country = country.replace('Bel\xc3\xa7ika','Belgium').replace('Birle\xc5\x9fik Arap Emirlikleri','United Arab Emirates').replace('\xc4\xb0sve\xc3\xa7','Swedish').replace('Yeni Zelanda','New Zeland').replace('','')
                country = country.replace('Brezilya','Brazil').replace('Bulgaristan','Bulgaria').replace('\xc4\xb0talya','Italy').replace('\xc4\xb0svi\xc3\xa7re','Swiss').replace('Yunanistan','Greece')
                country = country.replace('\xc3\x87ek Cumhuriyeti','Czech Republic').replace('\xc3\x87in','China').replace('Japonya','Japan').replace('Kanada','Canada').replace('Tayvan','Taiwan')
                country = country.replace('Danimarka','Denmark').replace('Endonezya','Indonesia').replace('L\xc3\xbcksemburg','Luxembourg').replace('Macaristan','Hungary')
                country = country.replace('Fransa','France').replace('G\xc3\xbcney Afrika','South Africa').replace('Meksika','Mexican').replace('Norve\xc3\xa7','Norway')
                country = country.replace('G\xc3\xbcney Kore','South Korea').replace('Hindistan','India').replace('Polonya','Poland').replace('Romanya','Romania')
                country = country.replace('Hollanda','Netherlands').replace('Rusya','Russia').replace('\xc5\x9eili','Chile').replace('Singapur','Singapore')
                country = addon.unescape(country)
                if 'implode' not in url:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %country,url,1,art+'icon2.png',fanart,'')
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_TITLE )




def YEAR(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="http://www.izlemeyedeger.com/film-arsivi\?genre=\&year=(.*?)\&country=\&sort=\&orderby=" class="gender">').findall(link) 
        for year in match:
                url = 'http://www.izlemeyedeger.com/film-arsivi?genre=&year='+year+'&country=&sort=&orderby='
                addDir('[B][COLOR white]%s[/COLOR][/B]' %year,url,1,art+'icon2.png',fanart,'')




def regex_from_to(text, from_string, to_string, excluding=True):
        if excluding:
                try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
                except: r = ''
        else:
                try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
                except: r = ''
        return r




def regex_get_all(text, start_with, end_with):
        r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
        return r




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




def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description} )
        liz.setProperty('fanart_image', fanart)
        if mode==3:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def PT(url):
        addon.log('Play Trailer %s' % url)
        notification( addon.get_name(), 'fetching trailer', addon.get_icon())
        xbmc.executebuiltin("PlayMedia(%s)"%url)




def notification(title, message, icon):
        addon.show_small_popup( addon.get_name(), message.title(), 5000, icon)
        return




def addDir2(name,url,mode,iconimage,itemcount):
        name = name.replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
        meta = metaget.get_meta('movie',name)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        name = '[B][COLOR white]' + name + '[/COLOR][/B]'
        meta['title'] = name
        contextMenuItems = []
        if meta['trailer']>'':
                contextMenuItems.append(('Play Trailer', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 8, 'url':meta['trailer']})))
        contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        if mode==3:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems=itemcount)
        else:
             ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True,totalItems=itemcount)
        return ok




def addLink(name,url,mode,iconimage,fanart,description=''):
        #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        #ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok




def OPEN_URL(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = requests.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore').decode('ascii')
    return link




''' Why recode whats allready written and works well,
    Thanks go to Eldrado for it '''

def setView(content, viewType):
        
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if addon.get_setting('auto-view') == 'true':

        print addon.get_setting(viewType)
        if addon.get_setting(viewType) == 'Info':
            VT = '504'
        elif addon.get_setting(viewType) == 'Info2':
            VT = '503'
        elif addon.get_setting(viewType) == 'Info3':
            VT = '515'
        elif addon.get_setting(viewType) == 'Fanart':
            VT = '508'
        elif addon.get_setting(viewType) == 'Poster Wrap':
            VT = '501'
        elif addon.get_setting(viewType) == 'Big List':
            VT = '51'
        elif viewType == 'default-view':
            VT = addon.get_setting(viewType)

        print viewType
        print VT
        
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )




params=get_params()
url=None
name=None
mode=None
iconimage=None
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
        description=urllib.unquote_plus(params["description"])
except:
        pass




if mode==None or url==None or len(url)<1:
        CAT()

elif mode==1:
        INDEX(url)

elif mode==3:
        LINK(url)

elif mode==4:
        SEARCH()

elif mode==5:
        GENRE(url)

elif mode==6:
        YEAR(url)

elif mode==7:
        COUNTRY(url)

elif mode == 8:
        PT(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
