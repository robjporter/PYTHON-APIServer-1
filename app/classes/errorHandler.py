from flask import jsonify, request
from app.classes import switch

class ApiErrorBaseClass( Exception ):
    status = 500
    message = 'Internal Error'
    extras = None

    @property
    def toJSON( self ):
        return { k:getattr(self, k) for k in ['status', 'message', 'extras'] if getattr(self, k)}

    @property
    def toXML( self ):
        pass

    @property
    def toHTML( self ):
        response = "<html>"
        response += "Status = " + str( self.status )+ "<br>"
        response += "Message = " + self.message + "<br>"
        response += "Extras = " + self.extras + "<br>"
        response += "</html>"
        return response


class CustomErrorMessage( ApiErrorBaseClass ):
    def __init__( self, code ):
        self.status = code
        self.message = "Hope this works!"
        self.extras = "my Extras"

class RequestForUnsupportedMediaFormat( ApiErrorBaseClass ):
    status = 415
    message = ""
    extras = ""

class UnsupportedRequestMethod( ApiErrorBaseClass ):
    status = 301
    message = ""
    extras = ""

class RequestFromBlockedIP( ApiErrorBaseClass ):
    status = 403
    message = "This resource has been denied due to an access request from a blocked IP address."
    extras = ""

class ResourceDoesNotExist2( ApiErrorBaseClass ):
      status = 404
      message = "Resource does not exist"
      extras = "BlahBlah"

class CustomApiErrorClass( ApiErrorBaseClass ):
     @property
     def custom_data( self ):
            return {'status': "failure", 'error': self.message}

class ResourceDoesNotExist( CustomApiErrorClass ):
     status = 404
     message = "Resource does not exist"
     extras = "BlahBlah"

class MissingRequiresParameters( CustomApiErrorClass ):
    status = 400
    message = "Missing required params"
    def __init__(self, missing_prams):
            self.missing_params = missing_params
            self.message = self.message + ': ' + ', '.join([x for x in missing_params])
