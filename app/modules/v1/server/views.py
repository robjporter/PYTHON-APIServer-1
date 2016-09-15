from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort
from . import server
import datetime
from app.classes import stringFunctions
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit
from app.classes.helpers import file_size
import psutil

version = "0.1.0"

@server.route( '/version' )
def myprofile():
    return jsonify( version = version )

@server.route( "/cpu/count/logical" )
def cpucount():
	return jsonify({ "cpucount" : psutil.cpu_count() })

@server.route( "/cpu/count/physical" )
def cpucountlogical():
    return jsonify({ "cpucount" : psutil.cpu_count( logical = False ) })

@server.route( "/cpu/overview" )
def cpuoverview():
    return jsonify({ "cputimes" : psutil.cpu_times() })

@server.route( "/cpu/user" )
def cpuusertime():
    return jsonify({ "cpuuser" : psutil.cpu_times()[ 0 ] })

@server.route( "/cpu/system" )
def cpusystemtime():
    return jsonify({ "cpusystem" : psutil.cpu_times()[ 2 ] })

@server.route( "/cpu/idle" )
def cpuidletime():
    return jsonify({ "cpuidle" : psutil.cpu_times()[ 3 ] })

@server.route( "/cpu/wait" )
def cpuwaittime():
    return jsonify({ "cpuiowait" : psutil.cpu_times()[ 4 ] })

@server.route( "/cpu/overview/percent" )
def cpuoverviewpercent():
    return jsonify({ "cputimespercent" : psutil.cpu_times_percent() })

@server.route( "/cpu/user/percent" )
def cpuusertimepercent():
    return jsonify({ "cpuuserpercent" : psutil.cpu_times_percent()[ 0 ] })

@server.route( "/cpu/system/percent" )
def cpusystemtimepercent():
    return jsonify({ "cpusystempercent" : psutil.cpu_times_percent()[ 2 ] })

@server.route( "/cpu/idle/percent" )
def cpuidletimepercent():
    return jsonify({ "cpuidlepercent" : psutil.cpu_times_percent()[ 3 ] })

@server.route( "/cpu/percent" )
def cpupercent():
    return jsonify({ "cpupercent" : psutil.cpu_percent() })

@server.route( "/memory/overview" )
def memoryoverview():
    return jsonify({ "virtualmemory" : psutil.virtual_memory() })

@server.route( "/memory/total" )
def memorytotal():
    return jsonify({ "memorytotal" : psutil.virtual_memory()[ 0 ]})

@server.route( "/memory/total/format" )
def memorytotalformatted():
    return jsonify({ "memorytotal" : file_size( psutil.virtual_memory()[ 0 ])})

@server.route( "/memory/available" )
def memoryavailable():
    return jsonify({ "memoryavailable" : psutil.virtual_memory()[ 1 ]})

@server.route( "/memory/available/format" )
def memoryavailableformatted():
    return jsonify({ "memoryavailable" : file_size( psutil.virtual_memory()[ 1 ])})

@server.route( "/memory/used/percent" )
def memoryusedpercent():
    return jsonify({ "memorypercent" : psutil.virtual_memory()[ 2 ]})

@server.route( "/memory/swap" )
def memoryswapoverview():
    return jsonify({ "swapmemory" : psutil.swap_memory() })

@server.route( "/memory/swap/total" )
def memoryswaptotal():
    return jsonify({ "swapmemorytotal" : psutil.swap_memory()[ 0 ] })

@server.route( "/memory/swap/total/format" )
def memoryswaptotalformatted():
    return jsonify({ "swapmemorytotal" : file_size( psutil.swap_memory()[ 0 ])})

@server.route( "/memory/swap/used" )
def memoryswapused():
    return jsonify({ "swapmemoryused" : psutil.swap_memory()[ 1 ] })

@server.route( "/memory/swap/used/format" )
def memoryswapusedformatted():
    return jsonify({ "swapmemoryused" : file_size( psutil.swap_memory()[ 1 ])})

@server.route( "/memory/swap/free" )
def memoryswapfree():
    return jsonify({ "swapmemoryfree" : psutil.swap_memory()[ 2 ] })

@server.route( "/memory/swap/free/format" )
def memoryswapfreeformatted():
    return jsonify({ "swapmemoryfree" : file_size( psutil.swap_memory()[ 2 ])})

@server.route( "/memory/swap/used/percent" )
def memoryswapusedpercent():
    return jsonify({ "swapmemorypercent" : psutil.swap_memory()[ 3 ] })

@server.route( "/partitions" )
def diskpartitions():
    return jsonify({ "partitions" : psutil.disk_partitions() })

@server.route( "/partitions/root/usage" )
def diskpartitionusage():
    return jsonify({ "partitionusage" : psutil.disk_usage('/') })

@server.route( "/partitions/root/size" )
def diskpartitionsize():
    return jsonify({ "partitionsize" : psutil.disk_usage('/')[ 0 ] })

@server.route( "/partitions/root/used" )
def diskpartitionused():
    return jsonify({ "partitionused" : psutil.disk_usage('/')[ 1 ] })

@server.route( "/partitions/root/free" )
def diskpartitionfree():
    return jsonify({ "partitionfree" : psutil.disk_usage('/')[ 2 ] })

@server.route( "/partition/root/percent" )
def diskpartitionpercent():
    return jsonify({ "partitionpercentused" : psutil.disk_usage('/')[ 3 ] })

@server.route( "/io/overview" )
def iocountersoverview():
    return jsonify({ "iocounters" : psutil.disk_io_counters( perdisk = False )})

@server.route( "/io/read" )
def iocountersread():
    return jsonify({ "ioread" : psutil.disk_io_counters( perdisk = False )[ 0 ]})

@server.route( "/io/write" )
def iocounterswrite():
    return jsonify({ "iowrite" : psutil.disk_io_counters( perdisk = False )[ 1 ]})

@server.route( "/io/read/bytes" )
def iocountersreadbytes():
    return jsonify({ "ioreadbytes" : psutil.disk_io_counters( perdisk = False )[ 2 ]})

@server.route( "/io/write/bytes" )
def iocounterswritebytes():
    return jsonify({ "iowritebytes" : psutil.disk_io_counters( perdisk = False )[ 3 ]})

@server.route( "/network" )
def networkingoverview():
    return jsonify({ "networking" : psutil.net_io_counters( pernic = True ) })

@server.route( "/network/connections" )
def networkconnections():
    return jsonify({ "connections" : psutil.net_connections() })

@server.route( "/network/stats" )
def networkstats():
    return jsonify({ "networkstats" : psutil.net_if_stats() })

@server.route( "/network/stats/<adapter>" )
def networkstatsadapter( adapter ):
	tmp = psutil.net_if_stats()
	if( adapter in tmp ):
		return jsonify({ "networkstats" : tmp[ adapter ] })
	else:
		raise ResourceDoesNotExist()

@server.route( "/network/stats/<adapter>/status" )
def networkstatsadapterstatus( adapter ):
	tmp = psutil.net_if_stats()
	if( adapter in tmp ):
		return jsonify({ "networkstats" : tmp[ adapter ][ 0 ] })
	else:
		raise ResourceDoesNotExist()

@server.route( "/network/stats/<adapter>/mtu" )
def networkstatsadaptermtu( adapter ):
	tmp = psutil.net_if_stats()
	if( adapter in tmp ):
		return jsonify({ "networkstats" : tmp[ adapter ][ 3 ] })
	else:
		raise ResourceDoesNotExist()

@server.route( "/users" )
def users():
    return jsonify({ "users" : psutil.users() })

@server.route( "/boottime" )
def boottime():
    return jsonify({ "boottime" : psutil.boot_time() })

@server.route( "/boottime/format" )
def boottimeformatted():
	return jsonify({ "boottime" : datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S") })
