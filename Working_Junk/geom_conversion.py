__author__ = 'matt'
"""
Objective: Convert output from shapely (WKT) to GeoJSON
"""

from shapely.geometry import Point
from vectorformats.Formats import GeoJSON, WKT

# Create Shapely Geometry and Buffer
p1 = Point(10,10)
p1buff = p1.buffer(10)

## Create New Instance of WKT Class
#wkt1 = WKT.WKT()
## Decode WKT of Buffer to a vectorformats feature
#wkt1_decoded = wkt1.decode(p1buff.to_wkt())
## Create New Instance of GeoJSON Class
#geojson1 = GeoJSON.GeoJSON()
## Re-encode WKT decoded features as GeoJSON
#print geojson1.encode(wkt1_decoded, to_string=True)

def wkt_to_geojson(wktStr):
    """Return GeoJSON from a WKT string."""
    # Create instances of vectorfeatures WKT/GeoJSON Classes
    inWKT = WKT.WKT()
    outGeoJSON = GeoJSON.GeoJSON()
    # Decode WKT to vectorformats features, and re-encode as GeoJSON
    return outGeoJSON.encode(inWKT.decode(wktStr), to_string=True)

print wkt_to_geojson(p1buff.to_wkt())

