import os

import geopandas as gpd
from shapely import wkt

# from shapely.geometry import Point
from shapely.geometry.base import BaseGeometry

class Shp:
    def __init__(self, dataset:object,geometry_column_name:str,filename:str|None=None,crs:str|None=None):
        """
        Export gpd.GeoDataFrame to shapefile format

        Parameters:
        -----------
        
        dataset: gpd.GeoDataFrame or pd.DataFrame
            Any object like gpd.GeoDataFrame or pd.DataFrame
        geometry_column_name: str
            name of the column that stores the geometry
        filename: str 
            The name you chose when shapefile is created
        crs: str 
            Coordinate Reference System

        Returns: Shapefile format dataset
        """
        self.dataset = dataset
        self.geometry_column_name = geometry_column_name
        if not filename.strip():
            raise ValueError("⚠️ The filename is required and cannot be empty")
        self.filename = filename
        if crs is None:
            raise ValueError("⚠️ CRS is required. e.g: 'EPSG:4326' ")
        self.crs = crs 
    
    

    # Evaluates if the dataset is a GeoDataFrame
    def is_geodataframe(self):
        return isinstance(self.dataset,gpd.GeoDataFrame)
    
    def build_geodataframe(self):
        # Evaluates if the geometry column is already a shapely object
        def safe_wkt_load(x):
            if isinstance(x,str):
                return wkt.loads(x)
            elif isinstance(x,BaseGeometry):
                return x
            else:
                raise TypeError(f"Data type not recognized: {type(x)}")
            
        if self.is_geodataframe() == False:
            # Convert to a geometry
            df_copy = self.dataset.copy()

            # Evaluate if dataset contains a column named: "geometry"
            cols_list = list(df_copy.columns)
            
            if cols_list.count("geometry"):
                # create a GeoDataFrame
                gdf = gpd.GeoDataFrame(df_copy,geometry="geometry", crs=self.crs)
            else:
                df_copy["geometry"] = df_copy[self.geometry_column_name].apply(safe_wkt_load)
                
                # Create a GeoDataFrame
                gdf = gpd.GeoDataFrame(df_copy,geometry="geometry", crs=self.crs)

                # Remove the geometry column name to avoid duplicated geometries
                gdf = gdf.drop(columns=[self.geometry_column_name])

            return gdf

        else:
            return self.dataset
        
    def export_shp(self):
        gdf = self.build_geodataframe()

        folder = "shapefiles"
        try:
            if not os.path.exists(folder):
                os.makedirs(folder)
                print(f"The folder '{folder}' was successfully created.")
            else:
                print(f"The folder '{folder}' is already existed.")

            shp_path = os.path.join(folder,f"{self.filename}.shp")

            print(f"The shapefile creation process is starting {self.filename} ...")

            gdf.to_file(shp_path)

            print(f"Shapefile '{self.filename}' successfully created \nEnd of the process")
        except Exception as e:
            print(f"Error in the shapefile export process: {e}")

