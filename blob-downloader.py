import ffmpeg

url = "https://cfvod.kaltura.com/scf/hls/p/1756931/sp/175693100/serveFlavor/entryId/0_9jnbt7ws/v/2/flavorId/0_2z889lcd/name/a.mp4/index.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMTc1NjkzMS9zcC8xNzU2OTMxMDAvc2VydmVGbGF2b3IvZW50cnlJZC8wXzlqbmJ0N3dzL3YvMioiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1OTMzNzA2ODJ9fX1dfQ__&Signature=ex3qs8ADDbM7uxiBMzGqK-jWNTZa7PoxsSHwtiyF3dGcfHk85xkwjzLzj-rxBHoYq4rmE~EtaljKUZxCk7dgxbsEqUOesjVvGp8k8q0AI6HxNGFITVzJP8T3FazRtwsN~5tkKK24DTXYmNHeRZOGAOyaowzuKlKL2UmhQsBkrr4thjIlWE2yyK5HRHPZXf0ilj3U18QFapytCGfmrjdpOX8Ac6gjFJqy9TYi6d9jUMYDCm-su3j8D7pzp49nsMeE5yXUa4xuqPVUk6RzeNz6Cgjb3Dn2tbJKThxHQdFVsET7N9PQt05PDIo39tloDSUcp98Yf5NqDqDoes6PtjyOQw__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A"
stream = ffmpeg.input(url).output('output.mp4').run()