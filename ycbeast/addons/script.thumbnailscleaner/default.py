# -*- coding: utf-8 -*-

###########################
# Thumbnails Cleaner      #
# by Max (m4x1m) Headroom #
###########################

import os, xbmcaddon, xbmcgui
from resources.lib.tcCommon import *

addonSettings = xbmcaddon.Addon( "script.thumbnailscleaner" )
addonName     = addonSettings.getAddonInfo( "name" )
addonVersion  = addonSettings.getAddonInfo( "version" )
addonResource = os.path.join( addonSettings.getAddonInfo( "path" ), "resources", "lib" )

dbCheck = "True"
try: dbTest = RawXBMC.Execute( 'SELECT idVersion FROM version' )
except:
     dbCheck = "False"
     xbmcgui.Dialog().ok( "%s - %s" % ( addonName, addonLanguage(32118) ),  addonLanguage(32119), addonLanguage(32120) )

if dbCheck == "True":
     xbmc.log( "[%s] - Starting %s v%s " % ( addonName, addonName, addonVersion ) )
     xbmc.executebuiltin( 'XBMC.RunScript( %s )' % os.path.join( addonResource, "tcMain.py" ) )