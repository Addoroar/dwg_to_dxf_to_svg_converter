import os
import subprocess
import sys

# Function to install a package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["matplotlib", "ezdxf","os","subprocess","sys"]

# Check and install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Package {package} not found. Installing...")
        install_package(package)

# Check if ODAFileConverter is installed
ODA_CONVERTER_PATH = r"C:/Program Files/ODA/ODAFileConverter 25.12.0/ODAFileConverter.exe"
if not os.path.exists(ODA_CONVERTER_PATH):
    print("ODAFileConverter not found. Please download and install it from https://www.opendesign.com/guestfiles/oda_file_converter")

# Correctly quoted ODA File Converter path
ODA_CONVERTER = f'"{ODA_CONVERTER_PATH}"'

import matplotlib.pyplot as plt
import ezdxf 
from ezdxf.addons.drawing import RenderContext, Frontend 
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend

def convert_dwg_to_dxf(input_folder, output_folder, input_file_type, output_file_type, recursive_flag, audit_flag):
    command = f'{ODA_CONVERTER} "{input_folder}" "{output_folder}" {input_file_type} {output_file_type} {recursive_flag} {audit_flag}'
    print(f"Running ODA Command: {command}")  # Debugging
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"ODA Error: {result.stderr.decode()}")
        return None
    return 0

def convert_dxf_to_svg(input_folder, output_folder):
    # Process all DXF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".dxf"):
            dxf_path = os.path.join(input_folder, filename)
            svg_filename = os.path.splitext(filename)[0] + ".svg"
            svg_path = os.path.join(output_folder, svg_filename)
            try:
                # Read DXF file
                doc = ezdxf.readfile(dxf_path)
                
                # Create a figure and render the DXF content
                fig = plt.figure()
                out = MatplotlibBackend(fig.add_axes([0, 0, 1, 1]))
                ezdxf.addons.drawing.properties.MODEL_SPACE_BG_COLOR = "#FFFFFF"
                Frontend(RenderContext(doc), out).draw_layout(doc.modelspace(), finalize=True)
                
                # Save the output as an SVG file
                fig.savefig(svg_path)
                print(f"Converted: {filename} -> {svg_filename}")
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")
            
    return 0    

# Define input and output directories
input_folder = r"./dwg"
output_folder = r"./dxf"

#ODA Parameters
input_file_type = "ACAD2018"
output_file_type = "DXF"
recursive_flag = 0
audit_flag = 1

convert_dwg_to_dxf(input_folder, output_folder, input_file_type, output_file_type, recursive_flag, audit_flag)

# Define input and output directories
input_folder = "./dxf"
output_folder = "./svg"

convert_dxf_to_svg(input_folder, output_folder)