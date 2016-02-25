from __future__ import unicode_literals
from addon.common.addon import Addon
import sys,os
import urlparse,urllib
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from resources.lib.modules import control


addon = Addon('plugin.video.castaway', sys.argv)
addon_handle = int(sys.argv[1])

AddonPath = addon.get_path()
IconPath = os.path.join(AddonPath , "resources/media/")
fanart = os.path.join(AddonPath + "/fanart.jpg")
def icon_path(filename):
    if 'http://' in filename:
        return filename
    return os.path.join(IconPath, filename)

args = urlparse.parse_qs(sys.argv[2][1:])
mode = args.get('mode', None)


if mode is None:
    addon.add_item({'mode': 'live_sport'}, {'title':'Live Sport'}, img=icon_path('live_sport.jpg'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'live_tv'}, {'title':'Live TV'}, img=icon_path('live_tv.jpg'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'p2p_corner'}, {'title':'P2P Corner'}, img=icon_path('p2p_corner.jpg'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'on_demand_sport_categories'}, {'title':'Sport On Demand'}, img=icon_path('sport_on_demand.jpg'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'tools'}, {'title':'Tools'}, img=icon_path('tools.jpg'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'my_castaway'}, {'title':'My Castaway'}, img=icon_path('my_castaway.jpg'), fanart=fanart,is_folder=True)

    addon.end_of_directory()
    from resources.lib.modules import cache, control, changelog
    cache.get(changelog.get, 600000000, control.addonInfo('version'), table='changelog')
    

elif mode[0]=='my_castaway':
    addon.add_item({'mode': 'keyboard_open'}, {'title':'Open URL'}, img=icon_path('live.png'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'x'}, {'title':'[COLOR yellow]Follow me @natko1412[/COLOR]'}, img=icon_path('twitter.png'), fanart=fanart)
    addon.end_of_directory()


elif mode[0]=='keyboard_open':
    keyboard = xbmc.Keyboard('', 'Enter URL:', False)
    keyboard.doModal()
    if keyboard.isConfirmed():
        query = keyboard.getText()
        import liveresolver
        url=query
        resolved = liveresolver.resolve(url)
        xbmc.Player().play(resolved)

elif mode[0] == 'live_sport':
    sources = os.listdir(AddonPath + '/resources/lib/sources/live_sport')
    sources.remove('__init__.py')
    for source in sources:
        if '.pyo' not in source and '__init__' not in source:
            try:
                source = source.replace('.py','')
                exec "from resources.lib.sources.live_sport import %s"%source
                info = eval(source+".info()")
                addon.add_item({'mode': 'open_live_sport', 'site': info.mode}, {'title': info.name}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
            except:
                pass
    addon.end_of_directory()



elif mode[0] == 'live_tv':
    sources = os.listdir(AddonPath + '/resources/lib/sources/live_tv')
    sources.remove('__init__.py')
    for source in sources:
        if '.pyo' not in source and '__init__' not in source:
            try:
                source = source.replace('.py','')
                exec "from resources.lib.sources.live_tv import %s"%source
                info = eval(source+".info()")
                addon.add_item({'mode': 'open_live_tv', 'site': info.mode}, {'title': info.name}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
            except:
                pass
    addon.end_of_directory()


elif mode[0] == 'on_demand_sport_categories':
    addon.add_item({'mode': 'on_demand_sport', 'category':'football'}, {'title':'Football'}, img=icon_path('icons/soccer.png'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'on_demand_sport', 'category':'basketball'}, {'title':'Basketball'}, img=icon_path('icons/basketball.png'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'on_demand_sport', 'category':'american_football'}, {'title':'American Football'}, img=icon_path('icons/football.png'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'on_demand_sport', 'category':'hockey'}, {'title':'Hockey'}, img=icon_path('icons/hockey.png'), fanart=fanart,is_folder=True)

    addon.end_of_directory()

elif mode[0] == 'on_demand_sport':
    cat = args['category'][0]
    sources = os.listdir(AddonPath + '/resources/lib/sources/on_demand_sport/%s'%cat)
    sources.remove('__init__.py')
    for source in sources:
        if '.pyo' not in source and '__init__' not in source:
            try:
                source = source.replace('.py','')
                exec "from resources.lib.sources.on_demand_sport.%s import %s"%(cat,source)
                info = eval(source+".info()")
                addon.add_item({'mode': 'open_demand_sport', 'site': info.mode, 'category':cat}, {'title': info.name}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
            except:
                pass
    addon.end_of_directory()

elif mode[0] == 'p2p_corner':
    sources = os.listdir(AddonPath + '/resources/lib/sources/p2p_sport')
    sources.remove('__init__.py')
    for source in sources:
        if '.pyo' not in source and '__init__' not in source:
            try:
                source = source.replace('.py','')
                exec "from resources.lib.sources.p2p_sport import %s"%source
                info = eval(source+".info()")
                addon.add_item({'mode': 'open_p2p_sport', 'site': info.mode}, {'title': info.name}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
            except:
                pass
    addon.end_of_directory()













elif mode[0] == 'open_live_sport':
    site = args['site'][0]
    exec "from resources.lib.sources.live_sport import %s"%site
    source = eval(site+".main()")
    info = eval(site+".info()")
    if not info.categorized:
        events = source.events()
        for event in events:
            if not info.multilink:
                browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
                context = [('Open in browser','RunPlugin(%s)'%browser)]
                addon.add_video_item({'mode': 'play', 'url': event[0], 'title':event[1], 'img': icon_path(info.icon)}, {'title': event[1]}, img=icon_path(info.icon), fanart=fanart, contextmenu_items=context)
            else:
                addon.add_item({'mode': 'get_sport_event','site':site, 'url': event[0], 'title':event[1], 'img': icon_path(info.icon)}, {'title': event[1]}, img=icon_path(info.icon), fanart=fanart,is_folder=True)

    else:
        source = eval(site+".main()")
        categories  = source.categories()
        for cat in categories:
            addon.add_item({'mode': 'open_sport_cat', 'url': cat[0], 'site': info.mode}, {'title': cat[1]}, img=icon_path(cat[2]), fanart=fanart,is_folder=True)

    addon.end_of_directory()




elif mode[0] == 'open_live_tv':
    site = args['site'][0]
    try:
        next_page = args['next'][0]
    except:
        next_page = None
    exec "from resources.lib.sources.live_tv import %s"%site
    info = eval(site+".info()")
    try: special = info.special
    except: special = False
    if not info.categorized:
        if next_page:
            source = eval(site+".main(url=next_page)")
        else:
            source = eval(site+".main()")
        channels = source.channels()
        for channel in channels:
            if not info.multilink:
                browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(channel[0])
                context = [('Open in browser','RunPlugin(%s)'%browser)]
                if not special:
                    addon.add_video_item({'mode': 'play', 'url': channel[0], 'title': channel[1], 'img':channel[2]}, {'title': channel[1]}, img=channel[2], fanart=fanart, contextmenu_items=context)
                else:
                    addon.add_item({'mode': 'play_special', 'url': channel[0], 'title': channel[1], 'img':channel[2], 'site': site}, {'title': channel[1]}, img=channel[2], fanart=fanart, contextmenu_items=context, is_folder=True)
            else:

                addon.add_item({'mode': 'get_tv_event', 'url': channel[0],'site':site , 'title':channel[1], 'img': channel[2]}, {'title': channel[1]}, img=channel[2], fanart=fanart,is_folder=True)

        if (info.paginated and source.next_page()):
            addon.add_item({'mode': 'open_live_tv', 'site': info.mode, 'next' : source.next_page()}, {'title': 'Next Page >>'}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
    else:
        source = eval(site+".main()")
        categories  = source.categories()
        for cat in categories:
            thumb = cat[2]
            if not 'http' in thumb:
                thumb = icon_path(thumb)
            addon.add_item({'mode': 'open_tv_cat', 'url': cat[0], 'site': info.mode}, {'title': cat[1]}, img=thumb, fanart=fanart, is_folder=True)


    addon.end_of_directory()

elif mode[0] == 'open_p2p_sport':
    site = args['site'][0]
    try:
        next_page = args['next'][0]
    except:
        next_page = None
    exec "from resources.lib.sources.p2p_sport import %s"%site
    info = eval(site+".info()")
    if not info.categorized:
        if next_page:
            source = eval(site+".main(url=next_page)")
        else:
            source = eval(site+".main()")
        channels = source.channels()
        for event in channels:
            if not info.multilink:
                browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
                context = [('Open in browser','RunPlugin(%s)'%browser)]
                addon.add_video_item({'mode': 'play', 'url': event[0],'title':event[1], 'img': event[2]}, {'title': event[1]}, img=event[2], fanart=fanart, contextmenu_items=context)
            else:
                addon.add_item({'mode': 'get_p2p_event', 'url': event[0],'site':site , 'title':event[1], 'img': event[2]}, {'title': event[1]}, img=event[2], fanart=fanart,is_folder=True)
    
        if (info.paginated and source.next_page()):
            addon.add_item({'mode': 'open_live_p2p', 'site': info.mode, 'next' : source.next_page()}, {'title': 'Next Page >>'}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
    else:
        source = eval(site+".main()")
        categories  = source.categories()
        for cat in categories:
            addon.add_item({'mode': 'open_p2p_cat', 'url': cat[0], 'site': info.mode}, {'title': cat[1]}, img=icon_path(cat[2]), fanart=fanart,is_folder=True)

    addon.end_of_directory()








elif mode[0]=='open_p2p_cat':
    url = args['url'][0]
    site = args['site'][0]
    exec "from resources.lib.sources.p2p_sport import %s"%site
    info = eval(site+".info()")
    source = eval(site+".main()")
    channels = source.channels(url)

    for event in channels:
        if not info.multilink:
            browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
            context= [('Open in browser','RunPlugin(%s)'%browser)]
            addon.add_video_item({'mode': 'play', 'url': event[0],'title':event[1], 'img': event[2]}, {'title': event[1]}, img=event[2], fanart=fanart,contextmenu_items=context)
        else:
            addon.add_item({'mode': 'get_p2p_event', 'url': event[0],'site':site , 'title':event[1], 'img': event[2]}, {'title': event[1]}, img=event[2], fanart=fanart,is_folder=True)
    
    if (info.paginated and source.next_page()):
        addon.add_item({'mode': 'open_p2p_cat', 'site': info.mode, 'url': source.next_page()}, {'title': 'Next Page >>'}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
    
    addon.end_of_directory()

elif mode[0] == 'open_demand_sport':
    cat = args['category'][0]
    site = args['site'][0]
    try:
        next_page = args['next'][0]
    except:
        next_page = None
    exec "from resources.lib.sources.on_demand_sport.%s import %s"%(cat,site)
    info = eval(site+".info()")
    if not info.categorized:
        if next_page:
            source = eval(site+".main(url=next_page)")
        else:
            source = eval(site+".main()")
        items = source.items()
        for item in items:
            if info.multilink:
                addon.add_item({'mode': 'open_od_item', 'url': item[1], 'title': item[0], 'img':item[2],'site': info.mode, 'category':cat}, {'title': item[0]}, img=item[2], fanart=fanart,is_folder=True)
            else:
                addon.add_item({'mode': 'play_od_item', 'url': item[1], 'title': item[0], 'img':item[2],'site': info.mode, 'category':cat}, {'title': item[0]}, img=item[2], fanart=fanart)

        if (info.paginated and source.next_page()):
            addon.add_item({'mode': 'open_demand_sport','site': info.mode, 'next' : source.next_page(), 'category':cat}, {'title': 'Next Page >>'}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
    else:
        source = eval(site+".main()")
        categories  = source.categories()
        for c in categories:
            addon.add_item({'mode': 'open_demand_cat', 'url': c[0], 'site': info.mode, 'category':cat}, {'title': c[1]}, img=icon_path(c[2]), fanart=fanart,is_folder=True)


    addon.end_of_directory()

elif mode[0] == 'open_demand_cat':
    site = args['site'][0]
    url = args['url'][0]
    cat = args['category'][0]
    try:
        next_page = args['next'][0]
    except:
        next_page = None
    exec "from resources.lib.sources.on_demand_sport.%s import %s"%(cat,site)
    info = eval(site+".info()")
    if next_page:
        source = eval(site+".main(url=next_page)")
    else:
        source = eval(site+".main(url=url)")
    items = source.items()
    for item in items:
        if info.multilink:
            addon.add_item({'mode': 'open_od_item', 'url': item[1], 'title': item[0], 'img':item[2],'site': info.mode, 'category':cat}, {'title': item[0]}, img=item[2], fanart=fanart,is_folder=True)
        else:
            addon.add_item({'mode': 'play_od_item', 'url': item[1], 'title': item[0], 'img':item[2],'site': info.mode, 'category':cat}, {'title': item[0]}, img=item[2], fanart=fanart)

    if (info.paginated and source.next_page()):
        addon.add_item({'mode': 'open_demand_cat', 'url': source.next_page(), 'site': info.mode, 'next' : source.next_page(), 'category':cat}, {'title': 'Next Page >>'}, img=icon_path(info.icon), fanart=fanart,is_folder=True)


    addon.end_of_directory()


elif mode[0]=='open_tv_cat':
    url = args['url'][0]
    site = args['site'][0]
    exec "from resources.lib.sources.live_tv import %s"%site
    info = eval(site+".info()")
    source = eval(site+".main()")
    channels = source.channels(url)

    for event in channels:
        if not info.multilink:
            browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
            context = [('Open in browser','RunPlugin(%s)'%browser)]
            addon.add_video_item({'mode': 'play', 'url': event[0],'title':event[1], 'img': event[2]}, {'title': event[1]}, img=event[2], fanart=fanart, contextmenu_items=context)
        else:
            addon.add_item({'mode': 'get_tv_event', 'url': event[0],'site':site , 'title':event[1], 'img': event[2]}, {'title': event[1]}, img=event[2], fanart=fanart,is_folder=True)
    
    if (info.paginated and source.next_page()):
        addon.add_item({'mode': 'open_tv_cat', 'site': info.mode, 'url': source.next_page()}, {'title': 'Next Page >>'}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
    
    addon.end_of_directory()


elif mode[0]=='open_sport_cat':
    url = args['url'][0]
    site = args['site'][0]
    exec "from resources.lib.sources.live_sport import %s"%site
    info = eval(site+".info()")
    source = eval(site+".main()")
    events = source.events(url)
    for event in events:
        if not info.multilink:
            browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
            context = [('Open in browser','RunPlugin(%s)'%browser)]
            addon.add_video_item({'mode': 'play', 'url': event[0],'title':event[1], 'img': icon_path(info.icon)}, {'title': event[1]}, img=icon_path(info.icon), fanart=fanart, contextmenu_items=context)
        else:
            addon.add_item({'mode': 'get_sport_event', 'url': event[0],'site':site , 'title':event[1], 'img': icon_path(info.icon)}, {'title': event[1]}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
    if (info.paginated and source.next_page()):
        addon.add_item({'mode': 'open_cat', 'site': info.mode, 'url': source.next_page()}, {'title': 'Next Page >>'}, img=icon_path(info.icon), fanart=fanart,is_folder=True)
    
    addon.end_of_directory()


elif mode[0]=='open_od_item':
    url = args['url'][0]
    title = args['title'][0]
    site = args['site'][0]
    img = args['img'][0]
    cat = args['category'][0]
    exec "from resources.lib.sources.on_demand_sport.%s import %s"%(cat,site)
    info = eval(site+".info()")
    source = eval(site+".main()")
    links = source.links(url)
    for link in links:
        addon.add_item({'mode': 'play_od_item', 'url': link[1], 'title': title, 'img':img,'site': info.mode, 'category':cat}, {'title': link[0]}, img=img, fanart=fanart)
    addon.end_of_directory()




elif mode[0]=='get_sport_event':
    url = args['url'][0]
    title = args['title'][0]
    site = args['site'][0]
    img = args['img'][0]
    exec "from resources.lib.sources.live_sport import %s"%site
    info = eval(site+".info()")
    source = eval(site+".main()")
    events = source.links(url)

    #auto play if only 1 link
    if len(events)==1:
        import liveresolver
        resolved = liveresolver.resolve(events[0][0])
        player=xbmc.Player()
        li = xbmcgui.ListItem(title)
        li.setThumbnailImage(icon_path(info.icon))
        player.play(resolved,listitem=li)
    else:
        autoplay = addon.get_setting('autoplay')
        if autoplay == 'false':
            for event in events:
                browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
                context = [('Open in browser','RunPlugin(%s)'%browser)]
                addon.add_video_item({'mode': 'play', 'url': event[0],'title':title, 'img': img}, {'title': event[1]}, img=img, fanart=fanart, contextmenu_items=context)
            addon.end_of_directory()
        else:
            for event in events:
                import liveresolver
                try:
                    resolved = liveresolver.resolve(event[0])
                except:
                    resolved = None
                if resolved:
                    player=xbmc.Player()
                    li = xbmcgui.ListItem(title)
                    li.setThumbnailImage(img)
                    player.play(resolved,listitem=li)
                    break
            control.infoDialog("No stream found")

elif mode[0]=='get_tv_event':
    url = args['url'][0]
    title = args['title'][0]
    site = args['site'][0]
    img = args['img'][0]
    exec "from resources.lib.sources.live_tv import %s"%site
    info = eval(site+".info()")
    source = eval(site+".main()")
    events = source.links(url)

    #auto play if only 1 link
    if len(events)==1:
        import liveresolver
        resolved = liveresolver.resolve(events[0][0])
        player=xbmc.Player()
        li = xbmcgui.ListItem(title)
        li.setThumbnailImage(icon_path(info.icon))
        player.play(resolved,listitem=li)
    else:
        autoplay = addon.get_setting('autoplay')
        if autoplay == 'false':
            for event in events:
                browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
                context = [('Open in browser','RunPlugin(%s)'%browser)]
                addon.add_video_item({'mode': 'play', 'url': event[0],'title':title, 'img': img}, {'title': event[1]}, img=img, fanart=fanart, contextmenu_items=context)
            addon.end_of_directory()
        else:
            for event in events:
                import liveresolver
                try:
                    resolved = liveresolver.resolve(event[0])
                except:
                    resolved = None
                if resolved:
                    player=xbmc.Player()
                    li = xbmcgui.ListItem(title)
                    li.setThumbnailImage(img)
                    player.play(resolved,listitem=li)
                    break
            control.infoDialog("No stream found")

elif mode[0]=='get_p2p_event':
    url = args['url'][0]
    title = args['title'][0]
    site = args['site'][0]
    img = args['img'][0]
    exec "from resources.lib.sources.p2p_sport import %s"%site
    info = eval(site+".info()")
    source = eval(site+".main()")
    events = source.links(url)

    #auto play if only 1 link
    if len(events)==1:
        import liveresolver
        resolved = liveresolver.resolve(events[0][0])
        player=xbmc.Player()
        li = xbmcgui.ListItem(title)
        li.setThumbnailImage(icon_path(info.icon))
        player.play(resolved,listitem=li)
    else:
        autoplay = addon.get_setting('autoplay')
        if autoplay == 'false':
            for event in events:
                browser = 'plugin://plugin.program.chrome.launcher/?url=%s&mode=showSite&stopPlayback=no'%(event[0])
                context = [('Open in browser','RunPlugin(%s)'%browser)]
                addon.add_video_item({'mode': 'play', 'url': event[0],'title':title, 'img': img}, {'title': event[1]}, img=img, fanart=fanart, contextmenu_items=context)
            addon.end_of_directory()
        else:
            for event in events:
                import liveresolver
                try:
                    resolved = liveresolver.resolve(event[0])
                except:
                    resolved = None
                if resolved:
                    player=xbmc.Player()
                    li = xbmcgui.ListItem(title)
                    li.setThumbnailImage(img)
                    player.play(resolved,listitem=li)
                    break
            control.infoDialog("No stream found")




elif mode[0] == 'play':
    url = args['url'][0]
    title = args['title'][0]
    img = args['img'][0]
    import liveresolver
    resolved = liveresolver.resolve(url)
    li = xbmcgui.ListItem(title, path=resolved)
    li.setThumbnailImage(img)
    li.setLabel(title)
    li.setProperty('IsPlayable', 'true')
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, li)

elif mode[0] == 'play_special':
    url = args['url'][0]
    title = args['title'][0]
    img = args['img'][0]
    site = args['site'][0]
    exec "from resources.lib.sources.live_tv import %s"%(site)
    source = eval(site+'.main()')
    resolved = source.resolve(url)
    li = xbmcgui.ListItem(title, iconImage=img)
    li.setThumbnailImage(img)
    xbmc.Player().play(resolved, li)

elif mode[0]=='play_od_item':
    url = args['url'][0]
    title = args['title'][0]
    site = args['site'][0]
    img = args['img'][0]
    cat = args['category'][0]
    exec "from resources.lib.sources.on_demand_sport.%s import %s"%(cat,site)
    info = eval(site+".info()")
    source = eval(site+".main()")
    resolved = source.resolve(url)
    li = xbmcgui.ListItem(title, path=resolved)
    li.setThumbnailImage(img)
    li.setLabel(title)
    li.setProperty('IsPlayable', 'true')
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, li)
       

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################
####
####______________________________________________________________________________________________TOOLS_________________________________________________________________________________________________
####
########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################


elif mode[0]=='tools':
    addon.add_item({'mode': 'addon_installer'}, {'title':'Install external addons'}, img=icon_path('tools.jpg'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'settings'}, {'title':'Settings'}, img=icon_path('tools.jpg'), fanart=fanart,is_folder=True)
    addon.add_item({'mode': 'x'}, {'title':'[COLOR yellow]Follow me @natko1412[/COLOR]'}, img=icon_path('twitter.png'), fanart=fanart)

    addon.end_of_directory()


elif mode[0]=='settings':
    from resources.lib.modules import control
    control.openSettings()

elif mode[0]=='addon_installer':
    from resources.lib.modules import addonInstaller
    addons = addonInstaller.get_addons()
    for a in addons:
        addon.add_item({'mode': 'install', 'id':a[2], 'key':a[1], 'name':a[0]}, {'title': a[0], 'plot': 'Install addon'}, img=a[3], fanart=fanart, is_folder=True)

    addon.end_of_directory()

elif mode[0]=='install':
    id = args['id'][0]
    key = args['key'][0]
    name = args['name'][0]

    from resources.lib.modules import addonInstaller
    if not addonInstaller.isInstalled(id):
        addonInstaller.install(key)
    else:
        from resources.lib.modules import control
        control.infoDialog('%s already installed'%name)

