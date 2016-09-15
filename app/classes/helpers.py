from flask import request
from math import log2

def file_size( size, standard = False ):
    _suffixes = None
    if( standard ):
        _suffixes = [ 'bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'EiB', 'ZiB' ]
    else:
        _suffixes = [ 'bytes', 'KB', 'MB', 'GB', 'TB', 'EB', 'ZB' ]

    order = int( log2( size ) / 10 ) if size else 0
    return '{:.4g} {}'.format( size / ( 1 << ( order * 10 )), _suffixes[ order])

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def request_wants_json():
    if( 'accept' in request.headers ):
        if request.headers[ 'accept' ] == "application/json" or request.headers[ 'accept' ] == "":
            return True
        else:
            return False
    return True

def request_wants_html():
    if( 'accept' in request.headers ):
        if "text/html" in request.headers[ 'accept' ]:
            return True
        else:
            return False
    return False

def request_wants_xml():
    if( 'accept' in request.headers ):
        if request.headers[ 'accept' ] == "application/xml":
            return True
        else:
            return False
    return False
