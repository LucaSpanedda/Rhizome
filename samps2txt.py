# librerie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import argparse

# Print the sample rate and length of the audio file in seconds
print('''
This code take as arguments the .wav and export the sample values in a .txt
''')

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("audiofilein", help="Name of the audio file with the extension")
args = parser.parse_args()

# leggiamo il file audio e ne stampiamo la durata
[fs, x] = read(args.audiofilein)
print("SR: ",fs,"\ndimensione del file audio in campioni: ", np.size(x))

# normalizziamo il file audio(a 0 dB)
# dividendo il file per l'assoluto del suo massimo
x = x/np.max(abs(x))

# salva file audio su testo
np.savetxt((args.audiofilein)+".txt", x, fmt='%1.8f')