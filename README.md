# SR_tools
The project is for providing some scripts and examples of tools for processing images in the field of SR.
It contains:  
- [extract_rect](https://github.com/chxy95/SR_tools#extract_rect)
## Extract_rect
The script *extract_rect.py* is for extracting ROI from a group of images.  
### Usage
Put the images for operation in the folder of *testset* and name them with the correct format as the example in the script.  
Run the script:  
```
python extract_rect.py
```
Click and drag the mouse for selecting the rectangle ROI, and press the ESC to end the process.
### Results
For an image *HR_test.png*, three images will be generated for your utilizing in the folder *asserts*.  
For example:  
<img src="https://raw.githubusercontent.com/chxy95/SR_tools/master/asserts/example.png" width="1000"/>  
More examples can be found in folders of *testset* and *asserts*.
