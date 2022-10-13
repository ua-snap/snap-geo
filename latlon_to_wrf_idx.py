"""Convert lat, lon coordinates to 1-indexed row and column indices on the WRF grid"""

from argparse import ArgumentParser
import numpy as np
from affine import Affine
from pyproj import Transformer
from pyproj.crs import CRS


parser = ArgumentParser(
    description="Convert lat and lon coordinates to 1-indexed row and column indices on the WRF grid"
)
parser.add_argument(
    "-lat", dest="lat", help="Latitude"
)
parser.add_argument(
    "-lon", dest="lon", help="Longitude"
)

# parse the args and unpack
args = parser.parse_args()

# derive transformer from WGS84 to CRS from WRF proj4 string
wrf_proj_str = "+units=m +proj=stere +lat_ts=64.0 +lon_0=-152.0 +lat_0=90.0 +x_0=0 +y_0=0 +a=6370000 +b=6370000"
wrf_crs = CRS.from_proj4(wrf_proj_str)
transformer = Transformer.from_crs("epsg:4326", wrf_crs)
wrf_coords = transformer.transform(args.lat, args.lon)

transform = Affine(20000.0, 0.0, -2620000.0, 0.0, -20000.0, -172425.4773716638)

# here we multiply the hardcoded WRF affine transform by the (x, y) WRF coordinate pair
# that maps the xy coordinates to column/row values, but as reals insead of ints
# we add 0.5 to that result because *.5 represents the pixel center, so that bumps us
#  to the edge of the pixel and effectively making the subsequent rounding go to 1-indexed values for MATLAB
#  (we would substract 0.5 before rounding to get 0-indexed python array indices)
c, r = np.round(np.array(~transform * wrf_coords) + 0.5).astype(int)

print(f"Row: {r}; Column: {c}")
