from shapely.geometry import Point
from urlparse import parse_qs

def create_buff(x,y,buff):
    """Return a WKT representation for a point and buffer distance"""
    pointIn = Point(x,y)
    pointBuff = pointIn.buffer(buff)
    return pointBuff.wkt

def application(environ, start_response):
    """
    for a query string such as: http://localhost/wsgitest?x=5&y=10&buff=15
    the query string dictionary will look like:
    {'x': ['5'], 'y': ['10'], 'buff':['15']}
    """
    parseDict = parse_qs(environ['QUERY_STRING'])
    # Shapely expecting floats, not strings
    x = float(parseDict['x'][0])
    y = float(parseDict['y'][0])
    buff = float(parseDict['buff'][0])

    pointInfo = create_buff(x,y,buff)
    output = pointInfo

    # Create headers and return buffered point as WKT
    status = '200 OK'
    response_headers = [('Content-type','text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

