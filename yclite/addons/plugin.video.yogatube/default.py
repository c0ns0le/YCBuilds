# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Binky TV special thanks to original authors of the code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: Dandymedia
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.yogatube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "yogawithadriene"
YOUTUBE_CHANNEL_ID_2 = "lesleyfightmaster"
YOUTUBE_CHANNEL_ID_3 = "KinoYoga"
YOUTUBE_CHANNEL_ID_4 = "SarahBethShow"


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
        title="Yoga With Adriene",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-6-7NkPxEzZY/AAAAAAAAAAI/AAAAAAAAAAA/37wERyk2F-8/s100-c-k-no/photo.jpg",
        folder=True )

plugintools.add_item( 
        #action="", 
        title="Fightmaster Yoga",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-pnKh0WkTUfQ/AAAAAAAAAAI/AAAAAAAAAAA/2JTCHYaJiUw/s100-c-k-no/photo.jpg",
        folder=True )

plugintools.add_item( 
        #action="", 
        title="Kino Yoga",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-lrP8_CZD8rI/AAAAAAAAAAI/AAAAAAAAAAA/MRZqY0Nnct4/s100-c-k-no/photo.jpg",
        folder=True )

plugintools.add_item( 
        #action="", 
        title="Sarah Beth Yoga",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-E7LtrDuV4i8/AAAAAAAAAAI/AAAAAAAAAAA/hfkg7ULyf5k/s100-c-k-no/photo.jpg",
        folder=True )


				
run()		
