# 8Bitify
A python program to deconstruct any audio .wav file, then discretize the contents into an 8bit resolution.

Type "python3 main.py -h" to access the help menu for the program.

The project has expanded to an experimentation CLI where the user operates on audio data and plots / plays / saves the results. Future work would range to various new experiments / signal processing techniques.

## dependancies
- numpy (operate on raw audio data via linear algebra etc.)
  * http://www.numpy.org/ (python3 -m pip install numpy)
- sounddevice (audio playback) (needs new library option for python3 support)
  * https://pypi.python.org/pypi/sounddevice/
- scipy (generate various wave forms for operations etc.)
  * https://www.scipy.org/install.html
- pysoundfile (deconstruct / reconstruct various audio file types)
  * http://pysoundfile.readthedocs.io/en/0.9.0/
- argparse (aid in POSIX style CLI interface)
  * https://docs.python.org/3/howto/argparse.html
- matplotlib (visualize experiments)
  * https://matplotlib.org/

## installation
*Note: assumes a linux installation, for other instructions please see all dependancies' web pages as appropriate*
- sudo apt-get install python3 python3-pip python3-numpy python3-cffi python3-matplotlib libsndfile1
- sudo python3 -m pip install pysoundfile sounddevice
