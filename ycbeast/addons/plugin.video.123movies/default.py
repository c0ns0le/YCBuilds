#!/usr/bin/python
# (c)2uk3y, December 8, 2015
# Greetz to: TioEuy & Bosen
# Version:
# 20151208: 1.0: First release
# Addon is based on Dramaonline Addon authored by Aresu.
# License GPL Version 2

import xbmc,xbmcplugin
import xbmcgui
import sys
import urllib, urllib2
import time
import re
from htmlentitydefs import name2codepoint as n2cp
import httplib
import urlparse
from os import path, system
import socket
from urllib2 import Request, URLError, urlopen
from urlparse import parse_qs
from urllib import unquote_plus
import xbmcaddon
import json

pass#print  "Here in default-py sys.argv =", sys.argv

mainURL="http://123movies.to"
thisPlugin = int(sys.argv[1])
addonId = "plugin.video.123movies"
dataPath = xbmc.translatePath('special://profile/addon_data/%s' % (addonId))
addon = xbmcaddon.Addon()
path = addon.getAddonInfo('path')
pic = path+"/icon.png"
picNext = path+"/next.png"
picFanart = path+"/fanart.jpg"
progress = xbmcgui.DialogProgress()

#if not path.exists(dataPath):
#       cmd = "mkdir -p " + dataPath
#       system(cmd)
     
Host = "http://123movies.to"
movieHost = Host+"/movie/filter"

def getUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
def playVideo(url):
    player = xbmc.Player()
    player.play(url)

def gedebug(strTxt):
    print '##################################################################################################'
    print '### GEDEBUG: ' + str(strTxt)
    print '##################################################################################################'
    return
    
def addSearch():
    searchStr = ''
    keyboard = xbmc.Keyboard(searchStr, 'Search')
    keyboard.doModal()
    if (keyboard.isConfirmed()==False):
      return
    searchStr=keyboard.getText()
    if len(searchStr) == 0:
      return
    else:
      return searchStr 

def showSearch():
    stext = addSearch()
    name = stext
    try:
      url = Host + "/movie/search/" + stext.replace(' ','%20')
      ok = showMovieList('', '', '', '', '', '', '', url)
    except:
      pass

def showMainMenu():
    addDirectoryItem("Featured", {
      "name":"Featured", "url":Host, "mode":1, "section":"movie-featured"
      }, pic)
    addDirectoryItem("Movies", {
      "name":"Movies", "url":Host, "mode":4, "section":"movie"
      }, pic)
    addDirectoryItem("TV-Series", {
      "name":"TV-Series", "url":Host, "mode":4, "section":"series"
      }, pic)
    addDirectoryItem("Latest Movies", {
      "name":"Latest Movies", "url":Host, "mode":1, "section":"mlw-latestmovie"
      }, pic)
    addDirectoryItem("Latest TV-Series", {
      "name":"Latest TV-Series", "url":Host, "mode":1, "section":"mlw-featured"
      }, pic)
    addDirectoryItem("Top Viewed Today", {
      "name":"Top Viewed Today", "url":Host, "mode":1, "section":"topview-today"
      }, pic)
    addDirectoryItem("Most Favorite", {
      "name":"Most Favorite", "url":Host, "mode":1, "section":"top-favorite"
      }, pic)
    addDirectoryItem("Top Rating", {
      "name":"Top Rating", "url":Host, "mode":1, "section":"top-rating"
      }, pic)
    addDirectoryItem("Top IMDb", {
      "name":"Top IMDb", "url":Host, "mode":1, 'imdb':'topimdb'
      }, pic)
    addDirectoryItem("Search", {"name":"Search", "url":Host, "mode":99}, pic)
    xbmcplugin.endOfDirectory(thisPlugin)

def showFilterMenu(section):
    addDirectoryItem("Most Viewed", {
      "name":"Most Viewed", "url":Host, "mode":1, "section":section, "sortby":"view"
      }, pic)
    addDirectoryItem("Most Favorite", {
      "name":"Most Favorite", "url":Host, "mode":1, "section":section, "sortby":"favorite"
      }, pic)
    addDirectoryItem("Top Rating", {
      "name":"Top Rating", "url":Host, "mode":1, "section":section, "sortby":"rating"
      }, pic)
    addDirectoryItem("Genre", {"name":"Genre", "url":Host, "mode":41, "section":section, "filters":"genre"}, pic)
    addDirectoryItem("Country", {"name":"Country", "url":Host, "mode":41, "section":section, "filters":"country"}, pic)
    addDirectoryItem("Year", {"name":"Year", "url":Host, "mode":41, "section":section, "filters":"year"}, pic)

    xbmcplugin.endOfDirectory(thisPlugin)

def showFilterList(section, filters):
    url = movieHost+'/'+section
    # gedebug(url)
    if filters == 'genre':
      lister = getGenre(url)
    elif filters == 'country':
      lister = getCountry(url)
    elif filters == 'year':
      lister = getYear(url)

    for value,title in lister:
      title = re.sub(r"\s$", '', title)
      addDirectoryItem(title, {"name":title, "url":Host, "mode":1, "section":section, "sortby":"all", filters:value}, pic)

    if filters == 'year':
      title = "Older"
      value = "older-2011"
      addDirectoryItem(title, {"name":title, "url":Host, "mode":1, "section":section, "sortby":"all", filters:value}, pic)

    xbmcplugin.endOfDirectory(thisPlugin)

def getGenre(url):
    content = getUrl(url)
    # gedebug(content)
    regEx = 'value="(.+?)".*?name="genres\[\]"\n*\s*.*>(.+?)</label>'
    match = re.compile(regEx).findall(content)
    return match

def getCountry(url):
    content = getUrl(url)
    # gedebug(content)
    regEx = 'value="(.+?)".*?name="countries\[\]"\n*\s*.*>(.+?)</label>'
    match = re.compile(regEx).findall(content)
    return match

def getYear(url):
    content = getUrl(url)
    # gedebug(content)
    regEx = 'value="(.+?)".*?name="year"\n*\s*.*>(.+?)</label>'
    match = re.compile(regEx).findall(content)
    return match

# http://123movies.to/movie/search/mission impossible
# http://123movies.to/movie/filter/all/latest/1-24-12/3-23/2014/all/3
def showMovieList(section='all', sortby='latest', genre='all', country='all', year='all', other='all', page='', search='', imdb=''):
    # gedebug(movieHost + '/' + section + '/' + sortby + '/' + genre + '/' + country + '/' + year + '/' + other + '/' + page)
    url = movieHost + '/' + section + '/' + sortby + '/' + genre + '/' + country + '/' + year + '/' + other + '/' + page

    search = search.replace('%3a',':').replace('%2f','/')

    if not page: page = 1

    if search:
      url = search + '/' + str(page)

    if imdb:
      url = mainURL+'/movie/'+imdb + '/' + str(page)

    if section == 'movie-featured' or section == 'mlw-latestmovie' or section == 'mlw-featured':
      url = Host

    if section == 'topview-today' or section == 'top-favorite' or section == 'top-rating':
      url = mainURL+'/site/ajaxContentBox/'+section

    gedebug(url)
    content = getUrl(url)
    # gedebug(content)
    if section == 'movie-featured' or section == 'mlw-latestmovie' or section == 'mlw-featured':
      regEx = '<.*'+section+'.*?\n\s*(.+?)<scrip'
      content = re.compile(regEx, re.DOTALL).findall(content)[0]

    if section == 'topview-today' or section == 'top-favorite' or section == 'top-rating':
      data = json.loads(content)
      content = data['content']
      # gedebug(data['content'])

    regEx = '<.*ml-item.*\n*\s*<a href="(.+?)"\n*\s*.*\n*\s*.*\n*\s*title="(.+?)".*\n*\s*(<.).*\n*\s*.*data-original="(.+?)"'
    match = re.compile(regEx).findall(content)

    for url,title,mode,pic in match:

      if mode == '<s':
        mode = 3
      else:
        mode = 2
      # gedebug(mode)
      addDirectoryItem(title, {"name":title, "url":url, "mode":mode}, pic)

    pageNext = int(page)+1
    # # gedebug(pageNext)
    urlNext = movieHost + '/' + section + '/' + sortby + '/' + genre + '/' + country + '/' + year + '/' + other + '/' + str(pageNext)

    if search:
      urlNext = search + '/' + str(pageNext)
      # gedebug('search='+urlNext)
      addDirectoryItem("[I]Next Page[/I]", {
        "name":"Next Page", "url":urlNext, "mode":1, "page":pageNext, "search":search
        }, picNext)
    elif imdb:
      urlNext = mainURL+'/movie/'+imdb + '/' + str(pageNext)
      # gedebug('search='+urlNext)
      addDirectoryItem("[I]Next Page[/I]", {
        "name":"Next Page", "url":urlNext, "mode":1, "page":pageNext, "imdb":imdb
        }, picNext)
    elif section == 'movie-featured' or section == 'mlw-latestmovie' or section == 'mlw-featured' or section == 'topview-today' or section == 'top-favorite' or section == 'top-rating':
      pass
    else:
      # gedebug('not search='+urlNext)
      addDirectoryItem("[I]Next Page[/I]", {
          "name":"Next Page", "url":urlNext, "mode":1, "section":section, "sortby":sortby, "genre":genre, "country":country, "year":year, "other":other, "page":pageNext, "search":search
          }, picNext)

    xbmcplugin.endOfDirectory(thisPlugin)


def showMovieLink(url):
    url = url+'watching.html'
    content = getUrl(url)
    # gedebug(content)
    regEx = '<.*movie-id="(.+?)"\n*\s*.*="(.+?)"'
    match = re.compile(regEx).findall(content)[0]
    movieID = match[0]
    movieToken = match[1]
    server = '9'
    # gedebug(movieID + ' - ' + movieToken)

    # get thumbnail
    regEx = '<meta property="og:image" content="(.+?)"/>'
    pic = re.compile(regEx).findall(content)[0]
    
    # progress bar create
    progress.create('Progress', 'Please wait while we grab all source.')

    try: #search server
      content = getUrl(mainURL+'/movie/loadepisodes/'+movieID)
      regEx = 'id="server-(.+?)"'
      match = re.compile(regEx).findall(content)
      # gedebug(match)
      if len(match) > 1:
        i = 0
        l = len(match)
        intl = str(l)+'.0'

        for server in match:
          # gedebug('more 1 :'+server)
          # progess bar update
          updateProgressBar(i, l, intl)
          if progress.iscanceled():
            progress.close()
            break
          i = i + 1
          getQuality(movieID, movieToken, server, pic)
      else:
        # gedebug('only 1 :'+server)
        getQuality(movieID, movieToken, server, pic)
    except:
      pass

    progress.close()
    xbmcplugin.endOfDirectory(thisPlugin)

def showEpisodeMenu(url):
    url = url+'watching.html'
    content = getUrl(url)
    # gedebug(content)

    # get thumbnail
    regEx = '<meta property="og:image" content="(.+?)"/>'
    pic = re.compile(regEx).findall(content)[0]
    # gedebug(pic)

    # search episode
    regEx = '<.*movie-id="(.+?)"\n*\s*.*="(.+?)"'
    match = re.compile(regEx).findall(content)[0]
    movieID = match[0]
    movieToken = match[1]
    server = '9'
    # gedebug(movieID + ' - ' + movieToken)
    episodes = getEpisode(movieID)

    for episode in episodes:
      addDirectoryItem(episode, {"name":episode, "url":url, "mode":31, 'mvID':movieID, 'mvToken':movieToken, 'thumbnail':pic}, pic)

    xbmcplugin.endOfDirectory(thisPlugin)

def showEpisodeLink(mvID, mvToken, epName, thumbnail=''):
    # gedebug(mvID + ' - ' + mvToken + ' - ' + epName)
    movieID = mvID
    movieToken = mvToken
    pic = thumbnail
    # gedebug(pic)
    # progress bar create
    progress.create('Progress', 'Please wait while we grab all source.')
    # server = '9'
    try: #search server
      content = getUrl(mainURL+'/movie/loadepisodes/'+movieID)
      regEx = 'id="server-(.+?)"'
      match = re.compile(regEx).findall(content)
      # gedebug(match)
      if len(match) > 1:
        i = 0
        l = len(match)
        intl = str(l)+'.0'
  
        for server in match:
          # progess bar update
          updateProgressBar(i, l, intl)
          if progress.iscanceled():
            progress.close()
            break
          i = i + 1
          # gedebug('more 1 :'+server)
          getQuality(movieID, movieToken, server, pic, epName)
      else:
        # gedebug('only 1 :'+server)
        getQuality(movieID, movieToken, server, pic, epName)
    except:
      pass

    progress.close()
    xbmcplugin.endOfDirectory(thisPlugin)

def updateProgressBar(i, l, intl):
    percent = int( ( i / float(intl) ) * 100)
    message = "Server found : " + str(i) + " out of "+str(l)
    progress.update( percent, "", message, "" )
    # print "Message " + str(i) + " out of 10"
    xbmc.sleep( 1000 )

def getEpisode(movieID):
    content = getUrl(mainURL+'/movie/loadepisodes/'+movieID)
    # gedebug(content)
    #search episode
    regEx = 'les-content">\n*\s*(.*?)\n*\s*</div>'
    match = re.compile(regEx, re.DOTALL).findall(content)[0]
    # gedebug(match)
    # serach title
    regEx = 'title="(.*?)"'
    match = re.compile(regEx).findall(match)
    # gedebug(match)
    return match

def getQuality(movieID, movieToken, server, pic='', epName=''):
    url = mainURL + '/movie/loadepisoderss/' + movieID + '/' + movieToken + '/' + server
    # gedebug(url)
    content = getUrl(url)
    quality = ''
    # gedebug(content)
    if epName:
      epName = epName.replace('%20',' ').replace('%3a',':')
      regEx = '<title>'+epName+'</title>\n*\s*(.+?)\n*\s*</item>'
      content = re.compile(regEx, re.DOTALL).findall(content)[0]
      # gedebug(content)
    else:
      # quality = ''
      regEx0 = '<title>(.+?)</title>'
      q = re.compile(regEx0).findall(content)[0]
      if q == 'TS' or q == 'CAM':
        quality = '  |  ' + q
      # gedebug(q)

    regEx = 'source.*\n*\s*file="(.+?)"\n*\s*label="(.+?)"'
    match = re.compile(regEx).findall(content)
    gedebug(match)

    for url,label in match:
      regEx = '=m(.+)'
      match = re.compile(regEx).findall(url)[0]
      # gedebug(match)
      if match == '18': label = 'SD'
      elif match == '22': label = 'HD'
      title = 'Server '+ server + '  |  ' + label + quality
      addDirectoryItem(title, {"name":title, "url":url, "mode":69}, pic)

std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}  

def addDirectoryItem(name, parameters={},pic=""):
    li = xbmcgui.ListItem(name,iconImage="", thumbnailImage=pic)
    li.setInfo( "video", { "Title" : name, "FileName" : name} )
    if pic == path+"/icon.png" or pic == path+"/next.png": pic = picFanart
    li.setProperty('Fanart_Image', pic)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)


def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

params = parameters_string_to_dict(sys.argv[2])
name =  str(params.get("name", ""))
url =  str(params.get("url", ""))
url = urllib.unquote(url)
mode =  str(params.get("mode", ""))
section =  str(params.get("section", ""))
sortby =  str(params.get("sortby", "latest"))
genre =  str(params.get("genre", "all"))
country = str(params.get("country", "all"))
year = str(params.get("year", "all"))
other = str(params.get("other", "all"))
page = str(params.get("page", ""))
mvID = str(params.get("mvID", ""))
mvToken = str(params.get("mvToken", ""))
filters = str(params.get("filters", ""))
search = str(params.get("search", ""))
imdb = str(params.get("imdb", ""))
thumbnail = str(params.get("thumbnail", ""))
thumbnail = urllib.unquote(thumbnail)

#### ACTIONS ####
if not sys.argv[2]:
    pass#print  "Here in default-py going in showContent"
    ok = showMainMenu()
else:
    if mode == str(1): #Click Latest Movie / TV Series
        ok = showMovieList(section, sortby, genre, country, year, other, page, search, imdb)
    elif mode == str(2):  #Click Movie Title
        ok = showMovieLink(url)
    elif mode == str(3):  #Click TV Series Title
        ok = showEpisodeMenu(url)
    elif mode == str(31):  #Click Episode
        ok = showEpisodeLink(mvID, mvToken, name, thumbnail)
    elif mode == str(4):  #Click Drama Other
        ok = showFilterMenu(section)
    elif mode == str(41):  #Click Drama Other
        ok = showFilterList(section, filters) 
    elif mode == str(99):  #Click Search
        ok = showSearch()
    elif mode == str(69): #Play video
        ok = playVideo(url)
