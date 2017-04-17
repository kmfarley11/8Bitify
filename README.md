# 8Bitify
A python program to deconstruct any audio .wav file, then discretize the contents into an 8bit resolution.

The idea could potentially expand depending on results of development and experiments.

## dependancies
- numpy (operate on raw audio data via linear algebra etc.)
  * http://www.numpy.org/ (python3 -m pip install numpy)
- ~~snack~~ (audio playback) (needs new library option for python3 support)
- pysoundfile (deconstruct / reconstruct various audio file types)
  * http://pysoundfile.readthedocs.io/en/0.9.0/

## potential dependancies
- matplotlib (visualize experiments)
  * https://matplotlib.org/

## installation
*Note: assumes a linux installation, for other instructions please see all dependancies' web pages as appropriate*
- sudo apt-get install python3 python3-pip python3-numpy python3-cffi libsndfile1
- sudo python3 -m pip install pysoundfile
