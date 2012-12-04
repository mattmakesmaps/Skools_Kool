"""
A generalized WSGI script accepting a tuple of coordinate pairs, a buffer, and geom type.
Will return as WKT a Polygon representation of that buffer.

args:
coords - A tuple of coordinate pairs.
bufferdist - The desired buffer distance.
geomtype - the input geometry type. Point, Line, Polygon.

An Example Query String:
http://localhost/geombuffer?coords=((-1.0,-1.0),(-1.0,1.0),(1.0,1.0),(1.0,-1.0))&bufferdist=20&geomtype=polygon

Resulting *args tuple:
({'bufferdist': ['20'], 'geomtype': ['polygon'], 'coords': ['((-1.0,-1.0),(-1.0,1.0),(1.0,1.0),(1.0,-1.0))']},)

"""
from shapely.geometry import Point, LineString, Polygon
from urlparse import parse_qs
from ast import literal_eval

def create_buff(*args, **kwargs):
    """Return a WKT representation for a geom and buffer distance"""
    try:
        # Parse useful values from the Query String.
        coords = literal_eval(args[0]['coords'][0]) # literal_eval should help protect against injection
        geomtypeStr = args[0]['geomtype'][0].lower()
        geomBuff = literal_eval(args[0]['bufferdist'][0])

        # Dispatch table. Is there a better way to create instances of these objects?
        geomDispatch = {'point':Point, 'line':LineString, 'polygon':Polygon}

        if geomtypeStr in geomDispatch:
            # Create the input/buffer geometry instances
            inputGeom = geomDispatch[geomtypeStr](coords)
            buffGeom = inputGeom.buffer(geomBuff)

        return buffGeom.wkt

    except Exception, e:
        # TODO: Replace with more appropriate exception.
        print e

def application(environ, start_response):
    """
    The mod_wsgi application function. Generates response headers and handles the CGI environ variables.
    """
    parseDict = parse_qs(environ['QUERY_STRING'])
    output = create_buff(parseDict)

    # Create headers and return buffered point as WKT
    status = '200 OK'
    response_headers = [('Content-type','text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

