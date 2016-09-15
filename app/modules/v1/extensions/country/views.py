from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort
from . import country
import datetime, json

from app.classes import stringFunctions
from app.classes.bashcolors import colors
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit
from app.classes.decorators.timing import add_timing_information
from app.classes.cache import cache

def setup():
    app.logger.info( colors.getInfo() + "Country setup complete" )
    try:
        if( 'countries' not in app.extensions[ 'registry' ][ app.config[ 'EXTENSION_NAMESPACE' ] ] ):
            app.extensions[ 'registry' ][ app.config[ 'EXTENSION_NAMESPACE' ]].register( { "countries": loadJSONData() })
    except Exception as e:
        print( e )

def loadJSONData():
    import os
    json_data = open( os.path.dirname(os.path.abspath( __file__ )) + "/static/data/data.json", "r", encoding="utf-8" )
    data = json.load( json_data )
    app.logger.debug( colors.getDebug() + "APP->MODULES->EXTENSIONS->COUNTRY->VIEWS->loadJSONData complete" )
    return data

def getData( code, item ):
    data = None
    for obj in app.extensions[ 'registry' ][ app.config[ 'EXTENSION_NAMESPACE' ]]:
        if( 'countries' in obj ):
            data = obj[ 'countries' ]
            break
    if( data != None ):
        for country in data:
            if code.upper() == country[ 'ISO3166-1-Alpha-2' ] or code.upper() == country[ 'ISO3166-1-Alpha-3' ]:
                return country[ item ]
    return "NOT FOUND"

@country.route( "/" )
@add_timing_information
def index():
    return "name 	1 	string 	Country's official English short name\
    ISO3166-1-Alpha-2 	3 	string 	Alpha-2 codes from ISO 3166-1\
    ISO3166-1-Alpha-3 	4 	string 	Alpha-3 codes from ISO 3166-1 (synonymous with World Bank Codes)\
    ISO3166-1-numeric 	5 	integer 	Numeric codes from ISO 3166-1 (synonymous with UN Statistics M49 Codes)\
    ITU 	6 	string 	Codes assigned by the International Telecommunications Union\
    MARC 	7 	string 	MAchine-Readable Cataloging codes from the Library of Congress\
    WMO 	8 	string 	Country abbreviations by the World Meteorological Organization\
    DS 	9 	string 	Distinguishing signs of vehicles in international traffic\
    Dial 	10 	string 	Country code from ITU-T recommendation E.164, sometimes followed by area code\
    FIFA 	11 	string 	Codes assigned by the Fédération Internationale de Football Association\
    FIPS 	12 	string 	Codes from the U.S. standard FIPS PUB 10-4\
    GAUL 	13 	integer 	Global Administrative Unit Layers from the Food and Agriculture Organization\
    IOC 	14 	string 	Codes assigned by the International Olympics Committee\
    currency_alphabetic_code 	15 	string 	ISO 4217 currency alphabetic code\
    currency_country_name 	16 	string 	ISO 4217 country name\
    currency_minor_unit 	17 	integer 	ISO 4217 currency number of minor units\
    currency_name 	18 	string 	ISO 4217 currency name\
    currency_numeric_code 	19 	integer 	ISO 4217 currency numeric code\
    is_independent 	20 	string 	Country status, based on the CIA World Factbook"

@country.route( "/<code>/name" )
def getName( code ):
    print( "INSIDE" )
    return getData( code, "name" )

@country.route( "/<code>/iso2" )
def getISO2( code ):
    return getData( code, "ISO3166-1-Alpha-2" )

@country.route( "/<code>/iso3" )
def getISO3( code ):
    return getData( code, "ISO3166-1-Alpha-3" )

@country.route( "/<code>/isonum" )
def getISONUM( code ):
    return getData( code, "ISO3166-1-numeric" )

@country.route( "/<code>/itu" )
def getITU( code ):
    return getData( code, "ITU" )

@country.route( "/<code>/marc" )
def getMARC( code ):
    return getData( code, "MARC" )

@country.route( "/<code>/wmo" )
def getWMO( code ):
    return getData( code, "WMO" )

@country.route( "/<code>/ds" )
def getDS( code ):
    return getData( code, "DS" )

@country.route( "/<code>/dial" )
def getDial( code ):
    return getData( code, "Dial" )

@country.route( "/<code>/fifa" )
def getFifa( code ):
    return getData( code, "FIFA" )

@country.route( "/<code>/fips" )
def getFips( code ):
    return getData( code, "FIPS" )

@country.route( "/<code>/gaul" )
def getGaul( code ):
    return getData( code, "GAUL" )

@country.route( "/<code>/ioc" )
def getIOC( code ):
    return getData( code, "IOC" )

@country.route( "/<code>/currencycode" )
def getCurrencyCode( code ):
    return getData( code, "currency_alphabetic_code" )

@country.route( "/<code>/currencycountry" )
def getCurrencyCountry( code ):
    return getData( code, "currency_country_name" )

@country.route( "/<code>/currency" )
def getCurrency( code ):
    return getData( code, "currency_name" )

@country.route( "/<code>/currencynumber" )
def getCurrencyNumber( code ):
    return getData( code, "currency_numeric_code" )

@country.route( "/<code>/currencyunit" )
def getCurrencyUnit( code ):
    return getData( code, "currency_minor_unit" )

@country.route( "/<code>/independent" )
def getCurrencyIndependent( code ):
    return getData( code, "is_independent" )
