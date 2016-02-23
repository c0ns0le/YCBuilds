import sys,urllib,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,json
import urlresolver
import requests
from addon.common.addon import Addon
from addon.common.net import Net
from metahandler import metahandlers

#DiziBox Add-on Created By Mucky Duck (2/2016)

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.mddizibox'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
metaset = selfAddon.getSetting('enable_meta')
metaget = metahandlers.MetaData(preparezip=False)
baseurl = 'http://www.dizibox.com'
net = Net()




def CAT():
        addDir('[B][COLOR white]Popular Episodes[/COLOR][/B]',baseurl+'/populer-dizilerden-son-bolumler/',1,icon,fanart,'')
        addDir('[B][COLOR white]Latest Episodes[/COLOR][/B]',baseurl,1,icon,fanart,'')
        addDir('[B][COLOR white]Popular Shows[/COLOR][/B]',baseurl+'/arsiv/',1,icon,fanart,'')
        addDir('[B][COLOR white]Top IMDB[/COLOR][/B]',baseurl+'/arsiv/?orderby=imdb',1,icon,fanart,'')
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',6,icon,fanart,'')
        addDir('[B][COLOR white]Genre[/COLOR][/B]',baseurl,2,icon,fanart,'')
        addDir('[B][COLOR white]A/Z[/COLOR][/B]',baseurl,5,icon,fanart,'')




def INDEX(url):
        link = OPEN_URL(url)
        try:
                all_links = regex_get_all(link, '<h1 class', '</article><div')
        except:
                all_links = regex_get_all(link, '<h1 class', '</article><div')
        all_videos = regex_get_all(str(all_links), '<article', '</article>')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, 'alt="', '"').replace('.sezon','.Season').replace('.blm','.Episode')
                name = addon.unescape(name)
                name = name.encode('ascii', 'ignore').decode('ascii')
                url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
                thumb = regex_from_to(a, 'src="', '"')
                
                if metaset=='true':
                        if '/diziler/' not in url:
                                addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,3,thumb,items,'',name)
                        else:
                                addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,7,thumb,items,'',name)
                else:
                        if '/diziler/' not in url:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,3,thumb,fanart,'')
                        else:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,7,thumb,fanart,'')
        try:
                match = re.compile("<a class='page-numbers' href='(.*?)'>(.*?)</a>").findall(link)
                for url, pn in match:
                        addDir('[I][B][COLOR cyan]Page %s >>>[/COLOR][/B][/I]' %pn,url,1,icon,fanart,'')
        except: pass
        setView('tvshows', 'show-view')




def SEA(url,name,description,show_title):
        if show_title == None:
             show_title =  description  
        link = OPEN_URL(url)
        try:
                thumb = re.compile('<img .*?rc="(.*?)"').findall(link)[0]
        except:
                thumb = icon
        #match=re.compile('/dizi.*?/(.*?)/').findall(url)
        all_links = regex_get_all(link, 'seasons-list', '</div>')
        all_videos = regex_get_all(str(all_links), '<a', '</a>')
        items = len(all_videos)
        for a in all_videos:
                seas = regex_from_to(a, 'button .*?>', '<').replace('. Sezon','')
                name2 = regex_from_to(a, '/dizi.*?/', '/').replace('. Sezon','')
                url2 = 'http://www.dizibox.com/dizi/'+name2+'/'+seas+'-sezon-'+name2
                if metaset=='true':
                        if '/1-' in url2:
                                url2 = url
                                addDir2('[B][COLOR white]Season %s[/COLOR][/B]' %seas,url2,8,thumb,items,'',show_title)
                        else:
                                addDir2('[B][COLOR white]Season %s[/COLOR][/B]' %seas,url2,8,thumb,items,'',show_title)
                else:
                        if '/1-' in url2:
                                url2 = url
                                addDir('[B][COLOR white]Season %s[/COLOR][/B]' %seas,url2,8,thumb,fanart,'')
                        else:
                                addDir('[B][COLOR white]Season %s[/COLOR][/B]' %seas,url2,8,thumb,fanart,'')
        setView('tvshows', 'show-view')



def EPI(url,name,iconimage,show_title):
        link = OPEN_URL(url)
        match=re.compile('class="post-title"> <a href="(.*?)" class=".*?">(.*?)</a> <a href=".*?" class="date">.*?</a></div>').findall(link) 
        items = len(match)
        for url, name2 in match:
                name2 = name2.replace('.Sezon','.').replace('.Blm','').replace('. ve','&')
                name2 = addon.unescape(name2)
                name3 = re.split(r'\.', name2, re.I)[0]
                name4 = re.split(r'\.', name2, re.I)[1]
                if metaset=='true':
                        addDir2('[B][COLOR white]Season %s[/COLOR][/B] [B][COLOR cyan]Episode %s[/COLOR][/B]' %(name3,name4),url,3,iconimage,items,'',show_title)
                else:
                        addDir('[B][COLOR white]Season %s[/COLOR][/B] [B][COLOR cyan]Episode %s[/COLOR][/B]' %(name3,name4),url,3,iconimage,fanart,'')
        setView('tvshows', 'show-view')



def LINK(url,name,iconimage,show_title):
        link = OPEN_URL(url)
        match=re.compile("<option.*?'(.*?)'.*?>(.*?)</option>").findall(link) 
        items = len(match)
        for url2, name2 in match:
                if 'Kset' not in name2:
                        url2 = url2.replace('woca-current-page',url)
                        if metaset=='true':
                                addDir2('[B][COLOR white]%s[/COLOR][/B]' %name2,url2,4,iconimage,items,'',show_title)
                        else:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url2,4,iconimage,fanart,'')
        setView('tvshows', 'show-view')




def SEARCH():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = baseurl+'/?s='+search
                INDEX(url)




def GENRE(url):
        link = OPEN_URL(url)
        match=re.compile("<li><a href='(.*?)'>(.*?)</a></li>").findall(link) 
        for url, name in match:
                name = name.replace('Aile','Family').replace('Aksiyon','Action').replace('Belgesel','Documentary')
                name = name.replace('Bilimkurgu','Science fiction').replace('Biyografi','Biography')
                name = name.replace('Dram','Drama').replace('Gerilim','Thriller').replace('Gizem','Mystery')
                name = name.replace('Komedi','Comedy').replace('Korku','Fear').replace('Macera','Adventure')
                name = name.replace('Mini Dizi','Miniseries').replace('Mzik','Music').replace('Mzikal','Musical')
                name = name.replace('Politik','Political').replace('Romantik','Romantic').replace('Sava','War').replace('Spor','Sport')
                name = name.replace('Su','Crime').replace('Tarih','History')
                if '/tur/' in url:
                        nono = ['Animasyon', 'Bilim kurgu', 'Casusluk', 'Fantastik', 'Mecha', 'Polisiye']
                        if name not in nono:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,1,icon,fanart,'')
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_TITLE )




def AZ(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, 'alphabetical-category-list', '</ul>')
        all_videos = regex_get_all(str(all_links), '<li>', '</li>')
        for a in all_videos:
                name = regex_from_to(a, 'title="', '"')
                name = addon.unescape(name)
                name = name.encode('ascii', 'ignore').decode('ascii')
                url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,7,icon,fanart,name)




def RESOLVE(url,name,iconimage):
        link = OPEN_URL(url)
        link = re.findall(r'<span class="object-wrapper"><IFRAM.*?RC="(.*?)" .*?>', str(link), re.I|re.DOTALL)[0]
        try:
                query = {'v': re.split(r'v=', link, re.I)[1]}
                headers = {'host': 'play.dizibox.net', 'referer': url, 'user-agent':User_Agent}
                link = requests.get(link, params=query, headers=headers).text
                link = link.encode('ascii', 'ignore').decode('ascii')
                try:
                        url = re.compile('"file":"(.*?)"').findall(link)[-1]
                except:
                        url = re.compile('"file":"(.*?)"').findall(link)[0]
                url = url.replace('\/','/')
        except:pass
        try:
                query = {'v': re.split(r'v=', link, re.I)[1]}
                headers = {'host': 'play.dizibox.net', 'referer': url, 'user-agent':User_Agent}
                r = requests.get(link, params=query, headers=headers).text
                r = link.encode('ascii', 'ignore').decode('ascii')
                url = re.compile("create_ifr\('(.*?)\+'\?").findall(r)[0]
                url = url.replace('+','').replace("'","")
                url = urlresolver.resolve(url)
        except:pass
                
        try:
                link = link.replace('&#038;','&')
                if '/vk/' in url:
                        url = url.replace('http://play.dizibox.net/vk/?oid=','http://vk.com/video_ext.php?site=&license=&oid=')
                        url = urlresolver.resolve(link)
        except:pass
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={'Title':description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(str(url))
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                




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
        if mode==4:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def notification(title, message, icon):
        addon.show_small_popup( addon.get_name(), message.title(), 5000, icon)
        return




def addDir2(name,url,mode,iconimage,itemcount,description,show_title):
        show_title = show_title.replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
        try:
                show_title = re.split(r" \|", str(show_title), re.I)[0]
        except: pass
        print '#######################################name='+name
        print '#######################################show_title='+show_title
        print '#######################################url='+url
        meta = metaget.get_meta('tvshow',show_title)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        meta['title'] = name
        contextMenuItems = []
        contextMenuItems.append(('Show Info', 'XBMC.Action(Info)'))
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&show_title="+urllib.quote_plus(show_title)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        if mode==4:
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
show_title=None



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
try:
        show_title=urllib.unquote_plus(params["show_title"])
except:
        pass




if mode==None or url==None or len(url)<1:
        CAT()

elif mode==1:
        INDEX(url)

elif mode==2:
        GENRE(url)

elif mode==3:
        LINK(url,name,iconimage,show_title)

elif mode==4:
        RESOLVE(url,name,iconimage)

elif mode==5:
        AZ(url)

elif mode==6:
        SEARCH()

elif mode==7:
        SEA(url,name,description,show_title)

elif mode==8:
        EPI(url,name,iconimage,show_title)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
