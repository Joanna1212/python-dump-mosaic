# python-dump-mosaic
-----
This is an interesting python project.
It can help you to reconstruct your favourite image with many small images which has similiar color. It look like mosaic style.

---
## Environment
* python 3.6
* scipy
* matplotlib
* pickle
* numpy

## Instruction
You should save an image "input.jpg" under current directory.

* python process.py
It can help you to save the vectors of each images the file ".\\assets\\thumb". These images are material of your mosaic.

* python dump.py
It can dump your mosaic-style-picture saved as "output.jpg" under current directory. Each mosaic grid is in size of 20*20.

The effect of our project can be seen as follow:
![output example](https://github.com/Joanna1212/python-dump-mosaic/blob/master/output.jpg)