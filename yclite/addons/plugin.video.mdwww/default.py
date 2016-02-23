import urllib,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import urlresolver
import requests
from addon.common.addon import Addon
from addon.common.net import Net
from metahandler import metahandlers

#We Watch Wrestling Add-on Created By Mucky Duck (1/2016)

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.mdwww'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
metaset = selfAddon.getSetting('enable_meta')
metaget = metahandlers.MetaData()
baseurl = 'http://watchwrestling.club/' ##http://entertainment4u.cc/category/2000/ alternate url
baseurl2 = 'http://wewatchwrestlingpodcast.com/'
net = Net()



def CAT():
        addDir('[B][COLOR white]Wrestling[/COLOR][/B]','url',1,icon,fanart,'')
        #addDir('[B][COLOR white]TV-Shows[/COLOR][/B]',baseurl+'tv-shows/',9,icon,fanart,'')
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',7,icon,fanart,'')
        addDir('[B][COLOR white]Movies[/COLOR][/B]','url',3,icon,fanart,'')
        addDir('[B][COLOR white]Anime[/COLOR][/B]',baseurl+'anime/',9,icon,fanart,'')
        addDir('[B][COLOR white]Sport[/COLOR][/B]','url',6,icon,fanart,'')
        




def WRESTLING():
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',7,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Date[/COLOR][/B]',baseurl+'category/wrestling/?orderby=date',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Title[/COLOR][/B]',baseurl+'category/wrestling/?orderby=title',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Views[/COLOR][/B]',baseurl+'category/wrestling/?orderby=view',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Comments[/COLOR][/B]',baseurl+'category/wrestling/?orderby=comment',8,icon,fanart,'')
        addDir('[B][COLOR white]WWE[/COLOR][/B]',baseurl,2,icon,fanart,'')
        addDir('[B][COLOR white]TNA[/COLOR][/B]',baseurl+'category/wrestling/tna/',8,icon,fanart,'')
        addDir('[B][COLOR white]ROH[/COLOR][/B]',baseurl+'category/wrestling/roh/',8,icon,fanart,'')
        addDir('[B][COLOR white]NJPW[/COLOR][/B]',baseurl+'category/wrestling/njpw/',8,icon,fanart,'')
        addDir('[B][COLOR white]Lucha Underground[/COLOR][/B]',baseurl+'category/wrestling/lucha-underground/',8,icon,fanart,'')
        addDir('[B][COLOR white]Wrestling Pay Per Views[/COLOR][/B]',baseurl+'category/wrestling/wrestling-pay-per-views/',8,icon,fanart,'')
        addDir('[B][COLOR white]Wrestlemania 1-31[/COLOR][/B]',baseurl+'category/wrestlemania-1-31-hd/',8,icon,fanart,'')
        addDir('[B][COLOR white]Wrestling Library[/COLOR][/B]',baseurl+'category/wrestling/wrestling-library/',8,icon,fanart,'')




def WWE(url):
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',7,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Date[/COLOR][/B]',baseurl+'category/wrestling/wwe/?orderby=date',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Title[/COLOR][/B]',baseurl+'category/wrestling/wwe/?orderby=title',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Views[/COLOR][/B]',baseurl+'category/wrestling/wwe/?orderby=view',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Comments[/COLOR][/B]',baseurl+'category/wrestling/wwe/?orderby=comment',8,icon,fanart,'')
        link = OPEN_URL(url)
        all_links = regex_get_all(link, '>WWE</a>', '</ul>')
        all_videos = regex_get_all(str(all_links), '<li', '</li>')
        for a in all_videos:
                name = regex_from_to(a, 'href=.*?>', '<')
                url = regex_from_to(a, 'href="', '"')
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,8,icon,fanart,'')




def MOVIES():
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',7,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Date[/COLOR][/B]',baseurl+'category/movies/?orderby=date',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Title[/COLOR][/B]',baseurl+'category/movies/?orderby=title',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Views[/COLOR][/B]',baseurl+'category/movies/?orderby=view',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Comments[/COLOR][/B]',baseurl+'category/movies/?orderby=comment',8,icon,fanart,'')
        addDir('[B][COLOR white]Genres[/COLOR][/B]',baseurl,4,icon,fanart,'')
        addDir('[B][COLOR white]Years[/COLOR][/B]',baseurl+'years/',5,icon,fanart,'')
        addDir('[B][COLOR white]Bollywood Movies[/COLOR][/B]',baseurl+'category/movies/bollywood-movies/',8,icon,fanart,'')
        addDir('[B][COLOR white]Chinese Movies[/COLOR][/B]',baseurl+'category/movies/chinese-movies/',8,icon,fanart,'')
        addDir('[B][COLOR white]Korean Movies[/COLOR][/B]',baseurl+'category/movies/korean-movies/',8,icon,fanart,'')




def SPORTS():
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',7,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Date[/COLOR][/B]',baseurl+'category/sports/?orderby=date',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Title[/COLOR][/B]',baseurl+'category/sports/?orderby=title',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Views[/COLOR][/B]',baseurl+'category/sports/?orderby=view',8,icon,fanart,'')
        addDir('[B][COLOR white]Sort By Comments[/COLOR][/B]',baseurl+'category/sports/?orderby=comment',8,icon,fanart,'')
        



def INDEX(url):
        link = OPEN_URL(url)
        try:
                match = re.compile("<span class='pages'>(.*?)</span>").findall(link)[0]
                addLink('[I][B][COLOR red]%s[/COLOR][/B][/I]' %match,'url','',icon,fanart,'')
        except: pass
        all_videos = regex_get_all(link, 'class="col-md-3', '<div class="clearfix">')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, 'title="', '"')
                name = name.replace('HD Free Online','').replace('Watch ','')
                name = addon.unescape(name)
                name = name.encode('ascii', 'ignore').decode('ascii')
                url = regex_from_to(a, 'href="', '"')
                thumb = regex_from_to(a, 'src="', '"')
                if metaset=='true':
                        if 'tv-show' or 'anime' in url:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,10,thumb,fanart,'')
                        else:
                                addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,10,thumb,items)
                else:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,10,thumb,fanart,'')
        try:
                np=re.compile('<a class="nextpostslink" rel="next" href="(.*?)">').findall(link)[0] 
                addDir('[I][B][COLOR red]Next Page >>>[/COLOR][/B][/I]',np,8,icon,fanart,'')
        except: pass
        setView('movies', 'movie-view')




def INDEX2(url):
        link = OPEN_URL(url)
        try:
                match = re.compile("<span class='pages'>(.*?)</span>").findall(link)[0]
                addLink('[I][B][COLOR red]%s[/COLOR][/B][/I]' %match,'url','',icon,fanart,'')
        except: pass
        all_videos = regex_get_all(link, '<div class="wpb_wrapper">', '</h3>')
        items = len(all_videos)
        print url
        for a in all_videos:
                name = regex_from_to(a, 'h3>', '<')
                name = name.replace('HD Free Online','').replace('Watch ','')
                name = addon.unescape(name)
                name = name.encode('ascii', 'ignore').decode('ascii')
                url = regex_from_to(a, 'href="', '"')
                thumb = regex_from_to(a, 'src="', '"')
                if metaset=='true':
                        if 'tv-show' or 'anime' in url:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,8,thumb,fanart,'')
                        else:
                                addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,10,thumb,items)
                else:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,10,thumb,fanart,'')
        try:
                np=re.compile('<a class="nextpostslink" rel="next" href="(.*?)">').findall(link)[0] 
                addDir('[I][B][COLOR red]Next Page >>>[/COLOR][/B][/I]',np,9,icon,fanart,'')
        except: pass
        setView('movies', 'movie-view')




def LINKS(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, '<div class="wpb_column vc_column_container', '</div></div></div>')
        all_videos = regex_get_all(str(all_links), '<div class="wpb_wrapper">', '</div></div>')
        for a in all_videos:
                name = regex_from_to(a, 'blank">', '<').replace('<span class="wpb_button  wpb_btn-danger wpb_regularsize">','')
                name = name.replace('<i class="vc_btn3-icon fa fa-play-circle-o">','')
                name = addon.unescape(name)
                name = name.encode('ascii', 'ignore').decode('ascii')
                url = regex_from_to(a, 'href="', '"')
                print url
                name2 = url.replace('http://','').replace('https','').replace('www.','')
                name2 = re.split(r'\.', name2, re.I)[0]
                name3 = regex_from_to(a, '</i>', '<')
                if name == '':
                        name = name3
                if name > '':
                        if 'watchwrestling.club' not in url:
                                if 'youwatch' in url:
                                        addDir('[B][I][COLOR red]Watch[/COLOR][/I] [COLOR white]%s[/COLOR] [I][COLOR red]At [/COLOR][/I] [COLOR white]%s[/COLOR][/B]' %(name,name2),url,99,'',fanart,'')
                                else:
                                        addDir('[B][I][COLOR red]Watch[/COLOR][/I] [COLOR white]%s[/COLOR] [I][COLOR red]At [/COLOR][/I] [COLOR white]%s[/COLOR][/B]' %(name,name2),url,100,'',fanart,'')
        setView('movies', 'movie-view')




def SEARCH():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = baseurl+'/?s='+search
                INDEX(url)




def GENRE(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, '>Genres</a>', '</ul>')
        all_videos = regex_get_all(str(all_links), '<li', '</li>')
        for a in all_videos:
                name = regex_from_to(a, 'href=.*?>', '<')
                url = regex_from_to(a, 'href="', '"')
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,8,icon,fanart,'')




def YEARS(url):
        link = OPEN_URL(url)
        match = re.compile('<a class="wpb_button_a" title="(.*?)" href="(.*?)">').findall(link)
        for name, url in match:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,8,icon,fanart,'')




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




def RESOLVE(name,url,iconimage):
        url1 = urlresolver.resolve(url)
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={'Title':description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(str(url1))
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)




def YWATCHRESOLVE(name,url,iconimage):
        link = OPEN_URL(url)
        link = re.findall(r'<IFRAM.*?RC="(.*?)" .*?>', str(link), re.I|re.DOTALL)[0]
        link = link.replace('//','http://').replace('\n','')
        headers = {}
        headers['User-Agent'] = User_Agent
        link = requests.get(link, headers=headers).text
        link = re.findall(r'<IFRAM.*?RC="(.*?)" .*?>', str(link), re.I|re.DOTALL)[0]
        video_id = re.split(r'l?', link, re.I)[1].replace('?','')
        form_data={video_id:''}
        host = link.replace('http://','').replace('https://','').partition('/')[0]
        headers = {'host': host, 'referer': link, 'user-agent':User_Agent}
        link = requests.get(link, data=form_data, headers=headers).text
        try:
                url = re.compile('file:"(.*?)"').findall(link)[-1]
        except:
                url = re.compile('file:"(.*?)"').findall(link)[0]
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
        if iconimage=='':
                iconimage=icon
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description} )
        liz.setProperty('fanart_image', fanart)
        if mode==100 or mode==99:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def addDir2(name,url,mode,iconimage,itemcount):
        name = name.replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
        splitName=name.partition('(')
        simplename=""
        simpleyear=""
        if len(splitName)>0:
            simplename=splitName[0]
            simpleyear=splitName[2].partition(')')
        if len(simpleyear)>0:
            simpleyear=simpleyear[0]
        meta = metaget.get_meta('movie',simplename,simpleyear)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        contextMenuItems = []
        contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)')),
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        name = name+'[COLOR white]'+'[/COLOR]'
        if mode==100 or mode==99:
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
site=None

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
        WRESTLING()

elif mode==2:
        WWE(url)

elif mode==3:
        MOVIES()

elif mode==4:
        GENRE(url)

elif mode==5:
        YEARS(url)

elif mode==6:
        SPORTS()

elif mode==7:
        SEARCH()

elif mode==8:
        INDEX(url)

elif mode==9:
        INDEX2(url)

elif mode==10:
        LINKS(url)

elif mode==99:
        YWATCHRESOLVE(name,url,iconimage)

elif mode==100:
        RESOLVE(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
