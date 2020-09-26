# AugmentLabelIMG 
[![HitCount](http://hits.dwyl.com/BendiXB/AugmentLabelIMG.svg)](http://hits.dwyl.com/BendiXB/AugmentLabelIMG)

A simple pythonscript to augment an annotated image dataset in JPG/XML Format as used by LabelIMG (https://github.com/tzutalin/labelImg).
The script will rotate the images 4 times and mirror the resulting images and the annotations making for an expansion by the factor of 8.

## Usage
0. Download the repository from the GitHub website and unzip it or directly clone it. 
`git clone https://github.com/BendiXB/AugmentLabelIMG.git`
1. Clear the `dataset/` and `output/` directories of example data and copy your dataset to `dataset/` for it to be processed by the program.
2. Run `augment.py` in Python3. `sudo python3 augment.py`
3. Your dataset will now be augmented and saved to `output/`.

## Example
|rotation |not mirrored                      |mirrored                                            |
|---------|----------------------------------|----------------------------------------------------|
|0°       |![0°](/output/IMG_6166-0.JPG)     |![0° mirrored](/output/IMG_6166-0-mirrored.JPG)     |
|90°      |![90°](/output/IMG_6166-90.JPG)   |![90° mirrored](/output/IMG_6166-90-mirrored.JPG)   |
|180°     |![180°](/output/IMG_6166-180.JPG) |![180° mirrored](/output/IMG_6166-180-mirrored.JPG) |
|270°     |![270°](/output/IMG_6166-270.JPG) |![270° mirrored](/output/IMG_6166-270-mirrored.JPG) |

## Contributers
@ockapunktnet
@BendiXB
