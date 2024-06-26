import rasterio
from rasterio.features import geometry_mask
import geopandas as gpd

def create_binary_image(sar_image_path, shapefile_path, output_image_path):
    """
    Create a binary land-water mask from a SAR image and a shapefile.

    Parameters:
    sar_image_path (str): The file path to the SAR image.
    shapefile_path (str): The file path to the shapefile.
    output_image_path (str): The file path to save the binary mask image.
    """
    # Read SAR image
    with rasterio.open(sar_image_path) as src:
        sar_data = src.read(1)
        transform = src.transform
        profile = src.profile

    # Read shapefile
    gdf = gpd.read_file(shapefile_path)
    mask = geometry_mask(gdf.geometry, out_shape=sar_data.shape, transform=transform, invert=True)

    # Create a new image with the same dimensions as the SAR image
    binary_image = mask.astype('uint8') * 255

    # Update the profile for the output image
    profile.update(count=1, dtype='uint8')

    # Write the new image
    with rasterio.open(output_image_path, 'w', **profile) as dst:
        dst.write(binary_image, 1)

    print(f'Processed image {sar_image_path}')

if __name__ == "__main__":
    for i in range(1,168):
        sar_image_path = f"ur\{i}.tiff"
        shapefile_path = f"ur\shpfiles\{i}.shp"
        output_image_path = f"ur\masks\{i}_mask.tiff"

        create_binary_image(sar_image_path, shapefile_path, output_image_path)
        print(f'processed image {i}')
