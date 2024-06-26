import rasterio
import geopandas as gpd
from shapely.geometry import box
from fiona.crs import from_epsg

def get_sar_image_bounds(sar_image_path):
    """
    Get the bounds of the SAR image.

    Parameters:
    sar_image_path (str): The file path to the SAR image.

    Returns:
    tuple: The bounds of the SAR image (left, bottom, right, top).
    """
    with rasterio.open(sar_image_path) as src:
        return src.bounds

def clip_shapefile_to_image_extent(input_data, bounds, crs):
    """
    Clip the shapefile to the extent of the SAR image.

    Parameters:
    input_data (GeoDataFrame): The input shapefile data.
    bounds (tuple): The bounds to clip to (left, bottom, right, top).
    crs (CRS): The coordinate reference system to use.

    Returns:
    GeoDataFrame: The clipped shapefile data.
    """
    left, bottom, right, top = bounds
    clip_extent = gpd.GeoDataFrame(geometry=[box(left, bottom, right, top)], crs=crs)
    return gpd.overlay(input_data, clip_extent, how='intersection')

def save_shapefile(data, output_file_path):
    """
    Save the clipped shapefile data to a file.

    Parameters:
    data (GeoDataFrame): The clipped shapefile data.
    output_file_path (str): The file path to save the data.
    """
    data.to_file(output_file_path, driver='ESRI Shapefile')

def process_image(i, input_data):
    """
    Process a single SAR image and clip the shapefile to its extent.

    Parameters:
    i (int): The index of the image.
    input_data (GeoDataFrame): The input shapefile data.
    """
    sar_image_path = f'ur/{i}.tiff'
    output_file_path = f'ur/shpfiles1/{i}.shp'

    bounds = get_sar_image_bounds(sar_image_path)
    clipped_data = clip_shapefile_to_image_extent(input_data, bounds, from_epsg(4326))
    save_shapefile(clipped_data, output_file_path)
    print(f'Processed image {i}')

def main():
    """
    Main function to process multiple SAR images.
    """
    input_file_path = 'land-polygons-split-4326/land-polygons-split-4326/land_polygons.shp'
    input_data = gpd.read_file(input_file_path)
    for i in range(1, 168):
        process_image(i, input_data)

if __name__ == "__main__":
    main()
