# -*- coding: utf-8 -*-

###########################
# Thumbnails Cleaner      #
# by Max (m4x1m) Headroom #
###########################

import xbmc, xbmcgui
import os, shutil
from tcCommon import *

class tcQueryGui( xbmcgui.WindowXMLDialog ):

     def __init__( self, *args, **kwargs ):
	  xbmcgui.WindowXMLDialog.__init__( self )
	  self.getQuery          = "" # Text Query
	  self.lists             = [] # Imported List From Query Result
	  self.choose            = [] # User Choice
	  self.destinationFolder = addonSettings.getSetting( "destinationFolder" ) # Get the destination folder
	  self.queryTable()

     def onInit( self ):
	  self.defineControls()
	  self.labelTitle.setLabel( addonLanguage(32148) )
	  self.buttonAll.setLabel( addonLanguage(32141) )
	  self.buttonNone.setLabel( addonLanguage(32142) )
	  self.buttonDelete.setLabel( addonLanguage(32144) )
	  self.buttonQuit.setLabel( addonLanguage(32145) )
	  self.itemsList.reset()
	  for itemList in self.lists: self.itemsList.addItem( xbmcgui.ListItem( itemList ) )

     def defineControls( self ):
	  # IDs
	  self.idList   = 10
	  self.idTitle  = 90
	  self.idAll    = 91
	  self.idNone   = 92
	  self.idDelete = 93
	  self.idQuit   = 94
	  # Controls
	  self.itemsList    = self.getControl( self.idList )
	  self.labelTitle   = self.getControl( self.idTitle )
	  self.buttonAll    = self.getControl( self.idAll )
	  self.buttonNone   = self.getControl( self.idNone )
	  self.buttonDelete = self.getControl( self.idDelete )
	  self.buttonQuit   = self.getControl( self.idQuit )

     def queryTable( self ):
	  if not self.getQuery:
	       keyboard = xbmc.Keyboard()
	       keyboard.doModal()
	       self.getQuery = keyboard.getText()
	  if self.getQuery:
	       self.lists = []; self.choose = []; getQuery = self.getQuery.replace("'", "''")
	       match = RawXBMC.Execute( "SELECT url FROM texture WHERE url LIKE '%" + getQuery + "%'" )
	       for base in match: self.lists.append( base[0] )
	       if len( self.lists ) > 0: self.doModal()
	       else:
		    self.getQuery = ""; self.queryTable()

     def onClick( self, controlId ):
	  if controlId == self.idList:
	       itemSelected = self.itemsList.getSelectedItem()
	       try:
		    self.choose.remove( itemSelected.getLabel() )
		    itemSelected.setIconImage( "" )
	       except:
		    self.choose.append( itemSelected.getLabel() )
		    itemSelected.setIconImage( cleanIcon )
	  elif controlId == self.idAll:
	       self.choose = []
	       for i in range( 0, len( self.lists ) ):
		    item = self.itemsList.getListItem( i )
		    self.choose.append( item.getLabel() )
		    item.setIconImage( cleanIcon )
	  elif controlId == self.idNone:
	       self.choose = []
	       for i in range( 0, len( self.lists ) ):
		    item = self.itemsList.getListItem( i )
		    item.setIconImage( "" )
	  elif controlId == self.idDelete:
	       for url in self.choose:
		    url = url.replace("'", "''")
		    cachedUrl = RawXBMC.Execute( "SELECT cachedurl FROM texture WHERE url='" + url + "'" )
		    cachedUrlPath = os.path.join( thumbnailsFolder, cachedUrl[0][0] )
		    try: shutil.move( cachedUrlPath, self.destinationFolder )
		    except: pass
		    RawXBMC.Execute( "DELETE FROM texture WHERE url='" + url + "'" )
	       self.queryTable()
	  elif controlId == self.idQuit: self.close()