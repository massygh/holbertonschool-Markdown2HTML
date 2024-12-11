#!/usr/bin/env python3

import sys
import os

# Check if the number of arguments is less than 3 (script name + 2 arguments)
if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

# Assign command-line arguments to variables
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the markdown file exists
if not os.path.isfile(markdown_file):
    sys.stderr.write(f"Missing {markdown_file}\n")
    sys.exit(1)

# If requirements are met, proceed to convert Markdown to HTML
try:
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    # A simple replacement approach for converting markdown to HTML
    html_content = markdown_content.replace("\n", "<br>")  # Convert newlines to <br>

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    sys.exit(0)
except Exception as e:
    sys.stderr.write(str(e) + "\n")
    sys.exit(1)