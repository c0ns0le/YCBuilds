# -*- coding: utf-8 -*-

###########################
# Thumbnails Cleaner      #
# by Max (m4x1m) Headroom #
###########################

import xbmcgui
from tcMain import *
from tcCommon import *

class tcMainGui( xbmcgui.WindowXMLDialog ):

     def __init__( self, *args, **kwargs ):
	  xbmcgui.WindowXMLDialog.__init__( self )
	  self.doModal()

     def onInit( self ):
	  self.defineControls()
	  # Fixed Labels
	  self.labelTitle.setLabel("%s v%s" % ( addonName, addonVersion ) )
	  self.labelAuthor.setLabel("by %s" % addonAuthor )
	  self.labelFiles.setLabel( addonLanguage(32130) )
	  self.labelSizes.setLabel( addonLanguage(32131) )
	  self.labelTextures.setLabel( addonLanguage(32132) )
	  self.labelBefore.setLabel( addonLanguage(32133) )
	  self.labelAfter.setLabel( addonLanguage(32134) )
	  # Buttons Labels
	  self.buttonClean.setLabel( addonLanguage(32135) )
	  self.buttonSimulate.setLabel( addonLanguage(32136) )
	  self.buttonQuery.setLabel( addonLanguage(32137) )
	  self.buttonEmpty.setLabel( addonLanguage(32138) )
	  self.buttonSettings.setLabel( addonLanguage(32139) )
	  self.buttonExit.setLabel( addonLanguage(32140) )
	  Cleaner( self ).setLabelInfo()
	  log( normalize( "Database folder selected: " + databaseFolder ) )
	  log( normalize( "Thumbnails folder selected: " + thumbnailsFolder ) )

     def defineControls( self ):
	  self.idCancel = (9, 10)
	  # Id Fixed Labels
	  self.idTitle    = 90
	  self.idAuthor   = 91
	  self.idFiles    = 92
	  self.idSizes    = 93
	  self.idTextures = 94
	  self.idBefore   = 95
	  self.idAfter    = 96
	  # Id Output
	  self.idBeforeFiles    = 220
	  self.idBeforeSizes    = 221
	  self.idBeforeTextures = 222
	  self.idAfterFiles     = 223
	  self.idAfterSizes     = 224
	  self.idAfterTextures  = 225
	  # Id Buttons
	  self.idClean    = 21
	  self.idSimulate = 22
	  self.idQuery    = 23
	  self.idEmpty    = 24
	  self.idSettings = 25
	  self.idExit     = 26
	  # Fixed Labels
	  self.labelTitle    = self.getControl(self.idTitle)
	  self.labelAuthor   = self.getControl(self.idAuthor)
	  self.labelFiles    = self.getControl(self.idFiles)
	  self.labelSizes    = self.getControl(self.idSizes)
	  self.labelTextures = self.getControl(self.idTextures)
	  self.labelBefore   = self.getControl(self.idBefore)
	  self.labelAfter    = self.getControl(self.idAfter)
	  # Output
	  self.labelBeforeFiles    = self.getControl(self.idBeforeFiles)
	  self.labelBeforeSizes    = self.getControl(self.idBeforeSizes)
	  self.labelBeforeTextures = self.getControl(self.idBeforeTextures)
	  self.labelAfterFiles     = self.getControl(self.idAfterFiles)
	  self.labelAfterSizes     = self.getControl(self.idAfterSizes)
	  self.labelAfterTextures  = self.getControl(self.idAfterTextures)
	  # Buttons
	  self.buttonClean    = self.getControl(self.idClean)
	  self.buttonSimulate = self.getControl(self.idSimulate)
	  self.buttonQuery    = self.getControl(self.idQuery)
	  self.buttonEmpty    = self.getControl(self.idEmpty)
	  self.buttonSettings = self.getControl(self.idSettings)
	  self.buttonExit     = self.getControl(self.idExit)

     def onClick( self, controlId ):
	  if controlId == self.idClean: Cleaner( self ).doClean(False)
	  elif controlId == self.idSimulate: Cleaner( self ).doClean(True)
	  elif controlId == self.idQuery: Cleaner( self ).queryGui()
	  elif controlId == self.idEmpty: Cleaner( self ).emptyTable()
	  elif controlId == self.idSettings: addonSettings.openSettings()
	  elif controlId == self.idExit: self.closeDialog()

     def closeDialog( self ):
	  self.close()