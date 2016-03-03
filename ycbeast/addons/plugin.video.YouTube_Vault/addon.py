"""
 Author: Tvaddons

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 """

import urllib,urllib2,re,xbmcplugin,xbmcgui,os,sys,datetime
from resources.lib.common_variables import *
from resources.lib.directory import *
from resources.lib.youtubewrapper import *
from resources.lib.watched import * 

fanart = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.YouTube_Vault', 'fanart.jpg'))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.YouTube_Vault/resources/img', ''))

def CATEGORIES():
        addDir('Movies','url',10,art + 'Movies.png')
        addDir('Tv','url',11,art + 'Tv.png')
        addDir('Cartoons','url',12,art + 'Cartoons.png')
        addDir('Music','url',13,art + 'Music.png')
        addDir('News','url',14,art + 'news.png')
        addDir('Sports','url',15,art + 'Sports.png')
        

def Movies():
        addDir(''+translate(10012)+'','PLAA9E622BC2614112',1,art + 'Action Movies.png')
        addDir(''+translate(10013)+'','PLX0yDcKZhjGyd3SPqKOh8VTuXzhuWIyea',1,art + 'Anime Movies.png')
        addDir(''+translate(10014)+'','PL7DEonMNS4tGWRx1NFRvcmUvab5jW-PjI',1,art + 'Christian Movies.png')
        addDir(''+translate(10015)+'','PLjuR5ouJJf7oFy9kYTjeOdc8n6yGm_U64',1,art + 'Comedy Movies.png')
        addDir(''+translate(10016)+'','PLC2C9BFC77856C976',1,art + 'HORROR Movies.png')
        addDir(''+translate(10017)+'','PLKkDjgBOPjWE3t8xy7gO6w1gc2dy2R_r_',1,art + 'Family Movies.png')
        addDir(''+translate(10018)+'','PL3R5u7N6Bi3Rg-EKzpJ2EvBTgcB9HFIzR',1,art + 'Romance/Drama Movies.png')
        addDir(''+translate(10019)+'','PLm28lpCzRlQme34bn8hNtamOKd8IkdVX4',1,art + 'Sci-Fi Movies.png')
        addDir(''+translate(10020)+'','PL41192DFD0509F2E4',1,art + 'Western Movies.png')
        addDir(''+translate(10021)+'','PLuUIACjjMlWODq95IAHdMgUTRFEMGfJ3y',1,art + 'LMN Movies.png')
        addDir(''+translate(10023)+'','PLYLlM9kXGIDk1FsIpOofry-QHnrCpg-T3',1,art + 'Hallmark Movies.png')
        addDir(''+translate(10024)+'','PLlZ10h1bYswNr7BWSKrXlbfg5ByJV48xI',1,art + 'Old Horror Movies.png')
        addDir(''+translate(10025)+'','PLsQEhfECqlFaCk_rdvaYf4EwBIFYQfeh3',1,art + '1920-1939 Movies.png')
        addDir(''+translate(10026)+'','PLsQEhfECqlFb0twj4EX0nNUViCj58RxOk',1,art + '1940-1959 Movies.png')
        addDir(''+translate(10027)+'','PLsQEhfECqlFaibL0k032xIj2IbkfKoJd9',1,art + '1960-1979 Movies.png')
        addDir(''+translate(10028)+'','PLsQEhfECqlFbT2HQd8qQMsF2jWxXj6xzB',1,art + '1980-1999 Movies.png')
        addDir(''+translate(10029)+'','PLsQEhfECqlFbhv2s_3pmhRE20bJx_1lZY',1,art + '2000-2009 Movies.png')

def Tv():
        addDir(''+translate(40033)+'','PL6fJmjt84zZiWk6e8mBtjFUU2PCVcO_I6',1,art + 'Tv.png')
        addDir(''+translate(40034)+'','PLSBxUok6vJJkrLBcHGAoSP264Aihm5FC4',1,art + 'Tv.png')
        addDir(''+translate(40035)+'','PLA9t0Lw1Waqe6ZrFKiJnvZQZdtiPmpffr',1,art + 'Tv.png')
        addDir(''+translate(40036)+'','PLMU_iGRst5xaE-fTWw35CksMPYqlxguNp',1,art + 'Tv.png')
        addDir(''+translate(40037)+'','PLABBf_0W_aItG7pZMsTRE1k5L0GjE4zK8',1,art + 'Tv.png')
        addDir(''+translate(40038)+'','PLoXLTb9MXwazYf147EoQJt-wmkuVKZVfc',1,art + 'Tv.png')
        addDir(''+translate(40039)+'','PL2AF155372EFE8DA0',1,art + 'Tv.png')
        addDir(''+translate(40040)+'','PL-aJSrEGIGy4Muhw4lhuYII5kDrBlUqrv',1,art + 'Tv.png')
        addDir(''+translate(40041)+'','PLUDizevuO8OonDbpnQk1pVOu2nxQKnoKy',1,art + 'Tv.png')
        addDir(''+translate(40042)+'','PLum50h_rWpG6qIKOwiUdqryoVyAAS4qPd',1,art + 'Tv.png')
        addDir(''+translate(40043)+'','PL6fJmjt84zZjHtICMv908RZVxqO7HXUxa',1,art + 'Tv.png')
        addDir(''+translate(40044)+'','PLeagipoZmyfk6_dnkTew2tJMmr2KdeK6Z',1,art + 'Tv.png')
        addDir(''+translate(40045)+'','PL6fJmjt84zZg552GekYb5Pgchr9330p6b',1,art + 'Tv.png')
        addDir(''+translate(40046)+'','PLZVMGCh7sZUgxG1erdqZNTQiotE3ers6z',1,art + 'Tv.png')
        addDir(''+translate(40047)+'','PL12C0C916CECEA3BC',1,art + 'Tv.png')
        addDir(''+translate(40048)+'','PLFtpZ659RpvF42PE6uKm6mQjuz8uDq2jp',1,art + 'Tv.png')
        addDir(''+translate(40049)+'','PL551DB3E031657F74',1,art + 'Tv.png')
        addDir(''+translate(40050)+'','PLjcUMSbqsHuWOJt83lfT0G4VbjazjDhkH',1,art + 'Tv.png')
        addDir(''+translate(40051)+'','PL9udHiBT2yQefMH9oTv74odwI6KFvVYGU',1,art + 'Tv.png')
        addDir(''+translate(40052)+'','PLvhcaElZ90ayqqYXPm0Xtgk0Lix5YjRQM',1,art + 'Tv.png')
        addDir(''+translate(40053)+'','PL8hg3-ygwIqIlV91K9INgmLw253Z_JQfc',1,art + 'Tv.png')
        addDir(''+translate(40054)+'','PLum50h_rWpG4QQOifQeDFZyfZYH3Qx76i',1,art + 'Tv.png')
        addDir(''+translate(40055)+'','PLht_Yj17XWWpcipa-Dr6i-8_0c-eSWi0g',1,art + 'Tv.png')
        addDir(''+translate(40056)+'','PLomOrqWjsaoBQLzHA7ve3vNRx2tGrNQ4x',1,art + 'Tv.png')
        addDir(''+translate(40057)+'','PLABBf_0W_aIvHH5MU0xHa82YYlmwWCr4g',1,art + 'Tv.png')
        addDir(''+translate(40058)+'','PLmHgXUJMN1TXCZbl3w_RYofN_XMCRDtdy',1,art + 'Tv.png')
        addDir(''+translate(40059)+'','PLABBf_0W_aIt_IJp02LykSgIzcov2Q3hH',1,art + 'Tv.png')
        addDir(''+translate(40060)+'','PLsPbqGD7bfUApUGk6WXBsUJCEyYM94yTv',1,art + 'Tv.png')
        addDir(''+translate(40061)+'','PLABBf_0W_aIvtE6_CK-1IbeNUtkfQJtLN',1,art + 'Tv.png')
        addDir(''+translate(40062)+'','PLD75qpSXCKDDfj1R4jJG2dYVMZ7g7jOOo',1,art + 'Tv.png')
        addDir(''+translate(40063)+'','PLyLrnNOEPdo430q3kcZmUHtbbPfv4vycg',1,art + 'Tv.png')
        addDir(''+translate(40064)+'','PLQpmN1igDvPLQl1spKWXqtXixo8nNpLjq',1,art + 'Tv.png')
        addDir(''+translate(40065)+'','PLdcKBzTef6vDvDP2IXvCE2i96WEjc4pJF',1,art + 'Tv.png')
        addDir(''+translate(40066)+'','PL2F217D855BEA1AD6',1,art + 'Tv.png')
        addDir(''+translate(40067)+'','PL1p5cydiDufi2rr-8jlkxIpJjBM_536O5',1,art + 'Tv.png')
        addDir(''+translate(40068)+'','PLMhHNVrSAz9panKWofOiqFeec2AoryHZM',1,art + 'Tv.png')
        addDir(''+translate(40069)+'','PLMhHNVrSAz9qF4cl3gwNi1J4n9cLd4zJX',1,art + 'Tv.png')
        addDir(''+translate(40070)+'','PLMhHNVrSAz9piWuj1RAokuiB0D24Or7EU',1,art + 'Tv.png')
        addDir(''+translate(40071)+'','PLMhHNVrSAz9oEqp1rboHh-hD2N9N6QXKY',1,art + 'Tv.png')
        addDir(''+translate(40072)+'','PLMhHNVrSAz9q-b_8XN4lru5bls-fQoN4h',1,art + 'Tv.png')
        addDir(''+translate(40073)+'','PLMhHNVrSAz9qiS1B9wQ4Xtos61_0jBNZL',1,art + 'Tv.png')
        addDir(''+translate(40074)+'','PLMhHNVrSAz9roEUXKl694C98X_E5P2ZKg',1,art + 'Tv.png')
        addDir(''+translate(40075)+'','PLenx8C5_mz59B7yGggKpmpT_-iazUbgte',1,art + 'Tv.png')
        addDir(''+translate(40076)+'','PLY5hFG53Fodrx8LASo63ygjtgxwBuKAhR',1,art + 'Tv.png')
        addDir(''+translate(40077)+'','PLDvHMbD9mOa-XjmatpSOgeeSu_vaEF6I9',1,art + 'Tv.png')
        addDir(''+translate(40078)+'','PLeagipoZmyfkDCN7P2Em5JNuYkVWdr2i5',1,art + 'Tv.png')
        addDir(''+translate(40079)+'','PLAt-Zrdficj3jycviMgHFN1owckcFh6b5',1,art + 'Tv.png')
		
def Cartoons():
        addDir(''+translate(30021)+'','PLcRPn2pJRe5cINS3lccT3Ubx1n_VtZCIA',1,art + 'Cartoons.png')
        addDir(''+translate(30022)+'','PLZVMGCh7sZUh_jIqrYMKYyyPNJtpng_ZC',1,art + 'Cartoons.png')
        addDir(''+translate(30024)+'','PLzLQUGUmDNnZm_IK0PoVaeHHj2QPyZgDH',1,art + 'Cartoons.png')
        addDir(''+translate(30027)+'','PLlKv1wPSQiYfATd5clTuDfSfxZXUxtG5O',1,art + 'Cartoons.png')
        addDir(''+translate(30023)+'','PLIEbITAtGBebu6sbY14JHRSCgLWAWhcvV',1,art + 'Cartoons.png')
        addDir(''+translate(30025)+'','PLICkv4ALPsh_NESTsgFJkeXeh9yUWzLhf',1,art + 'Cartoons.png')
        addDir(''+translate(30026)+'','PL6fJmjt84zZie95U29YKamr0Ph2lJD277',1,art + 'Cartoons.png')
        addDir(''+translate(30028)+'','PL1E1DDEA933CD12FF',1,art + 'Cartoons.png')
        addDir(''+translate(30029)+'','PLTLP-p6a1SEPXfKtkDEfBL2nM9kZ97jpb',1,art + 'Cartoons.png')
        addDir(''+translate(30030)+'','PL3432ABAC840E3DF3',1,art + 'Cartoons.png')
        addDir(''+translate(30031)+'','PLbrxg_e8MbbF-psMIds86ndWuTehx4kQS',1,art + 'Cartoons.png')
        addDir(''+translate(30032)+'','PLtXcJHjzQOdOJyKUf4N_im5szCADvUbb_',1,art + 'Cartoons.png')
        addDir(''+translate(30033)+'','PLYvGyqxhIGIkFWcCHQKVpKIy5CVpZs1D-',1,art + 'Cartoons.png')
        addDir(''+translate(30034)+'','PLrhuB2KrXOjikfPLJhTmz2qKDkltz9L8Y',1,art + 'Cartoons.png')
        addDir(''+translate(30035)+'','PLqcNVz8UuCsLhpzTjL0JGj3YuMyWWd5Ug',1,art + 'Cartoons.png')
        addDir(''+translate(30036)+'','PLsFmiuNwu758huWLmxTM4NCln7tbqJDPn',1,art + 'Cartoons.png')
        addDir(''+translate(30037)+'','PLtfPnJye9L3dxlbWP7OlJH-_yI3PYsh9r',1,art + 'Cartoons.png')
        addDir(''+translate(30038)+'','PLeagipoZmyfkWkyetCWsJMGy8yBvHdJs-',1,art + 'Cartoons.png')
        addDir(''+translate(30039)+'','PLeagipoZmyfmBwqCrCc8p7cE6QdLes-eL',1,art + 'Cartoons.png')
        addDir(''+translate(30040)+'','PLeagipoZmyfn9MhKB9Smgqob8CLNiaA51',1,art + 'Cartoons.png')
        addDir(''+translate(30041)+'','PLS3SOlSTtJcDe-vQ-T46r_cB1U_ENAuKF',1,art + 'Cartoons.png')
        addDir(''+translate(30042)+'','PLeagipoZmyfl46t2ABPQitVy1V7qu2vrG',1,art + 'Cartoons.png')
        addDir(''+translate(30043)+'','PL67492B3700EA9340',1,art + 'Cartoons.png')
        addDir(''+translate(30044)+'','PL_plhzjgRin_lTnP3hkylujEzC9Ir5krr',1,art + 'Cartoons.png')
        addDir(''+translate(30045)+'','PLZs0gQed9tMQtGV1ZuPglUryJWuJECZ5D',1,art + 'Cartoons.png')
        addDir(''+translate(30046)+'','PLaE8D0PEpUTtHl3NzB3VfscnmW68cZC58',1,art + 'Cartoons.png')
        addDir(''+translate(30047)+'','PL2469F219C9FEABC0',1,art + 'Cartoons.png')
        addDir(''+translate(30048)+'','PLDJplukjMGFMD9ix6GOiKWc5sTnYih8OX',1,art + 'Cartoons.png')
        addDir(''+translate(30049)+'','PLyz03hm3jrASCj1qP4cp9jhlLbKVHGLf1',1,art + 'Cartoons.png')
        addDir(''+translate(30050)+'','PLZs0gQed9tMT5KX9M_PYxrVeVUiJ8aWuS',1,art + 'Cartoons.png')
        addDir(''+translate(30051)+'','PLZs0gQed9tMQzdY8EKdrADeCZ7OJS-AZK',1,art + 'Cartoons.png')
        addDir(''+translate(30052)+'','PLeagipoZmyfkwcDThw6yIE3cqQAb8-KQ-',1,art + 'Cartoons.png')
        addDir(''+translate(30053)+'','PLnhtGTQWc2dumToZlzsKI8RCOwgzpykly',1,art + 'Cartoons.png')
        addDir(''+translate(30054)+'','PLB06DDF14D951C23C',1,art + 'Cartoons.png')
        addDir(''+translate(30055)+'','PLZxHX9waSzmv8CeVWGzqSPJK7KPC0HlSF',1,art + 'Cartoons.png')
        addDir(''+translate(30056)+'','PLCD5B9AD1151F3E0B',1,art + 'Cartoons.png')
        addDir(''+translate(30057)+'','PLOLEQVkmI9eugSKUsrQBH0rxMN-qBLUyV',1,art + 'Cartoons.png')
        addDir(''+translate(30058)+'','PLeagipoZmyfm_yCiyU_LYR86ZcJFc0k6d',1,art + 'Cartoons.png')
        addDir(''+translate(30059)+'','PLPe7Z5Wz5D5XbCFeDlr5XLP32vXa-G--0',1,art + 'Cartoons.png')
        addDir(''+translate(30060)+'','PLPe7Z5Wz5D5Uyc2W-P7BvU6iym7ZY2FyF',1,art + 'Cartoons.png')
        addDir(''+translate(30061)+'','PLiBi9LVIrC-fVelw2-I2r-yrEk6SpXfO8',1,art + 'Cartoons.png')
        addDir(''+translate(30062)+'','PLKav3i3U4Xl58bqa1gmIxehnpDxA32HHc',1,art + 'Cartoons.png')

def Music():
        addDir(''+translate(50001)+'','PL55713C70BA91BD6E',1,art + 'Music.png')
        addDir(''+translate(50002)+'','PLDcnymzs18LVXfO_x0Ei0R24qDbVtyy66',1,art + 'Music.png')
        addDir(''+translate(50003)+'','PL3485902CC4FB6C67',1,art + 'Music.png')
        addDir(''+translate(50004)+'','PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI',1,art + 'Music.png')
        addDir(''+translate(50005)+'','PLGBuKfnErZlAkaUUy57-mR97f8SBgMNHh',1,art + 'Music.png')
        addDir(''+translate(50006)+'','PL2BN1Zd8U_MsyMeK8r9Vdv1lnQGtoJaSa',1,art + 'Music.png')
        addDir(''+translate(50007)+'','PLnpWcMv6bu2X0xfAD6Kt-MgIIFOCNb067',1,art + 'Music.png')
        addDir(''+translate(50008)+'','PLuK6flVU_Aj5EJ9Pp-C9N7XA0YJr_GrJI',1,art + 'Music.png')
        addDir(''+translate(50009)+'','PLuK6flVU_Aj45QZ_A5ld0-pP3CIkoNQDk',1,art + 'Music.png')
        addDir(''+translate(50010)+'','PLh__qJ1ro4JgQI6aAgk5dduKLZUGr1Tiw',1,art + 'Music.png')
        addDir(''+translate(50011)+'','PLCEE7B2A4B9C9BCE7',1,art + 'Music.png')
        addDir(''+translate(50012)+'','PL04199B0AF6C7C9F8',1,art + 'Music.png')
        addDir(''+translate(50013)+'','PLrEnWoR732-D67iteOI6DPdJH1opjAuJt',1,art + 'Music.png')

def News():
        addDir(''+translate(60001)+'','PLr1-FC1l_JLFcq9r9Y3uFLkH8G37WmMRQ',1,art + 'News.png')
        addDir(''+translate(60002)+'','PLNjtpXOAJhQLmUEyuWw4hW_6gX8JMJUof',1,art + 'News.png')
        addDir(''+translate(60003)+'','PL6XRrncXkMaV2KPi6KHFAGE6VLSibWe2P',1,art + 'News.png')
        addDir(''+translate(60004)+'','PL0tDb4jw6kPxZ7ZJtMk6gqiQIU-nMeaVS',1,art + 'News.png')
        addDir(''+translate(60005)+'','PL5E6638EB9ECF2329',1,art + 'News.png')
        addDir(''+translate(60006)+'','PLlTLHnxSVuIyeEZPBIQF_krewJkY2JSwi',1,art + 'News.png')
        addDir(''+translate(60007)+'','PLEb3ThbkPrFabMf542Iic5Hxw2xlrgusX',1,art + 'News.png')

def Sports():
        addDir(''+translate(70001)+'','PLyXm-hnmX1_qxDKgYmXzxABejOkwfkjBG',1,art + 'Sports.png')
        addDir(''+translate(70002)+'','PLlVlyGVtvuVndLGz3vK0nKYUVyCv_8WCY',1,art + 'Sports.png')
        addDir(''+translate(70003)+'','PLrbOUcXk2JPVj8tD4xG1XNOmD_72qi8OM',1,art + 'Sports.png')
        addDir(''+translate(70004)+'','PL1ZcZsep3ZaOPf47uErRQ-z12GBjoXbtE',1,art + 'Sports.png')
           
           
	

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


params=get_params()
url=None
name=None
mode=None
iconimage=None
page = None
token = None

try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except:
	try: 
		mode=params["mode"]
	except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: token=urllib.unquote_plus(params["token"])
except: pass
try: page=int(params["page"])
except: page = 1

print ("Mode: "+str(mode))
print ("URL: "+str(url))
print ("Name: "+str(name))
print ("iconimage: "+str(iconimage))
print ("Page: "+str(page))
print ("Token: "+str(token))

		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def create_directory(dir_path, dir_name=None):
    if dir_name:
        dir_path = os.path.join(dir_path, dir_name)
    dir_path = dir_path.strip()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        return_youtubevideos(name,url,token,page)

elif mode==5: 
        play_youtube_video(url)

elif mode==6:
        mark_as_watched(url)

elif mode==7:
        removed_watched(url)

elif mode==8:
        add_to_bookmarks(url)

elif mode==9:
        remove_from_bookmarks(url)
		
elif mode==10:
        print ""+url
        Movies()
		
elif mode==11:
        print ""+url
        Tv()

elif mode==12:
        print ""+url
        Cartoons()

elif mode==13:
        print ""+url
        Music()
        
elif mode==14:
        print ""+url
        News()

elif mode==15:
        print ""+url
        Sports()		

xbmcplugin.endOfDirectory(int(sys.argv[1]))
