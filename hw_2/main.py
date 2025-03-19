from super_latex_tools.latex_tools import generate_latex_table, generate_latex_image
from pdflatex import PDFLaTeX
import os

table_data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 22, "Chicago"],
    ["David", 28, "San Francisco"],
    ["Eve", 35, "Houston"],
]

print(os.listdir())
IMAGE_PATH = "/Users/cormeum/Desktop/ai talent hub/advanced-python-itmo/hw_2/data/latex_image.png" # absolute path to image
table_code = generate_latex_table(table_data)
image_code = generate_latex_image(IMAGE_PATH, caption="my image")

output_file = "output/generated_table_and_image.tex"
with open(output_file, "w") as file:
    file.write(f'''
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{table_code}\n\n{image_code}
\\end{{document}}
''')