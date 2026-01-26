# Geometry datasets to shapefile format

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GeoPandas](https://img.shields.io/badge/GeoPandas-3CB371?style=for-the-badge&logo=python&logoColor=white)

This repository provides a Python 🐍 utility for exporting datasets to Shapefile format. It supports both `pandas DataFrames` and `GeoPandas GeoDataFrames`, allowing seamless handling of spatial and no-spatial data.


## 🧭 Overview
The tool is designed to work with all geometries types: `Point`, `LineString` and `Polygon`, and ensuring compatibility with common GIS workflows. It includes functions for validating geometries, transforming coordinate reference systems when needed, and exporting clean, ready-to-use Shapefiles for further analysis in GIS platforms such as QGIS and ArcGIS.

## ⚙️ Installation
**Prerequisites**
- Python > 3.10

> You can use this repository in two different ways: Clone the repository or install as a dependency

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

    3. 📦 Install repository as a dependency:

        ```bash
        pip install git+https://github.com/r3card0/geom-to-shapefile.git@v0.2.0
        ```

        The following libraries will be installed:

        ```bash
        certifi==2026.1.4
        export-to-shp @ git+https://github.com/r3card0/geom-to-shapefile.git@cde51dcf63f4b1b7dbd9e39cf4a8baecedc1fec9
        geopandas==1.1.2
        numpy==2.2.6
        packaging==25.0
        pandas==2.3.3
        pyogrio==0.12.1
        pyproj==3.7.1
        python-dateutil==2.9.0.post0
        pytz==2025.2
        shapely==2.1.2
        six==1.17.0
        tzdata==2025.3
        ```


# Versions
|Version|Description|
|-|-|
|v0.1.0|Initial Version - Handle `Point` Geometry|
|v0.2.0|Handle `Any` type Geometry|

# 🚗 Usage
**Basic Example in a Notebook**

When the repository was cloned

```python
import sys
from pathlib import Path

# Get root folder
project_root = Path.cwd().parent
sys.path.insert(0, str(project_root))

# Initialize the class
from src.export_to_shp import Shp

# Create dummy data
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Point A', 'Point B', 'Point C', 'Point D', 'Point E'],
    'value': [100, 250, 175, 300, 425],
    'geometry': [
            Point(-99.133, 19.432),  # México City
            Point(-99.150, 19.450),
            Point(-99.120, 19.410),
            Point(-99.140, 19.425),
            Point(-99.160, 19.440)
            ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create instance: Setting filename and EPSG is required 
five_points = Shp(df,"geometry","mex_five_points","EPSG:4326")
```
1. Export to shapefile

```python
five_points.export_shp()
```

**Input Validation**

Thisproject peformes **early validation** of required input attributes to ensure data consistency and to avoid ambiguous spatial operations.

**`filename`**
* Type:`str`
* Required: Yes

The `filename` attribute, represents the name of the input or output file used by the process.

Validation rules:

* The attribute must be provided.
* If `filename` is `None`, empty, or missing, the process will fall immediately.

Rationale:
> A valid filename is required for reading, writing or tracking outputs.
> Failing early prevents silent errors and incomplete executions.

Example error:
```bash
ValueError: ⚠️ The filename is required and cannot be empty
```

**`crs` (Coordinate Reference System)**

* Type:`str`
* Required: Yes
* Expected format: EPSG code(e.g. `EPSG:4326`)

The `crs` attribute explicity defines the Coordinate Reference System of the input geometry.

Validation Rules:

* The CRS must be explicity provided.
* A valid CRS string is required (for example: `EPSG:4326`)
* If `crs` is `None` or invalid, the process will fail
* Only geographic coordinate systems (longitude/latitude in degrees or decimals) are accepted

Rationale:

> Spatial operations as distance calculations, reprojections, or clustering require a known and explicit CRS.

Example Error:

```bash
ValueError: CRS is required (expected a geographic CRS such as EPGS:4326)
```

**Design Principle**

This project follows a fail-fast approach:
* Invalid or missing inputs are rejected immediately.
* Errors are raised at object initialization rather than during processing.
* This ensures predictable behavior and easier debugging.

### Class Methods

|method|description|Returns|
|-|-|-|
|**is_geodataframe**|Evaluate if the object is a `GeoDataFrame`|Boolean: `False` or `True`|
|**build_geodataframe**|Convert a `DataFrame` to a `GeoDataFrame`|`GeoDataFrame` dataset|
|**export_shp**|Export `GeoDataFrame` to a `Shapefile` format|`Shapefile` of `Point`, `LineString`, `Polygon` geometry. Create a folder named `shapefiles` and exports the file into it|

# Contributing

For improvements or bug resports, please submit an issue or pull request to the repository

## 🔗 References
**Geopandas**
* [Geopandas - Documentation](https://geopandas.org/en/stable/)

**Shapely**
* [Shapely - Documentation](https://shapely.readthedocs.io/en/stable/)
* [Shapely - Geometry Types](https://shapely.readthedocs.io/en/stable/geometry.html#geometry-types)
* [Shapely - wkt.loads](https://shapely.readthedocs.io/en/stable/manual.html#shapely.wkt.loads)
* [Shapely - BaseGeometry](https://github.com/shapely/shapely/blob/main/shapely/geometry/base.py)

**Python**

* [isinstance() - Documentation](https://docs.python.org/3/library/functions.html#isinstance)
* [Built-in Exception](https://docs.python.org/3/library/functions.html#isinstance)
* [raise exception](https://www.w3schools.com/python/gloss_python_raise.asp)
* [os - Documentation](https://docs.python.org/3/library/os.html)

**Pandas**
* [Pandas - apply()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)



# 👤 Author

* GitHub: [r3card0](https://github.com/r3card0)
* LinkedIn: [Ricardo](https://www.linkedin.com/in/ricardordzsaldivar/)

Update: Jan 2026
