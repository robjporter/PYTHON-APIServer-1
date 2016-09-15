import datetime

def inject_time():
    return dict( current_time = datetime.datetime.utcnow())

def format_price( amount, currency = u'€' ):
    return u'{0:.2f}{1}'.format( amount, currency )