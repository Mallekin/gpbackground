# create a desktop background using samples from a Gaussian Process prior 

usage: gpbackground.py [-h] [-r RESOLUTION] [-b BACKGROUND] [-s SAMPLESIZE]
                       [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -r RESOLUTION, --resolution RESOLUTION
                        background resoltion; default 1024x768
  -b BACKGROUND, --background BACKGROUND
                        plot background color; default #152233, use \# in your shell
  -s SAMPLESIZE, --samplesize SAMPLESIZE
                        number of samples to draw from prior; default 7
  -o OUTPUT, --output OUTPUT
                        output file path, name and type (png, pdf, ps, eps and svg); default displays plot
