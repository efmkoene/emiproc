#%%
import pandas as pd
from pathlib import Path
import numpy as np
import geopandas as gpd
from typing import Any, Iterable
from shapely.geometry import Point, MultiPolygon, Polygon
from emiproc.inventories.utils import add_inventories, crop_with_shape
from emiproc.plots import explore_inventory, explore_multilevel
from emiproc.utilities import ProgressIndicator
from emiproc.regrid import (
    calculate_weights_mapping,
    geoserie_intersection,
    get_weights_mapping,
    remap_inventory,
)
from emiproc.inventories import Inventory
from emiproc.grids import GeoPandasGrid
from emiproc.inventories.utils import group_categories


serie = gpd.GeoSeries(
    [
        Polygon(((0, 0), (0, 1), (1, 1), (1, 0))),
        Polygon(((0, 1), (0, 2), (1, 2), (1, 1))),
        Polygon(((1, 0), (1, 1), (2, 1), (2, 0))),
        Polygon(((1, 1), (1, 2), (2, 2), (2, 1))),
        Polygon(((2, 1), (2, 2), (3, 2), (3, 1))),
    ]
)
triangle = Polygon(((0.5, 0.5), (1.5, 0.5), (1.5, 1.5)))

# Check the intersection
cropped, weights = geoserie_intersection(
    serie, triangle, keep_outside=True, drop_unused=False
)


inv = Inventory.from_gdf(
    gpd.GeoDataFrame(
        {
            ("adf", "CH4"): [i + 3 for i in range(len(serie))],
            ("adf", "CO2"): [i for i in range(len(serie))],
            ("liku", "CO2"): [i for i in range(len(serie))],
            ("test", "NH3"): [i + 1 for i in range(len(serie))],
        },
        geometry=serie,
    )
)

inv.gdf
inv_with_pnt_sources = inv.copy()
inv_with_pnt_sources.gdfs["blek"] = gpd.GeoDataFrame(
    {
        "CO2": [1, 2, 3],
    },
    geometry=[Point(0.75, 0.75), Point(0.25, 0.25), Point(1.2, 1)],
)
inv_with_pnt_sources.gdfs["liku"] = gpd.GeoDataFrame(
    {
        "CO2": [1, 2],
    },
    geometry=[Point(0.65, 0.75), Point(1.1, 0.8)],
)
inv_with_pnt_sources.gdfs["other"] = gpd.GeoDataFrame(
    {
        "AITS": [i+1 for i in range(5)],
    },
    geometry=    [
        Polygon(((0, 0), (0, 1), (1, 1), (1, 0))),
        Polygon(((0, 1), (0, 2), (1, 2), (1, 1))),
        Polygon(((1, 0), (1, 1), (2, 1), (2, 0))),
        Polygon(((1, 1), (1, 2), (2, 2), (2, 1))),
        Polygon(((2, 1), (2, 2), (3, 2), (3, 1))),
    ],
)
cropped = crop_with_shape(inv_with_pnt_sources, triangle, modify_grid=True)
#%%

def test_basic_crop():

    cropped = crop_with_shape(inv, triangle)

def test_with_modify_grid():

    cropped = crop_with_shape(inv, triangle, modify_grid=True)

    assert 4 not in cropped.gdf.index
    # Check an expected value
    assert cropped.gdf[("adf", "CH4")].iloc[0] == 3 / 8


def test_with_gdfs():

    cropped = crop_with_shape(inv_with_pnt_sources, triangle, modify_grid=True)

    assert len(cropped.gdfs["blek"]) == 2
    # Check  expected values
    assert cropped.gdfs["blek"]["CO2"].iloc[0] == 1 / 2  # At the boundary divided by 2
    assert cropped.gdfs["blek"]["CO2"].iloc[1] == 3

    # Check  point outside disappeared
    assert len(cropped.gdfs["liku"]) == 1
    # Make sure the index was reset
    assert 1 not in cropped.gdfs["liku"].index
    assert 0 in cropped.gdfs["liku"].index
    
    assert len(cropped.gdfs['other']) == 3
    assert cropped.gdfs["other"]['AITS'].iloc[0] == 1 / 8
    assert cropped.gdfs["other"]['AITS'].iloc[1] == 3 / 4
    assert cropped.gdfs["other"]['AITS'].iloc[2] == 4 / 8

def test_with_modify_grid_and_cached():
    w_file = Path('.emiproc_test_with_modify_grid_and_cached')
    cropped = crop_with_shape(inv, triangle, weight_file=w_file, modify_grid=True)

    assert 4 not in cropped.gdf.index
    cropped = crop_with_shape(inv, triangle, weight_file=w_file, modify_grid=True)

    assert 4 not in cropped.gdf.index
# %%
