import os
import unittest2 as unittest
from flask import Flask
import main

class unittests( unittest.TestCase ):
    def setUp( self ):
        app.config[ 'TESTING' ] = True
        app.config[ 'DEBUG' ] = False
        app.config[ 'WTF_CSRF_ENABLED' ] = False
        self.app = app.test_client()

    def tearDown( self ):
        print( "TEARDOWN" )

    def test_v1Index2( self ):
        rv = self.app.get( '/v1/' )
        self.assertEqual( rv.status_code, 200 )

    def test_v1Index( self ):
        rv = self.app.get( '/v1/' )
        assert "Start Bootstrap" in str( rv.data )

if __name__ == '__main__':
    unittest.main()
