# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pulse music by pulsemediahubuk (pulsemediahub)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: pulsemediahubuk
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.pulsemusic'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "YMDrizzyWeezy"
YOUTUBE_CHANNEL_ID_2 = "AdeleVEVO"
YOUTUBE_CHANNEL_ID_3 = "SamSmithWorldVEVO"
YOUTUBE_CHANNEL_ID_4 = "AmoLaSplendidaMusica"
YOUTUBE_CHANNEL_ID_5 = "chargers708"
YOUTUBE_CHANNEL_ID_6 = "clubmusicmixes"
YOUTUBE_CHANNEL_ID_7 = "clubmusicdjs"
YOUTUBE_CHANNEL_ID_8 = "ClubMusicParty"
YOUTUBE_CHANNEL_ID_9 = "Dj3P51LON"
YOUTUBE_CHANNEL_ID_10 = "bbcradio1"
YOUTUBE_CHANNEL_ID_11 = "MusicEDM"
YOUTUBE_CHANNEL_ID_12 = "oldiesfan1968"
YOUTUBE_CHANNEL_ID_13 = "MrArianit500"
YOUTUBE_CHANNEL_ID_14 = "oldiebutgoodiesongs"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="hip hop",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://icons.iconarchive.com/icons/limav/music-folder/128/Hip-Hop-1-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Adele",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://s30.postimg.org/9ayxe03dp/ADELE.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sam Smith",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://s30.postimg.org/8zm2ezcbh/SAM.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Music Jukebox",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://icons.iconarchive.com/icons/heylove/vintage/128/Jukebox-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Best Trance Music",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://icons.iconarchive.com/icons/rud3boy/mac-apps/128/audacity-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Club Music Mixes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://icons.iconarchive.com/icons/treetog/i/128/Audio-File-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="club music djs",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://icons.iconarchive.com/icons/iconshock/vector-twitter/128/twitter-dj-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Club Music Party",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://icons.iconarchive.com/icons/tsukasa-tux/daft-punks/128/Guyman-Helmet-Music-icon.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="EHS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://icons.iconarchive.com/icons/limav/music-folder/128/Electronic-1-icon.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="bbc radio 1",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://icons.iconarchive.com/icons/uriy1966/wooden/128/Radio-icon.png",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Music EDM",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://icons.iconarchive.com/icons/icons8/ios7/128/Music-Dj-icon.png",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="country music",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://icons.iconarchive.com/icons/limav/music-folder/128/Country-1-icon.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="MUSIC CHARTS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://icons.iconarchive.com/icons/designcontest/ecommerce-business/128/bar-chart-icon.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="oldiebutgoodiesongs",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://icons.iconarchive.com/icons/treetog/junior/128/folder-blue-music-icon.png",
        folder=True ) 
		
           
   	
run()
