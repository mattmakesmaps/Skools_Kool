"""
Goal is to take generalize pointbuffer.wsgi to accept points,lines,polygons
Polygons look like Polygon(((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0)))

An Example Query String:
http://localhost/geombuffer?geom=((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0))&buffer=20

Resulting *args tuple:
({'buffer': ['20'], 'geom': ['((-1.0, -1.0), (-1.0, 1.0), (1.0, 1.0), (1.0, -1.0))']},)

"""
from shapely.geometry import Point, LineString, Polygon
from urlparse import parse_qs

def create_buff(*args, **kwargs):
    """Return a WKT representation for a geom and buffer distance"""
    if 'geom' in args[0]:
        geomStr = args[0]['geom'][0]

    return 'args: %s \n geomStr: %s' % (str(args), geomStr)

def application(environ, start_response):
    """
    for a query string such as: http://localhost/wsgitest?x=5&y=10&buff=15
    the query string dictionary will look like:
    {'x': ['5'], 'y': ['10'], 'buff':['15']}
    """
    parseDict = parse_qs(environ['QUERY_STRING'])
    pointInfo = create_buff(parseDict)
#    # Shapely expecting floats, not strings
#    x = float(parseDict['x'][0])
#    y = float(parseDict['y'][0])
#    buff = float(parseDict['buff'][0])
#
#    pointInfo = create_buff(x,y,buff)
    output = pointInfo

    # Create headers and return buffered point as WKT
    status = '200 OK'
    response_headers = [('Content-type','text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

