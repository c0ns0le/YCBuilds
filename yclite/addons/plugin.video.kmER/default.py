import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
import HTMLParser
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.video.kmER'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'kmER.db')
net = Net()
addon = Addon('plugin.video.kmER', sys.argv)
BASE_URL = 'http://www.freekidsmovies.net/'
BASE_URL3 = 'http://www.princessmovies.tv'
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)
img = addon.queries.get('img', None)
fanart = addon.queries.get('fanart', None)
text = addon.queries.get('text', None)
#\s*?#

def GetTitles2(section, url, startPage= '1', numOfPages= '1'): #b
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('style=".+?"><a href="(.+?)" target=".+?">(.+?)<', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img': 'https://i.ytimg.com/vi/tNXAwrT_jzk/maxresdefault.jpg', 'fanart': 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg', 'text': name}, {'title':  name.strip()}, img= 'https://i.ytimg.com/vi/tNXAwrT_jzk/maxresdefault.jpg', fanart= 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg')             
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): #p
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<b><span style=".+?;"><a href="(.+?)" target="_blank">(.+?)</a>.+?</span>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img': 'https://i.ytimg.com/vi/tNXAwrT_jzk/maxresdefault.jpg', 'fanart': 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg', 'text': name}, {'title':  name.strip()}, img= 'https://i.ytimg.com/vi/tNXAwrT_jzk/maxresdefault.jpg', fanart= 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg')             
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetTitles1(section, url, startPage= '1', numOfPages= '1'): 
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<h3 class="post-title" style=".+?"><a style=".+?" href="(.+?)"><span style=".+?">(.+?)</span></a></h3>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img': 'https://i.ytimg.com/vi/tNXAwrT_jzk/maxresdefault.jpg', 'fanart': 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg', 'text': name}, {'title':  name.strip()}, img= 'https://i.ytimg.com/vi/tNXAwrT_jzk/maxresdefault.jpg', fanart= 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg')             
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles(section, url, startPage= '1', numOfPages= '1'): 
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<article class=".+?">\s*?<a href="(.+?)" title="(.+?)" rel=".+?" id=".+?">\s*?<div class=".+?"><img width=".+?" height=".+?" src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img': img, 'fanart': fanart, 'text': name}, {'title':  name.strip()}, img= img, fanart= img)      
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart= 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg')
        setView('tvshows', 'tvshows-view')       
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks(section, url, img, fanart, text):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match2 = re.compile("src='http://www.spruto.tv/(.+?)'").findall(content)
        match = re.compile('SRC="(.+?)"').findall(content)
        match3 = re.compile('src="(.+?)"').findall(content)
        match1 = re.compile('<meta name="description" itemprop="description" content="(.+?)" />').findall(content)
        listitem = GetMediaInfo(content)
        for name in match1:
                addon.add_directory({'mode': 'GetLinks1', 'section': section, 'img': img}, {'title':  '[COLOR darkturquoise][B]' + name.strip() + '[/B] [/COLOR]'}, img= img, fanart= img) 
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url': 'http://www.spruto.tv/' + url, 'listitem': listitem, 'img': img, 'text': text}, {'title':  'spruto.tv'}, img= img, fanart= img)
        for url in match + match3:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img= img, fanart= img)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks1(url, img, text):                                           
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('file: "http://www.spruto.tv/(.+?)mp4"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': 'http://www.spruto.tv/' + url + 'mp4', 'listitem': listitem, 'img': img, 'text': text}, {'title':  'Load : ' + text}, img= img , fanart= img)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo1(url, listitem, img, text):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem(text, iconImage= img, thumbnailImage= img)
        li.setProperty('fanart_image', 'https://i.ytimg.com/vi/XJtQ0lNDdnY/maxresdefault.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

def PlayVideo(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

def MainMenu():   
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/',
                             'startPage': '1', 'numOfPages': '2'}, {'title':  '[B]Latest Movies[/B]'}, img=IconPath + 'icon.png', fanart= 'https://i.ytimg.com/vi/XJtQ0lNDdnY/maxresdefault.jpg')
        addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[B]Movies Genre[/B]'}, img=IconPath + 'icon.png', fanart= 'https://i.ytimg.com/vi/XJtQ0lNDdnY/maxresdefault.jpg')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL + '/list-disney-channel-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[B]Disney channel movies[/B]'}, img=IconPath + 'icon.png', fanart= 'https://i.ytimg.com/vi/XJtQ0lNDdnY/maxresdefault.jpg')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/disney-princess/list-of-all-disney-princess-movies.html',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[B]Disney Princess Movies[/B]'}, img=IconPath + 'icon.png', fanart= 'https://i.ytimg.com/vi/XJtQ0lNDdnY/maxresdefault.jpg')
        #addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL3 + '/barbie-movies/list-of-all-barbie-movies.html',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[B]Barbie Movies[/B]'}, img=IconPath + 'icon.png', fanart= 'https://i.ytimg.com/vi/XJtQ0lNDdnY/maxresdefault.jpg')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Search[/COLOR]'}, img=IconPath + 'icon.png', fanart= 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'icon.png', fanart= 'http://bwalles.com/wp-content/uploads/2013/10/Disney-1080p-Wallpaper-10-1024x576.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GenreMenu(): 
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]action [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]adventure [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/animated',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]animated [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/christmas-2',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]christmas [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]comedy [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/disney-nature',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]disney nature [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/dogs',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]dogs [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]drama [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]fantasy [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/musical',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]musical [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/pixar',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]pixar [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/princesses',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]princesses [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/romantic',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]romantic [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/science-fiction',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]science fiction [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/spooky',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lime]Sci-fi [/COLOR] >>'}, img=IconPath + 'icon.png', fanart= 'http://www.hdesktops.com/wp-content/uploads/2013/12/purple-3d-abstract-wallpaper-desktop-background-171.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('Search')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return

def Search(query):
        url = 'http://www.freekidsmovies.net/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<article class=".+?">\s*?<a href="(.+?)" title="(.+?)" rel=".+?" id=".+?">\s*?<div class=".+?"><img width=".+?" height=".+?" src="(.+?)"').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img= img, fanart= img)
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

if mode == 'main': 
	MainMenu()
elif mode == 'GenreMenu':
        GenreMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, url, startPage, numOfPages)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetLinks':
	GetLinks(section, url, img, fanart, text)
elif mode == 'GetLinks1':
	GetLinks1(url, img, text)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem, img, text)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
xbmcplugin.endOfDirectory(int(sys.argv[1]))