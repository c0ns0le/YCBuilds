'''
    USTVnow Plus Add-on
    
    This version of USTVnow has been built by combining the best of all
    available version of USTVnow found online. This version has been streamlined 
    to use the USTVnow API directly to avoid many of the issues in previous versions.

    The following developers have all contributed to this version directly or indirectly.

    mhancoc7, t0mm0, jwdempsey, esxbr, Lunatixz, yrabl, ddurdle

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from resources.lib import Addon, ustvnow_plus
import sys, os, urllib, urllib2
import json
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addonid   = addon.getAddonInfo('id')
plugin_path = xbmcaddon.Addon(id=addonid).getAddonInfo('path')

Addon.plugin_url = sys.argv[0]
Addon.plugin_handle = int(sys.argv[1])
Addon.plugin_queries = Addon.parse_query(sys.argv[2][1:])

write_path = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'guide'))

setup = Addon.get_setting('setup')
setup_new = Addon.get_setting('setup_new')
email = Addon.get_setting('email')
password = Addon.get_setting('password')
ustv = ustvnow_plus.Ustvnow(email, password)

dlg = xbmcgui.Dialog()

Addon.log('plugin url: ' + Addon.plugin_url)
Addon.log('plugin queries: ' + str(Addon.plugin_queries))
Addon.log('plugin handle: ' + str(Addon.plugin_handle)) 

if int(Addon.get_setting('quality')) < 0:
    Addon.set_setting('quality', '0')
elif int(Addon.get_setting('quality')) > 3:
    Addon.set_setting('quality', '3')

if int(Addon.get_setting('rec_quality')) < 0:
    Addon.set_setting('rec_quality', '0')
elif int(Addon.get_setting('rec_quality')) > 2:
    Addon.set_setting('rec_quality', '2')

quality_type = int(Addon.get_setting('quality'))

rec_quality_type = int(Addon.get_setting('rec_quality'))

if setup != 'true':
    dlg.ok(Addon.get_string(30000),Addon.get_string(20002),Addon.get_string(20003))
    # Enter Email
    retval = dlg.input(Addon.get_string(20004), type=xbmcgui.INPUT_ALPHANUM)
    if retval and len(retval) > 0:
        Addon.set_setting('email', str(retval))
        email = Addon.get_setting('email')
    # Enter Password
    retval = dlg.input(Addon.get_string(20005), type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
    if retval and len(retval) > 0:
        Addon.set_setting('password', str(retval))
        password = Addon.get_setting('password')
    if len(Addon.get_setting('email')) > 0 and len(Addon.get_setting('password')) > 0:
        Addon.set_setting('setup', 'true')
        dlg.ok(Addon.get_string(30000), Addon.get_string(200001), Addon.get_string(200000))
    else:
        dlg.ok(Addon.get_string(30000), Addon.get_string(20002),Addon.get_string(20003))
elif setup_new != 'true':
    dlg.ok(Addon.get_string(30000),Addon.get_string(50000),Addon.get_string(50001))
    Addon.set_setting('setup_new', 'true')

mode = Addon.plugin_queries['mode']

if mode == 'main':
    Addon.log(mode)
    ustv.build_main()

elif mode == 'live':
    channels = ustv.get_channels(quality_type)
    if channels:
        for c in channels:
            rURL = "plugin://plugin.video.ustvnow.tva/?name=" + c['name'] + "&mode=play"
            name = c["name"];
            if Addon.get_setting('logo') == '0':
                logo = c["poster_url"];
                poster_url = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', c['name']+'.png'))
            else:
                logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', c['name']+'.png'))
                poster_url = c["poster_url"];
            episode_title = c["episode_title"];
            title = c["title"];
            plot = c["plot"].replace("&amp;", "&").replace('&quot;','"');
            mediatype = c["mediatype"];
            if mediatype != "movie":
                tvshowtitle = title
            if name == 'AE':
                name = 'A&E'
            if name == 'MY9':
                name = 'My9'
            if episode_title != "":
                title = '%s - %s - %s (Started at %s)' % (name, (title).replace('&amp;','&').replace('&quot;','"'), (episode_title).replace('&amp;','&').replace('&quot;','"').replace(';',' -'), c['event_date_time'])
            else:
                title = '%s - %s (Started at %s)' % (name, (title).replace('&amp;','&').replace('&quot;','"'), c['event_date_time'])
            cm_refresh = (Addon.get_string(30007), 
                      'XBMC.RunPlugin(%s/?mode=refresh)' % 
                           (Addon.plugin_url))
            cm_rec = (Addon.get_string(30008), 
                      'XBMC.RunPlugin(%s/?mode=record&rec=%s&set=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(c['rec_url']),urllib.quote(c['set_url']),urllib.quote(c['mediatype'])))
            cm_increase = (Addon.get_string(30105) + Addon.qualityName(quality_type + 1), 
                          'XBMC.RunPlugin(%s/?mode=increase)' % 
                               (Addon.plugin_url))
            cm_decrease = (Addon.get_string(30107)  + Addon.qualityName(quality_type - 1), 
                          'XBMC.RunPlugin(%s/?mode=decrease)' % 
                               (Addon.plugin_url))
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_rec]
                
            elif Addon.get_setting('rec_live') == 'false' and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase]
                
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_rec]
                
            elif Addon.get_setting('rec_live') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and  name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and  name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase]
                
            else:
                cm_menu = [cm_refresh]
            if Addon.get_setting('extended_context') == 'true':
                cm_view = False
            else:
                cm_view = True
            Addon.add_video_item(rURL,
            
                                 {'title': title,
                                 'plot': plot,
                                 'mediatype': mediatype,
                                 'tvshowtitle': tvshowtitle},
                                 img=poster_url, fanart=logo, playable=c['playable'], cm=cm_menu, cm_replace=cm_view)
            xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'recordings':
    recordings = ustv.get_recordings('recordings')
        
    if recordings:
        for r in sorted(recordings, reverse=True):
            rURL = "plugin://plugin.video.ustvnow.tva/?scheduleid=" + str(r['scheduleid']) + "&mode=play_dvr"
            channel = r['channel']
            if r['channel'] == 'AE':
                channel = 'A&E'
            if r['channel'] == 'MY9':
                channel = 'My9'
            if r['episode_title'] != "":
                title = '%s - %s (Recorded: %s on %s) - (Expires: %s)' % (r['title'], r['episode_title'], r['event_date_time'], channel ,r['expire_date_time'])
                title = title.replace('&amp;','&').replace('&quot;','"')
            else:
                title = '%s (Recorded: %s on %s) - (Expires: %s)' % (r['title'], r['event_date_time'], channel ,r['expire_date_time'])
                title = title.replace('&amp;','&').replace('&quot;','"')

            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', r['channel']+'.png'))
            poster_url = r["icon"];
            dvrtimertype = r['dvrtimertype']
            mediatype = r['mediatype']
            cm_refresh = (Addon.get_string(30007),
                  'XBMC.RunPlugin(%s/?mode=refresh)' % 
                       (Addon.plugin_url))
            cm_set_recurring = (Addon.get_string(30026), 
                      'XBMC.RunPlugin(%s/?mode=set&set=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['set_url'])))
            cm_del_recurring = (Addon.get_string(30022), 
                      'XBMC.RunPlugin(%s/?mode=remove&remove=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['remove_url'])))
            cm_del = (Addon.get_string(30004), 
                      'XBMC.RunPlugin(%s/?mode=delete&del=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['del_url'])))
            cm_increase = (Addon.get_string(30105) + Addon.qualityName(rec_quality_type + 1), 
                          'XBMC.RunPlugin(%s/?mode=increase_rec)' % 
                               (Addon.plugin_url))
            cm_decrease = (Addon.get_string(30107) + Addon.qualityName(rec_quality_type - 1), 
                          'XBMC.RunPlugin(%s/?mode=decrease_rec)' % 
                               (Addon.plugin_url))
            if Addon.get_setting('rec_live') == 'true' and dvrtimertype == 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV' and rec_quality_type == 2:
                cm_menu = [cm_refresh, cm_decrease, cm_set_recurring, cm_del]
            elif Addon.get_setting('rec_live') == 'true' and dvrtimertype == 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV' and rec_quality_type == 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_set_recurring, cm_del]
            elif Addon.get_setting('rec_live') == 'true' and dvrtimertype == 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV' and rec_quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_set_recurring, cm_del]
            elif  Addon.get_setting('rec_live') == 'true' and dvrtimertype != 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV' and rec_quality_type == 2:
                cm_menu = [cm_refresh, cm_decrease, cm_del_recurring]
            elif  Addon.get_setting('rec_live') == 'true' and dvrtimertype != 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV' and rec_quality_type == 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_del_recurring]
            elif  Addon.get_setting('rec_live') == 'true' and dvrtimertype != 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV' and rec_quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_del_recurring]
            elif  Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and mediatype == 'MV' and rec_quality_type == 2:
                cm_menu = [cm_refresh, cm_decrease, cm_del]
            elif  Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and mediatype == 'MV' and rec_quality_type == 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_del]
            elif  Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and mediatype == 'MV' and rec_quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_del]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and rec_quality_type == 2:
                cm_menu = [cm_refresh, cm_decrease, cm_del]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and rec_quality_type == 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_del]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and rec_quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_del]
            else:
                cm_menu = [cm_refresh]
            Addon.add_video_item(rURL, {'title': title, 
                                                   'plot': r['plot'],
                                                   'plotoutline': r['synopsis'],
                                                   'tvshowtitle': r['tvshowtitle'],
                                                   'dateadded': r['rec_date']},
                                 img=poster_url, fanart=logo, cm=cm_menu, cm_replace=True, playable=r['playable'])
        xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'scheduled':
    recordings = ustv.get_recordings('scheduled')
        
    if recordings:
        for r in sorted(recordings, reverse=True):
            channel = r['channel']
            if r['channel'] == 'AE':
                channel = 'A&E'
            if r['channel'] == 'MY9':
                channel = 'My9'
            if r['episode_title'] != "":
                title = '%s - %s (%s on %s)' % (r['title'], r['episode_title'], r['event_date_time'], channel)
                title = title.replace('&amp;','&').replace('&quot;','"')
            else:
                title = '%s (%s on %s)' % (r['title'], r['event_date_time'], channel)
                title = title.replace('&amp;','&').replace('&quot;','"')
            plot = '[B]' + r['title'] + '[/B]'
            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', r['channel']+'.png'))
            poster_url = r["icon"];
            dvrtimertype = r['dvrtimertype']
            mediatype = r['mediatype']
            cm_refresh = (Addon.get_string(30007), 
                  'XBMC.RunPlugin(%s/?mode=refresh)' % 
                       (Addon.plugin_url))
            cm_set_recurring = (Addon.get_string(30026), 
                      'XBMC.RunPlugin(%s/?mode=set&set=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['set_url'])))
            cm_del_recurring = (Addon.get_string(30022), 
                      'XBMC.RunPlugin(%s/?mode=remove&remove=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['remove_url'])))
            cm_del = (Addon.get_string(30004), 
                      'XBMC.RunPlugin(%s/?mode=delete&del=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['del_url'])))
            if Addon.get_setting('rec_live') == 'true' and dvrtimertype == 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV':
                cm_menu = [cm_refresh, cm_set_recurring, cm_del]
            elif  Addon.get_setting('rec_live') == 'true' and dvrtimertype != 0 and Addon.get_setting('dvr') == 'true' and mediatype != 'MV':
                cm_menu = [cm_refresh, cm_del_recurring]
            elif  Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and mediatype == 'MV':
                cm_menu = [cm_refresh, cm_del]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false':
                cm_menu = [cm_refresh, cm_del]
            else:
                cm_menu = [cm_refresh]
            Addon.add_list_item(r['title'], {'title': title, 'plot': plot, 
                                                   'dateadded': r['rec_date']},
                                 img=poster_url, fanart=logo, cm=cm_menu, cm_replace=True, playable=False)
        xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'recurring':
    recordings = ustv.get_recordings('recurring')
        
    if recordings:
        for r in sorted(recordings, reverse=True):
            cm_del_recurring = (Addon.get_string(30022), 
                      'XBMC.RunPlugin(%s/?mode=remove&remove=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['remove_url'])))
            cm_refresh = (Addon.get_string(30007), 
                  'XBMC.RunPlugin(%s/?mode=refresh)' % 
                       (Addon.plugin_url))
            channel = r['channel']
            if r['channel'] == 'AE':
                channel = 'A&E'
            if r['channel'] == 'MY9':
                channel = 'My9'
            title = '%s (%s)' % (r['title'], channel)
            title = title.replace('&amp;','&').replace('&quot;','"')
            plot = '[B]' + r['title'] + '[/B]'
            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', r['channel']+'.png'))
            poster_url = r["icon"];
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true':
                cm_menu = [cm_refresh, cm_del_recurring]
            else:
                cm_menu = [cm_refresh]
            Addon.add_list_item(r['title'], {'title': title, 'plot': plot},
                                 img=poster_url, fanart=logo, cm=cm_menu, cm_replace=True, playable=False)
        xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'movies_now':
    now = ustv.get_movies(int(quality_type), 'now')
        
    if now:
        for r in now:
            channel = r['channel']
            rURL = "plugin://plugin.video.ustvnow.tva/?name=" + r['channel'] + "&mode=play"
            if r['channel'] == 'AE':
                channel = 'A&E'
            if r['channel'] == 'MY9':
                channel = 'My9'

            title = '%s (Started at %s on %s)' % (r['title'], r['event_date_time_now'], channel)
            title = title.replace('&amp;','&').replace('&quot;','"')

            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', r['channel']+'.png'))
            poster_url = r["icon"];
            dvrtimertype = r['dvrtimertype']
            mediatype = r['mediatype']
            cm_refresh = (Addon.get_string(30007),
                  'XBMC.RunPlugin(%s/?mode=refresh)' % 
                       (Addon.plugin_url))
            cm_rec = (Addon.get_string(30008), 
                      'XBMC.RunPlugin(%s/?mode=record&rec=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['rec_url']),urllib.quote(r['mediatype'])))
            cm_increase = (Addon.get_string(30105) + Addon.qualityName(quality_type + 1), 
                          'XBMC.RunPlugin(%s/?mode=increase)' % 
                               (Addon.plugin_url))
            cm_decrease = (Addon.get_string(30107)  + Addon.qualityName(quality_type - 1), 
                          'XBMC.RunPlugin(%s/?mode=decrease)' % 
                               (Addon.plugin_url))
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_rec]
                
            elif Addon.get_setting('rec_live') == 'false' and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase]

            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_rec]
                
            elif Addon.get_setting('rec_live') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase]

            else:
                cm_menu = [cm_refresh]
            Addon.add_video_item(rURL, {'title': title,'plot': r['plot']},
                                 img=poster_url, fanart=logo, cm=cm_menu, cm_replace=True, playable=r['playable'])
        xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'movies_today':
    today = ustv.get_movies(int(quality_type), 'today')
        
    if today:
        for r in today:
            channel = r['channel']
            if r['channel'] == 'AE':
                channel = 'A&E'
            if r['channel'] == 'MY9':
                channel = 'My9'

            title = '%s (%s on %s)' % (r['title'], r['event_date_time'], channel)
            title = title.replace('&amp;','&').replace('&quot;','"')

            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', r['channel']+'.png'))
            poster_url = r["icon"];
            dvrtimertype = r['dvrtimertype']
            mediatype = r['mediatype']
            cm_refresh = (Addon.get_string(30007), 
                  'XBMC.RunPlugin(%s/?mode=refresh)' % 
                       (Addon.plugin_url))
            cm_rec = (Addon.get_string(30008), 
                      'XBMC.RunPlugin(%s/?mode=record&rec=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['rec_url']),urllib.quote(r['mediatype'])))
            
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true':
                cm_menu = [cm_refresh, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9']:
                cm_menu = [cm_refresh, cm_rec]
            else:
                cm_menu = [cm_refresh]
            
            Addon.add_list_item(r['title'], {'title': title,'plot': r['plot']},
                                 img=poster_url, fanart=logo, cm=cm_menu, cm_replace=True, playable=r['playable'])
        xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'movies_later':
    later = ustv.get_movies(int(quality_type), 'later')
        
    if later:
        for r in later:
            channel = r['channel']
            if r['channel'] == 'AE':
                channel = 'A&E'
            if r['channel'] == 'MY9':
                channel = 'My9'

            title = '%s (%s on %s)' % (r['title'], r['event_date_time'], channel)
            title = title.replace('&amp;','&').replace('&quot;','"')
 
            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', r['channel']+'.png'))
            poster_url = r["icon"];
            dvrtimertype = r['dvrtimertype']
            mediatype = r['mediatype']
            cm_refresh = (Addon.get_string(30007), 
                  'XBMC.RunPlugin(%s/?mode=refresh)' % 
                       (Addon.plugin_url))
            cm_rec = (Addon.get_string(30008), 
                      'XBMC.RunPlugin(%s/?mode=record&rec=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(r['rec_url']),urllib.quote(r['mediatype'])))
            
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true':
                cm_menu = [cm_refresh, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and channel in ['CW','ABC','FOX','PBS','CBS','NBC','My9']:
                cm_menu = [cm_refresh, cm_rec]
            else:
                cm_menu = [cm_refresh]
            
            Addon.add_list_item(r['title'], {'title': title,'plot': r['plot']},
                                 img=poster_url, fanart=logo, cm=cm_menu, cm_replace=True, playable=False)
        xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'sports_now':
    channels = ustv.get_sports(quality_type, 'now')
    if channels:
        for c in channels:
            rURL = "plugin://plugin.video.ustvnow.tva/?name=" + c['name'] + "&mode=play"
            name = c["name"];

            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', c['name']+'.png'))
            poster_url = c["poster_url"];
            title = c["title"];
            plot = c["plot"].replace("&amp;", "&").replace('&quot;','"');
            mediatype = c["mediatype"];
            if mediatype != "movie":
                tvshowtitle = title
            if name == 'AE':
                name = 'A&E'
            if name == 'MY9':
                name = 'My9'

            title = '%s (Started at %s on %s)' % (c['title'], c['event_date_time_now'], name)
            cm_refresh = (Addon.get_string(30007), 
                      'XBMC.RunPlugin(%s/?mode=refresh)' % 
                           (Addon.plugin_url))
            cm_rec = (Addon.get_string(30008), 
                      'XBMC.RunPlugin(%s/?mode=record&rec=%s&set=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(c['rec_url']),urllib.quote(c['set_url']),urllib.quote(c['mediatype'])))
            cm_increase = (Addon.get_string(30105) + Addon.qualityName(quality_type + 1), 
                          'XBMC.RunPlugin(%s/?mode=increase)' % 
                               (Addon.plugin_url))
            cm_decrease = (Addon.get_string(30107)  + Addon.qualityName(quality_type - 1), 
                          'XBMC.RunPlugin(%s/?mode=decrease)' % 
                               (Addon.plugin_url))
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_rec]
                
            elif Addon.get_setting('rec_live') == 'false' and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase]

            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase, cm_rec]
                
            elif Addon.get_setting('rec_live') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                cm_menu = [cm_refresh, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                cm_menu = [cm_refresh, cm_increase, cm_decrease]
            elif Addon.get_setting('rec_live') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                cm_menu = [cm_refresh, cm_increase]

            else:
                cm_menu = [cm_refresh]
            Addon.add_video_item(rURL,
            
                                 {'title': title,
                                 'plot': plot,
                                 'mediatype': mediatype,
                                 'tvshowtitle': tvshowtitle},
                                 img=poster_url, fanart=logo, playable=c['playable'], cm=cm_menu, cm_replace=True)
            xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'sports_today':
    channels = ustv.get_sports(quality_type, 'today')
    if channels:
        for c in channels:
            rURL = "plugin://plugin.video.ustvnow.tva/?name=" + c['name'] + "&mode=play"
            name = c["name"];

            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', c['name']+'.png'))
            poster_url = c["poster_url"];
            title = c["title"];
            plot = c["plot"].replace("&amp;", "&").replace('&quot;','"');
            mediatype = c["mediatype"];
            if mediatype != "movie":
                tvshowtitle = title
            if name == 'AE':
                name = 'A&E'
            if name == 'MY9':
                name = 'My9'
            title = '%s (%s on %s)' % (title, c['event_date_time'], name)
            title = title.replace('&amp;','&').replace('&quot;','"')
            cm_refresh = (Addon.get_string(30007), 
                      'XBMC.RunPlugin(%s/?mode=refresh)' % 
                           (Addon.plugin_url))
            cm_rec = (Addon.get_string(30008), 
                      'XBMC.RunPlugin(%s/?mode=record&rec=%s&set=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(c['rec_url']),urllib.quote(c['set_url']),urllib.quote(c['mediatype'])))
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true':
                cm_menu = [cm_refresh, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9']:
                cm_menu = [cm_refresh, cm_rec]
            else:
                cm_menu = [cm_refresh]
            Addon.add_list_item(c['title'],
            
                                 {'title': title,
                                 'plot': plot,
                                 'mediatype': mediatype,
                                 'tvshowtitle': tvshowtitle},
                                 img=poster_url, fanart=logo, playable=False, cm=cm_menu, cm_replace=True)
            xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'sports_later':
    channels = ustv.get_sports(quality_type, 'later')
    if channels:
        for c in channels:
            rURL = "plugin://plugin.video.ustvnow.tva/?name=" + c['name'] + "&mode=play"
            name = c["name"];
            logo = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', c['name']+'.png'))
            poster_url = c["poster_url"];
            title = c["title"];
            plot = c["plot"].replace("&amp;", "&").replace('&quot;','"');
            mediatype = c["mediatype"];
            if mediatype != "movie":
                tvshowtitle = title
            if name == 'AE':
                name = 'A&E'
            if name == 'MY9':
                name = 'My9'
            title = '%s (%s on %s)' % (title, c['event_date_time'], name)
            title = title.replace('&amp;','&').replace('&quot;','"')
            cm_refresh = (Addon.get_string(30007), 
                      'XBMC.RunPlugin(%s/?mode=refresh)' % 
                           (Addon.plugin_url))
            cm_rec = (Addon.get_string(30008), 
                      'XBMC.RunPlugin(%s/?mode=record&rec=%s&set=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(c['rec_url']),urllib.quote(c['set_url']),urllib.quote(c['mediatype'])))
            if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true':
                cm_menu = [cm_refresh, cm_rec]
            elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9']:
                cm_menu = [cm_refresh, cm_rec]
            else:
                cm_menu = [cm_refresh]
            Addon.add_list_item(c['title'],
            
                                 {'title': title,
                                 'plot': plot,
                                 'mediatype': mediatype,
                                 'tvshowtitle': tvshowtitle},
                                 img=poster_url, fanart=logo, playable=False, cm=cm_menu, cm_replace=True)
            xbmcplugin.setContent(Addon.plugin_handle, 'movie')

elif mode == 'guidedata':
    fpath = Addon.plugin_queries['file']               
    Addon.makeXMLTV(ustv.get_guidedata(quality_type),urllib.unquote(fpath))

elif mode == 'tvguide':  
    fpath = os.path.join(write_path, 'xmltv.xml')  
    try:
        name = Addon.plugin_queries['name']
        listings = ustv.get_tvguide(fpath, 'programs', name)
        if listings:
            for l in range(len(listings)):
                cm_refresh = (Addon.get_string(30007), 
                          'XBMC.RunPlugin(%s/?mode=refresh)' % 
                           (Addon.plugin_url))
                cm_rec = (Addon.get_string(30008), 
                          'XBMC.RunPlugin(%s/?mode=record&rec=%s&set=%s&mt=%s)' % 
                           (Addon.plugin_url, urllib.quote(listings[l][9]),urllib.quote(listings[l][10]),urllib.quote(listings[l][8])))
                cm_increase = (Addon.get_string(30105) + Addon.qualityName(quality_type + 1), 
                          'XBMC.RunPlugin(%s/?mode=increase)' % 
                               (Addon.plugin_url))
                cm_decrease = (Addon.get_string(30107)  + Addon.qualityName(quality_type - 1), 
                          'XBMC.RunPlugin(%s/?mode=decrease)' % 
                               (Addon.plugin_url))
                if Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 3:
                    cm_menu = [cm_refresh, cm_decrease, cm_rec]
                elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type <= 2 and quality_type >= 1:
                    cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
                elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'true' and quality_type == 0:
                    cm_menu = [cm_refresh, cm_increase, cm_rec]
                    
                elif Addon.get_setting('rec_live') == 'false' and quality_type == 3:
                    cm_menu = [cm_refresh, cm_decrease]
                elif Addon.get_setting('rec_live') == 'false' and quality_type <= 2 and quality_type >= 1:
                    cm_menu = [cm_refresh, cm_increase, cm_decrease]
                elif Addon.get_setting('rec_live') == 'false' and quality_type == 0:
                    cm_menu = [cm_refresh, cm_increase]
                    
                elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                    cm_menu = [cm_refresh, cm_decrease, cm_rec]
                elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                    cm_menu = [cm_refresh, cm_increase, cm_decrease, cm_rec]
                elif Addon.get_setting('rec_live') == 'true' and Addon.get_setting('dvr') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                    cm_menu = [cm_refresh, cm_increase, cm_rec]
                    
                elif Addon.get_setting('rec_live') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 3:
                    cm_menu = [cm_refresh, cm_decrease]
                elif Addon.get_setting('rec_live') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type <= 2 and quality_type >= 1:
                    cm_menu = [cm_refresh, cm_increase, cm_decrease]
                elif Addon.get_setting('rec_live') == 'false' and name in ['CW','ABC','FOX','PBS','CBS','NBC','My9'] and quality_type == 0:
                    cm_menu = [cm_refresh, cm_increase]
                    
                else:
                    cm_menu = [cm_refresh]
                if listings[l][11] == '0':
                    playable = False
                else:
                    playable = True
                rURL = "plugin://plugin.video.ustvnow.tva/?name="+listings[l][0]+"&mode=play"
                if listings[l][4] == '\n':
                    title = '%s (%s)' % ((listings[l][2]).replace('&amp;','&'), listings[l][7])
                else:
                    title = '%s - %s (%s)' % ((listings[l][2]).replace('&amp;','&'), (listings[l][4]).replace('&amp;','&').replace('&quot;','"'), listings[l][7])
                Addon.add_video_item(rURL,
                                     {'title': title,
                                      'plot': listings[l][3].replace('&amp;','&').replace('&quot;','"')},
                                     img=listings[l][6].replace(' ','%20') , playable=playable, cm=cm_menu, cm_replace=True)

    except:
        if Addon.makeXMLTV(ustv.get_guidedata(quality_type),urllib.unquote(fpath)) == True:
            listings = ustv.get_tvguide(fpath)
            if listings:
                for l in range(len(listings)):
                    url = "plugin://plugin.video.ustvnow.tva/?name="+listings[l]+"&mode=tvguide"
                    Addon.log('adding dir: %s' % (listings[l]))
                    img = xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'logos', listings[l])+'.png')
                    fanart = ''
                    if listings[l] == 'AE':
                        listings[l] = 'A&E'
                    if listings[l] == 'MY9':
                        listings[l] = 'My9'
                    listitem = xbmcgui.ListItem(listings[l], iconImage=img, thumbnailImage=img)
                    if not fanart:
                        fanart = plugin_path + '/fanart.jpg'
                    listitem.setProperty('fanart_image', fanart)
                    xbmcplugin.addDirectoryItem(Addon.plugin_handle, url, listitem, 
                                                isFolder=True, totalItems=len(listings))
                    xbmcplugin.setContent(Addon.plugin_handle, 'files')

elif mode == 'delete':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30005))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        ustv.delete_recording(Addon.plugin_queries['del'])
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        xbmc.executebuiltin('Container.Refresh')

elif mode == 'remove':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30019))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        ustv.remove_recurring(Addon.plugin_queries['remove'])
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        xbmc.executebuiltin('Container.Refresh')

elif mode == 'set':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30023))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        ustv.set_recurring(Addon.plugin_queries['set'])
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        xbmc.executebuiltin('Container.Refresh')

elif mode == 'record':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30009))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        ustv.record_show(Addon.plugin_queries['rec'])
        if Addon.plugin_queries['mt'] != 'movie' and Addon.plugin_queries['mt'] != 'MV' and Addon.get_setting('dvr') == 'true':
            ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30027))
            if ret == 1:
                ustv.set_recurring(Addon.plugin_queries['set'])
                xbmc.executebuiltin("Dialog.Close(busydialog)")
            else:
                xbmc.executebuiltin("Dialog.Close(busydialog)")
    xbmc.executebuiltin('Container.Refresh')

elif mode == 'refresh':
    xbmc.executebuiltin('Container.Refresh')

elif mode == 'increase':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30104))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        Addon.set_setting('quality',str((quality_type + 1)))
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        xbmc.executebuiltin('Container.Refresh')

elif mode == 'decrease':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30106))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        Addon.set_setting('quality',str((quality_type - 1)))
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        xbmc.executebuiltin('Container.Refresh')

elif mode == 'increase_rec':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30108))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        Addon.set_setting('rec_quality',str((rec_quality_type + 1)))
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        xbmc.executebuiltin('Container.Refresh')

elif mode == 'decrease_rec':
    ret = dlg.yesno(Addon.get_string(30000), Addon.get_string(30109))
    if ret == 1:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        Addon.set_setting('rec_quality',str((rec_quality_type - 1)))
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        xbmc.executebuiltin('Container.Refresh')

elif mode == 'settings':

    version = xbmcaddon.Addon(id=addonid).getAddonInfo('version')
    addon_name = xbmcaddon.Addon(id=addonid).getAddonInfo('name')
    Addon.set_setting('version', version)
    Addon.set_setting('addon_name', addon_name)

    token_check = ustv._get_json('gtv/1/live/getcustomerkey', {'token': Addon.get_setting('token')})['username']
    if token_check != Addon.get_setting('email'):
        ustv.token = ustv._login()
    else:
        ustv.token = Addon.get_setting('token')
    try:
        customer_key = ustv._get_json('gtv/1/live/getcustomerkey', {'token': Addon.get_setting('token')})['customerkey']
        
        account_fname = ustv._get_json('gtv/1/live/getaccountsubscription', {'username': Addon.get_setting('email'), 'customerkey': customer_key})['fname']

        account_lname = ustv._get_json('gtv/1/live/getaccountsubscription', {'username': Addon.get_setting('email'), 'customerkey': customer_key})['lname']
        account_name = account_fname + ' ' + account_lname
        Addon.set_setting('account_name',account_name)

        account_plan = ustv._get_json('gtv/1/live/getaccountsubscription', {'username': Addon.get_setting('email'), 'customerkey': customer_key})['subscription']
        Addon.set_setting('account_plan',account_plan)

        account_status = ustv._get_json('gtv/1/live/getaccountsubscription', {'username': Addon.get_setting('email'), 'customerkey': customer_key})['ocaccountstatus']
        Addon.set_setting('account_status',account_status)

        date_opened = ustv._get_json('gtv/1/live/getaccountsubscription', {'username': Addon.get_setting('email'), 'customerkey': customer_key})['dateopened']
        Addon.set_setting('date_opened',date_opened)

        dvr_points = ustv._get_json('gtv/1/live/getaccountsubscription', {'username': Addon.get_setting('email'), 'customerkey': customer_key})['dvrpoints']
        Addon.set_setting('dvr_points',str(dvr_points))
    except:
        pass

    Addon.show_settings()

elif mode=='play':
    name = Addon.plugin_queries['name']
    Addon.log(name)
    channels = []
    channels = ustv.get_link(quality_type)
    if channels:
        Addon.log(str(channels))
        for c in channels:
            if c['name'] == name:
                url = c['url']
                Addon.log(url)
                item = xbmcgui.ListItem(path=url)
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

elif mode=='play_dvr':
    scheduleid = Addon.plugin_queries['scheduleid']
    if rec_quality_type == 0:
        recordings_quality = '350'
    elif rec_quality_type == 1:
        recordings_quality = '650'
    elif rec_quality_type == 2:
        recordings_quality = '950'
    else:
        recordings_quality = '950'
    Addon.log(scheduleid)
    channels = []
    channels = ustv.get_dvr_link(rec_quality_type,recordings_quality)
    if channels:
        Addon.log(str(channels))
        for c in channels:
            if c['scheduleid'] == scheduleid:
                url = c['url']
                Addon.log(url)
                item = xbmcgui.ListItem(path=url)
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

Addon.end_of_directory()
