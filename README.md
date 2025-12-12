# Geometry datasets to shapefile format

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GeoPandas](https://img.shields.io/badge/GeoPandas-3CB371?style=for-the-badge&logo=python&logoColor=white)

This repository provides a Python 🐍 utility for exporting datasets to Shapefile format. It supports both `pandas DataFrames` and `GeoPandas GeoDataFrames`, allowing seamless handling of spatial and no-spatial data.

The tool is designed to work with geometries of type `Point`, ensuring compatibility with common GIS workflows. It includes functions for validating geometries, transforming coordinate reference systems when needed, and exporting clean, ready-to-use Shapefiles for further analysis in GIS platforms such as QGIS and ArcGIS.

# 🚀 Getting Ready
**Prerequisites**
- Python > 3.10

You can use this repository in two different ways: Clone the repository or install as a dependency

1. Clone the repository

    Follows the steps below to clone and work directly with the source code

    Clone repository
    ```bash
    git clone https://github.com/r3card0/geom-to-shapefile.git
    ```

2. Install as a dependency

    Alternatively, you can install this repository as a dependency within your own project:

    1. Create a Python virtual environment

        ```python
        python3 -m venv <virtual_env_name>
        ```

    2. Activate virtual environment
        
        ```python
        source <virtual_env_name>/bin/activate
        ```

    3. Install libraries `geopandas` 

        ```bash
        pip install geopandas
        ```

        **Required Libraries**

         * `shapely` - Geometry handling

        and install repository as a dependency:

        ```bash
        pip install git+https://github.com/r3card0/geom-to-shapefile.git@v0.1.0
        ```




# Basic Usage

1. Initialize the Class

    ```python
    from export_to_shp import Shp 

    import pandas as pd
    from shapely.geometry import Point

    # Create dummy data
    data = {
        'id': [1, 2, 3, 4, 5],
        'nombre': ['Punto A', 'Punto B', 'Punto C', 'Punto D', 'Punto E'],
        'valor': [100, 250, 175, 300, 425],
        'geometry': [
            Point(-99.133, 19.432),  # Ciudad de México
            Point(-99.150, 19.450),
            Point(-99.120, 19.410),
            Point(-99.140, 19.425),
            Point(-99.160, 19.440)
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Create instance (default CRS is EPSG:4326 - WGS84)
    five_points = Shp(df,"geometry","mex_five_points")
    ```
2. Export to shapefile

    ```python
    five_points.export_shp()
    ```
### Class Methods

|method|description|Returns|
|-|-|-|
|**is_geodataframe**|Evaluates if the object is a `GeoDataFrame`|Boolean: `False` or `True`|
|**build_geodataframe**|Converts a `DataFrame` to a `GeoDataFrame`|`GeoDataFrame` dataset|
|**export_shp**|Exports `GeoDataFrame` to a `Shapefile` format|`Shapefile` of `Point` geometry. Create a folder named `shapefiles` and exports the file into it|

# Contributing

For improvements or bug resports, please submit an issue or pull request to the repository

# Author

[r3card0](https://github.com/r3card0)

Last Update: Nov 2025
