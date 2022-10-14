"""This should test that a shape containing a hole is properly working.

One test should be on a test data and one on a country like south africa.
"""
from shapely.geometry import Polygon
import cartopy.io.shapereader as shpreader

# TODO: implmeent test for souht aftrica with has a shape


shpfilename = shpreader.natural_earth(
    resolution="10m", category="cultural", name="admin_0_countries"
)

countries = list(shpreader.Reader(shpfilename).records())
sa_geometry = countries[36].geometry

# The country (no islands), this one has holes
main_geom = sa_geometry.geoms[0]