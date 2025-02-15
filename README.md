# JSON to Table Image Converter

This project converts JSON data into a structured table format and saves it as an image.

## Features
- Converts JSON data into a table
- Saves the table as an image (PNG, JPG, etc.)
- Customizable table styling (colors, fonts, etc.)

## Requirements
Make sure you have the following dependencies installed:

```bash
pip install pandas pillow
```

## Usage
1. Prepare a JSON file (e.g., `data.json`) with the following structure:

```json
[
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 28, "City": "Chicago"}
]
```

2. Run the script to generate an image:

```bash
python convert.py
```

3. The generated table image will be saved as `output.png` in the project folder.

## Example Output
![Table Image Example](output.png)

## Customization
- Modify font size, colors, and table styles inside the script.
- Change the output format (PNG, JPG) by modifying the saving function.

## License
This project is open-source and available under the MIT license.

