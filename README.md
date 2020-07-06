# AugmentLabelIMG
A simple pythonscript to augment an annotated image dataset in JPG/XML Format as used by LabelIMG (https://github.com/tzutalin/labelImg).
The script will rotate the images 4 times and mirror the resulting images and the annotations making for an expansion by the factor of 8.


## Usage
0. Download the repository from the GitHub website and unzip it or directly clone it. 
`git clone https://github.com/BendiXB/AugmentLabelIMG.git`
1. Clear the `dataset/` and `output/` directories of example data and copy your dataset to `dataset/` for it to be processed by the program.
2. Run `diversify.py` in Python3. `sudo python3 augment.py`
3. Your dataset will now be augmented and saved to `output/`.

## Contributers
@ockapunktnet
@BendiXB
