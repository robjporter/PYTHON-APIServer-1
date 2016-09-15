def reverse_filter( s ):
    return s[ ::-1 ]

def string_trim_upper( value ):
  return value.strip().upper()
  
def string_trim_lower( value ):
  return value.strip().lower()
  
def datetimeformat( value, format='%H:%M / %d-%m-%Y' ):
    return value.strftime( format )

