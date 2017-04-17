#!/usr/bin/python3
### matrix_ops.py
#
#   Description: functions included allow for various audio file operations 
#       (i.e. eight_bitify, superimpose_square) 
#
#   Requires: numpy
#       (sudo apt-get install python3-numpy)
#
#   Tests available: python3 -m doctest matrix_ops.py
#
###

import numpy as np      # matrix ops via numpy: audio data of shape (num_data, num_channels)

# global vars for convenience / testing
audioFileDir = "../Test Files/"
testOrchFile = "383929__oymaldonado__uplifting-orchestra.wav"
testGuitarFile = "ThuMar2302_40_45UTC2017.wav"
testWavFileOut = "testWavOut.wav"

def eight_bitify(data):
	""" takes numpy matrix of audio data, returns modded numpy data

	>>> t = np.array([1, 2, -5, 4, 5, 6, 120, 355, -500])
	>>> t
	array([   1,    2,   -5,    4,    5,    6,  120,  355, -500])
	>>> t.shape
	(9,)
	>>> result = eight_bitify(t)
	>>> result.shape
	(9,)
	>>> result
	array([   1,    2,   -5,    4,    5,    6,  120,  355, -500])

	"""
	moddedData = np.array(data)

	# do 8bit rectification here...
	# probably will use np.where, or maybe use a lambda function, math function, or a cast

	return moddedData