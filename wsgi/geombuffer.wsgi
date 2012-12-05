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

TODO: Extract geometry creation functionality from create_buff. Will be useful if other functions are
      created to do different spatial analyses (e.g. Union, Intersect, etc.)
"""
from shapely.geometry import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
from urlparse import parse_qs
from ast import literal_eval

def create_geom():
    """Given values from a WSGI Environ dictionary, return a shapely geom"""
    pass

def create_buff(*args, **kwargs):
    """Return a WKT representation for a geom and buffer distance"""
    try:
        # Parse useful values from the Query String.
        try:
            coords = literal_eval(args[0]['coords'][0]) # literal_eval should help protect against injection
            geomtypeStr = args[0]['geomtype'][0].lower()
            geomBuff = literal_eval(args[0]['bufferdist'][0])
        except KeyError, e:
            return 'KeyError: Required Param Not Found: %s' % str(e)

        # Dispatch table. Is there a better way to create instances of these objects?
        geomDispatch = {'point':Point, 'linestring':LineString, 'polygon':Polygon,
                        'multipoint':MultiPoint,'multilinestring':MultiLineString,
                        'multipolygon':MultiPolygon}

        if geomtypeStr in geomDispatch:
            # Create the input geometry instance
            inputGeom = geomDispatch[geomtypeStr](coords)
        else:
            raise KeyError('geomtype value %s not supported.' % geomtypeStr)

        # Create the buffer geometry instance
        buffGeom = inputGeom.buffer(geomBuff)
        return buffGeom.wkt

    except Exception, e:
        # TODO: Replace with more appropriate exception.
        return "Encountered Error: %s" % str(e)

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

