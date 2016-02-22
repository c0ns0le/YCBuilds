import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import shutil
import urllib2,urllib
import re
import extract
import downloader
import time
from addon.common.addon import Addon
from addon.common.net import Net
 

###THANK YOU TO THE PEOPLE THAT ORIGINALY WROTE SOME OF THIS CODE WITHOUT YOU I STILL PROBABLY WOULDNT HAVE A CLUE WHERE TO START###

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon_id = 'plugin.video.mdwizard'
ADDON = xbmcaddon.Addon(id=addon_id)
AddonTitle="MD Wizard" 
net = Net()
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
VERSION = "1.1.4"
DBPATH = xbmc.translatePath('special://database')
TNPATH = xbmc.translatePath('special://thumbnails');
PATH = "Mucky Ducks Wizard"            
BASEURL = "http://mediaportal4kodi.ml"
H = 'http://'


exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NDQgMTcyKCk6CgkzMignODEgMTZkJywnMWQnLDEsMmYrJzgxLjMxJyxlLCcnKQoJMzIoJzE0ZCAxNDcnLDFjMCsnLzFhYS8xNmEuMWFjPzE2MT0zLjAnLDE5LDJmKydjMC4zMScsZSwnJykKCTMyKCdlYyAxNjQnLDFjMCwyLDJmKydlYy4zMScsZSwnJykKCTMyKCcyNScsMWMwLDMsMmYrJzI1LjMxJyxlLCcnKQoJMzIoJzU4IDdhIDJlJywxYzAsNCwyZisnMmUuMzEnLGUsJycpCiMJMzIoJzEzNCBlOCBlMCcsJ2VjJywxNSwyZisnYTkuMzEnLGUsJycpCgk1NCgnNjAnLCAnYTEnKQoKNDQgMjUoKToKCTFiZCgnMzcgODMnLCcxZCcsMTQsMmYrJzI1LjMxJyxlLCcnKQoJMWJkKCczNyA2YycsJzFkJyw2LDJmKycyNS4zMScsZSwnJykKCTFiZCgnMTcwIGJhJywnMWQnLDEwLDJmKycyNS4zMScsZSwnMTVkIDExNSAxYTMgMTY3JykKIwkzMignMTkyIDE1NCBmMyAxNjggYTgnLCcxZCcsOSwyZisnMS4xOTcnLGUsJzFhZCAxMmIgMTBiJykKCTFiZCgnYWIgMWFmIDFjNCcsJzFkJywxMiwyZisnMjUuMzEnLGUsJycpCgkxYmQoJ2IxIDEwZSAzNyBmMS4xNzgmZWEgMTU1JywnMWQnLDEzLDJmKycyNS4zMScsZSwnMTg1IDE1NyAxOGEgMTFmIDE4YSAxMTcgMWM1IDEyOCAxMDUgZWQgMTRlIDE5ZiAxN2QgMWExIDFiYyAxNDkgODYuZGInKQoJNTQoJzYwJywgJ2ExJykKCgo0NCBkNigpOgoJMWJkKCdhYiA1OCAyZScsMWMwLDgsMmYrJzJlLjMxJyxlLCcnKQoJMWJkKCdjYiAyZScsMWMwKycvNDEvYzguNWEnLDcsMmYrJzJlLjMxJyxlLCcnKQoJMWJkKCdjNCAyZScsMWMwKycvNDEvMTNhLjVhJyw3LDJmKycyZS4zMScsZSwnJykKCTFiZCgnOGUgMmUnLDFjMCsnLzQxL2Q5LjVhJyw3LDJmKycyZS4zMScsZSwnJykKCTFiZCgnYzYgMmUnLDFjMCsnLzQxLzE0Zi41YScsNywyZisnMmUuMzEnLGUsJycpCgkxYmQoJ2M5IDRmIDE5MScsMWMwKycvNDEvMTEwLjVhJyw3LDJmKycyZS4zMScsZSwnJykKCTFiZCgnYzkgNGYgMTkwJywxYzArJy80MS8xMDcuNWEnLDcsMmYrJzJlLjMxJyxlLCcnKQoJMWJkKCczNyAyZScsMWMwLDExLDJmKycyZS4zMScsZSwnJykKCTU0KCc2MCcsICdhMScpCgo0NCBmMCgpOgoJMzIoJzEyOSBlOCBlMCAxOTYgMTVjIDkwIGZmJywxYzArJy80MS85NS8xMTItOTYuMTM4Jyw1LDJmKydhOS4zMScsZSwnJykKCTFiZCgnOTcgMTU5IDFhMCA3YScsMWMwKycvNDEvOTUvZjkuNWEnLDE3LDJmKydhOS4zMScsZSwnJykKCTFiZCgnOTcgMTIxLjFhNSAxMmUgMTZmJywnMTg4Oi8vZWIuMTI1LjFhZS8xMmEuMTljJywxNiwyZisnYTkuMzEnLGUsJycpCgkxYmQoJzE2MCBlOCBmNycsJzFkJywxOCwyZisnYTkuMzEnLGUsJycpCgkKCgo0NCAxM2UoKToKCTQ4ID0gNjkoMWMwKzFjMisxYTkpLjY1KCdcMWI0JywnJykuNjUoJ1wxY2InLCcnKQoJNTcgPSAxMTMuNzMoJzFiPSIoLis/KSIuKz8xOTQ9IiguKz8pIi4rPzE3Nz0iKC4rPykiLis/ZTE9IiguKz8pIi4rPzhhPSIoLis/KSInKS43MSg0OCkKCWMgMWIsMWQsNDIsNDcsMWMgMWI5IDU3OgoJCQkzMigxYiwxZCw1LDQyLDQ3LDFjKQoJNTQoJzYwJywgJ2ExJykKCQoKNDQgODEoKToKCTViOgoJCTQ4ID0gNjkoMWNlKzFjNisxYjMrMWE5KS42NSgnXDFiNCcsJycpLjY1KCdcMWNiJywnJykKCQk1NyA9IDExMy43MygnMWI9IiguKz8pIi4rPzE5ND0iKC4rPykiLis/MTc3PSIoLis/KSIuKz9lMT0iKC4rPykiLis/OGE9IiguKz8pIicpLjcxKDQ4KQoJCWMgMWIsMWQsNDIsNDcsMWMgMWI5IDU3OgoJCQkzMigxYiwxZCw1LDQyLDQ3LDFjKQoJMmM6IDIzCgk1NCgnNjAnLCAnMTBjJykKCgo0NCAxNTAoMWIsMWQsMWMpOgoJMWNhID0gMWEuMWQxKDFkMC4xY2EuMThlKCc2YjovLzU2Lzk2JywnOWYnKSkKCWUzID0gMTMwLmI0KCkKCWUzLjE0MygiMTZjIDE1OCAzOCIsImQ1ICIsJycsICc2MSAxMDgnKQoJYzE9MWQwLjFjYS4xOGUoMWNhLCAxYisnLjEzOCcpCgk1YjoKCSAgIDFkMC42ZShjMSkKCTJjOgoJICAgMjMKCThiLmY2KDFkLCBjMSwgZTMpCgk2OCA9IDFhLjFkMSgxZDAuMWNhLjE4ZSgnNmI6Ly8nLCc1NicpKQoJMTg5LjE2MigyKQoJZTMuMTQ1KDAsIiIsICJkYyAxYTYgNjEgMTA4IikKCTI5ICc9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0nCgkyOSA2OAoJMjkgJz09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PScKCTEyMC4xMmYoYzEsNjgsZTMpCgkxYzEgPSAxMzAuMWNmKCkKCTFjMS42ZCgiNzQgNTAiLCAiNjEgZDggMTQ5IDE1ZiBiNyAxMDQgMTM5IiwiWzJiIDk4XTgwIGI3IGQyIDEzYyA3NCA1MFsvMmJdIikKCgoKNDQgMTgyKDFkKToKCTQ4ID0gNjkoMWQpCgk1Nz0xMTMuNzMoJzwxMDkgMWM3PSIuKz8iPjxhIDlkPSIoLis/KSI+KC4rPyk8L2E+PC8xMDk+JykuNzEoNDgpCgljIDFkLDFiIDFiOSA1NzoKCQkxMGEgPSAnMTY2PTExLjAnCgkJMWIgPSAxYi42NSgnJjE5ZTsnLCcmJykKCQkxYmYgMTBhIDFhNyAxYjkgMWQ6CgkJCTMyKCdbMmIgMTYzXSUxY2NbLzJiXScgJTFiLDFkLDIwLDJmKydjMC4zMScsZSwnJykKCTU5Ljc2KCBiZD0xMzcoIDEzMS5mZFsgMSBdICksIDg4PTU5LjRiICkKCjQ0IDE2ZSgxZCk6Cgk0OCA9IDY5KDFkKQoJNWI6CgkJNTc9MTEzLjczKCcmODU7MWImOGQ7KC4rPykmODU7MWImOGQ7PDEwMyAvPiY4NTsxZCY4ZDs8YSA5ZD0iKC4rPykiIGFhPSI3YyIgOTE9Ijk0Ij4uKz88L2E+Jjg1OzFkJjhkOzwxMDMgLz4mODU7ZjgmOGQ7PGEgOWQ9IiguKz8pIiBhYT0iN2MiIDkxPSI5NCI+Lis/PC9hPiY4NTtmOCY4ZDs8MTAzIC8+Jjg1OzQ3JjhkOzxhIDlkPSIoLis/KSIgYWE9IjdjIiA5MT0iOTQiPi4rPzwvYT4mODU7NDcmOGQ7PDEwMyAvPiY4NTsxYyY4ZDsoLis/KSY4NTsxYyY4ZDsnKS43MSg0OCkKCQljIDFiLDFkLDQyLDQ3LDFjIDFiOSA1NzoKCQkJMzIoMWIsMWQsNSw0Miw0NywxYykKCTJjOiAyMwoJNTQoJzYwJywgJzEwYycpCgk1OS43NiggYmQ9MTM3KCAxMzEuZmRbIDEgXSApLCA4OD01OS40YiApCgoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyMjCWYzIGE4JjkwCSAgIyMjCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgo0NCBlNygpOgoJMWEuNzIoICc5OScgKQoJMWEuNzIoICc5ZScgKQoJMWMxID0gMTMwLjFjZigpCgkxYzEuNmQoIjgyIDM4IiwgJycsJwkJCQkJCQkJIGJhIGM3IDopJywgIgkJCQkJCSAgWzJiIGNhXTgwIGI3IGQyIDEzYyA4MiAzOFsvMmJdIikKCTUxCgkKIzQ0IGI1KDFkKToKIwkyOSAnIyMjJysxOTMrJyAtIDQ2IDEwZi4xNzggIyMjJwojCTFjYSA9IDFhLjFkMSgxZDAuMWNhLjE4ZSgnNmI6Ly8xMDInLCcnKSkKIwk2Nz0xZDAuMWNhLjE4ZSgxY2EsICcxMDEuZGInKQojCTViOgojCQkxZDAuNmUoNjcpCiMJCTFjMSA9IDEzMC4xY2YoKQojCQkyOSAnPT09IDgyIDM4IC0gNDYJJyszOSg2NykrJwk9PT0nCiMJCTFjMS42ZCgxOTMsICIJICAgN2QgMTBkLmRiIDg3IDYxIGJmIGI3IDEwNCAxNDIiKQojCTJjOgojCQkxYzEgPSAxMzAuMWNmKCkKIwkJMWMxLjZkKDE5MywgIgkgICAxMzIgMTgxIGI3IDdkIikKIwk1MQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyMjCWY0IGYzIGE4JjkwICAjIyMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiMjIwkgMzcgZDEJCSMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKNDQgY2YoKToKCTViOgoJCTFiZiAxZDAuMWNhLjI0KDFiOCk9PTNlOgoJCQkxYzEgPSAxMzAuMWNmKCkKCQkJMWJmIDFjMS4yMigiMWJjIDg5IiwgIlsyYiBjYV1bYl0jIyMjIyMjIyMjMTE4IGIxIDEwZSMjIyMjIyMjIyNbL2JdWy8yYl0iLCAiZmEgMTE5IDEyMiAxNzQgOTIgMTM1IDRlIGRmLmRiIiwgIjE5NSAzYyAxN2YgM2MgMzAgMjEgMWI3IDExYz8gZmEgMTlhIDFhMiBiZSAxM2YiKToKCQkJCWMgMWNkLCAxYmIsIDE3YiAxYjkgMWQwLjM0KDFiOCk6CgkJCQkJNWUgPSAwCgkJCQkJNWUgKz0gNDUoMTdiKQoJCQkJCTFiZiA1ZSA+IDA6CQkJCQoJCQkJCQljIGYgMWI5IDE3YjoKCQkJCQkJCTFkMC4xYmUoMWQwLjFjYS4xOGUoMWNkLCBmKSkJCQkgICAKCQljMyA9IDFkMC4xY2EuMThlKDE1MiwiODYuZGIiKQkJCSAgIAoJCTFkMC4xYmUoYzMpCgkJMWMxLjZkKCIxMWUgNzQiLCAiNjEgMTI3IDc0IDIxIDExNiA5MiAxMWQiKQoJMmM6IAoJCTFjMSA9IDEzMC4xY2YoKQoJCTFjMS42ZCgxOTMsICJlNCA2YSA4OSBjNSBlNSA3NCA1MCAxODMgYTYiKQoJNTEKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiMjIwkgMTUzIDM3IGQxCSMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyMjCSAgIDM3IDgzCSAgICMjIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKNDQgZDcoMWQpOgoJMjkgJyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwkgICA0NiAxMDAgODMJCQkgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjJwoJNGMgPSAxZDAuMWNhLjE4ZSgxYS4xZDEoJzZiOi8vNTYnKSwgJzFiMScpCgkxYmYgMWQwLjFjYS4yNCg0Yyk9PTNlOgkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCg0Yyk6CgkJCTVlID0gMAoJCQk1ZSArPSA0NSgxN2IpCgkJCgkJIyAzMyAxN2IgNGUgM2YgMjggMjEgN2YKCQkJMWJmIDVlID4gMDoKCQoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYmYgMWMxLjIyKCIxYmMgNzQgMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQk1YjoKCQkJCQkJCTFkMC4xYmUoMWQwLjFjYS4xOGUoMWNkLCBmKSkKCQkJCQkJMmM6CgkJCQkJCQkyMwoJCQkJCWMgZCAxYjkgMWJiOgoJCQkJCQk1YjoKCQkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkyYzoKCQkJCQkJCTIzCgkJCQkJCQoJCQkzNToKCQkJCTIzCgkxYmYgMWEuOWEoJzEzZC5mYi5jZCcpOgoJCTc4ID0gMWQwLjFjYS4xOGUoJy9iMy8xNDEvZDAvYWQvY2UvYjgvZTYvJywgJ2RhJykKCQkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCg3OCk6CgkJCTVlID0gMAoJCQk1ZSArPSA0NSgxN2IpCgkJCgkJCTFiZiA1ZSA+IDA6CgoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYmYgMWMxLjIyKCIxYmMgY2QgMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSAxYjkgJ2RhJyIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQkxZDAuMWJlKDFkMC4xY2EuMThlKDFjZCwgZikpCgkJCQkJYyBkIDFiOSAxYmI6CgkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkKCQkJMzU6CgkJCQkyMwoJCTc3ID0gMWQwLjFjYS4xOGUoJy9iMy8xNDEvZDAvYWQvY2UvYjgvZTYvJywgJzcwJykKCQkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCg3Nyk6CgkJCTVlID0gMAoJCQk1ZSArPSA0NSgxN2IpCgkJCgkJCTFiZiA1ZSA+IDA6CgoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYmYgMWMxLjIyKCIxYmMgY2QgMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSAxYjkgJzcwJyIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQkxZDAuMWJlKDFkMC4xY2EuMThlKDFjZCwgZikpCgkJCQkJYyBkIDFiOSAxYmI6CgkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkKCQkJMzU6CgkJCQkyMwoJCQkgICMgNTIgMWNhIDIxIDE2OSBmZSAxYjEgMTdiCgkJCQkJCQkgCgoJIyA1MiAxY2EgMjEgMTdhIDFjOCAxODYgMWIxIDE3YgoJNTMgPSAxZDAuMWNhLjE4ZSgxYS4xZDEoJzZiOi8vMmQvMWJhLzM2LjQwLmQ0LzFiMScpLCAnJykKCTFiZiAxZDAuMWNhLjI0KDUzKT09M2U6CQoJCWMgMWNkLCAxYmIsIDE3YiAxYjkgMWQwLjM0KDUzKToKCQkJNWUgPSAwCgkJCTVlICs9IDQ1KDE3YikKCQkKCQkjIDMzIDE3YiA0ZSAzZiAyOCAyMSA3ZgoJCQkxYmYgNWUgPiAwOgoJCgkJCQkxYzEgPSAxMzAuMWNmKCkKCQkJCTFiZiAxYzEuMjIoIjFiYyAxYTggMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQkxZDAuMWJlKDFkMC4xY2EuMThlKDFjZCwgZikpCgkJCQkJYyBkIDFiOSAxYmI6CgkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkKCQkJMzU6CgkJCQkyMwoJCQkJCgkJCQkjIDUyIDFjYSAyMSAxNDAgMWIxIDE3YgoJM2Q9IDFkMC4xY2EuMThlKDFhLjFkMSgnNmI6Ly8yZC8xYmEvMzYuNDAuMTlkLzFiMScpLCAnJykKCTFiZiAxZDAuMWNhLjI0KDNkKT09M2U6CQoJCWMgMWNkLCAxYmIsIDE3YiAxYjkgMWQwLjM0KDNkKToKCQkJNWUgPSAwCgkJCTVlICs9IDQ1KDE3YikKCQkKCQkjIDMzIDE3YiA0ZSAzZiAyOCAyMSA3ZgoJCQkxYmYgNWUgPiAwOgoJCgkJCQkxYzEgPSAxMzAuMWNmKCkKCQkJCTFiZiAxYzEuMjIoIjFiYyAxNDAgMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQkxZDAuMWJlKDFkMC4xY2EuMThlKDFjZCwgZikpCgkJCQkJYyBkIDFiOSAxYmI6CgkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkKCQkJMzU6CgkJCQkyMwoJCQkJCgkJCQkjIDUyIDFjYSAyMSAxNTYgYWYgMWIxIDE3YgoJNDM9IDFkMC4xY2EuMThlKDFhLjFkMSgnNmI6Ly8yZC8xYmEvMzYuNDAuMTI2LzkzJyksICcnKQoJMWJmIDFkMC4xY2EuMjQoNDMpPT0zZToJCgkJYyAxY2QsIDFiYiwgMTdiIDFiOSAxZDAuMzQoNDMpOgoJCQk1ZSA9IDAKCQkJNWUgKz0gNDUoMTdiKQoJCQoJCSMgMzMgMTdiIDRlIDNmIDI4IDIxIDdmCgkJCTFiZiA1ZSA+IDA6CgkKCQkJCTFjMSA9IDEzMC4xY2YoKQoJCQkJMWJmIDFjMS4yMigiMWJjIDE1NiBhZiAyNiAyNyIsIDM5KDVlKSArICIgMTdiIDJhIiwgIjY2IDNjIDMwIDIxIDdmIDNhPyIpOgoJCQkJCgkJCQkJYyBmIDFiOSAxN2I6CgkJCQkJCTFkMC4xYmUoMWQwLjFjYS4xOGUoMWNkLCBmKSkKCQkJCQljIGQgMWI5IDFiYjoKCQkJCQkJMWMzLjFlKDFkMC4xY2EuMThlKDFjZCwgZCkpCgkJCQkJCQoJCQkzNToKCQkJCTIzCgkJCQkKCQkJCQoJCQkJIyA1MiAxY2EgMjEgZDMgOGMgMWIxIDE3YgoJM2IgPSAxZDAuMWNhLjE4ZSgxYS4xZDEoJzZiOi8vMmQvMWJhLzE0OC4xNTEuMTJjLjhiJyksICcnKQoJMWJmIDFkMC4xY2EuMjQoM2IpPT0zZToJCgkJYyAxY2QsIDFiYiwgMTdiIDFiOSAxZDAuMzQoM2IpOgoJCQk1ZSA9IDAKCQkJNWUgKz0gNDUoMTdiKQoJCQoJCSMgMzMgMTdiIDRlIDNmIDI4IDIxIDdmCgkJCTFiZiA1ZSA+IDA6CgkKCQkJCTFjMSA9IDEzMC4xY2YoKQoJCQkJMWJmIDFjMS4yMigiMWJjIGQzIDhjIDI2IDI3IiwgMzkoNWUpICsgIiAxN2IgMmEiLCAiNjYgM2MgMzAgMjEgN2YgM2E/Iik6CgkJCQkKCQkJCQljIGYgMWI5IDE3YjoKCQkJCQkJMWQwLjFiZSgxZDAuMWNhLjE4ZSgxY2QsIGYpKQoJCQkJCWMgZCAxYjkgMWJiOgoJCQkJCQkxYzMuMWUoMWQwLjFjYS4xOGUoMWNkLCBkKSkKCQkJCQkJCgkJCTM1OgoJCQkJMjMKCQkJCQoJCQkJIyA1MiAxY2EgMjEgMTRhIDFiMSAxN2IKCTE3OSA9IDFkMC4xY2EuMThlKDFhLjFkMSgnNmI6Ly8yZC8xYmEvMzYuNDAuMWE0LzEzYicpLCAnJykKCTFiZiAxZDAuMWNhLjI0KDE3OSk9PTNlOgkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCgxNzkpOgoJCQk1ZSA9IDAKCQkJNWUgKz0gNDUoMTdiKQoJCQoJCSMgMzMgMTdiIDRlIDNmIDI4IDIxIDdmCgkJCTFiZiA1ZSA+IDA6CgkKCQkJCTFjMSA9IDEzMC4xY2YoKQoJCQkJMWJmIDFjMS4yMigiMWJjIDE0YSAyNiAyNyIsIDM5KDVlKSArICIgMTdiIDJhIiwgIjY2IDNjIDMwIDIxIDdmIDNhPyIpOgoJCQkJCgkJCQkJYyBmIDFiOSAxN2I6CgkJCQkJCTFkMC4xYmUoMWQwLjFjYS4xOGUoMWNkLCBmKSkKCQkJCQljIGQgMWI5IDFiYjoKCQkJCQkJMWMzLjFlKDFkMC4xY2EuMThlKDFjZCwgZCkpCgkJCQkJCQoJCQkzNToKCQkJCTIzCgoJCQkJIyA1MiAxY2EgMjEgOGYgMWIxIDE3YgoJNmYgPSAxZDAuMWNhLjE4ZSgxYS4xZDEoJzZiOi8vMmQvMWJhLzM2LjQwLjhmLzFiMScpLCAnJykKCTFiZiAxZDAuMWNhLjI0KDE3OSk9PTNlOgkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCg2Zik6CgkJCTVlID0gMAoJCQk1ZSArPSA0NSgxN2IpCgkJCgkJIyAzMyAxN2IgNGUgM2YgMjggMjEgN2YKCQkJMWJmIDVlID4gMDoKCQoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYmYgMWMxLjIyKCIxYmMgZWYgMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQkxZDAuMWJlKDFkMC4xY2EuMThlKDFjZCwgZikpCgkJCQkJYyBkIDFiOSAxYmI6CgkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkKCQkJMzU6CgkJCQkyMwoKCQkJCQkjIDUyIDFjYSAyMSAxMWEgMWIxIDE3YgoJNjMgPSAxZDAuMWNhLjE4ZSgxYS4xZDEoJzZiOi8vMmQvMWJhLzM2LjQwLmVlLzI2JyksICcnKQoJMWJmIDFkMC4xY2EuMjQoMTc5KT09M2U6CQoJCWMgMWNkLCAxYmIsIDE3YiAxYjkgMWQwLjM0KDYzKToKCQkJNWUgPSAwCgkJCTVlICs9IDQ1KDE3YikKCQkKCQkjIDMzIDE3YiA0ZSAzZiAyOCAyMSA3ZgoJCQkxYmYgNWUgPiAwOgoJCgkJCQkxYzEgPSAxMzAuMWNmKCkKCQkJCTFiZiAxYzEuMjIoIjFiYyAxMjMgMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQkxZDAuMWJlKDFkMC4xY2EuMThlKDFjZCwgZikpCgkJCQkJYyBkIDFiOSAxYmI6CgkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkKCQkJMzU6CgkJCQkyMwoKCQkJCQkjIDUyIDFjYSAyMSA3ZSAxNmIgMWIxIDE3YgoJNjQgPSAxZDAuMWNhLjE4ZSgxYS4xZDEoJzZiOi8vMmQvMWJhLzM2LjQwLmYyLzFiMScpLCAnJykKCTFiZiAxZDAuMWNhLjI0KDE3OSk9PTNlOgkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCg2NCk6CgkJCTVlID0gMAoJCQk1ZSArPSA0NSgxN2IpCgkJCgkJIyAzMyAxN2IgNGUgM2YgMjggMjEgN2YKCQkJMWJmIDVlID4gMDoKCQoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYmYgMWMxLjIyKCIxYmMgYWMgMTVhIDI2IDI3IiwgMzkoNWUpICsgIiAxN2IgMmEiLCAiNjYgM2MgMzAgMjEgN2YgM2E/Iik6CgkJCQkKCQkJCQljIGYgMWI5IDE3YjoKCQkJCQkJMWQwLjFiZSgxZDAuMWNhLjE4ZSgxY2QsIGYpKQoJCQkJCWMgZCAxYjkgMWJiOgoJCQkJCQkxYzMuMWUoMWQwLjFjYS4xOGUoMWNkLCBkKSkKCQkJCQkJCgkJCTM1OgoJCQkJMjMKCgkJCQkJIyA1MiAxY2EgMjEgNzUgMWIxIDE3YgoJNDkgPSAxZDAuMWNhLjE4ZSgxYS4xZDEoJzZiOi8vMmQvMWJhLzM2LjQwLjc1LzFiMScpLCAnJykKCTFiZiAxZDAuMWNhLjI0KDE3OSk9PTNlOgkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCg0OSk6CgkJCTVlID0gMAoJCQk1ZSArPSA0NSgxN2IpCgkJCgkJIyAzMyAxN2IgNGUgM2YgMjggMjEgN2YKCQkJMWJmIDVlID4gMDoKCQoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYmYgMWMxLjIyKCIxYmMgYmMgMjYgMjciLCAzOSg1ZSkgKyAiIDE3YiAyYSIsICI2NiAzYyAzMCAyMSA3ZiAzYT8iKToKCQkJCQoJCQkJCWMgZiAxYjkgMTdiOgoJCQkJCQkxZDAuMWJlKDFkMC4xY2EuMThlKDFjZCwgZikpCgkJCQkJYyBkIDFiOSAxYmI6CgkJCQkJCTFjMy4xZSgxZDAuMWNhLjE4ZSgxY2QsIGQpKQoJCQkJCQkKCQkJMzU6CgkJCQkyMwoKCQkJCQkjIDUyIDFjYSAyMSBhNC5jYyAxYjEgMTdiCgk1YyA9IDFkMC4xY2EuMThlKDFhLjFkMSgnNmI6Ly8yZC8xYmEvMzYuNDAuYTQuY2MvMWIxJyksICcnKQoJMWJmIDFkMC4xY2EuMjQoMTc5KT09M2U6CQoJCWMgMWNkLCAxYmIsIDE3YiAxYjkgMWQwLjM0KDVjKToKCQkJNWUgPSAwCgkJCTVlICs9IDQ1KDE3YikKCQkKCQkjIDMzIDE3YiA0ZSAzZiAyOCAyMSA3ZgoJCQkxYmYgNWUgPiAwOgoJCgkJCQkxYzEgPSAxMzAuMWNmKCkKCQkJCTFiZiAxYzEuMjIoIjFiYyBmYyAyNiAyNyIsIDM5KDVlKSArICIgMTdiIDJhIiwgIjY2IDNjIDMwIDIxIDdmIDNhPyIpOgoJCQkJCgkJCQkJYyBmIDFiOSAxN2I6CgkJCQkJCTFkMC4xYmUoMWQwLjFjYS4xOGUoMWNkLCBmKSkKCQkJCQljIGQgMWI5IDFiYjoKCQkJCQkJMWMzLjFlKDFkMC4xY2EuMThlKDFjZCwgZCkpCgkJCQkJCQoJCQkzNToKCQkJCTIzCgoJCQkJCSMgNTIgMWNhIDIxIDdlIDFiMSAxN2IKCTYyID0gMWQwLjFjYS4xOGUoMWEuMWQxKCc2YjovLzJkLzFiYS8zNi40MC43ZS8xNGMnKSwgJycpCgkxYmYgMWQwLjFjYS4yNCgxNzkpPT0zZToJCgkJYyAxY2QsIDFiYiwgMTdiIDFiOSAxZDAuMzQoNjIpOgoJCQk1ZSA9IDAKCQkJNWUgKz0gNDUoMTdiKQoJCQoJCSMgMzMgMTdiIDRlIDNmIDI4IDIxIDdmCgkJCTFiZiA1ZSA+IDA6CgkKCQkJCTFjMSA9IDEzMC4xY2YoKQoJCQkJMWJmIDFjMS4yMigiMWJjIGFjIDI2IDI3IiwgMzkoNWUpICsgIiAxN2IgMmEiLCAiNjYgM2MgMzAgMjEgN2YgM2E/Iik6CgkJCQkKCQkJCQljIGYgMWI5IDE3YjoKCQkJCQkJMWQwLjFiZSgxZDAuMWNhLjE4ZSgxY2QsIGYpKQoJCQkJCWMgZCAxYjkgMWJiOgoJCQkJCQkxYzMuMWUoMWQwLjFjYS4xOGUoMWNkLCBkKSkKCQkJCQkJCgkJCTM1OgoJCQkJMjMKCgkJCSAgICMgNTIgMWNhIDIxIDExMSAxYjEgMTdiCgk0ZCA9IDFkMC4xY2EuMThlKDFhLjFkMSgnNmI6Ly81Ni8xMTEnKSwgJycpCgkxYmYgMWQwLjFjYS4yNCg0ZCk9PTNlOgkKCQljIDFjZCwgMWJiLCAxN2IgMWI5IDFkMC4zNCg0ZCk6CgkJCTVlID0gMAoJCQk1ZSArPSA0NSgxN2IpCgkgICAKCQkjIDMzIDE3YiA0ZSAzZiAyOCAyMSA3ZgoJCQkxYmYgNWUgPiAwOgogICAKCQkJCTFjMSA9IDEzMC4xY2YoKQoJCQkJMWJmIDFjMS4yMigiMWJjIDE4YyAyNyIsIDM5KDVlKSArICIgMTdiIDJhIiwgIjY2IDNjIDMwIDIxIDdmIDNhPyIpOgoJCQkgICAKCQkJCQljIGYgMWI5IDE3YjoKCQkJCQkJMWQwLjFiZSgxZDAuMWNhLjE4ZSgxY2QsIGYpKQoJCQkJCWMgZCAxYjkgMWJiOgoJCQkJCQkxYzMuMWUoMWQwLjFjYS4xOGUoMWNkLCBkKSkKCgkJCQkJIyA1MiAxY2EgMjEgYjIgMWIxIDE3YgoJCgk1ZiA9IDFhLjFkMSgnNmI6Ly9iYi8xYmEvMzYuNDAuYjInKQoJMWMxID0gMTMwLjFjZigpCgk1YjoKCQkxYmYgMWMxLjIyKCIxYmMgMTI0IDI2IDI3IiwgIjY2IDNjIDMwIDIxIDdmIDFiMSIpOgoJCQk3OSA9IDFkMC4xY2EuMThlKDVmLCIxYjEuZGIiKQoJCQkxZDAuMWJlKDc5KQoKCTJjOgoJCTIzCgkKCTFjMSA9IDEzMC4xY2YoKQoJMWMxLjZkKCI4MiAzOCIsICIJCQkJCWY1IDZhIDYxIGJmICAiLCAiCQkJCSAgIFsyYiBjYV04MCBiNyBkMiAxM2MgODIgMzhbLzJiXSIpCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMJIDE1MyAzNyA4MwkgIyMjCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMJIDM3IDZjCSAgIyMjCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgkKNDQgYjAoMWQpOgoJMjkgJyMjIycrMTkzKycgLSA0NiA2YyMjIycKCTVkID0gMWEuMWQxKDFkMC4xY2EuMThlKCc2YjovLzU2Lzk2LzlmJywgJycpKQoJNWI6CQoJCWMgMWNkLCAxYmIsIDE3YiAxYjkgMWQwLjM0KDVkKToKCQkJNWUgPSAwCgkJCTVlICs9IDQ1KDE3YikKCQkJCgkJIyAzMyAxN2IgNGUgM2YgMjggMjEgN2YKCQkJMWJmIDVlID4gMDoKCQoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYmYgMWMxLjIyKCIxYmMgMTFiIDI2IDI3IiwgMzkoNWUpICsgIiAxN2IgMmEiLCAiNjYgM2MgMzAgMjEgN2YgM2E/Iik6CgkJCQkJCQkKCQkJCQljIGYgMWI5IDE3YjoKCQkJCQkJMWQwLjFiZSgxZDAuMWNhLjE4ZSgxY2QsIGYpKQoJCQkJCWMgZCAxYjkgMWJiOgoJCQkJCQkxYzMuMWUoMWQwLjFjYS4xOGUoMWNkLCBkKSkKCQkJCQkxYzEgPSAxMzAuMWNmKCkKCQkJCQkxYzEuNmQoMTkzLCAiCSAgIDZhIDdiIDEyZiAxN2UiKQoJCQkJMzU6CgkJCQkJCTIzCgkJCTM1OgoJCQkJMWMxID0gMTMwLjFjZigpCgkJCQkxYzEuNmQoMTkzLCAiCSAgIDEzMiA3YiAyMSAzNyIpCgkyYzogCgkJMWMxID0gMTMwLjFjZigpCgkJMWMxLjZkKDE5MywgImU0IDZhIDdiIGM1IGU1IDc0IDUwIDE4MyBhNiIpCgk1MQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyMjCWY0IDM3IDZjICAgIyMjCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMJICAgNGEgMmUJICAgIyMjCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIAoJCjQ0IDE3MygxZCwxYik6CgkxY2EgPSAxYS4xZDEoMWQwLjFjYS4xOGUoJzZiOi8vNTYvNTUnLCcnKSkKCTY3PTFkMC4xY2EuMThlKDFjYSwgJzFmLjVhJykKCTFjMSA9IDEzMC4xY2YoKQoJZTk9MWQwLjFjYS4xOGUoMWNhLCAnMWYuNWEuZTknKQoJMWJmIDFkMC4xY2EuMjQoZTkpPT0xNzE6IAoJCTFiZiAxYzEuMjIoIjE4NCAxOGIgYTAiLCAnMTdjIGQyIDEyZCAxOGIgMTA1IGEwPycsJycsICJbYl1bMmIgMTk5XQkgMWIyIDE0NCAxNDYgMWM5IDE4NyAhISFbL2JdWy8yYl0iKToKCQkJMjkgJyMjIycrMTkzKycgLSA1OCAyZSMjIycKCQkJMWNhID0gMWEuMWQxKDFkMC4xY2EuMThlKCc2YjovLzU2LzU1JywnJykpCgkJCTY3PTFkMC4xY2EuMThlKDFjYSwgJzFmLjVhJykKCQkJNWI6CgkJCQkxZDAuNmUoNjcpCgkJCQkyOSAnPT09IDgyIDM4IC0gOWMJJyszOSg2NykrJwk9PT0nCgkJCTJjOgoJCQkJMjMKCQkJNDg9MTM2LmEzKDFkKS5hZQoJCQlhID0gYzIoNjcsIjFiNiIpIAoJCQlhLmUyKDQ4KQoJCQlhLmRkKCkKCQkJMjkgJz09PSA4MiAzOCAtIGI2IDEzMwknKzM5KDY3KSsnCT09PScKCQkJMWMxID0gMTMwLjFjZigpCgkJCTFjMS42ZCgxOTMsICIJICAgMTA2IDE4MCAxNGIgNGEgMmUiKQoJMzU6IAoJCTI5ICcjIyMnKzE5MysnIC0gNTggMmUjIyMnCgkJMWNhID0gMWEuMWQxKDFkMC4xY2EuMThlKCc2YjovLzU2LzU1JywnJykpCgkJNjc9MWQwLjFjYS4xOGUoMWNhLCAnMWYuNWEnKQoJCTViOgoJCQkxZDAuNmUoNjcpCgkJCTI5ICc9PT0gODIgMzggLSA5YwknKzM5KDY3KSsnCT09PScKCQkyYzoKCQkJMjMKCQk0OD0xMzYuYTMoMWQpLmFlCgkJYSA9IGMyKDY3LCIxYjYiKSAKCQlhLmUyKDQ4KQoJCWEuZGQoKQoJCTI5ICc9PT0gODIgMzggLSBiNiAxMzMJJyszOSg2NykrJwk9PT0nCgkJMWMxID0gMTMwLjFjZigpCgkJMWMxLjZkKDE5MywgIgkgICAxMDYgMTgwIDE0YiA0YSAyZSIpCQoJNTEKCjQ0IGEyKDFkLDFiKToKCTI5ICcjIyMnKzE5MysnIC0gYWIgYjkgMmUjIyMnCgkxY2EgPSAxYS4xZDEoMWQwLjFjYS4xOGUoJzZiOi8vNTYvNTUnLCcnKSkKCTY3PTFkMC4xY2EuMThlKDFjYSwgJzFmLjVhJykKCTViOgoJCWE9YzIoNjcpLjE3NSgpCgkJMWJmICcxOGQnIDFiOSBhOgoJCQkxYj0nYzQnCgkJODQgJzE2NScgMWI5IGE6CgkJCTFiPSdjNicKCQk4NCAnYzgnIDFiOSBhOgoJCQkxYj0nY2InCgkJODQgJzExMCcgMWI5IGE6CgkJCTFiPScxYWIgYzkgNGYnCgkJODQgJzEwNycgMWI5IGE6CgkJCTFiPScxOWIgYzkgNGYnCgkJODQgJ2Q5JyAxYjkgYToKCQkJMWI9JzhlJwoJMmM6CgkJMWI9IjFiNSA1OCIKCTFjMSA9IDEzMC4xY2YoKQoJMWMxLjZkKDE5MywiWzJiIDk4XTE0NCAxOGZbLzJiXSAiKyAxYisiWzJiIDk4XSAyZSA3YSAxNWVbLzJiXSIpCgk1MQoKNDQgOWIoMWQpOgoJMjkgJyMjIycrMTkzKycgLSA0NiBiOSAyZSMjIycKCTFjYSA9IDFhLjFkMSgxZDAuMWNhLjE4ZSgnNmI6Ly81Ni81NScsJycpKQoJNjc9MWQwLjFjYS4xOGUoMWNhLCAnMWYuNWEnKQoJNWI6CgkJMWQwLjZlKDY3KQoJCTFjMSA9IDEzMC4xY2YoKQoJCTI5ICc9PT0gODIgMzggLSA0NgknKzM5KDY3KSsnCT09PScKCQkxYzEuNmQoMTkzLCAiCSAgIDdkIDRhIGE1IDg3IikKCTJjOgoJCTFjMSA9IDEzMC4xY2YoKQoJCTFjMS42ZCgxOTMsICIJICAgMTMyIDRhIGE1IGI3IDdkIikKCTUxCgojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojIyMJIGY0IDRhIDJlCSAjIyMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKMWIzID0gJy5hNy4xYjAnCjFhOSA9ICcvNDEuMTk4JwoxYzYgPSAxNWIuZGUoJzE3NicpCjFjMiA9ICcvMTE0Jw==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|4|5|6|7|8|9|a|B|for|d|FANART|f|10|11|12|13|14|15|16|17|18|19|xbmc|name|description|url|rmtree|advancedsettings|20|to|yesno|pass|exists|MAINTENANCE|Cache|Files|option|print|found|COLOR|except|profile|XML|ART|want|png|addDir|Count|walk|else|plugin|DELETE|Wizard|str|them|downloader_cache_path|you|channel4_cache_path|True|give|video|wizard|iconimage|iplayer_cache_path|def|len|DELETING|fanart|link|supercartoons_cache_path|Advanced|SORT_METHOD_VIDEO_TITLE|xbmc_cache_path|temp_cache_path|and|RECOMMENDED|mediaportal|return|Set|wtf_cache_path|setView|userdata|home|match|ADVANCED|xbmcplugin|xml|try|tvonline_cache_path|packages_cache_path|file_count|genesis_cache_path|movies|Please|youtube_cache_path|phoenix_cache_path|ytmusic_cache_path|replace|Do|advance|addonfolder|OPEN_URL|Deleting|special|PACKAGES|ok|remove|m4me_cache_path|LocalAndRental|findall|executebuiltin|compile|KODI|supercartoons|addSortMethod|atv2_cache_b|atv2_cache_a|genesiscache|SETTINGS|Packages|bbc_link|Remove|youtube|delete|Brought|PREMIUM|MD|CACHE|elif|lt|Textures13|Sucessfull|sortMethod|Thumbnails|escription|downloader|Downloader|gt|MIKEY1234|movies4me|ADDONS|target|thumbnail|iplayer_http_cache|_blank|customftv|addons|RENEGADES|yellow|UpdateLocalAddons|getCondVisibility|DELETEADVANCEDXML|REMOVING|href|UpdateAddonRepos|packages|Original|MAIN|CHECKADVANCEDXML|http_GET|tvonline|Settings|facebook|mediaportal4kodi|REPOS|ftv|class|CHECK|YouTube|Library|content|iPlayer|DELETEPACKAGES|ANDROID|genesis|private|DialogProgress|FIXREPOSADDONS|WRITING|To|AppleTV|ADVANCE|REFRESH|masterprofile|SuperCartoons|handle|Be|Reboot|shared|lib|open|text13|0CACHE|please|TUXENS|SUCCESSFUL|muckys|P2P|gold|MUCKYS|cc|ATV2|Caches|DELETETHUMBS|mobile|THUMBS|You|Simple|whatthefurk|Downloading|ADVANCEDXML|DELETECACHE|Disconnect|mikey|Other|db|Extracting|close|getSetting|textures13|GUIDE|anart|write|dp|Error|visit|Video|UPDATEREPO|FTV|bak|THUBMNAIL|renegades|URL|Thumnails|phstreams|Movies4me|CUSTOMFTV|TEXTURE13|spotitube|FIX|End|Finished|download|DATABASE|icon|settings|This|platform|TVonline|argv|Archives|REQUIRED|STANDARD|addons16|database|br|Take|Your|Done|p2p2|Wait|span|nono|Database|INFO|Addona16|ONLY|ADDONS16|p2p1|temp|ftvguide|re|freefix|Refresh|rebuild|Windows|WARNING|feature|phoenix|Package|proceed|library|Restart|Android|extract|ADDONS2|deletes|Phoenix|Genesis|x10host|iplayer|restart|Deletes|INSTALL|addons2|Corrupt|simple|Backed|UPDATE|all|xbmcgui|sys|No|NEW|CUSTOM|folder|net|int|zip|Effect|0cache|Images|By|system|URLFIX|Undone|4oD|var|Affect|create|YOU|update|CANNOT|BUILDS|script|The|ITV|new|kodion|SHARED|Folder|tuxens|WIZARD|module|DBPATH|END|RESORT|FOLDER|BBC|Works|Ducks|FIRST|Music|ADDON|OTHER|Force|SETUP|Power|RESET|board|sleep|white|FIXES|tuxen|topic|Repos|EMPTY|Cydia|index|music|Mucky|BUILD|USERL|DAILY|FORCE|False|INDEX|AXML|your|read|User|mg|DB|itv_cache_path|What|files|Have|Does|done|sure|Adding|File|USER|on|Back|Only|Furk|BACK|http|time|On|Up|Temp|zero|join|HAVE|XML2|XML1|LAST|AddonTitle|rl|Are|AND|jpg|txt|red|Can|2nd|ini|4od|amp|But|RUN|Not|NOT|All|itv|INI|Zip|not|WTF|T|smf|1st|php|Fix|com|MY|ml|cache|AS|N|n|NO|w|do|TNPATH|in|addon_data|dirs|Delete|addDir2|unlink|if|BASEURL|dialog|F|shutil|IP|It|U|id|th|GO|path|r|s|root|H|Dialog|os|translatePath".split("|")))


################################
###        CHECK IP          ###
################################
#Thanks to metalkettle for his work on the original IP checker addon        

def IPCHECK(url='http://www.iplocation.net/',inc=1):
    match=re.compile("<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>").findall(net.http_GET(url).content)
    for ip, region, country, isp in match:
        if inc <2: dialog=xbmcgui.Dialog(); dialog.ok('Check My IP',"[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ip, '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % country, '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % isp)
        inc=inc+1

#################################
###      END CHECK IP         ###
#################################

#################################
###       CUSTOM FTV          ###
#################################

def CUSTOMINI(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("MD Wizard", '                                    Install Latest .ini File'):
        print '###'+AddonTitle+' - CUSTOM FTV INI###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.ftvguide',''))
        advance=os.path.join(path, 'addons2.ini')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== MD Wizard - WRITING NEW    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "                               Done Adding New .ini File")  
    return

def CUSTOMSET(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("MD Wizard", '                               Install Custom Settings'):
        print '###'+AddonTitle+' - CUSTOM FTV SETTINGS###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.ftvguide',''))
        advance=os.path.join(path, 'settings.xml')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== MD Wizard - WRITING NEW    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "                               Done Adding New Settings")  
    return


def DELETEFTVDB():
    try:
        ftvpath = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.ftvguide',''))
        if os.path.exists(ftvpath)==True:
            dialog = xbmcgui.Dialog()
            if dialog.yesno("MD WIzard", "                               Delete FTV Guide Database"):
                ftvsource = os.path.join(ftvpath,"source.db")               
                os.unlink(ftvsource)               
        dialog.ok("MD Wizard", "                                     FTV Database Reset")
    except: 
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "               Error Deleting Database No Database To Delete")
    return

#################################
###      END CUSTOM FTV       ###
#################################
        
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
          
        
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param


def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir2(name,url,mode,iconimage,description,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        

def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    #if addon.get_setting('auto-view') == 'true':

    #    print addon.get_setting(viewType)
    #    if addon.get_setting(viewType) == 'Info':
    #        VT = '515'
    #    elif addon.get_setting(viewType) == 'Wall':
    #        VT = '501'
    #    elif viewType == 'default-view':
    #        VT = addon.get_setting(viewType)

    #    print viewType
    #    print VT
        
    #    xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )
        
        
if mode==None or url==None or len(url)<1:
        INDEX()

elif mode==1:
        PREMIUM()

elif mode==2:
        URLFIX()

elif mode==3:
        MAINTENANCE()

elif mode==4:
        ADVANCEDXML()

elif mode==5:
        WIZARD(name,url,description)

elif mode==6:
        DELETEPACKAGES(url)

elif mode==7:
        AXML(url,name)

elif mode==8:
        CHECKADVANCEDXML(url,name)

elif mode==9:
        FIXREPOSADDONS(url)

elif mode==10:
        UPDATEREPO()

elif mode==11:
        DELETEADVANCEDXML(url)

elif mode==12:
        IPCHECK()

elif mode==13:
        DELETETHUMBS()

elif mode==14:
        DELETECACHE(url)

elif mode==15:
        CUSTOMFTV()

elif mode==16:
        CUSTOMINI(url,name)

elif mode==17:
        CUSTOMSET(url,name)

elif mode==18:
        DELETEFTVDB()

elif mode==19:
        USER(url)

elif mode==20:
        USERL(url)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
