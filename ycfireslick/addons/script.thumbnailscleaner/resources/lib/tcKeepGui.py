# -*- coding: utf-8 -*-

###########################
# Thumbnails Cleaner      #
# by Max (m4x1m) Headroom #
###########################

import xbmcgui
from tcCommon import *

class tcKeepGui( xbmcgui.WindowXMLDialog ):

     def __init__( self, xmlFile, resourcePath, defaultName = 'Default', forceFallback = False, parent = None ):
	  xbmcgui.WindowXML.__init__( self )
	  self.choose = []
	  self.parent = parent
	  self.selelectKeepTextures()

     def onInit( self ):
	  self.defineControls()
	  self.labelTitle.setLabel( addonLanguage(32147) )
	  self.buttonAll.setLabel( addonLanguage(32141) )
	  self.buttonNone.setLabel( addonLanguage(32142) )
	  self.buttonProceed.setLabel( addonLanguage(32143) )
	  self.buttonAbort.setLabel( addonLanguage(32146) )
	  self.itemsList.reset()
	  for itemList in self.parent.texturesList: self.itemsList.addItem( xbmcgui.ListItem( itemList[0] ) )

     def defineControls( self ):
	  # IDs
	  self.idList    = 10
	  self.idTitle   = 90
	  self.idAll     = 91
	  self.idNone    = 92
	  self.idProceed = 93
	  self.idAbort   = 94
	  # Controls
	  self.itemsList     = self.getControl( self.idList )
	  self.labelTitle    = self.getControl( self.idTitle )
	  self.buttonAll     = self.getControl( self.idAll )
	  self.buttonNone    = self.getControl( self.idNone )
	  self.buttonProceed = self.getControl( self.idProceed )
	  self.buttonAbort   = self.getControl( self.idAbort )

     def selelectKeepTextures( self ):
	  self.doModal()

     def onClick( self, controlId ):
	  if controlId == self.idList:
	       itemSelected = self.itemsList.getSelectedItem()
	       try:
		    self.choose.remove( itemSelected.getLabel() )
		    itemSelected.setIconImage( "" )
	       except:
		    self.choose.append( itemSelected.getLabel() )
		    itemSelected.setIconImage( keepIcon )
	  elif controlId == self.idAll:
	       self.choose = []
	       for i in range( 0, len( self.parent.texturesList ) ):
		    item = self.itemsList.getListItem( i )
		    self.choose.append( item.getLabel() )
		    item.setIconImage( keepIcon )
	  elif controlId == self.idNone:
	       self.choose = []
	       for i in range( 0, len( self.parent.texturesList ) ):
		    item = self.itemsList.getListItem( i )
		    item.setIconImage( "" )
	  elif controlId == self.idProceed:
	       self.parent.keepTextures = self.choose
	       self.close()
	  elif controlId == self.idAbort:
	       self.parent.cancelOperation = True
	       self.close()