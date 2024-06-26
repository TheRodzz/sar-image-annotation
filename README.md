Sure! Here is the complete `README.md` file that includes detailed descriptions, installation instructions, usage guidelines for both scripts, contribution guidelines, and license information.

### README.md

```markdown
# SAR Image Processing

## Description
This project contains two scripts for processing SAR images:

1. **clip_shapefile.py**: Clips a vector shapefile of land polygons to the extent of a SAR image.
2. **create_binary_mask.py**: Creates a binary land-water mask from a SAR image and a shapefile.

## Installation
To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```
2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Clip Shapefile to SAR Image Extent
This script clips a vector shapefile of land polygons to the extent of a SAR image.

**Run the script**:
```bash
python clip_shapefile.py
```

You will be prompted to enter:
- The path to the SAR image file.
- The path to the input shapefile.
- The path to save the clipped shapefile.

Example usage:
```
Enter the path to the SAR image file: ur/1.tiff
Enter the path to the input shapefile: land-polygons-split-4326/land_polygons.shp
Enter the path to save the clipped shapefile: ur/shpfiles1/1.shp
```

### Create Binary Land-Water Mask
This script creates a binary land-water mask from a SAR image and a shapefile.

**Run the script**:
```bash
python create_binary_mask.py
```

You will be prompted to enter:
- The path to the SAR image file.
- The path to the input shapefile.
- The path to save the binary mask image.

Example usage:
```
Enter the path to the SAR image file: ur/1.tiff
Enter the path to the input shapefile: ur/shpfiles1/1.shp
Enter the path to save the binary mask image: ur/masks/1_mask.tiff
```

## Contributing
We welcome contributions to improve these scripts and add new features. To contribute, follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature-branch
   ```
5. **Open a pull request**.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Summary
- **Description**: Provides a brief overview of the project and its scripts.
- **Installation**: Instructions to clone the repository and install dependencies.
- **Usage**: Detailed steps to run each script with example prompts.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Information about the project's license.

This README should give users a clear understanding of how to set up and use the scripts, as well as how to contribute to the project. If you have any additional information you'd like to include, feel free to let me know!