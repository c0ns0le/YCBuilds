import xbmcaddon
import xbmcgui
 
__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
 
line1 = "iVue Tv Guide has Ceased, For more information GOTO ivuetvguide.com or Facebook group"
line2 = "I'm afraid the amount of leeches and sellers and profiteers abusing this service has forced it to close"
line3 = "But for the true users of iVue GOTO the above group or pages and learn about iVue2"
 
xbmcgui.Dialog().ok(__addonname__, line1, line2, line3)