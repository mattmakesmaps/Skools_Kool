"""
A generalized WSGI script accepting a tuple of coordinate pairs, a buffer, and geom type.
Will return as WKT a Polygon representation of that buffer.

args:
coords - A tuple of coordinate pairs.
bufferdist - The desired buffer distance.
geomtype - the input geometry type. Point, Line, Polygon.
format - Output format, either WKT or GeoJSON.

An Example Query String:
http://localhost/geombuffer?coords=((-1.0,-1.0),(-1.0,1.0),(1.0,1.0),(1.0,-1.0))&bufferdist=20&geomtype=polygon&format=geojson

Invalid Geometry Query:
http://localhost/geombuffer?coords=((0,0),(0,2),(1,1),(2,2),(2,0),(1,1),(0,0))&bufferdist=20&geomtype=polygon&format=wkt

Resulting *args tuple:
({'bufferdist': ['20'], 'geomtype': ['polygon'], 'coords': ['((-1.0,-1.0),(-1.0,1.0),(1.0,1.0),(1.0,-1.0))']},)
"""
from shapely.geometry import Point, LineString, Polygon
from vectorformats.Formats import GeoJSON, WKT
from urlparse import parse_qs
from ast import literal_eval

def wkt_to_geojson(wktStr):
    """Return GeoJSON from a WKT string."""
    try:
        # Create instances of vectorfeatures WKT/GeoJSON Classes
        inWKT = WKT.WKT()
        outGeoJSON = GeoJSON.GeoJSON()
        # Decode WKT to vectorformats features, and re-encode as GeoJSON
        return outGeoJSON.encode(inWKT.decode(wktStr), to_string=True)
    except Exception, e:
        raise Exception(str(e))

def create_geom(*args):
    """Return a Shapely Geom from a WSGI Environ Dictionary"""
        # Parse useful values from the Query String.
    try:
        coords = literal_eval(args[0]['coords'][0]) # literal_eval should help protect against injection
        geomtypeStr = args[0]['geomtype'][0].lower()
    except KeyError, e:
        raise KeyError('Required URL Parameter %s not found.' % str(e))

    # Dispatch table. Is there a better way to create instances of these objects?
    geomDispatch = {'point':Point, 'linestring':LineString, 'polygon':Polygon,
                    'multipoint':MultiPoint,'multilinestring':MultiLineString,
                    'multipolygon':MultiPolygon}

    # Create the input geometry instance.
    if geomtypeStr in geomDispatch:
        inputGeom = geomDispatch[geomtypeStr](coords)
    else:
        raise KeyError('URL Parameter geomtype value %s not supported.' % geomtypeStr)

    if inputGeom.is_valid:
        return inputGeom
    else:
        raise ValueError('Coordinates passed do not form a valid %s.' % geomtypeStr)

def create_buff(*args):
    """Return a WKT representation for a geom and buffer distance"""
    try:
        # Create Input Geom
        inputGeom = create_geom(*args)
        # Parse useful values from the Query String.
        try:
            geomBuff = literal_eval(args[0]['bufferdist'][0])
            geomFormat = args[0]['format'][0].lower()
        except KeyError, e:
            raise KeyError('Required URL Parameter not found %s' % str(e))

        # Create the buffer geometry instance
        buffGeom = inputGeom.buffer(geomBuff)
        if geomFormat == 'wkt':
            return buffGeom.wkt
        elif geomFormat == 'geojson':
            return wkt_to_geojson(buffGeom.wkt)
        else:
            raise ValueError('Acceptable Formats are wkt or geojson.')

    except Exception, e:
        return "Encountered Error: %s" % str(e)

def application(environ, start_response):
    """
    The mod_wsgi application function. Generates response headers and handles the CGI environ variables.
    """
    try:
        parseDict = parse_qs(environ['QUERY_STRING'])
        output = create_buff(parseDict)

        # Create headers and return buffered point as WKT
        status = '200 OK'
        response_headers = [('Content-type','text/plain'), ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output]
    except Exception, e:
        return "Encountered Error: %s" % str(e)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8240, application)
    print "Serving HTTP on port 8240..."

    # Respond to requests until process is killed
    httpd.serve_forever()
