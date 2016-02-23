import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,random

import window
rand=random.randint(1, 10000000)
path = xbmcaddon.Addon().getAddonInfo('path')
addon_id = 'plugin.video.aswizard'
selfAddon = xbmcaddon.Addon(id=addon_id)
comparefile = os.path.join(os.path.join(path,''), 'compare.txt')

#modify xml for uncached thumbnails
xmlpath = os.path.join(path,'resources','skins','Wookie','720p','wookie.xml')
print xmlpath

r = open(xmlpath);xml=r.read();r.close()
fanart=re.compile('<texture>(.+?)</texture>').findall(xml)[0]
icon=re.compile('<texture>(.+?)</texture>').findall(xml)[1]
xml=xml.replace(fanart,'http://wookiespmc.com/Notification/images/fanart.jpg?'+str(rand)).replace(icon,'http://wookiespmc.com/Notification/images/logo.jpg?'+str(rand))
xml_file = open(xmlpath, "w");xml_file.write(xml);xml_file.close()
#modify xml for uncached thumbnails

req = urllib2.Request('http://wookiespmc.com/Notification/message.txt?'+str(rand))
req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
response = urllib2.urlopen(req)
text=response.read()
response.close()
text='[B]'+text+'[/B]'#make all text bold
r = open(comparefile)
compfile = r.read()       
if compfile == text:quit()
elif len(text)==7:quit()
else:
      win = window.WookieWindow('wookie.xml',path,'Wookie',caption='',text=text)
      win.doModal()
      del win
      text_file = open(comparefile, "w")
      text_file.write(text)
      text_file.close()
quit()


