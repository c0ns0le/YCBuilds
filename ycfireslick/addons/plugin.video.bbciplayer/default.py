import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os
import HTMLParser

#ee3fa
ADDON = xbmcaddon.Addon(id='plugin.video.bbciplayer')


def fixImage(image, resolution):
    image = image.replace('80x80',     resolution)
    image = image.replace('304x304',   resolution)
    image = image.replace('672x378',   resolution)
    image = image.replace('832x468',   resolution)
    image = image.replace('1408x1408', resolution)
    return image



def CATEGORIES():
    addDir('My Searches','',11,'','')    
    addDir('Most Popular','http://www.bbc.co.uk/iplayer/group/most-popular',10,'','')
    addDir('iPlayer A-Z','url',3,'','')
    addDir('Categories','url',7,'','')
    addDir('Live','url',2,'','')


 
       
                                                                      
def char_range(c1, c2):
    
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)
 
    
def GetLive(url):
     
    channel_list = [
                            ('bbc_one_hd','bbc_one', 'BBC One'),
                            ('bbc_two_england', 'bbc_two', 'BBC Two'),
                            ('bbc_three','bbc_three', 'BBC Three'),
                            ('bbc_four','bbc_four', 'BBC Four'),
                            ('cbbc','cbbc', 'CBBC'),
                            ('cbeebies','cbeebies', 'CBeebies'),
                            ('bbc_news24','bbc_news24', 'BBC News Channel'),
                            ('bbc_parliament','bbc_parliament', 'BBC Parliament'),
                            ('bbc_alba','bbc_alba', 'Alba'),
                            ('s4cpbs','s4cpbs', 'S4c'),
                        ]
    for id, img, name in channel_list :
        iconimage = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.bbciplayer/img',img+'.png'))
        addDir(name,id,6,iconimage,'')       

def GetContent(url):
    nameurl=[]
    urlurl=[]
    for name in char_range('A', 'Z'):
        nameurl.append(name)
        urlurl.append(name.lower())
        
    link=OPEN_URL('http://www.bbc.co.uk/iplayer/a-z/%s'%urlurl[xbmcgui.Dialog().select('Please Select', nameurl)])
    match=re.compile('<a href="/iplayer/brand/(.+?)".+?<span class="title">(.+?)</span>',re.DOTALL).findall (link)

    for url , name in match:
        
        addDir(name,url,4,'','')


def NextPageGenre(url):

    NEW_URL = url
    link    = OPEN_URL(NEW_URL)

    html = link.replace('data-ip-episode', '-episode')
    html = html.replace('data-ip-src',     '-src')
    html = html.replace('data-ip-type',    '-type')

    #html = html.split('data-ip')
    addDir('*** [COLOR orange]Right Click Show To Grab All Episodes[/COLOR] ***','url',10,'','','')
    html=html.split('data-ip-id="')
    for p in html:
        try:
            IPID=p.split('"')[0]
            URL=re.compile('href="(.+?)"').findall (p)[0]
            name=re.compile('title="(.+?)"').findall (p)[0]
            iconimage=re.compile('img src="(.+?)"').findall (p)[0]
            plot=re.compile('<p class="synopsis">(.+?)</p>').findall (p)[0]

            #except:
                #name=name
            if 'http://www.bbc.co.uk' not in URL:
                
                _URL_='http://www.bbc.co.uk%s' %URL
            else:
                _URL = URL
                
            if not IPID in _URL_:
                IPID=IPID
            else:
                IPID=''
            
            addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot,IPID)
        except:pass    



    


def Genre(url):
    if not len(url)> 3:
        nameurl=[]
        urlurl=[]
        link=OPEN_URL('http://www.bbc.co.uk/iplayer')
        addDir('[COLOR orange]Right Click Show To Grab All Episodes[/COLOR]','url',10,'','','')
        match=re.compile('<a href="/iplayer/categories/(.+?)" class="stat">(.+?)</a>').findall(link)
        for url , name in match:
            
            h = HTMLParser.HTMLParser()
            nameurl.append(h.unescape(name))
            urlurl.append('/iplayer/categories/'+url)
        
        NEW_URL='http://www.bbc.co.uk%s/all?sort=dateavailable'%urlurl[xbmcgui.Dialog().select('Please Select Category', nameurl)]
    else:
        NEW_URL = url
    HTML=OPEN_URL(NEW_URL)
    html=HTML.split('data-ip-id="')
    for p in html:
        try:
            IPID=p.split('"')[0]
            URL=re.compile('href="(.+?)"').findall (p)[0]
            name=re.compile('title="(.+?)"').findall (p)[0]
            iconimage=re.compile('img src="(.+?)"').findall (p)[0]
            plot=re.compile('<p class="synopsis">(.+?)</p>').findall (p)[0]
            try:
                number=re.compile('>(.+?)</em>').findall(p)[0]

                if not IPID in URL:
                    name='%s - [COLOR orange](%s Available)[/COLOR]' % (name,number.strip())
            except:
                name=name
                
            if 'http://www.bbc.co.uk' not in URL:
                
                _URL_='http://www.bbc.co.uk%s' %URL
            else:
                _URL = URL

                
            if not IPID in _URL_:
                IPID=IPID
            else:
                IPID=''
            
            addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot,IPID)
        except:pass             

      
 
    try:
        nextpage = re.compile('class="next txt"> <a href="(.+?)"> Next <').findall(HTML)[0].replace('amp;','')

        if not nextpage in NEW_URL:
            _URL_='http://www.bbc.co.uk'+nextpage
            addDir('[COLOR blue]>> Next Page >>[/COLOR]',_URL_,7,'' ,'','')
    except:
        pass      
         

def POPULAR(url):
    NEW_URL=url
    html=OPEN_URL(NEW_URL)

    #match1=re.compile('data-ip-id="(.+?)">.+?href="(.+?)" title="(.+?)".+?img src="(.+?)".+?<p class="synopsis">(.+?)</p>',re.DOTALL).findall (html)
    html=html.split('data-ip-id="')
    for p in html:
        try:
            IPID=p.split('"')[0]
            URL=re.compile('href="(.+?)"').findall (p)[0]
            name=re.compile('title="(.+?)"').findall (p)[0]
            iconimage=re.compile('img src="(.+?)"').findall (p)[0]
            plot=re.compile('<p class="synopsis">(.+?)</p>').findall (p)[0]

            #except:
                #name=name    
            _URL_='http://www.bbc.co.uk%s' %URL
            if not IPID in _URL_:
                IPID=IPID
            else:
                IPID=''
            
            addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot,IPID)
        except:pass


def MySearch():
    addDir('Search','',9,'','')
    favs = ADDON.getSetting('favs').split(',')
    for title in favs:
        NEW_URL='http://www.bbc.co.uk/iplayer/search?q=%s' % title.replace(' ','%20')        
        addDir(title,NEW_URL,8,'','')
    

def Search(search_entered):
    favs = ADDON.getSetting('favs').split(',')
    if not search_entered:
        keyboard = xbmc.Keyboard('', 'Search iPlayer')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText()

    search_entered = search_entered.replace(',', '')

    if len(search_entered) == 0:
        return

    if not search_entered in favs:
        favs.append(search_entered)
        ADDON.setSetting('favs', ','.join(favs))

    search_entered = search_entered.replace(' ','%20')

    NEW_URL='http://www.bbc.co.uk/iplayer/search?q=%s' % search_entered

    NextPageGenre(NEW_URL)


def GetEpisodes(id, page=1):
    url  = 'http://www.bbc.co.uk/iplayer/episodes/%s?page=%d' % (id, page)
    link = OPEN_URL(url)
    html = link.split('data-ip-id="')
    for p in html:
        try:
            IPID=p.split('"')[0]
            URL=re.compile('href="(.+?)"').findall (p)[0]
            name=re.compile('title="(.+?)"').findall (p)[0]
            iconimage=re.compile('img src="(.+?)"').findall (p)[0]
            plot=re.compile('<p class="synopsis">(.+?)</p>').findall (p)[0]

            #except:
                #name=name
            
            if 'http://www.bbc.co.uk' not in URL:
                
                _URL_='http://www.bbc.co.uk%s' %URL
            else:
                _URL = URL
                
            if not IPID in _URL_:
                IPID=IPID
            else:
                IPID=''
            
            addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot,IPID)
        except:
            pass

    page = page + 1    
    if '/iplayer/episodes/%s?page=%d' % (id, page) in link:
        GetEpisodes(id, page=page)      



def GetPlayable(name,url,iconimage):

    _NAME_=name
    if 'plugin.video.bbciplayer' in iconimage:

        vpid=url

    else:    
        html = OPEN_URL(url)
      
        vpid=re.compile('"vpid":"(.+?)"').findall(html)[0]
    


    NEW_URL= "http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/stb-all-h264/vpid/%s" % vpid


    html = OPEN_URL(NEW_URL,True)

    match=re.compile('application="(.+?)".+?String="(.+?)".+?identifier="(.+?)".+?protocol="(.+?)".+?server="(.+?)".+?supplier="(.+?)"').findall(html.replace('amp;',''))
    for app,auth , playpath ,protocol ,server,supplier in match:

        port = '1935'
        if protocol == 'rtmpt': port = 80
        if supplier == 'limelight':
            url="%s://%s:%s/ app=%s?%s tcurl=%s://%s:%s/%s?%s playpath=%s" % (protocol,server,port,app,auth,protocol,server,port,app,auth,playpath)
            res=playpath.split('secure_auth/')[1]
            
        else:
           url="%s://%s:%s/%s?%s playpath=%s?%s" % (protocol,server,port,app,auth,playpath,auth)
           
        if supplier == 'akamai':
            res=playpath.split('secure/')[1]
            
        if supplier == 'level3':
            res=playpath.split('mp4:')[1]
            
        resolution=res.split('kbps')[0]
        if int(resolution) > 1400 :
            TITLE='[COLOR green][%s kbps][/COLOR] - [COLOR white]%s[/COLOR] - %s'%(resolution, supplier.upper(),server.upper())
        else:
            TITLE='[COLOR red][%s kbps][/COLOR] - [COLOR white]%s[/COLOR] - %s'%(resolution, supplier.upper(),server.upper())
        addDir(TITLE + ' : ' + _NAME_,url,200,iconimage,'')

    if ADDON.getSetting('hls')=='true':
        NEW_URL= "http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/apple-ipad-hls/vpid/%s" % vpid


        html = OPEN_URL(NEW_URL,True)

        match=re.compile('application="(.+?)".+?String="(.+?)".+?identifier="(.+?)".+?protocol="(.+?)".+?server="(.+?)".+?supplier="(.+?)"').findall(html.replace('amp;',''))
        for app,auth , playpath ,protocol ,server,supplier in match:

            port = '1935'
            if protocol == 'rtmpt': port = 80
            if supplier == 'limelight':
                url="%s://%s:%s/ app=%s?%s tcurl=%s://%s:%s/%s?%s playpath=%s" % (protocol,server,port,app,auth,protocol,server,port,app,auth,playpath)
                res=playpath.split('secure_auth/')[1]
                
            else:
               url="%s://%s:%s/%s?%s playpath=%s?%s" % (protocol,server,port,app,auth,playpath,auth)
               
            if supplier == 'akamai':
                res=playpath.split('secure/')[1]
                
            if supplier == 'level3':
                res=playpath.split('mp4:')[1]
                
            resolution=res.split('kbps')[0]
            if int(resolution) > 1400 :
                TITLE='[COLOR green][%s kbps][/COLOR] - [COLOR white]%s[/COLOR] - %s'%(resolution, supplier.upper(),server.upper())
            else:
                TITLE='[COLOR red][%s kbps][/COLOR] - [COLOR white]%s[/COLOR] - %s'%(resolution, supplier.upper(),server.upper())
            addDir(TITLE + ' : ' + _NAME_,url,200,iconimage,'')

        hls = re.compile('bitrate="(.+?)".+?connection href="(.+?)".+?transferFormat="(.+?)"/>').findall(html)
        for resolution, url, supplier in hls:
            server=url.split('//')[1]
            server=server.split('/')[0]
            if int(resolution) > 1400 :
                TITLE='[COLOR green][%s kbps][/COLOR] - [COLOR white]%s[/COLOR] - %s'%(resolution, supplier.upper(),server.upper())
            else:
                TITLE='[COLOR red][%s kbps][/COLOR] - [COLOR white]%s[/COLOR] - %s'%(resolution, supplier.upper(),server.upper())    
            addDir(TITLE + ' : ' + _NAME_,url,200,iconimage,'')
        
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)


def GetLivePlayable(name,url,iconimage):

    _NAME_=name

    if 'S4c' in name:
        NEW_URL='http://a.files.bbci.co.uk/media/live/manifests/hds/pc/llnw/s4cpbs.f4m'
    else:    
        NEW_URL = 'http://a.files.bbci.co.uk/media/live/manifesto/audio_video/simulcast/hds/uk/pc/ak/%s.f4m' % url  
    html = OPEN_URL(NEW_URL,True)

    match=re.compile('href="(.+?)"').findall(html.replace('amp;',''))
    item=len(match)-1
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(match[item].replace('f4m','m3u8'))
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

            

        #self.AddLiveLink( list, id.replace('_',' ').upper(), url, language = language.title(),host= 'BBC iPLAYER '+supplier,quality=quality_dict.get(res, 'NA'))       

 
def OPEN_URL(url,resolve=False):
    #print url
    if ADDON.getSetting('proxy')=='false':
        req = urllib2.Request(url)
    else:
        if resolve==True:
            import base64
            url=url.split('http')[1]
            req = urllib2.Request('http://www.openproxy.co.uk/browse.php?u='+base64.b64encode(url)+'=&b=13&f=norefer')
            req.add_header('Referer', 'http://www.openproxy.co.uk/')                
        else:
            req = urllib2.Request(url)
                                      
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
    
    
def PLAY_STREAM(name,url,iconimage):
    name = name.split(' : ', 1)[-1]

    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    

def addDir(name,url,mode,iconimage,description,IPID=''):
        if not name =='':
            try:
                h = HTMLParser.HTMLParser()
                name =h.unescape(name)
            except:pass    
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)+"&IPID="+urllib.quote_plus(IPID)
            ok=True
            #if not IPID == '':
                #name = name + ' - [COLOR orange](More Available)[/COLOR]'
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
            liz.setProperty('Fanart_Image', fixImage(iconimage, '1280x720'))
            menu=[]
            if not IPID == '':
                menu.append(('[COLOR orange]Grab All Episodes[/COLOR]','XBMC.Container.Update(%s?mode=4&url=%s)'% (sys.argv[0],IPID)))  
                liz.addContextMenuItems(items=menu, replaceItems=False)
            if mode == 8:
                menu.append(('[COLOR orange]Remove Search[/COLOR]','XBMC.Container.Update(%s?mode=12&name=%s)'% (sys.argv[0],name)))
                liz.addContextMenuItems(items=menu, replaceItems=False)
            if mode ==200 or mode ==6:
                liz.setProperty("IsPlayable","true")
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
            else:
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
            return ok
            
        
 
        
def setView(content, viewType):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
def get_params(path):
    params = {}
    path   = path.split('?', 1)[-1]
    pairs  = path.split('&')

    for pair in pairs:
        split = pair.split('=')
        if len(split) > 1:
            params[split[0]] = urllib.unquote_plus(split[1])

    return params
   
params      = get_params(sys.argv[2])            
url         = None
name        = None
mode        = None
iconimage   = None
description = None
IPID        = None

try:    url=params["url"]
except: pass

try:    name = params["name"]
except: pass

try:    iconimage = params["iconimage"]
except: pass

try:    mode = int(params["mode"])
except: pass

try:    description = params["description"]
except: pass

try:    IPID = params["IPID"]
except: pass    

print "Mode     : " + str(mode)
print "URL      : " + str(url)
print "Name     : " + str(name)
print "IconImage: " + str(iconimage)   
        
#these are the modes which tells the plugin where to go
       
if mode==1:
        print ""+url
        GetMain(url)

elif mode==2:
        print ""+url
        GetLive(url)        
        
elif mode==3:
        print ""+url
        GetContent(url)
     
elif mode==4:
        print ""+url
        GetEpisodes(url)

elif mode==5:
        GetPlayable(name,url,iconimage)

elif mode==6:
        GetLivePlayable(name,url,iconimage)

elif mode==7:
        Genre(url)


elif mode==8:
        NextPageGenre(url)  


elif mode==9:
        Search(url)    

elif mode==10:
        POPULAR(url)         

elif mode==11:
        MySearch()
        
elif mode == 12:
    favs = ADDON.getSetting('favs').split(",")
    try:
        favs.remove(name)
        ADDON.setSetting('favs', ",".join(favs))
    except:pass
    
    
    
elif mode==200:

        PLAY_STREAM(name,url,iconimage)

else:
    CATEGORIES()
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
