# DWG to DXF to SVG Converter

A simple script to convert **DWG** files to **DXF** and then to **SVG** using **ODA File Converter** and **ezdxf**.

## 📋 Requirements

### 1. Install Required Python Packages

Ensure you have the following Python libraries installed:

pip install matplotlib ezdxf

### 2. Ensure ODA File Converter is Installed
Download ODA File Converter from Open Design Alliance.
Install it and configure the path to the executable.
https://www.opendesign.com/guestfiles/oda_file_converter

## 📁 Project Structure
Your workspace should be structured as follows:

Project-Name/
#### │-- dwg/   # Input folder: Place all .dwg files here
#### │-- dxf/   # Intermediate folder: Stores converted .dxf files
#### │-- svg/   # Output folder: Stores converted .svg files
#### │-- dwg_to_dxf_to_svg.py  # The main script

## 🚀 How to Use
### 1. Place your .dwg files inside the dwg/ folder.

### 2. Run the script:
python dwg_to_dxf_to_svg.py


### 3. The script will:
Convert .dwg files from the dwg/ folder to .dxf in the dxf/ folder.
Convert .dxf files to .svg and store them in the svg/ folder.

### 4. Retrieve your .svg files from the svg/ folder or .dxf files from the .dxf folder if that is what you want.

## 🛠 Configuration
If needed, modify the script to specify:

Custom input/output folders
ODA File Converter path
DXF and SVG conversion parameters

## ❗ Troubleshooting
If the script doesn't work, ensure:
ODA File Converter is installed and accessible.
You have the necessary permissions for reading/writing files.
Required Python packages are installed.

