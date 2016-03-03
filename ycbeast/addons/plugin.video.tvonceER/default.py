import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
import HTMLParser
from TheYid.common.addon import Addon
from TheYid.common.net import Net

addon_id = 'plugin.video.tvonceER'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'tvonceER.db')
net = Net()
addon = Addon('plugin.video.tvonceER', sys.argv)
BASE_URL = 'http://tvonce.com/'
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
text = addon.queries.get('text', None)

def GetTitles2(section, url): 
    try:
        pageUrl = url
        print pageUrl
        html = net.http_GET(pageUrl).content              
        match = re.compile('<li><a title=".+?" href="http://tvonce.com/(.+?)/">(.+?)</a> <span class="mctagmap_count">.+?</span></li>', re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetTitles1', 'section': section, 'url': 'http://tvonce.com/' + movieUrl, 'img': 'http://images.cooltext.com/4603051.png' }, {'title':  name.strip()}, img= 'http://images.cooltext.com/4603051.png', fanart=FanartPath + 'fanart.jpg')         
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): 
    try:
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
                match = re.compile('<img  class="newsimage wp-post-image" src="(.+?)" alt=".+?"  title=".+?"/>\s*?<div class="newsimagebody">\s*?<i class="fa fa-chevron-right"></i>\s*?</div>\s*?</div>\s*?</a>\s*?<p class="newstag" style=".+?">\s*?<a href=".+?"  title=".+?">(.+?)</a>\s*?</p>\s*?<h1 class="newstitle"><a href="(.+?)"  title=".+?">(.+?)</a></h1>', re.DOTALL).findall(html)
                for img, name, movieUrl, name1 in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img': img }, {'title':  name.strip() + ' ' + name1}, img= img, fanart=FanartPath + 'fanart.jpg')     
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.jpg')      
        setView('tvshows', 'tvshows-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles(section, url, startPage= '1', numOfPages= '1'): 
    try:
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
                match = re.compile('<img  class="newsimage wp-post-image" src="(.+?)" alt=".+?"  title=".+?"/>\s*?<div class="newsimagebody">\s*?<i class="fa fa-chevron-right"></i>\s*?</div>\s*?</div>\s*?</a>\s*?<p class="newstag" style=".+?">\s*?<a href="(.+?)"  title=".+?">(.+?)</a>\s*?</p>\s*?<h1 class="newstitle"><a href=".+?"  title=".+?">(.+?)</a></h1>', re.DOTALL).findall(html)
                for img, movieUrl, name, name1 in match:
                        addon.add_directory({'mode': 'GetTitles1', 'section': section, 'url': movieUrl, 'img': img }, {'title':  name.strip() + ' ' + name1}, img= img, fanart=FanartPath + 'fanart.jpg')     
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.jpg')      
        setView('tvshows', 'tvshows-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles1(url, img):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<div class="newsarchive">\s*?(.+?)\s*?<a href="(.+?)">(.+?)</a>\s*?</div>').findall(content)
        match1 = re.compile('<h2 class="innerheading">(.+?)</h2><span class="taxonomy-description"><p>.+?</p>').findall(content)
        for name in match1:
                addon.add_directory({'url': url, 'listitem': listitem}, {'title': '[COLOR blue][B]' + name.strip() + '[/COLOR][/B]'}, img= img, fanart=FanartPath + 'fanart.jpg') 
        for date, url, name in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url, 'listitem': listitem, 'img': img}, {'title':  name.strip() + ' - ' + date}, img= img, fanart=FanartPath + 'fanart.jpg')  
    except:
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks(section, url, img, text):
    try:
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)" target="_blank">.+?</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title': host + ' : ' + title }, img= img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

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
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[B][COLOR blue]Latest :[/COLOR] Episodes[/B]'}, img=IconPath + 'tv.png', fanart=FanartPath + 'fanart.jpg') 

        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[B][COLOR blue]Latest :[/COLOR] Seasons[/B]'}, img=IconPath + 'tv.png', fanart=FanartPath + 'fanart.jpg') 

        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL + '/tv-shows/'}, {'title':  '[B][COLOR blue]List :[/COLOR] Episodes & Seasons[/B]'}, img=IconPath + 'tv.png', fanart=FanartPath + 'fanart.jpg') 

        #addon.add_directory({'mode': 'GenreMenu'}, {'title':  '[B][COLOR blue]Genre :[/COLOR] Full Seasons[/B]'}, img=IconPath + 'tv.png', fanart=FanartPath + 'fanart.jpg') 
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green]Search[/COLOR]'}, img=IconPath + 'tv.png', fanart=FanartPath + 'fanart.jpg') 
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'tv.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR yellow][B]www.entertainmentrepo.com  [/B][/COLOR]'}, img=IconPath + 'newart.jpg', fanart=FanartPath + 'newart.jpg') 
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
        url = 'http://tvonce.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="newsoverlay">\s*?<img  class="newsimage wp-post-image" src="(.+?)" alt=".+?"  title="(.+?)"/>\s*?<div class="newsimagebody">\s*?<i class="fa fa-chevron-right"></i>\s*?</div>\s*?</div>\s*?</a>\s*?<p class="newstag" style=".+?">\s*?<a href="(.+?)"  title=".+?">.+?</a>', re.DOTALL).findall(html)
        for img, name, movieUrl in match:
                addon.add_directory({'mode': 'GetTitles1', 'section': section, 'url': movieUrl, 'img': img }, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.jpg') 
        setView('tvshows', 'tvshows-view')
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
elif mode == 'GetTitles2': 
	GetTitles2(section, url)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(url, img)
elif mode == 'GetLinks':
	GetLinks(section, url, img, text)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
xbmcplugin.endOfDirectory(int(sys.argv[1]))