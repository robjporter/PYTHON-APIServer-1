import random, string

class stringFunctions:
    @classmethod
    def randomStringGenerator( self, length ):
        return ''.join( random.SystemRandom().choice( string.ascii_uppercase + string.digits ) for _ in range( length ))

    @classmethod
    def toDict( self, dictionary ):
        rv = dict( self.payload or ())
        rv['message'] = self.message
        return rv
