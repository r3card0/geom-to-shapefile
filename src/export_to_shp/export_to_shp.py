import os

import geopandas as gpd
from shapely import wkt
from shapely.geometry import Point

class Shp:
    def __init__(self, dataset:object,geometry_column_name:str,filename:str,crs=None):
        """
        Parameters:
        -----------
        
        dataset: means any object like GeoDataFrame or GeoDataFrame
        geometry_column_name : name of the column that stores the geometry
        filename: the name you chose when shapefile is created
        crs: Coordinate Reference System, by default EPSG:4326
        """
        self.dataset = dataset
        self.geometry_column_name = geometry_column_name
        self.filename = filename
        self.crs = crs if crs is not None else "EPSG:4326"
    
    

    # Evaluates if the dataset is a GeoDataFrame
    def is_geodataframe(self):
        return isinstance(self.dataset,gpd.GeoDataFrame)
    
    def build_geodataframe(self):
        # Evaluates if the geometry column is already a shapely object
        def safe_wkt_load(x):
            if isinstance(x,str):
                return wkt.loads(x)
            elif isinstance(x,Point):
                return x
            else:
                raise TypeError(f"Data type not recognized: {type(x)}")
            
        if self.is_geodataframe() == False:
            # Convert to a geometry
            df_copy = self.dataset.copy()
            df_copy["geometry_c"] = df_copy[self.geometry_column_name].apply(safe_wkt_load)

            # Create a GeoDataFrame
            gdf = gpd.GeoDataFrame(df_copy,geometry="geometry_c", crs=self.crs)
            
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

            print(f"Shapefile '{self.filename}' successfully created \n End of the process")
        except Exception as e:
            print(f"Error in the shapefile export process: {e}")

