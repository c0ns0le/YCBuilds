import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib, urllib2
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.oneclickwatch'
plugin = xbmcaddon.Addon(id=addon_id)
DB = os.path.join(xbmc.translatePath("special://database"), 'oneclickwatch.db')
BASE_URL = 'http://areaddl.com/'
BASE_URL1 = 'http://watchseries-onlines.ch/'
BASE_URL2 = 'http://www.rls-dl.com/'
BASE_URL4 = 'http://www.tvguide.com/'
BASE_URL5 = 'http://www.moviefone.com/'
BASE_URL6 = 'http://www.pogdesign.co.uk/'
BASE_URL8 = 'http://www.allcinemamovies.com/'
net = Net()
addon = Addon('plugin.video.oneclickwatch', sys.argv)

###### PATHS ###########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
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
name = addon.queries.get('name', None)

################################################################################# Titles OCW #################################################################################

def GetTitles(text, img, section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)<.+? src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img' : img, 'text' : name}, {'title':  name}, img=img, fanart=FanartPath + 'fanart.jpg') 
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage.png', fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- ovg tv index ---------------------------------------------------------------------------------#

def GetTitles8(url):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<li><a href="http://www.allcinemamovies.com/tv-tags/(.+?)">(.+?)</a></li>',re.DOTALL).findall(html)
        for url, name in match:
                addon.add_directory({'mode': 'GetTitles8a', 'url': 'http://www.allcinemamovies.com/tv-tags/' + url}, {'title':  name }, img= 'http://oi57.tinypic.com/zn7zp2.jpg', fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles8a(url, img, text):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<div class="item" style="text-align:center">\s*?<a href="(.+?)" class="spec-border-ie" title="">\s*?<img class="img-preview spec-border show-thumbnail"  src=".+?src=(.+?)&amp;w=130&amp;h=190&amp;zc=1" alt="Watch (.+?) Online"/>',re.DOTALL).findall(html)
        match1 = re.compile('</a></li>   <li><a href="http://www.allcinemamovies.com/tv-tags/(.+?)">.+?</a></li>',re.DOTALL).findall(html)
        for url, img, name in match:
                addon.add_directory({'mode': 'GetTitles8b', 'url': url, 'img' : img, 'text' : name }, {'title':  name}, img= img, fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg')
        for url in match1:
                addon.add_directory({'mode': 'GetTitles8a', 'url': 'http://www.allcinemamovies.com/tv-tags/' + url}, {'title': '[COLOR blue][B][I]Next page... [/B][/I][/COLOR]'}, img=IconPath + 'nextpage.png', fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg')
        setView('tvshows', 'tvshows-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles8b(url, img, text):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                    
        match = re.compile("<li ><a href='http://www.allcinemamovies.com/show/(.+?)'>(.+?)</a></li>",re.DOTALL).findall(html)
        for url, name in match:
                addon.add_directory({'mode': 'GetTitles8c', 'url': 'http://www.allcinemamovies.com/show/' + url, 'img' : img, 'text' : text }, {'title': name + '  - ' +  text }, img= img, fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg')
        setView('tvshows', 'tvshows-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles8c(url, img, text):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<a class="link" href="(.+?)" title=".+?"><span class=".+?">(.+?)</span> <span class="tooltip" original-title="seen"></span></a>',re.DOTALL).findall(html)
        for url, name in match: 
                addon.add_directory({'mode': 'GetLinks', 'url': url , 'img' : img, 'text' : name}, {'title': text + ' - ' + name }, img= img, fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry No Seasons Available[/B][/COLOR],[COLOR blue][B]Check A/Z index search[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#---------------------------------------------------------------------------- TV Calendar index ----------------------------------------------------------------------------------------------------#

def GetTitles6(section, url):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<strong><a href="./day/(.+?)" title="(.+?)">', re.DOTALL).findall(html)
        match1 = re.compile('<div class="month_name"><div class="prev-month"><a href="/cat/(.+?)"><span>.+?</span> <strong>(.+?)</strong></a></div> <h1><a href=".+?">.+?</a></h1> <div class=".+?"><a href=".+?"><span>.+?</span> <strong>.+?</strong></a></div></div><div id="loginbox"', re.DOTALL).findall(html)
        match2 = re.compile('<div class="next-month"><a href="/cat/(.+?)"><span>.+?</span> <strong>(.+?)</strong></a></div></div>\s*?<div class=".+?">', re.DOTALL).findall(html)
        for movieUrl, name in match1:
                addon.add_directory({'mode': 'GetTitles6', 'section': section, 'url': 'http://www.pogdesign.co.uk/cat/' + movieUrl }, {'title': '<< ' + name}, img= 'https://www.globalbrigades.org/media_gallery/thumb/320/0/VRS_Calendar2_512x512x32_2.png',  fanart=FanartPath + 'fanart.jpg') 
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetTitles6a', 'section': section, 'url': 'http://www.pogdesign.co.uk/cat/day/' + movieUrl }, {'title': '[B]' + name.replace('Thursday 1st October 2015', 'Choose a day') + '[/B]'}, img= 'https://www.globalbrigades.org/media_gallery/thumb/320/0/VRS_Calendar2_512x512x32_2.png',  fanart=FanartPath + 'fanart.jpg') 
        for movieUrl, name in match2:
                addon.add_directory({'mode': 'GetTitles6', 'section': section, 'url': 'http://www.pogdesign.co.uk/cat/' + movieUrl }, {'title': name + ' >>'}, img= 'https://www.globalbrigades.org/media_gallery/thumb/320/0/VRS_Calendar2_512x512x32_2.png',  fanart=FanartPath + 'fanart.jpg') 
        setView('tvshows', 'calendar-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles6a(text, img, query, section, name): 
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<div class="contbox ovbox" style=" background-image: url(.+?);">\s*?<h4><a href=".+?">(.+?)<span>.+?</span></a></h4>\s*?<h5><a href=".+?">(.+?)<span>(.+?)/span></a></h5>\s*?<div class=".+?">(.+?)<a href=".+?">.+?</a></div> \s*?<ul class=".+?">\s*?<li><strong>.+?</strong>(.+?)</li>',re.DOTALL).findall(html)
        for img, name1, query1, name, sum, time in match:
                img = 'http://www.pogdesign.co.uk/' + img.replace('(', '').replace(')', '')
                query = name1.replace('[', '').replace(']', '') + name.replace("'", "").replace(' 1,', '01').replace(' 2,', '02').replace(' 3,', '03').replace(' 4,', '04').replace(' 5,', '05').replace(' 6,', '06').replace(' 7,', '07').replace(' 8,', '08').replace(' 9,', '09').replace(' 1<', '01').replace(' 2<', '02').replace(' 3<', '03').replace(' 4<', '04').replace(' 5<', '05').replace(' 6<', '06').replace(' 7<', '07').replace(' 8<', '08').replace(' 9<', '09').replace('Season', 's').replace('Episode', 'e').replace(',', '').replace('<', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
                title = '[COLOR blue][B]' + name1 +'[/B][/COLOR]' + ' - ' + '[COLOR lime]' + query1 + '[/COLOR]' + ' - ' + '[COLOR pink][I]' + name.replace('<', ' ') + '[/I][/COLOR]' + ' - ' + '[COLOR khaki]' + sum + '[/COLOR]' + ' - ' + time
                query = query.replace("Marvel's Agents of S.H.I.E.L.D. ", 'marvels agents of s h i e l d ')
                query = query.replace('The Flash ', 'the flash 2014 ')
                query = query.replace('This Is England ', 'this is england 90 ')
                query = query.replace('Doctor Who ', 'doctor who 2005 ')
                query = query.replace('The Late Late Show Corden ', 'james corden ')
                query = query.replace('Blood and Oil ', 'blood and oil 2015 ')
                query = query.replace('Public Morals ', 'public morals 2015 ')
                query = query.replace('The Voice (US) ', 'the voice ')
                query = query.replace('Empire ', 'empire 2015 ')
                query = query.replace('&', 'and')
                query = query.replace("You're the Worst ", 'youre the worst ')
                query = query.replace('The Player ', 'the player 2015 ')
                query = query.replace('The Moaning of Life ', 'karl pilkington the moaning of life ')
                query = query.replace('Undateable ', 'Undateable 2014 ')
                query = query.replace('Scandal ', 'scandal US ')
                query = query.replace('Satisfaction ', 'satisfaction US ')
                query = query.replace('Jessie ', 'jessie 2011 ')
                query = query.replace('Legends ', 'legends 2014 ')
                addon.add_directory({'mode': 'Search1', 'section': section, 'query': query, 'img': img, 'name': name, 'text': name1 + query1 }, {'title': title}, img= img,  fanart=FanartPath + 'fanart.jpg')
        setView('tvshows', 'calendar-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- moviefone movie index ---------------------------------------------------------------------------------#

def GetTitles5(text, img, query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<img name="replace-image" rel=".+?" id=".+?" class=".+?" src=".+?" data-src="(.+?)" alt="(.+?)"/>',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search2', 'query': query, 'img' : img, 'text' : query}, {'title':  query}, img= img, fanart= 'https://irenehyleung.files.wordpress.com/2012/12/2012-movie-collage31.jpg')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- tvguide movie index ---------------------------------------------------------------------------------#

def GetTitles4(text, img, query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<span class="show-card show-card-small">\s*?<img src="(.+?)" class=".+?" alt=".+?" title="(.+?)" srcset=".+?" width=".+?" height=".+?" />',re.DOTALL).findall(html)
        for img, query in match:
                img = img.replace('100x133.png', '1000x339.png').replace('100x133.jpg', '1000x339.jpg')
                addon.add_directory({'mode': 'Search2', 'query': query, 'img' : img, 'text' : query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart.jpg')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- rls-dl tv index ----------------------------------------------------------------------------------------------------#

def GetTitles3(text, img, query, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                    
                match = re.compile('<div class="thumbn"><img src="(.+?)" alt="(.+?)" /></div>\s*?<div class="filmkutu-bilgi-hover">\s*?<ul class="filmkutu-bilgi-hover-liste">\s*?<li class="izlenme">\s*?<a href=".+?">', re.DOTALL).findall(html)
                for img, query in match:
                        query = query.replace('The Player ', 'The Player 2015 ')
                        query = query.replace('Doctor Who ', 'Doctor Who 2005 ')
                        query = query.replace('Blood and Oil ', 'Blood and Oil 2015 ')
                        query = query.replace('Public Morals ', 'public morals 2015 ')
                        query = query.replace('The Flash ', 'the flash 2014 ')
                        query = query.replace('scandal ', 'scandal US ')
                        query = query.replace('Legends ', 'legends 2014 ')
                        addon.add_directory({'mode': 'Search1', 'section': section, 'query': query, 'img' : img, 'text' : query}, {'title':  query}, img= img, fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage.png', fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg') 
        setView('tvshows', 'tvshows-view')   
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- watchseries-onlines a/z index ----------------------------------------------------------------------------------------------------#

def GetTitles2(section, query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<option class="level-0" value=".+?">(.+?)</option>', re.DOTALL).findall(html)
        for movieUrl in match:
                movieUrl = movieUrl.replace('English Premiere League', 'EPL')
                movieUrl = movieUrl.replace('TNA Bound For Glory', 'TNA iMPACT Wrestling')
                movieUrl = movieUrl.replace('AFL Game Day', 'AFL')
                movieUrl = movieUrl.replace('(', '').replace(')', '')
                movieUrl = movieUrl.replace('Next Step Realty NYC', 'NHL')
                movieUrl = movieUrl.replace('Come Dine With Me', 'College Football')
                movieUrl = movieUrl.replace('Tyler Perry&#8217;s The Haves and the Have Nots', 'UEFA Euro 2016')
                addon.add_directory({'mode': 'Search3', 'section': section, 'query': movieUrl}, {'title': movieUrl.replace('EPL', 'English Premiere League')}, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart= 'http://www.parka-show.com/wp-content/uploads/2014/05/TV-Shows.jpg') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- index search tv 1 ----------------------------------------------------------------------------------------------------#

def Search1(text, img, section, query, name):
    try:
        url = 'http://areaddl.com/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match1 = re.compile('<h2 class="title">(.+?)</h2>', re.DOTALL).findall(html)
        match2 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for name in match1:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR pink][B](' + name + ')[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.jpg')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem , 'img': img, 'text': text }, {'title':  '[COLOR powderblue][B]UpToStream : direct link to[/B][/COLOR]' + ' - ' + text},img=img,  fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in OCW [/B][/COLOR],[COLOR blue][B]Checking next site[/B][/COLOR],"")")
    try:
        url = 'http://new.myvideolinks.xyz/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li><a href="(.+?)">.+?</a></li>', re.DOTALL).findall(html)
        match5 = re.compile("onClick=.+?'(.+?)'", re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for url in match + match5:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title + '  (MVL)'}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in myvideolinks [/B][/COLOR],"")")
    try:
        url = 'http://rlssource.net/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href=(.+?) target=_blank>.+?</a>', re.DOTALL).findall(html)
        match1 = re.compile('<p><IFRAME SRC=(.+?) FRAMEBORDER=0', re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for url in match + match1:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title + '     [rlssource]'}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in rlssource [/B][/COLOR],"")")
    try:
        url = 'http://wanderingsouls.me/wp/index.php/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p style="text-align: center;"><a href=".+?">(.+?)</a></p>', re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title + '  ...(HQ-MQ) [WS]'}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in WS [/B][/COLOR],"")")
    try:
        url = 'http://watchseries-onlines.ch/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<div class="play-btn text-center"><a href="(.+?)" target="_blank" rel="nofollow">Play</a></div>', re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title + '  ...(MQ-LQ) [WSO]'}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in WSO [/B][/COLOR],"")")
    try:
        url = 'http://watchfree.eu/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p><a href="(.+?)" target="_blank">.+?</a></p>', re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title + '  ...(MQ-LQ) [watchfree]'}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in WSO [/B][/COLOR],[COLOR blue][B]Trying Backup site[/B][/COLOR],2000,"")")
    try:
        url = 'http://www.warezmovies.info/?s=' + query
        url = url.replace(' ', '+').replace('-', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url, 'img': img, 'text': text }, {'title':  title + ' [COLOR aqua]...(warezmovies)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry warezmovies search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.watchonlinefreeseries.com/?s=' + query
        url = url.replace(' ', '+').replace('-', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url, 'img': img, 'text': text }, {'title':  title + ' [COLOR blue]...(watchonlinefreeseries)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.jpg')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


#---------------------------------------------------------------------------- index search 2 movies ----------------------------------------------------------------------------------------------------#

def Search2(img, text, query):
    try:
        url = 'http://areaddl.com/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match1 = re.compile('<h2 class="title">(.+?)</h2>', re.DOTALL).findall(html)
        match = re.compile('<a href="(.+?)" rel="nofollow"', re.DOTALL).findall(html)
        match2 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        #match3 = re.compile('<meta name="description" itemprop="description" content="(.+?)" />').findall(content)
        for name in match1:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR pink][B](' + name + ')[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.jpg')
        #for name in match3:
                #addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title': '[COLOR blue][B]' + '(OCW) ' + name.replace('http://www.tvguide.com/', '').replace('http://www.tvrage.com/', '').replace('/', ' ').replace(';', ' ').replace('-', ' ').replace('tvshows', ' ').replace('_', ' ') + '[/B][/COLOR]' }, img= img, fanart=FanartPath + 'fanart.jpg')
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem , 'img': img, 'text': text }, {'title':  '[COLOR powderblue][B]UpToStream : direct link to[/B][/COLOR]' + ' - ' + text},img=img,  fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]No Links in OCW [/B][/COLOR],[COLOR blue][B]Trying Backup sites[/B][/COLOR],7000,"")")
    try:
        url = 'http://new.myvideolinks.xyz/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li><a href="(.+?)">.+?</a></li>', re.DOTALL).findall(html)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.filmfree4u.com/' + query + '/'
        url = url.replace(' ', '-')
        print url
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)" target="_blank">', re.DOTALL).findall(html)
        match2 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match2:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem , 'img': img, 'text': text }, {'title':  '[COLOR powderblue][B]UpToStream : direct link to[/B][/COLOR]' + ' - ' + text},img=img,  fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.movies360.info/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="featured-post clearfix">\s*?<a href="(.+?)" title="(.+?)" rel="nofollow" id="featured-thumbnail">\s*?<div class="featured-thumbnail"><img width=".+?" height=".+?" src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url, 'img': img, 'text': text }, {'title':  title + ' [COLOR green]...(movies360)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry movies360 search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://www.warezmovies.info/?s=' + query
        url = url.replace(' ', '+').replace('-', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>.+? src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url, 'img': img, 'text': text }, {'title':  title + ' [COLOR aqua]...(warezmovies)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.jpg')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- search 3 ----------------------------------------------------------------------------------------------------#

def Search3(img, text, query):
    try:
        url = 'http://areaddl.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>', re.DOTALL).findall(html)
        #match1 = re.compile('<div id="post-0" class="(post not-found post-listing)">', re.DOTALL).findall(html)
        match2 = re.compile('<div id="pagination"><a href="(.+?)" >Next page &raquo;</a></div></div>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url, 'img': img, 'text': title }, {'title':  title }, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        for url in match2:
                addon.add_directory({'mode': 'GetTitles7', 'url': url}, {'title':  '[COLOR blue][B][I]Next page...(OCW)[/B][/I][/COLOR]'}, img=IconPath + 'nextpage.png', fanart=FanartPath + 'fanart.jpg')
        #for title in match1:
                #addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title': '[COLOR red][B]NO LINKS AVAIALBLE IN OCW!![/B][/COLOR]' }, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        setView('tvshows', 'calendar-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Checking WSO FOR LINKS[/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
    try:
        url = 'http://watchseries-onlines.ch/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1 class="entry-title" itemprop="headline"><a href="(.+?)" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url, 'img': img, 'text': title }, {'title':  title + '   ...(WSO)...' }, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        setView('tvshows', 'calendar-view')
    except:
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles7(img, text, section, url):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>', re.DOTALL).findall(html)
        match1 = re.compile('<div id="pagination"><a href="(.+?)" >Next page &raquo;</a></div></div>', re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl, 'img': img , 'text': text }, {'title': name}, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        for url in match1:
                addon.add_directory({'mode': 'GetTitles7', 'url': url}, {'title':  '[COLOR blue][B][I]Next page...(OCW)[/B][/I][/COLOR]'}, img=IconPath + 'nextpage.png', fanart=FanartPath + 'fanart.jpg')
        setView('tvshows', 'calendar-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


##.replace('/', ' ')## \s*? ##
############################################################################### Get links #############################################################################################

def GetLinks(text, img, section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)"').findall(content)
        match1 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        match2 = re.compile('<IFRAME SRC="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks1', 'url':  url, 'listitem': listitem , 'img': img, 'text': text }, {'title':  '[COLOR blue][B]UpToStream : direct link to[/B][/COLOR]' + ' - ' + text},img=img,  fanart=FanartPath + 'fanart.jpg')
        for url in match + match2:
                host = GetDomain(url)
                if 'Unknown' in host:
                                continue
                r = re.search('\.rar[(?:\.html|\.htm)]*', url, re.IGNORECASE)
                if r:
                        continue
                if urlresolver.HostedMediaFile(url= url):
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem, 'img': img}, {'title':  '[COLOR lightcyan][B]' + host + '[/B][/COLOR]' + ' : ' + title}, img=img, fanart=FanartPath + 'fanart.jpg')

def GetLinks1(text, img, section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="http://uptostream.com/(.+?)" class="blue_link">http://uptostream.com/.+?</a>').findall(content)
        match1 = re.compile('<a href="http://uptobox.com/(.+?)" class="blue_link">http://uptobox.com/.+?</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'GetLinks1a', 'url': 'http://uptostream.com/' + url, 'listitem': listitem, 'img': img, 'text': text }, {'title':  '[COLOR blue][B]load stream (stream)[/B][/COLOR]' + ' : ' + text}, img=img, fanart=FanartPath + 'fanart.jpg')
        for url in match1:
                addon.add_directory({'mode': 'GetLinks1a', 'url': 'http://uptobox.com/' + url, 'listitem': listitem, 'img': img, 'text': text }, {'title':  'If no link above please try later'}, img=img, fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks1a(text, img, section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<source src='(.+?)' type='.+?' data-res='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem, 'img': img, 'text': text }, {'title': '[COLOR blue][B]' + name + '[/B][/COLOR]' + ' - ' + text }, img=img, fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################################################################# Play Video #####################################################################################

def PlayVideo(text, img, url, listitem):
    try:
        print 'in PlayVideo %s' % text
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'}, img=img, fanart=FanartPath + 'fanart.jpg')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

def PlayVideo1(text, img, url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY [/B][/COLOR]' + text , iconImage=img, thumbnailImage=img)
        li.setProperty('fanart_image', 'http://i.ytimg.com/vi/a-lCl3ZuZrE/maxresdefault.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

############################################################################# ### #####################################################################################

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

###################################################################### menus ####################################################################################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]OCW Latest Added Movies[/B] [/COLOR]>>'}, img=IconPath + 'movies1.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR blue][B]OCW Latest Added Episodes[/B] [/COLOR]>>'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles6', 'section': 'ALL', 'url': BASE_URL6 + '/cat/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orchid][B]TV Calendar [/B][/COLOR]'}, img=IconPath + 'cal.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles2', 'section': 'ALL', 'url': BASE_URL1 + '/'}, {'title':  '[COLOR greenyellow][B]TV Index Search[/B] (TV & Sport A-Z)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL2 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR greenyellow][B]TV Index Search[/B] (Episodes)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetTitles8', 'section': 'ALL', 'url': BASE_URL8 + '/tv-shows'}, {'title':  '[COLOR olivedrab][B]TV Genres[/B] (Full Seasons)[/COLOR]'}, img=IconPath + 'gen.png', fanart=FanartPath + 'fanart.jpg')

        addon.add_directory({'mode': 'GetTitles4', 'url': BASE_URL4 + '/movies/'}, {'title':  '[COLOR springgreen][B]Movies Index Search[/B] (Top Movies)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')

        addon.add_directory({'mode': 'GetTitles5', 'url': BASE_URL5 + '/new-movie-releases'}, {'title':  '[COLOR springgreen][B]Movies Index Search[/B] (Box Office)[/COLOR]'}, img=IconPath + 'indexs.png', fanart=FanartPath + 'fanart.jpg')

        addon.add_directory({'mode': 'GetSearchQuery4'},  {'title':  '[COLOR green][B]OCW TV Search[/B][/COLOR]'}, img=IconPath + 'searchs1.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'GetSearchQuery'},  {'title':  '[COLOR green][B]OCW google Search[/B][/COLOR]'}, img=IconPath + 'searchs1.png', fanart=FanartPath + 'fanart.jpg')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings[/COLOR]'}, img=IconPath + 'resolver1.png', fanart=FanartPath + 'fanart.jpg') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## search google #################################################################################################

def GetSearchQuery():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search OCW[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search(query)
	else:
                return  
def Search(query):
        url = 'http://www.google.com/search?q=site:areaddl.com/ ' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h3 class="r"><a href="(.+?)".+?onmousedown=".+?">(.+?)</a>').findall(html)
        for url, title in match:
                title = title.replace('<b>...</b>', '').replace('<em>', '').replace('</em>', '').replace('Watch', '').replace('Movies', '').replace('...', '').replace('|', '').replace('Online', '').replace('Free', '')
                addon.add_directory({'mode': 'GetLinks2', 'url': url}, {'title':  title}, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png',  fanart=FanartPath + 'fanart.jpg')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

######################################################################## search site #################################################################################################

def GetSearchQuery4():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search OCW[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search4(query)
	else:
                return  
def Search4(query):
    try:
        url = 'http://areaddl.com/' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?">(.+?)</a></h2>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks2', 'url': url}, {'title':  title }, img= 'https://briantudor.files.wordpress.com/2010/12/tv-icon1.png', fanart=FanartPath + 'fanart.jpg')
        setView('tvshows', 'calendar-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry search is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")

############################################################################### Get links & play for search #############################################################################################

def GetLinks2(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<a href="(.+?)"').findall(content)
        match1 = re.compile('href="(http://uptobox.com/.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks2a', 'url':  url, 'listitem': listitem}, {'title':  'UpToStream : direct link'}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks2a(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('Streaming link: <a href="(.+?)" class="blue_link">.+?</a>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'GetLinks2b', 'url': url, 'listitem': listitem}, {'title':  'load stream' + ' : ' + url}, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks2b(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("<source src='(.+?)' type='.+?' data-res='(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url, name in match:
                addon.add_directory({'mode': 'PlayVideo2', 'url': url, 'listitem': listitem}, {'title': name }, img= 'https://uptostream.com/images/logo.png', fanart=FanartPath + 'fanart.jpg')
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo2(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='http://silence-therapeutics-com.s3-eu-west-1.amazonaws.com/app/uploads/2015/05/play-button.png', thumbnailImage= 'https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/youtube-128.png')
        li.setProperty('fanart_image', 'http://i.ytimg.com/vi/a-lCl3ZuZrE/maxresdefault.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

########################################################################################################################################################################

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



#################################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles': 
	GetTitles(text, img, section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(section, query)
elif mode == 'GetTitles3': 
	GetTitles3(text, img, query, startPage, numOfPages)
elif mode == 'GetTitles4': 
	GetTitles4(text, img, query)
elif mode == 'GetTitles5': 
	GetTitles5(text, img, query)
elif mode == 'GetTitles6': 
	GetTitles6(section, url)
elif mode == 'GetTitles6a': 
	GetTitles6a(text, img, query, section, name)
elif mode == 'GetTitles7': 
	GetTitles7(text, img, section, url)
elif mode == 'GetTitles8': 
	GetTitles8(url)
elif mode == 'GetTitles8a': 
	GetTitles8a(url, img, text)
elif mode == 'GetTitles8b': 
	GetTitles8b(url, img, text)
elif mode == 'GetTitles8c': 
	GetTitles8c(url, img, text)
elif mode == 'GetLinks':
	GetLinks(text, img, section, url)
elif mode == 'GetLinks1':
	GetLinks1(text, img, section, url)
elif mode == 'GetLinks1a':
	GetLinks1a(text, img, section, url)
elif mode == 'GetLinks2':
	GetLinks2(section, url)
elif mode == 'GetLinks2a':
	GetLinks2a(section, url)
elif mode == 'GetLinks2b':
	GetLinks2b(section, url)
elif mode == 'GetSearchQuery':
	GetSearchQuery()
elif mode == 'Search':
	Search(query)
elif mode == 'Search1':
	Search1(text, img, section, query, name)
elif mode == 'Search2':
	Search2(img, text, query)
elif mode == 'Search3':
	Search3(text, img, query)
elif mode == 'GetSearchQuery4':
	GetSearchQuery4()
elif mode == 'Search4':
	Search4(query)
elif mode == 'PlayVideo':
	PlayVideo(text, img, url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(text, img, url, listitem)
elif mode == 'PlayVideo2':
	PlayVideo2(url, listitem)	
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
xbmcplugin.endOfDirectory(int(sys.argv[1]))