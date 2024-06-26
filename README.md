# SAR Image Processing

## Description
This project contains two scripts for processing SAR images:

1. **clipVectorByExtent.py**: Clips a vector shapefile of land polygons to the extent of a SAR image.
2. **createTruthMask.py**: Creates a binary land-water mask from a SAR image and a shapefile.

## Installation
To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheRodzz/sar-image-annotation.git
   cd sar-image-annotation
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
python clipVectorByExtent.py
```

You will need to update the file paths and the main loop according to your needs

### Create Binary Land-Water Mask
This script creates a binary land-water mask from a SAR image and a (clipped) shapefile.

**Run the script**:
```bash
python createTruthMask.py
```
You will need to update the file paths and the main loop according to your needs

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
