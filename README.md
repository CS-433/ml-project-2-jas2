# ML4Science project - Patent digitization
The aim of this project is to explore digitization solutions for patents.
## Scope
The corpus we are working with is a corpus of X US and UK patents from YYYY to YYYY. This corpus is a sample of a larger corpus of patents sharing the same caracteristics.
Those patents are in pdf files or in a collection of tif files. In the current state, they are not machine-readable. The goal of this project is to explore possible solutions to make them machine-readable.
## File structure
The UK patents are in PDF format which contain TIF files (content in stream
objects, format in "filter" header: CCITTFaxDecode).
The US patents are in TIF files and an XML.
## Run the project
### Folder tree
- Raw data was stored in *data/sample_1850_to_1859*
- Digitized data in *data/digitized_raw*
- Cleaned data in *data/sample_clean*
- Digitized clean data in *data/digitized_clean*
- Splited data was stored in *data/split* ; the split() functions was used to split cleaned data thus paths are hardcoded accordingly.

One of our last experiment used a ground truth. In folder *ground-truth/* we have :
- *di_raw* for digitized data
- *di_clean* for digitized clean data
- *ground_truth* for manually digitized images
In the same folder we have a main.py outputing a results.txt file.

__Functions assume this architeture.__

### Executable
All functions are called from main and are commented according to the needs of the moment.
