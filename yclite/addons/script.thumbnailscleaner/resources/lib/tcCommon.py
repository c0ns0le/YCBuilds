# -*- coding: utf-8 -*-

###########################
# Thumbnails Cleaner      #
# by Max (m4x1m) Headroom #
###########################

import xbmc, xbmcaddon, xbmcvfs
import os, sqlite3, unicodedata

addonSettings     = xbmcaddon.Addon( "script.thumbnailscleaner" )
addonAuthor       = addonSettings.getAddonInfo( "author" )
addonName         = addonSettings.getAddonInfo( "name" )
addonVersion      = addonSettings.getAddonInfo( "version" )
addonLanguage     = addonSettings.getLocalizedString
addonProfile      = xbmc.translatePath( addonSettings.getAddonInfo( "profile" ) )
addonIcon         = os.path.join( addonSettings.getAddonInfo( "path" ), "icon.png" )
addonBackup       = os.path.join( addonProfile, "backup" )
cleanIcon         = os.path.join( addonSettings.getAddonInfo( "path" ), "resources", "images", "cleanIcon.png" )
keepIcon          = os.path.join( addonSettings.getAddonInfo( "path" ), "resources", "images", "keepIcon.png" )
xbmcVersion       = xbmc.getInfoLabel( "System.BuildVersion" ).split(" ")[0]

if not xbmcvfs.exists( addonProfile ): xbmcvfs.mkdir( addonProfile )
if not xbmcvfs.exists( addonBackup ): xbmcvfs.mkdir( addonBackup )

databaseFolder    = xbmc.translatePath( "special://database" )
thumbnailsFolder  = xbmc.translatePath( "special://thumbnails" )

def log( msg ):
     xbmc.log( "[%s] - %s" % ( addonName, msg ) )

def _unicode( text, encoding='utf-8' ):
     try: text = unicode( text, encoding )
     except: pass
     return text

def normalize( text ):
     try: text = unicodedata.normalize( 'NFKD', _unicode( text ) ).encode( 'utf-8' )
     except: pass
     return text

def getHash( string ):
     string = string.lower()
     bytes = bytearray( string )
     crc = 0xffffffff;
     for b in bytes:
	  crc = crc ^ ( b << 24 )
	  for i in range(8):
	       if ( crc & 0x80000000 ): crc = ( crc << 1 ) ^ 0x04C11DB7
	       else: crc = crc << 1;
	  crc = crc & 0xFFFFFFFF
     return '%08x' % crc

def humanReadableSizeOf( size ):
     for x in ['bytes','KB','MB','GB']:
	  if size < 1024.0 and size > -1024.0:
	       return "%3.1f%s" % ( size, x )
	  size /= 1024.0
     return "%3.1f%s" % ( size, 'TB' )

def removeDuplicate( lists ):
     log( addonLanguage(32249) )
     seen = set()
     seenAdd = seen.add
     return [ x for x in lists if x not in seen and not seenAdd( x ) ]

class RawXBMC():
     @staticmethod
     def Query( Query ):
	  RawXBMCConnect = ConnectToXbmcDb()
	  Cursor = RawXBMCConnect.cursor()
	  Cursor.execute( Query )
	  Matches = []
	  for Row in Cursor: Matches.append( Row )
	  RawXBMCConnect.commit()
	  Cursor.close()
	  return Matches

     @staticmethod
     def Execute( Query ):
	  return RawXBMC.Query( Query )

def ConnectToXbmcDb():
     dbHost = os.path.join( databaseFolder, "Textures" + addonSettings.getSetting( "dbTextures" ) + ".db" )
     return sqlite3.connect( dbHost )