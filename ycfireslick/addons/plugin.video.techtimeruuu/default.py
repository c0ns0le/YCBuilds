#exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("OTIgMjEsOTQsMTQsYywxMTcsMTEsMTA2LDNhLDJmLDRmLDhlCmVmIGUyLjEzZC5iZCA5MiBhMAplZiBjOSA5MiA3MwoKM2UgICAgICAgID0gJzEwNC44NC4xMTUnCjE5ICAgICAgID0gOTQuYTAoZTk9M2UpCmRkICAgICAgICAgICA9IGEwKDNlLCAyZi4xYikKYzcgICAgICAgICAgPSAyMS42NygxMDYuZTguZTYoJ2EzOi8vZWMvYzEvJyArIDNlICwgJ2M3LjEwOCcpKQo5OCAgICAgICAgICAgID0gMjEuNjcoMTA2LmU4LmU2KCdhMzovL2VjL2MxLycgKyAzZSwgJzk4LmUwJykpCmFhICAgICAgICAgPSAnZjQ6Ly85MS43Yi4xMzgvYmIvNzAuYjknCjc0ICAgICAgICA9IDE5LjJjKCdjZicpCjM4ICAgICAgID0gMTkuMmMoJ2MwJykKNjMgICAgICAgPSBkZC5mZC4xNDYoJzYzJywgJycpCmFiICAgICAgICAgPSAxOS4yYygnYzUnKQpiYyA9JzcyOi8vOTEuODEuNGUvMTMvMTNhLzEwNT8xNTk9JwpiYSA9JyZkMD0xNTMmZjE9YWUmMTU1PTEyMSYxMGY9NDEmNjA9ODQmN2Y9NTAnCmYwID0gJzcyOi8vOTEuODEuNGUvMTMvMTNhL2IyP2YxPWFlJmNhPScKZGUgPSAnJjdmPTUwJjEwZj00MCcKCjNmIDcwKCk6CgkxNGE9NTIoYWEpCQoJMTc9M2EuMjUoJ2YzPSIoLis/KSIuKz80OD0iKC4rPykiLis/MTAxPSIoLis/KSInLDNhLjVhKS4yNCgxNGEpCgk0NCBmMyw0OCw2MyAyMyAxNzoKCQkxNiBjMiAnYmUnIDIzIGYzOgoJCQkyMChmMyw0OCwxLDYzLGM3KQoJCTE2ICdiZScgMjMgZjM6CgkJCTE2IDc0ID09ICc5ZSc6CgkJCQkxNiAzOCA9PSAnJzoKCQkJCSAgICA3OCA9IDE0LmJmKCkKCQkJCSAgICBiNCA9IDc4LmQ4KCdkNyBhNScsICcxNDggMTM5IDEyMiAxMTEgMTJmIGNmIDY0JywnJywnYjggMTE4IGEgYzAgMTExIGZmIGRhIDExMicsJ2I1JywnMTI5IDE0YycpCgkJCQkgICAgMTYgYjQgPT0gMToKCQkJCQk1NiA9IDIxLjlmKCcnLCAnMTEzIDk5JykKCQkJCQk1Ni5hZCgpCgkJCQkJMTYgKDU2LjdhKCkpOgoJCQkJCSAgICA4YSA9IDU2LmE3KCkKCQkJCQkgICAgMTkuZDkoJ2MwJyw4YSkgICAgICAKCQkJCQkyMChmMyw0OCwxLDYzLGM3KQoJCQkxNiA3NCA9PSAnOWUnOgoJCQkJMTYgMzggPD4gJyc6CgkJCQkJMjAoZjMsNDgsMSw2MyxjNykKCTNjKCcxNTIgMTM3IGY5IDEzNicsJzQ4JywyLCdmNDovLzkxLjdiLjEzOC9iYi8xMDIvZmUuMTA4JyxjNykKCTIxLmYoJzE1NC4yYSgxNDEpJykKICAgICAgCjNmIDc3KDQ4KToKCTE2ICc3MCcgMjMgNDg6CgkJOWMoNDgpCgkxNiAnYmUnIDIzIDQ4OgoJCTE2IDM4IDw+ICcnOgoJCQk3OCA9IDE0LmJmKCkKCQkJYjQgPSA3OC5kOCgnZDcgYTUnLCAnYjggMTFmIDEwYSBjMCAxNGIgMTE4JywnMTExIGYyJywnJywnYjUnLCcxMmMgMTRmIDEwYSAxMjMnKQoJCQkxNiBiNCA9PSAxOgoJCQkgICA1ODogICAgIAoJCQkgICAgICA1NiA9IDIxLjlmKCcnLCAnMTEzIDk5JykKCQkJICAgICAgNTYuYWQoKQoJCQkgICAgICAxNiAoNTYuN2EoKSk6CgkJCQkgICAgOGEgPSA1Ni5hNygpCgkJCSAgICAgIDE2IDhhID09IDM4OgoJCQkJMjYgPSA2Mig0OCkKCQkJCTQ0IDY4IDIzIDI2OgoJCQkJICAgICAgIDNjKDY4WyJmMyJdLDY4WyI0OCJdLDMsNjMsYzcpCgkJCSAgIDFlOjQ1CgkxNiAnYjYnIDIzIDQ4OgoJCTI2ID0gNjIoNDgpCgkJMTBlID0gNjUoMjYpCgkJNDQgNjggMjMgMjY6CgkJCTdjKDY4WyJmMyJdLDY4WyI0OCJdLDMsNjMsMTBlLDE4PTZmKQoJCWE5KCdiNicsICcxMjcnKQoJCTE2ICc3MCcgMjMgNDg6CgkJCTIxLmYoJzE1NC4yYSg1MCknKQoJNTcgJ2JlJyBjMiAyMyA0ODoKCQkxMjggPSA0OAoJCTI2ID0gNjIoNDgpCgkJNDQgNjggMjMgMjY6CgkJCTE2ICcxMy40ZS83ZD8zMz0nIDIzIDY4WyI0OCJdOgoJCQkJMjAoNjhbImYzIl0sNjhbIjQ4Il0sMyw2MyxjNykKCQkJNTcgJzEzLjRlLzU0PzVmPScgMjMgNjhbIjQ4Il06CgkJCQkyMCg2OFsiZjMiXSw2OFsiNDgiXSwzLDYzLGM3KQoJCQk1NToKCQkJCTE2ICdiOScgMjMgNjhbIjQ4Il06CgkJCQkJMjAoNjhbImYzIl0sNjhbIjQ4Il0sMyw2MyxjNykKCQkJCTU1OgoJCQkJCTNjKDY4WyJmMyJdLDY4WyI0OCJdLDMsNjMsYzcpCgkJMjEuZignMTU0LjJhKDUwKScpCgkKM2YgOWMoNDgpOgoJMTRhPTUyKDQ4KQkKCTE3PTNhLjI1KCdmMz0iKC4rPykiLis/NDg9IiguKz8pIi4rPzEwMT0iKC4rPykiJywzYS41YSkuMjQoMTRhKQoJNDQgZjMsNDgsNjMgMjMgMTc6CgkJMTYgJzEzLjRlLzU0PzVmPScgMjMgNDg6CgkJCTIwKGYzLDQ4LDMsNjMsYzcpCgkJNTcgJzEzLjRlLzdkPzMzPScgMjMgNDg6CgkJCTIwKGYzLDQ4LDMsNjMsYzcpCgkJNTU6CgkJCTIwKGYzLDQ4LDEsNjMsYzcpCgkyMS5mKCcxNTQuMmEoNTApJykKCjNmIDYyKDQ4KToKCTE0YT01Mig0OCkJCgk2MT0zYS4yNSgnXiMuKz86LT9bMC05XSooLio/KSwoLio/KVxmYyguKj8pJCcsM2EuMTU4KzNhLjE0ZCszYS5mYiszYS4xNTEpLjI0KDE0YSkKCTEwYiA9IFtdCgk0NCAxNWEsIGYzLCA0OCAyMyA2MToKCQkzNiA9IHsiMTVhIjogMTVhLCAiZjMiOiBmMywgIjQ4IjogNDh9CgkJMTBiLjhmKDM2KQoJNWYgPSBbXQoJNDQgNjggMjMgMTBiOgoJCTM2ID0geyJmMyI6IDY4WyJmMyJdLCAiNDgiOiA2OFsiNDgiXX0KCQk2MT0zYS4yNSgnICguKz8pPSIoLis/KSInLDNhLjE1OCszYS4xNGQrM2EuZmIrM2EuMTUxKS4yNCg2OFsiMTVhIl0pCgkJNDQgZDEsIGQ2IDIzIDYxOgoJCQkzNltkMS5jYygpLjExZSgpLjQoJy0nLCAnMTVjJyldID0gZDYuY2MoKQoJCTVmLjhmKDM2KQoJMWYgNWYKCSAgICAgCjNmIDk3KDQ4LGYzKToKCSAgICAyOSA0OAoJICAgIDE2ICdiOScgMjMgNDg6CgkJICAgIDI5ICcxMjQgYjknCgkJICAgIDc3KDQ4KQoJICAgIDU1OgoJCSAgICAxNiAnMTMuNGUvN2Q/MzM9JyAyMyA0ODoKCQkJMjkgJ2FjIDEwNycKCQkJM2QgPSA0OC44MCgnMzM9JylbMV0KCQkJODIgPSBiYyArIDNkICsgYmEKCQkJMzcgPSAxMS40YSg4MikKCQkJMzcuMmUoJzg5LTZjJywgJzRjLzUuMCAoMTU3OyBmYjsgMTU3IGNlIDUuMTsgZGMtY2I7IGQ1OjEuOS4wLjMpIDZkLzJkIDRiLzMuMC4zJykKCQkJNyA9IDExLjQ5KDM3KQoJCQkxNGE9Ny44NSgpCgkJCTcuNmIoKQoJCQkxNGEgPSAxNGEuNCgnXDE0NycsJycpLjQoJ1xmYycsJycpLjQoJyAgJywnJykKCQkJMTc9M2EuMjUoJyJhMiI6ICIoLis/KSIuKz8iODciOiAiKC4rPykiJywzYS41YSkuMjQoMTRhKQoJCQkyOSAxNwoJCQk0NCA5ZCxmMyAyMyAxNzoKCQkJCTQ4ID0gJzcyOi8vOTEuMTMuNGUvZGI/MTRlPScrOWQKCQkJCTNjKGYzLDQ4LDMsNjMsYzcpCgkJICAgIDU3ICcxMy40ZS81ND81Zj0nIDIzIDQ4OgoJCQkyOSAnYWMgZjYnCgkJCTNkID0gNDguODAoJzU0PzVmPScpWzFdCgkJCTgyID0gZjAgKyAzZCArIGRlCgkJCTM3ID0gMTEuNGEoODIpCgkJCTM3LjJlKCc4OS02YycsICc0Yy81LjAgKDE1NzsgZmI7IDE1NyBjZSA1LjE7IGRjLWNiOyBkNToxLjkuMC4zKSA2ZC8yZCA0Yi8zLjAuMycpCgkJCTcgPSAxMS40OSgzNykKCQkJMTRhPTcuODUoKQoJCQk3LjZiKCkKCQkJMTRhID0gMTRhLjQoJ1wxNDcnLCcnKS40KCdcZmMnLCcnKS40KCcgICcsJycpCgkJCTE3PTNhLjI1KCciODciOiAiKC4rPykiLis/ImEyIjogIiguKz8pIicsM2EuNWEpLjI0KDE0YSkKCQkJNDQgZjMsOWQgMjMgMTc6CgkJCQk0OCA9ICc3MjovLzkxLjEzLjRlL2RiPzE0ZT0nKzlkCgkJCQkzYyhmMyw0OCwzLDYzLGM3KQoJCSAgICA1NyAnYzYnIDIzIDQ4OgoJCQkgICAgMjkgJ2M4JwoJCQkgICAgNDggPSA0OC40KCc4NCcsJzExYy84NCcpCgkJCSAgICAzNyA9IDExLjRhKDQ4KQoJCQkgICAgMzcuMmUoJzg5LTZjJywgJzRjLzUuMCAoMTU3OyBmYjsgMTU3IGNlIDUuMTsgZGMtY2I7IGQ1OjEuOS4wLjMpIDZkLzJkIDRiLzMuMC4zJykKCQkJICAgIDcgPSAxMS40OSgzNykKCQkJICAgIDE0YT03Ljg1KCkKCQkJICAgIDcuNmIoKQoJCQkgICAgMTc9M2EuMjUoJzE0OSIsIjQ4Ilw6IiguKz8pIicpLjI0KDE0YSlbMF0KCQkJICAgIDFhPTE3LjQoJ1wvJywnLycpCgkJCSAgICA0Mz01MwoJCQkgICAgMTNiPTE0LjMxKGYzLCAyYj02MyxlPTYzKTsgMTNiLjNiKCA2MD0iNWQiLCAyMj17ICI3MSI6IGYzIH0gKQoJCQkgICAgNDM9Yy4xM2UoNDc9NjYoMmYuMWJbMV0pLDQ4PTFhLDM0PTEzYikKCQkJICAgIDU4OgoJCQkJIDIxLmI3ICgpLmY1KDFhLCAxM2IsIDZmKQoJCQkJIDFmIDQzCgkJCSAgICAxZToKCQkJCSA0NQoJCSAgICA1NToKCQkJMjkgJzExNiAxMzInCgkJCTE2IDRmLjViKDQ4KS5lMSgpOgoJCQkJMWEgPSA0Zi41Yig0OCkuMTQ0KCkKCQkJNTU6IDFhPTQ4IAoJCQk0Mz01MwoJCQkxM2I9MTQuMzEoZjMsIDJiPTYzLGU9NjMpOyAxM2IuM2IoIDYwPSI1ZCIsIDIyPXsgIjcxIjogZjMgfSApCgkJCTQzPWMuMTNlKDQ3PTY2KDJmLjFiWzFdKSw0OD0xYSwzND0xM2IpCgkJCTU4OgoJCQkgICAgIDIxLmI3ICgpLmY1KDFhLCAxM2IsIDZmKQoJCQkgICAgIDFmIDQzCgkJCTFlOgoJCQkgICAgIDQ1CgkgICAgCjNmIGE4KCk6Cgk3NiA9ICcnCgllNSA9ICc3MjovLzEwYy4xMTQuNGUvMTBkLzE1MC80ZC04Yi8xMzA/OTYnCgkzNyA9IDExLjRhKGU1KQoJMzcuMmUoJzg5LTZjJywgJzRjLzUuMCAoMTU3OyBmYjsgMTU3IGNlIDUuMTsgZGMtY2I7IGQ1OjEuOS4wLjMpIDZkLzJkIDRiLzMuMC4zJykKCTcgPSAxMS40OSgzNykKCTE0YT03Ljg1KCkKCTcuNmIoKQoJMTRhID0gMTRhLjQoJy9mYycsJycpCgkxNGEgPSAxNGEuOTAoJ2RmLTgnKS4xMDMoJ2RmLTgnKS40KCcmIzM5OycsJ1wnJykuNCgnJiMxMDsnLCcgLSAnKS40KCcmIzExOTsnLCcnKQoJMTc9M2EuMjUoIjw4Nz4oLis/KTwvODc+Lis/PGE0PiguKz8pPC9hND4iLDNhLjVhKS4yNCgxNGEpWzE6XQoJNDQgMzAsIDk1IDIzIDE3OgoJICAgIDU4OgoJCQkgICAgMzAgPSAzMC45MCgnMTFiJywgJ2IzJykKCSAgICAxZToKCQkJICAgIDMwID0gMzAuOTAoJ2RmLTgnLCdiMycpCgkgICAgOTUgPSA5NVs6LTE1XQoJICAgIDMwID0gMzAuNCgnJjE0MzsnLCcnKQoJICAgIDk1ID0gJ1s2ZSBmN11bYl0nKzk1KydbL2JdWy82ZV0nCgkgICAgNzYgPSA3Nis5NSsnXGZjJyszMCsnXGZjJysnXGZjJwoJOWIoJ1s2ZSBmN11bYl1AZmFbL2JdWy82ZV0nLCA3NikKCjNmIDliKGE2LCA3Nik6CiAgICBlOSA9IDEyNQogICAgMjEuZignYWYoJWQpJyAlIGU5KQogICAgMjEuZDIoMTAwKQogICAgZTMgPSAxNC4xMDkoZTkpCiAgICBhMSA9IDUwCiAgICAxMWQgKGExID4gMCk6Cgk1ODoKCSAgICAyMS5kMigxMCkKCSAgICBhMSAtPSAxCgkgICAgZTMuN2UoMSkuZWQoYTYpCgkgICAgZTMuN2UoNSkuZjgoNzYpCgkgICAgMWYKCTFlOgoJICAgIDQ1CgkJCQkgICAgIAozZiA1Mig0OCk6Cgk0OCArPSAnPyVkPSVkJyAlICg4ZS5iMSgxLCBkNCksIDhlLmIxKDEsIGQ0KSkKCTM3ID0gMTEuNGEoNDgpCgkzNy4yZSgnODktNmMnLCAnNGMvNS4wICgxNTc7IGZiOyAxNTcgY2UgNS4xOyBkYy1jYjsgZDU6MS45LjAuMykgNmQvMmQgNGIvMy4wLjMnKQoJNyA9IDExLjQ5KDM3KQoJMTRhPTcuODUoKQoJMTRhID0gMTRhLjQoJ1wxNDcnLCcnKS40KCdcMTViJywnJykuNCgnJjEzYzsnLCcnKS40KCdcJycsJycpCgk3LjZiKCkKCTFmIDE0YQoKM2YgODgoKToKCTg2PVtdCgk3OT0yZi4xYlsyXQoJMTYgNjUoNzkpPj0yOgoJCTE1YT0yZi4xYlsyXQoJCTZhPTE1YS40KCc/JywnJykKCQkxNiAoMTVhWzY1KDE1YSktMV09PScvJyk6CgkJCTE1YT0xNWFbMDo2NSgxNWEpLTJdCgkJNDI9NmEuODAoJyYnKQoJCTg2PXt9CgkJNDQgMTU2IDIzIDExYSg2NSg0MikpOgoJCQkyOD17fQoJCQkyOD00MlsxNTZdLjgwKCc9JykKCQkJMTYgKDY1KDI4KSk9PTI6CgkJCQk4NlsyOFswXV09MjhbMV0KCQkJICAgICAgIAoJMWYgODYKCSAgICAgICAKM2YgMjAoZjMsNDgsMTIsNjMsYzcsMTQ1PScnKToKCWVlPTJmLjFiWzBdKyI/NDg9IisxMTcuNig0OCkrIiYxMj0iKzU5KDEyKSsiJmYzPSIrMTE3LjYoZjMpKyImNjM9IisxMTcuNig2MykrIiYxNDU9IisxMTcuNigxNDUpCgk0Mz01MwoJMTNiPTE0LjMxKGYzLCAyYj0iNjkuZTAiLCBlPTYzKQoJMTNiLjNiKCA2MD0iNWQiLCAyMj17ICI3MSI6IGYzLCAnZWInOiAxNDUgfSApCgkxM2IuMjcoJzFjJywgYzcpCgk0Mz1jLjEzZSg0Nz02NigyZi4xYlsxXSksNDg9ZWUsMzQ9MTNiLDE4PTUzKQoJMWYgNDMKCjNmIDNjKGYzLDQ4LDEyLDYzLGM3LDE0NT0nJyk6CgllZT0yZi4xYlswXSsiPzQ4PSIrMTE3LjYoNDgpKyImMTI9Iis1OSgxMikrIiZmMz0iKzExNy42KGYzKSsiJjYzPSIrMTE3LjYoNjMpKyImMTQ1PSIrMTE3LjYoMTQ1KQoJNDM9NTMKCTEzYj0xNC4zMShmMywgMmI9IjY5LmUwIiwgZT02MykKCTEzYi4zYiggNjA9IjVkIiwgMjI9eyAiNzEiOiBmMywgJ2ViJzogMTQ1IH0gKQoJMTNiLjI3KCcxYycsIGM3KQoJNDM9Yy4xM2UoNDc9NjYoMmYuMWJbMV0pLDQ4PWVlLDM0PTEzYiwxOD02ZikKCTFmIDQzCgozZiA3YyhmMyw0OCwxMiw2Myw5MywxOD02Zik6CgkxNiBhYj09JzllJzoKCSAgMTYgYzIgJzZlJyAyMyBmMzoKCSAgICA0Nj1mMy44ZCgnKCcpCgkgICAgNWM9IiIKCSAgICAxZD0iIgoJICAgIDE2IDY1KDQ2KT4wOgoJCTVjPTQ2WzBdCgkJMWQ9NDZbMl0uOGQoJyknKQoJICAgIDE2IDY1KDFkKT4wOgoJCTFkPTFkWzBdCgkgICAgMTMzID0gNzMuZTcoKQoJICAgIDgzID0gMTMzLmVhKCcxMjYnLCBmMz01YyAsMTNmPTFkKQoJICAgIGVlPTJmLjFiWzBdKyI/NDg9IisxMTcuNig0OCkrIiY1MT0iKzU5KDUxKSsiJjEyPSIrNTkoMTIpKyImZjM9IisxMTcuNihmMykKCSAgICA0Mz01MwoJICAgIDEzYj0xNC4zMShmMywgMmI9ODNbJ2U0J10sIGU9NjMpCgkgICAgMTNiLjNiKCA2MD0iNWQiLCAyMj0gODMgKQoJICAgIDMyID0gW10KCSAgICAzMi44ZigoJzEyMCBjNCcsICcxNDAuMTEwKDEzNCknKSkKCSAgICAxM2IuOGMoMzIsIGMzPTUzKQoJICAgIDE2IGMyIDgzWyc3NSddID09ICcnOiAxM2IuMjcoJzFjJywgODNbJzc1J10pCgkgICAgNTU6IDEzYi4yNygnMWMnLCBjNykKCSAgICA0Mz1jLjEzZSg0Nz02NigyZi4xYlsxXSksNDg9ZWUsMzQ9MTNiLDE4PTE4LGQzPTkzKQoJICAgIDFmIDQzCgk1NToKCSAgICBlZT0yZi4xYlswXSsiPzQ4PSIrMTE3LjYoNDgpKyImNTE9Iis1OSg1MSkrIiYxMj0iKzU5KDEyKSsiJmYzPSIrMTE3LjYoZjMpCgkgICAgNDM9NTMKCSAgICAxM2I9MTQuMzEoZjMsIDJiPTk4LCBlPTk4KQoJICAgIDEzYi4zYiggNjA9IjVkIiwgMjI9eyAiNzEiOiBmMyB9ICkKCSAgICAxM2IuMjcoJzFjJywgYzcpCgkgICAgNDM9Yy4xM2UoNDc9NjYoMmYuMWJbMV0pLDQ4PWVlLDM0PTEzYiwxOD0xOCkKCSAgICAxZiA0MwoJCjNmIGE5KDY0LCA5YSk6CiAgICAxNiA2NDoKCWMuY2QoNjYoMmYuMWJbMV0pLCA2NCkKICAgIDE2IDE5LjJjKCcxMzUtMTJhJyk9PSc5ZSc6CgkyMS5mKCIxNTQuMmEoJTE1MCkiICUgMTkuMmMoOWEpICkKCjE1YT04OCgpOyA0OD01ZTsgZjM9NWU7IDEyPTVlOyA1MT01ZTsgNjM9NWUKNTg6IDUxPTExNy4zNSgxNWFbIjUxIl0pCjFlOiA0NQo1ODogNDg9MTE3LjM1KDE1YVsiNDgiXSkKMWU6IDQ1CjU4OiBmMz0xMTcuMzUoMTVhWyJmMyJdKQoxZTogNDUKNTg6IDEyPTY2KDE1YVsiMTIiXSkKMWU6IDQ1CjU4OiA2Mz0xMTcuMzUoMTVhWyI2MyJdKQoxZTogNDUKIAojMjkgIjEzMTogIis1OSg1MSk7IDI5ICIxMmU6ICIrNTkoMTIpOyAyOSAiMTQyOiAiKzU5KDQ4KTsgMjkgIjEyZDogIis1OShmMykKIAoxNiAxMj09NWUgMTJiIDQ4PT01ZSAxMmIgNjUoNDgpPDE6IDcwKCkKNTcgMTI9PTE6NzcoNDgpCjU3IDEyPT0yOmE4KCkKNTcgMTI9PTM6OTcoNDgsZjMpCgpjLmIwKDY2KDJmLjFiWzFdKSk=")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|replace|5|quote_plus|response|8|9|a|B|xbmcplugin|d|thumbnailImage|executebuiltin|10|urllib2|mode|youtube|xbmcgui|15|if|match|isFolder|selfAddon|streamurl|argv|fanart_image|simpleyear|except|return|addDir|xbmc|infoLabels|in|findall|compile|channels|setProperty|splitparams|print|SetViewMode|iconImage|getSetting|2008092417|add_header|sys|status|ListItem|contextMenuItems|search_query|listitem|unquote_plus|item_data|req|adultpass|39|re|setInfo|addLink|searchterm|addon_id|def|AIzaSyBAdxZCHbeJwnQ7dDZQJNfcaF46MdqJ24E|AIzaSyA7v1QOHz8Q4my5J8uGSpr0zRrntRjnMmk|pairsofparams|ok|for|pass|splitName|handle|url|urlopen|Request|Firefox|Mozilla|AKfycbyBcUa5TlEQudk6Y_0o0ZubnmhGL_|com|urlresolver|50|site|open_url|True|playlist|else|keyb|elif|try|str|DOTALL|HostedMediaFile|simplename|Video|None|list|type|matches|GetList|iconimage|content|len|int|translatePath|channel|DefaultFolder|cleanedparams|close|Agent|Gecko|COLOR|False|Index|Title|https|metahandlers|adultopt|backdrop_url|text|GetChans|dialog|paramstring|isConfirmed|metalkettle|addLinkMeta|results|getControl|maxResults|split|googleapis|ytapi|meta|video|read|param|title|get_params|User|passw|b7Up8kQt11xgVwz3ErTo|addContextMenuItems|partition|random|append|decode|www|import|itemcount|xbmcaddon|dte|588677963413065728|PLAYLINK|icon|Password|viewType|showText|CatIndex|ytid|true|Keyboard|Addon|retry|videoId|special|pubDate|Content|heading|getText|TWITTER|setView|baseurl|metaset|Youtube|doModal|snippet|ActivateWindow|endOfDirectory|randint|playlistItems|ignore|ret|Cancel|movies|Player|Please|txt|ytapi2|UKTurk|ytapi1|common_addon|XXX|Dialog|password|addons|not|replaceItems|Information|enable_meta|dailymotion|fanart|DailyMotion|metahandler|playlistId|GB|strip|setContent|NT|adult|regionCode|field|sleep|totalItems|10000|rv|value|Adult|yesno|setSetting|accidental|watch|en|addon|ytpl2|utf|png|valid_url|resources|win|cover_url|twit|join|MetaData|path|id|get_meta|plot|home|setLabel|u|from|ytpl|part|continue|name|http|play|Playlist|blue|setText|Twitter|uk_turk|U|n|queries|twitter|prevent|100|img|thumbs|encode|plugin|search|os|Search|jpg|Window|the|li|script|macros|cnt|key|Action|to|access|Set|google|ukturk|Direct|urllib|set|x2026|range|ascii|embed|while|lower|enter|Movie|en_US|opted|money|Found|10147|movie|MAIN|burl|Lets|view|or|Show|Name|Mode|show|exec|Site|Link|mg|Info|auto|Feed|Turk|co|have|v3|liz|nbsp|libs|addDirectoryItem|year|XBMC|500|URL|amp|resolve|description|get|r|You|mp4|link|you|Go|M|v|me|s|S|UK|US|Container|hl|i|Windows|I|q|params|t|_".split("|")))

import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,urlresolver,random
from resources.libs.common_addon import Addon
from metahandler import metahandlers

addon_id        = 'plugin.video.techtimeruuu'
selfAddon       = xbmcaddon.Addon(id=addon_id)
addon           = Addon(addon_id, sys.argv)
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
baseurl         = 'http://spartanpixel.net/videos.txt'
adultopt        = selfAddon.getSetting('adult')
adultpass       = selfAddon.getSetting('password')
iconimage       = addon.queries.get('iconimage', '')
metaset         = selfAddon.getSetting('enable_meta')
ytapi1 ='https://www.googleapis.com/youtube/v3/search?q='
ytapi2 ='&regionCode=US&part=snippet&hl=en_US&key=AIzaSyA7v1QOHz8Q4my5J8uGSpr0zRrntRjnMmk&type=video&maxResults=50'
ytpl = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
ytpl2 = '&maxResults=50&key=AIzaSyBAdxZCHbeJwnQ7dDZQJNfcaF46MdqJ24E'

def Index():
    link=open_url(baseurl)  
    match=re.compile('name="(.+?)".+?url="(.+?)".+?img="(.+?)"',re.DOTALL).findall(link)
    for name,url,iconimage in match:
        if not 'XXX' in name:
            addDir(name,url,1,iconimage,fanart)
        if 'XXX' in name:
            if adultopt == 'true':
                if adultpass == '':
                    dialog = xbmcgui.Dialog()
                    ret = dialog.yesno('Adult Content', 'You have opted to show adult content','','Please set a password to prevent accidental access','Cancel','Lets Go')
                    if ret == 1:
						keyb = xbmc.Keyboard('', 'Set Password')
						keyb.doModal()
                    if (keyb.isConfirmed()):
                        passw = keyb.getText()
                        selfAddon.setSetting('password',passw)      
                    addDir(name,url,1,iconimage,fanart)
            if adultopt == 'true':
                if adultpass <> '':
                    addDir(name,url,1,iconimage,fanart)
    #addLink('UK Turk Twitter Feed','url',2,'http://www.metalkettle.co/UKTurk/thumbs/twitter.jpg',fanart)
    xbmc.executebuiltin('Container.SetViewMode(500)')

def GetChans(url):
    if 'Index' in url:
        CatIndex(url)
    #if 'XXX' in url:
    #    if adultpass <> '':
    #        dialog = xbmcgui.Dialog()
    #        ret = dialog.yesno('Adult Content', 'Please enter the password you set','to continue','','Cancel','Show me the money')
    #        if ret == 1:
    #           try:     
    #              keyb = xbmc.Keyboard('', 'Set Password')
    #              keyb.doModal()
    #              if (keyb.isConfirmed()):
    #                passw = keyb.getText()
    #              if passw == adultpass:
	#				channels = GetList(url)
	#				for channel in channels:
	#					addLink(channel["name"],channel["url"],3,iconimage,fanart)
    #          except:pass
    if 'movies' in url:
        channels = GetList(url)
        cnt = len(channels)
        for channel in channels:
            addLinkMeta(channel["name"],channel["url"],3,iconimage,cnt,isFolder=False)
        setView('movies', 'MAIN')
        if 'Index' in url:
            xbmc.executebuiltin('Container.SetViewMode(50)')
    elif 'XXX' not in url:
        burl = url
        channels = GetList(url)
        for channel in channels:
            if 'youtube.com/results?search_query=' in channel["url"]:
                addDir(channel["name"],channel["url"],3,iconimage,fanart)
            elif 'youtube.com/playlist?list=' in channel["url"]:
                addDir(channel["name"],channel["url"],3,iconimage,fanart)
            else:
                if 'txt' in channel["url"]:
                    addDir(channel["name"],channel["url"],3,iconimage,fanart)
                else:
                    addLink(channel["name"],channel["url"],3,iconimage,fanart)
        xbmc.executebuiltin('Container.SetViewMode(50)')

def CatIndex(url):
    link=open_url(url)  
    match=re.compile('name="(.+?)".+?url="(.+?)".+?img="(.+?)"',re.DOTALL).findall(link)
    for name,url,iconimage in match:
        if 'youtube.com/playlist?list=' in url:
            addDir(name,url,3,iconimage,fanart)
        elif 'youtube.com/results?search_query=' in url:
            addDir(name,url,3,iconimage,fanart)
        else:
            addDir(name,url,1,iconimage,fanart)
    xbmc.executebuiltin('Container.SetViewMode(50)')
	

def GetList(url):
    link=open_url(url)  
    matches=re.compile('^#.+?:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(link)
    li = []
    for params, name, url in matches:
        item_data = {"params": params, "name": name, "url": url}
        li.append(item_data)
    list = []
    for channel in li:
        item_data = {"name": channel["name"], "url": channel["url"]}
        matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
        for field, value in matches:
            item_data[field.strip().lower().replace('-', '_')] = value.strip()
        list.append(item_data)
    return list

def PLAYLINK(url,name):
        print url
        if 'txt' in url:
            print 'Found txt'
            GetChans(url)
        else:
            if 'youtube.com/results?search_query=' in url:
				print 'Youtube Search'
				searchterm = url.split('search_query=')[1]
				ytapi = ytapi1 + searchterm + ytapi2
				req = urllib2.Request(ytapi)
				req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				link = link.replace('\r','').replace('\n','').replace('  ','')
				match=re.compile('"videoId": "(.+?)".+?"title": "(.+?)"',re.DOTALL).findall(link)
				print match
				for ytid,name in match:
					url = 'https://www.youtube.com/watch?v='+ytid
					addLink(name,url,3,iconimage,fanart)
            elif 'youtube.com/playlist?list=' in url:
				print 'Youtube Playlist'
				searchterm = url.split('playlist?list=')[1]
				ytapi = ytpl + searchterm + ytpl2
				req = urllib2.Request(ytapi)
				req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				link = link.replace('\r','').replace('\n','').replace('  ','')
				match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
				for name,ytid in match:
					url = 'https://www.youtube.com/watch?v='+ytid
					addLink(name,url,3,iconimage,fanart)
            elif 'dailymotion' in url:
                print 'DailyMotion'
                url = url.replace('video','embed/video')
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                match=re.compile('mp4","url"\:"(.+?)"').findall(link)[0]
                streamurl=match.replace('\/','/')
                ok=True
                liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=streamurl,listitem=liz)
                try:
                 xbmc.Player ().play(streamurl, liz, False)
                 return ok
                except:
                 pass
            else:
				print 'Direct Link'
				if urlresolver.HostedMediaFile(url).valid_url():
					streamurl = urlresolver.HostedMediaFile(url).resolve()
				else: streamurl=url 
				ok=True
				liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
				ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=streamurl,listitem=liz)
				try:
					xbmc.Player ().play(streamurl, liz, False)
					return ok
				except:
					pass

def TWITTER():
    text = ''
    twit = 'https://script.google.com/macros/s/AKfycbyBcUa5TlEQudk6Y_0o0ZubnmhGL_-b7Up8kQt11xgVwz3ErTo/exec?588677963413065728'
    req = urllib2.Request(twit)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    link = link.replace('/n','')
    link = link.decode('utf-8').encode('utf-8').replace('&#39;','\'').replace('&#10;',' - ').replace('&#x2026;','')
    match=re.compile("<title>(.+?)</title>.+?<pubDate>(.+?)</pubDate>",re.DOTALL).findall(link)[1:]
    for status, dte in match:
        try:
                status = status.decode('ascii', 'ignore')
        except:
                status = status.decode('utf-8','ignore')
        dte = dte[:-15]
        status = status.replace('&amp;','')
        dte = '[COLOR blue][B]'+dte+'[/B][/COLOR]'
        text = text+dte+'\n'+status+'\n'+'\n'
    showText('[COLOR blue][B]@uk_turk[/B][/COLOR]', text)

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
		try:
			xbmc.sleep(10)
			retry -= 1
			win.getControl(1).setLabel(heading)
			win.getControl(5).setText(text)
			return
		except:
			pass

def open_url(url):
    url += '?%d=%d' % (random.randint(1, 10000), random.randint(1, 10000))
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    link = link.replace('\r','').replace('\t','').replace('&nbsp;','').replace('\'','')
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

def addDir(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLink(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def addLinkMeta(name,url,mode,iconimage,itemcount,isFolder=False):
    if metaset=='true':
      if not 'COLOR' in name:
        splitName=name.partition('(')
        simplename=""
        simpleyear=""
        if len(splitName)>0:
			simplename=splitName[0]
			simpleyear=splitName[2].partition(')')
        if len(simpleyear)>0:
			simpleyear=simpleyear[0]
			mg = metahandlers.MetaData()
			meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
			u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
			ok=True
			liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=iconimage)
			liz.setInfo( type="Video", infoLabels= meta )
			contextMenuItems = []
			contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
			liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
        return ok
    else:
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&site="+str(site)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
        return ok

def setView(content, viewType):
    if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
    if selfAddon.getSetting('auto-view')=='true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass

#print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)

if mode==None or url==None or len(url)<1: Index()
elif mode==1:GetChans(url)
elif mode==2:TWITTER()
elif mode==3:PLAYLINK(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
