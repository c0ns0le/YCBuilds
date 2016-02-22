# -*- coding: utf-8 -*-

###########################
# Thumbnails Cleaner      #
# by Max (m4x1m) Headroom #
###########################

import xbmc, xbmcgui
import os, sys, urllib, datetime, time, shutil
if sys.version_info >= (2, 7): import json
else: import simplejson as json
import tcMainGui, tcKeepGui, tcQueryGui
from tcCommon import *

class Cleaner:
     def __init__( self, parent ):
	  self.parent            = parent
	  self.filesList         = [] # Contents all Files
	  self.texturesList      = [] # Contents all Textures
	  self.totalFilesSize    = 0  # Initial Files Size
	  self.cancelOperation   = False # Init cancelOperation Flag
	  self.selectDestinationFolder() # Getting destinationFolder

     def selectDestinationFolder( self ):
	  self.destinationFolder = addonSettings.getSetting( "destinationFolder" )
	  if not self.destinationFolder:
	       self.destinationFolder = addonBackup

     def exploreThumbnailsFolder( self, thumbnailsFolder ):
	  basedir = thumbnailsFolder; subdirlist = []
	  for item in os.listdir( thumbnailsFolder ):
	       if os.path.isfile( os.path.join( basedir, item ) ):
		    last = os.path.split( os.path.dirname( basedir ) )[1]
		    itemWithDir = basedir + "/" + item
		    self.filesList.append( ( item ) ) # itemWithDir,
		    self.totalFilesSize = self.totalFilesSize + os.stat( os.path.join( basedir, item ) ).st_size
	       else: subdirlist.append( os.path.join( basedir, item ) )
	  for subdir in subdirlist:
	       self.exploreThumbnailsFolder( subdir )

     def setLabelInfo( self ):
	  # Get all Files in Thumbnails folder and all Textures in Database
	  self.exploreThumbnailsFolder( thumbnailsFolder )
	  if xbmcVersion >= 13:
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "Textures.GetTextures", "id": 1}' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'textures' ): getTextures = jSon['result']['textures']
	       except: getTextures = []
	  else: getTextures = RawXBMC.Execute( "SELECT id FROM texture" )
	  # set Labels
	  self.parent.labelBeforeFiles.setLabel( str( len( self.filesList ) ) )
	  self.parent.labelBeforeSizes.setLabel( humanReadableSizeOf( self.totalFilesSize ) )
	  self.parent.labelBeforeTextures.setLabel( str( len( getTextures ) ) )

     def excludeHash( self, sectionToDo, textToDo ):
	  countList = 1
	  Progress = xbmcgui.DialogProgress()
	  Progress.create( addonName )
	  log( normalize( addonLanguage(32300) % len( sectionToDo ) ) )
	  for s in sectionToDo:
	       Progress.update( ( countList*100 )/len( sectionToDo ), normalize( addonLanguage(32301) ) % len( sectionToDo ), textToDo, s )
	       if Progress.iscanceled():
		    Progress.close()
		    self.cancelOperation = True
		    break
	       urlHash = getHash( s )
	       extFile = s.split(".")[-1]
	       try: self.filesList.remove( urlHash + "." + extFile )
	       except:
		    # Workaround for the icons addon
		    if "icon.png" in s:
			 try: self.filesList.remove( urlHash + ".jpg" )
			 except: pass
	       cachedUrl = ""
	       for item in self.texturesList:
		    if item[0] == s.decode('utf-8'): cachedUrl = item[1]
	       if cachedUrl:
		    try: self.texturesList.remove( ( s.decode('utf-8'), cachedUrl ) )
		    except: pass
	       countList = countList + 1
	  Progress.close()

     def doClean( self, doSimulate=True ):
	  # Reset After Labels
	  self.parent.labelAfterFiles.setLabel( "" )
	  self.parent.labelAfterSizes.setLabel( "" )
	  self.parent.labelAfterTextures.setLabel( "" )
	  # Disable Buttons
	  self.parent.buttonClean.setEnabled( False )
	  self.parent.buttonSimulate.setEnabled( False )
	  self.parent.buttonQuery.setEnabled( False )
	  self.parent.buttonEmpty.setEnabled( False )
	  self.parent.buttonSettings.setEnabled( False )
	  self.startedAt = datetime.datetime.now()
	  if doSimulate == True: log( normalize( addonLanguage(32200) ) + self.startedAt.strftime( "%Y-%m-%d %H:%M:%d" ) )
	  else: log( normalize( addonLanguage(32201) ) + self.startedAt.strftime( "%Y-%m-%d %H:%M:%d" ) )
	  # Get all Files in Thumbnails folder
	  self.exploreThumbnailsFolder( thumbnailsFolder )
	  self.totalFilesList = len( self.filesList )
	  # Get all Textures in Database
	  if xbmcVersion >= 13:
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "Textures.GetTextures", "params": {"properties": ["url","cachedurl"]}, "id": 1}' )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'textures' ): getTextures = jSon['result']['textures']
		    for item in getTextures: self.texturesList.append( ( urllib.unquote_plus( normalize( item.get( 'url' ) ) ).replace( "image://", "" )[:-1].decode('utf-8'), item.get( 'cachedurl' ) ) )
	       except: pass
	  else:
	       getTextures = RawXBMC.Execute( "SELECT url, cachedurl FROM texture" )
	       for item in getTextures: self.texturesList.append( ( item[0], item[1] ) )
	  self.totalTexturesList = len( self.texturesList )
	  Progress = xbmcgui.DialogProgress()

	  # Movies
	  if self.cancelOperation != True and addonSettings.getSetting( "checkMovies" ) == "false":
	       log( normalize( "*** " + addonLanguage(32204) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataMovie = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": {"properties": ["art"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'movies' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32205) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['movies']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32204) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      for key in item.get( 'art' ):
				   valueText = urllib.unquote_plus( normalize( item.get('art')[key] ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMovie.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataMovie = removeDuplicate( dataMovie )
		    if self.cancelOperation != True and len( dataMovie ) > 0:
			 self.excludeHash( dataMovie, normalize( addonLanguage(32206) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # Sets
	  if self.cancelOperation != True and addonSettings.getSetting( "checkSets" ) == "false":
	       log( normalize( "*** " + addonLanguage(32207) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataSets = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovieSets", "params": {"properties": ["art"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'sets' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32208) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['sets']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32207) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      for key in item.get( 'art' ):
				   valueText = urllib.unquote_plus( normalize( item.get('art')[key] ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataSets.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataSets = removeDuplicate( dataSets )
		    if self.cancelOperation != True and len( dataSets ) > 0:
			 self.excludeHash( dataSets, normalize( addonLanguage(32209) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # TVShows
	  if self.cancelOperation != True and addonSettings.getSetting( "checkTVShows" ) == "false":
	       log( normalize( "*** " + addonLanguage(32210) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataTVShows = []; tvShows = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows", "params": {"properties": ["art"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'tvshows' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32211) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['tvshows']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32210) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      tvShows.append( ( item.get('tvshowid'), item.get('label') ) )
			      for key in item.get( 'art' ):
				   valueText = urllib.unquote_plus( normalize( item.get('art')[key] ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataTVShows.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataTVShows = removeDuplicate( dataTVShows )
		    if self.cancelOperation != True and len( dataTVShows ) > 0:
			 self.excludeHash( dataTVShows, normalize( addonLanguage(32212) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass
	  else: tvShows = []

	  # Seasons
	  if self.cancelOperation != True  and addonSettings.getSetting( "checkSeasons" ) == "false" and len( tvShows ) > 0:
	       log( normalize( "*** " + addonLanguage(32213) + " ***" ) )
	       dataSeasons = []; countList = 1
	       Progress.create( addonName )
	       for tvShow in tvShows:
		    Progress.update( ( countList*100 )/len( tvShows ), normalize( addonLanguage(32213) ), tvShow[1], " " )
		    if Progress.iscanceled():
			 Progress.close()
			 self.cancelOperation = True
			 break
		    jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetSeasons", "params": {"properties": ["art"], "tvshowid": %s}, "id": 1}' % tvShow[0] )
		    jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
		    jSon = json.loads( jSonQuery )
		    try:
			 if jSon['result'].has_key( 'seasons' ):
			      totalResults = jSon['result']['limits'].get('total')
			      log( normalize( addonLanguage(32214) % ( totalResults, tvShow[1] ) ) )
			      for item in jSon['result']['seasons']:
				   for key in item.get( 'art' ):
					if key.find("tvshow.") != 0:
					     valueText = urllib.unquote_plus( normalize( item.get('art')[key] ) )
					     valueText = valueText.replace( "image://", "" )[:-1]
					     if item.get('label') == "Season 1": # Workaround for season all posters
						  seasonAll = valueText.replace( "season01", "season-all" )
						  dataSeasons.append( seasonAll )
					     dataSeasons.append( valueText )
		    except: pass
		    time.sleep(0.0005)
		    countList = countList + 1
	       Progress.close()
	       dataSeasons = removeDuplicate( dataSeasons )
	       if self.cancelOperation != True and len( dataSeasons ) > 0:
		    self.excludeHash( dataSeasons, normalize( addonLanguage(32215) ) )
	       else: log( normalize( addonLanguage(32301) ) % "0" )

	  # Episodes
	  if self.cancelOperation != True and addonSettings.getSetting( "checkEpisodes" ) == "false" and len( tvShows ) > 0:
	       log( normalize( "*** " + addonLanguage(32216) + " ***" ) )
	       dataEpisodes = []; countList = 1
	       Progress.create( addonName )
	       for tvShow in tvShows:
		    Progress.update( ( countList*100 )/len( tvShows ), normalize( addonLanguage(32216) ), tvShow[1], " " )
		    if Progress.iscanceled():
			 Progress.close()
			 self.cancelOperation = True
			 break
		    jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetEpisodes", "params": {"properties": ["art"], "tvshowid": %s}, "id": 1}' % tvShow[0] )
		    jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
		    jSon = json.loads( jSonQuery )
		    try:
			 if jSon['result'].has_key( 'episodes' ):
			      totalResults = jSon['result']['limits'].get('total')
			      log( normalize( addonLanguage(32217) % ( totalResults, tvShow[1] ) ) )
			      for item in jSon['result']['episodes']:
				   for key in item.get( 'art' ):
					if key.find("tvshow.") != 0:
					     valueText = urllib.unquote_plus( normalize( item.get('art')[key] ) )
					     valueText = valueText.replace( "image://", "" )[:-1]
					     dataEpisodes.append( valueText )
		    except: pass
		    time.sleep(0.0005)
		    countList = countList + 1
	       Progress.close()
	       dataEpisodes = removeDuplicate( dataEpisodes )
	       if self.cancelOperation != True and len( dataEpisodes ) > 0:
		    self.excludeHash( dataEpisodes, normalize( addonLanguage(32218) ) )
	       else: log( normalize( addonLanguage(32301) ) % "0" )

	  # MusicVideos
	  if self.cancelOperation != True and addonSettings.getSetting( "checkMusicVideos" ) == "false":
	       log( normalize( "*** " + addonLanguage(32219) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataMusicVideos = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetMusicVideos", "params": {"properties": ["art"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'musicvideos' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32220) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['musicvideos']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32219) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      for key in item.get( 'art' ):
				   valueText = urllib.unquote_plus( normalize( item.get('art')[key] ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicVideos.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataMusicVideos = removeDuplicate( dataMusicVideos )
		    if self.cancelOperation != True and len( dataMusicVideos ) > 0:
			 self.excludeHash( dataMusicVideos, normalize( addonLanguage(32221) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # Video Genres
	  if self.cancelOperation != True and addonSettings.getSetting( "checkVideoGenres" ) == "false":
	       log( normalize( "*** " + addonLanguage(32222) + " ***" ) )
	       dataVideoGenres = []
	       # Movies
	       countList = 1
	       log( normalize( addonLanguage(32203) ) )
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetGenres", "params": {"sort": { "order": "ascending", "method": "label", "ignorearticle": true }, "properties": ["thumbnail"], "type": "movie"}, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'genres' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32224) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['genres']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32223) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataVideoGenres.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
	       except: pass
	       # TV Shows
	       countList = 1
	       log( normalize( addonLanguage(32203) ) )
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetGenres", "params": {"sort": { "order": "ascending", "method": "label", "ignorearticle": true }, "properties": ["thumbnail"], "type": "tvshow"}, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'genres' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32226) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['genres']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32225) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataVideoGenres.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
	       except: pass
	       # Music Videos
	       countList = 1
	       log( normalize( addonLanguage(32203) ) )
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetGenres", "params": {"sort": { "order": "ascending", "method": "label", "ignorearticle": true }, "properties": ["thumbnail"], "type": "musicvideo"}, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'genres' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32228) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['genres']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32227) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataVideoGenres.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
	       except: pass
	       dataVideoGenres = removeDuplicate( dataVideoGenres )
	       if self.cancelOperation != True and len( dataVideoGenres ) > 0:
		    self.excludeHash( dataVideoGenres, normalize( addonLanguage(32229) ) )
	       else: log( normalize( addonLanguage(32301) ) % "0" )

	  # Music Artists
	  if self.cancelOperation != True and addonSettings.getSetting( "checkMusicArtists" ) == "false":
	       log( normalize( "*** " + addonLanguage(32230) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataMusicArtists = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "AudioLibrary.GetArtists", "params": {"properties": ["thumbnail","fanart"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'artists' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32231) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['artists']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32230) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicArtists.append( valueText )
			      if item.get( 'fanart' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'fanart' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicArtists.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataMusicArtists = removeDuplicate( dataMusicArtists )
		    if self.cancelOperation != True and len( dataMusicArtists ) > 0:
			 self.excludeHash( dataMusicArtists, normalize( addonLanguage(32232) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # Music Albums
	  if self.cancelOperation != True and addonSettings.getSetting( "checkMusicAlbums" ) == "false":
	       log( normalize( "*** " + addonLanguage(32233) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataMusicAlbums = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "AudioLibrary.GetAlbums", "params": {"properties": ["thumbnail","fanart"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'albums' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32234) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['albums']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32233) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicAlbums.append( valueText )
			      if item.get( 'fanart' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'fanart' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicAlbums.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataMusicAlbums = removeDuplicate( dataMusicAlbums )
		    if self.cancelOperation != True and len( dataMusicAlbums ) > 0:
			 self.excludeHash( dataMusicAlbums, normalize( addonLanguage(32235) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # Music Songs
	  if self.cancelOperation != True and addonSettings.getSetting( "checkMusicSongs" ) == "false":
	       log( normalize( "*** " + addonLanguage(32236) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataMusicSongs = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "AudioLibrary.GetSongs", "params": {"properties": ["thumbnail","fanart"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'songs' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32237) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['songs']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32236) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicSongs.append( valueText )
			      if item.get( 'fanart' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'fanart' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicSongs.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataMusicSongs = removeDuplicate( dataMusicSongs )
		    if self.cancelOperation != True and len( dataMusicSongs ) > 0:
			 self.excludeHash( dataMusicSongs, normalize( addonLanguage(32238) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # Music Genres
	  if self.cancelOperation != True and addonSettings.getSetting( "checkMusicGenres" ) == "false":
	       log( normalize( "*** " + addonLanguage(32239) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataMusicGenres = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "AudioLibrary.GetGenres", "params": {"sort": { "order": "ascending", "method": "title", "ignorearticle": true }, "properties": ["thumbnail"]}, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'genres' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32240) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['genres']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32239) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataMusicGenres.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataMusicGenres = removeDuplicate( dataMusicGenres )
		    if self.cancelOperation != True and len( dataMusicGenres ) > 0:
			 self.excludeHash( dataMusicGenres, normalize( addonLanguage(32241) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # Actors
	  if self.cancelOperation != True and addonSettings.getSetting( "checkActors" ) == "false":
	       log( normalize( "*** " + addonLanguage(32245) + " ***" ) )
	       dataCast = []
	       # Movies
	       countList = 1
	       log( normalize( addonLanguage(32203) ) )
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": {"properties": ["cast"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'movies' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32205) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['movies']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32245) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      for cast in item.get( 'cast' ):
				   for key in cast:
					if key == "thumbnail":
					     valueText = urllib.unquote_plus( normalize( cast[key] ) )
					     valueText = valueText.replace( "image://", "" )[:-1]
					     dataCast.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
	       except: pass
	       # TV Shows
	       tvShows = []; countList = 1
	       log( normalize( addonLanguage(32203) ) )
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows", "params": {"properties": ["cast"], "sort": { "order": "ascending", "method": "title", "ignorearticle": true } }, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'tvshows' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32211) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['tvshows']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32246) ), item.get('label'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      tvShows.append( ( item.get('tvshowid'), item.get('label') ) )
			      for cast in item.get( 'cast' ):
				   for key in cast:
					if key == "thumbnail":
					     valueText = urllib.unquote_plus( normalize( cast[key] ) )
					     valueText = valueText.replace( "image://", "" )[:-1]
					     dataCast.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
	       except: pass
	       # Episodes
	       countList = 1
	       Progress.create( addonName )
	       for tvShow in tvShows:
		    Progress.update( ( countList*100 )/len( tvShows ), normalize( addonLanguage(32247) ), tvShow[1], " " )
		    if Progress.iscanceled():
			 Progress.close()
			 self.cancelOperation = True
			 break
		    jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "VideoLibrary.GetEpisodes", "params": {"properties": ["cast"], "tvshowid": %s}, "id": 1}' % tvShow[0] )
		    jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
		    jSon = json.loads( jSonQuery )
		    try:
			 if jSon['result'].has_key( 'episodes' ):
			      totalResults = jSon['result']['limits'].get('total')
			      log( normalize( addonLanguage(32217) % ( totalResults, tvShow[1] ) ) )
			      for item in jSon['result']['episodes']:
				   for cast in item.get( 'cast' ):
					for key in cast:
					     if key == "thumbnail":
						  valueText = urllib.unquote_plus( normalize( cast[key] ) )
						  valueText = valueText.replace( "image://", "" )[:-1]
						  dataCast.append( valueText )
		    except: pass
		    time.sleep(0.0005)
		    countList = countList + 1
	       Progress.close()
	       dataCast = removeDuplicate( dataCast )
	       if self.cancelOperation != True and len( dataCast ) > 0:
		    self.excludeHash( dataCast, normalize( addonLanguage(32248) ) )
	       else: log( normalize( addonLanguage(32301) ) % "0" )

	  # Addons
	  if self.cancelOperation != True and addonSettings.getSetting( "checkAddons" ) == "false":
	       log( normalize( "*** " + addonLanguage(32242) + " ***" ) )
	       log( normalize( addonLanguage(32203) ) )
	       dataAddons = []; countList = 1
	       xbmc.executebuiltin( "Notification(%s,%s,-1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = xbmc.executeJSONRPC( '{"jsonrpc": "2.0", "method": "Addons.GetAddons", "params": {"properties": ["thumbnail","fanart"]}, "id": 1}' )
	       xbmc.executebuiltin( "Notification(%s,%s,1,%s)" % ( addonName, normalize( addonLanguage(32203) ), addonIcon ) )
	       jSonQuery = unicode( jSonQuery, 'utf-8', errors='ignore' )
	       jSon = json.loads( jSonQuery )
	       try:
		    if jSon['result'].has_key( 'addons' ):
			 totalResults = jSon['result']['limits'].get('total')
			 log( normalize( addonLanguage(32243) % totalResults ) )
			 Progress.create( addonName )
			 for item in jSon['result']['addons']:
			      Progress.update( ( countList*100 )/totalResults, normalize( addonLanguage(32242) ), item.get('addonid'), " " )
			      if Progress.iscanceled():
				   Progress.close()
				   self.cancelOperation = True
				   break
			      if item.get( 'thumbnail' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'thumbnail' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataAddons.append( valueText )
			      if item.get( 'fanart' ) != "":
				   valueText = urllib.unquote_plus( normalize( item.get( 'fanart' ) ) )
				   valueText = valueText.replace( "image://", "" )[:-1]
				   dataAddons.append( valueText )
			      time.sleep(0.0005)
			      countList = countList + 1
			 Progress.close()
		    dataAddons = removeDuplicate( dataAddons )
		    if self.cancelOperation != True and len( dataAddons ) > 0:
			 self.excludeHash( dataAddons, normalize( addonLanguage(32244) ) )
		    else: log( normalize( addonLanguage(32301) ) % "0" )
	       except:
		    log( normalize( addonLanguage(32301) ) % "0" ); pass

	  # Process Textures Database
	  if self.cancelOperation != True:
	       newTextures = []
	       extraPattern = addonSettings.getSetting( "extraPattern" ).split( "|" )
	       for t in self.texturesList:
		    if not any( x in t[0] for x in extraPattern ): newTextures.append( ( t[0], t[1] ) )
		    else:
			 if t[1]:
			      cachedUrl = t[1].split("/")[1]
			      try: self.filesList.remove( cachedUrl )
			      except: pass
	       self.texturesList = newTextures
	       if ( len( self.texturesList ) > 0):
		    self.keepTextures = []
		    tcKeepGui.tcKeepGui( "script_thumbnails_cleaner-lists.xml", addonSettings.getAddonInfo( "path" ), "Default", forceFallback = False, parent = self )
		    if self.cancelOperation != True: self.excludeHash( self.keepTextures, normalize( addonLanguage(32250) ) )

	  # To the End
	  if self.cancelOperation != True:
	       self.totalTexturesList = self.totalTexturesList-len( self.texturesList )
	       # Re-Calculate Total Files and Sizes
	       self.totalFilesList = self.totalFilesList-len( self.filesList )
	       self.newTotalFileSize = 0
	       for f in self.filesList:
		    files = os.path.join( thumbnailsFolder, f[:1], f )
		    try: self.newTotalFileSize = self.newTotalFileSize + os.stat( files ).st_size
		    except: pass
	       self.totalFilesSize = self.totalFilesSize - self.newTotalFileSize
	       # Print After Labels
	       self.parent.labelAfterFiles.setLabel( str ( self.totalFilesList ) )
	       self.parent.labelAfterSizes.setLabel( humanReadableSizeOf( self.totalFilesSize ) )
	       self.parent.labelAfterTextures.setLabel( str( self.totalTexturesList ) )
	       # Finalize Clean
	       self.finalizeClean( doSimulate )
	  else:
	       log( normalize( addonLanguage(32501) ) )
	       xbmcgui.Dialog().ok( "%s - %s" % ( addonName, normalize( addonLanguage(32500) ) ), "%s" % normalize( addonLanguage(32501) ) )
	  self.finishAt = datetime.datetime.now()
	  self.tookTime = self.finishAt - self.startedAt
	  log( normalize( addonLanguage(32502) % str( self.tookTime ).split(".")[0] ) )
	  # Enable Buttons
	  self.parent.buttonClean.setEnabled( True )
	  self.parent.buttonSimulate.setEnabled( True )
	  self.parent.buttonQuery.setEnabled( True )
	  self.parent.buttonEmpty.setEnabled( True )
	  self.parent.buttonSettings.setEnabled( True )

     def finalizeClean( self, doSimulate=True ):
	  # Move files in destination folder or copy if simulate is active
	  Progress = xbmcgui.DialogProgress()
	  if doSimulate == False:
	       countList = 1
	       log( normalize( addonLanguage(32251) ) % len( self.texturesList ) )
	       Progress.create( addonName )
	       for t in self.texturesList:
		    Progress.update( ( countList*100 )/len( self.texturesList ), normalize( addonLanguage(32251) ) % len( self.texturesList ), t[0], " " )
		    url = t[0].replace("'", "''")
		    RawXBMC.Execute( "DELETE FROM texture WHERE url='" + url + "'" )
		    countList = countList + 1
	       Progress.close()
	  countList = 1
	  Progress.create( addonName )
	  for f in self.filesList:
	       files = os.path.join( thumbnailsFolder, f[:1], f )
	       if doSimulate == True:
		    Progress.update( ( countList*100 )/len( self.filesList ), normalize( addonLanguage(32160) ) % len( self.filesList ), files, " " )
		    try: shutil.copy2( files, self.destinationFolder )
		    except: pass
	       else:
		    Progress.update( ( countList*100 )/len( self.filesList ), normalize( addonLanguage(32161) ) % len( self.filesList ), files, " " )
		    try: os.remove( os.path.join( self.destinationFolder, f ) )
		    except: pass
		    try: shutil.move( files, self.destinationFolder )
		    except: pass
	       countList = countList + 1
	  Progress.close()
	  # Manage Textual Response
	  if doSimulate == True:
	       log( normalize( addonLanguage(32162) ) % ( str( len( self.filesList ) ), humanReadableSizeOf( self.newTotalFileSize ) ) )
	       log( normalize( addonLanguage(32163) ) % str( len( self.texturesList ) ) )
	       xbmcgui.Dialog().ok( addonName + " - " + normalize( addonLanguage(32166) ), normalize( addonLanguage(32167) ) + " " + addonName, normalize( addonLanguage(32162) ) % ( str( len( self.filesList ) ), humanReadableSizeOf( self.newTotalFileSize ) ), normalize( addonLanguage(32163) ) % str( len( self.texturesList ) ) )
	  else:
	       log( normalize( addonLanguage(32164) ) % ( str( len( self.filesList ) ), humanReadableSizeOf( self.newTotalFileSize ) ) )
	       log( normalize( addonLanguage(32165) ) % str( len( self.texturesList ) ) )
	       xbmcgui.Dialog().ok( addonName + " - " + normalize( addonLanguage(32166) ), normalize( addonLanguage(32167) ) + " " + addonName, normalize( addonLanguage(32164) ) % ( str( len( self.filesList ) ), humanReadableSizeOf( self.newTotalFileSize ) ), normalize( addonLanguage(32165) ) % str( len( self.texturesList ) ) )

     def queryGui( self ):
	  tcQueryGui.tcQueryGui( "script_thumbnails_cleaner-lists.xml", addonSettings.getAddonInfo( "path" ), "Default" )
	  self.setLabelInfo()

     def emptyTable( self ):
	  self.Erase = xbmcgui.Dialog().yesno( "%s" % addonName, "%s" % normalize( addonLanguage(32401) ), "%s" % normalize( addonLanguage(32402) ), " ", "%s" % "No", "%s" % "Yes" )
	  if self.Erase != 0:
	       shutil.copy2(databaseFolder + "/Textures" + addonSettings.getSetting( "dbTextures" ) + ".db", databaseFolder + "/Textures" + addonSettings.getSetting( "dbTextures" ) + ".db.bak")
	       RawXBMC.Execute( "DELETE FROM texture" )
	       log( normalize( addonLanguage(32403) ) )
	       log( normalize( addonLanguage(32404) ) )
	       xbmcgui.Dialog().ok( "%s - %s" % ( addonName, normalize( "Info" ) ), "%s" % normalize( addonLanguage(32403) ), normalize( addonLanguage(32404) ) )
	       self.setLabelInfo()

if ( __name__ == "__main__" ):
     tcMainGui.tcMainGui( "script_thumbnails_cleaner-main.xml", addonSettings.getAddonInfo( "path" ), "Default" )