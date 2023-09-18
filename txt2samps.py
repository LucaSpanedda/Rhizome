# librerie
# based on : www.daniweb.com/code/snippet263775.html
import math
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import argparse

# Print the sample rate and length of the audio file in seconds
print('''
This code take as arguments the .txt and export the sample values in a .wav
''')

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("txtfilein", help="Name of the samples file with the extension")
args = parser.parse_args()

# Audio will contain a long list of samples (i.e. floating point numbers describing the
# waveform). If you were working with a very long sound you'd want to stream this to
# disk instead of buffering it all in memory list this. But most sounds will fit in
# memory.
# name output
audio = np.loadtxt(args.txtfilein)
sample_rate = 44100.0

def save_wav(file_name):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1

    sampwidth = 2

    # 44100 is the industry standard sample rate - CD quality. If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the
    # sample size. So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer. NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return

save_wav((args.txtfilein)+".wav")