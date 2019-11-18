###
# Este script genera los espectogramas MFCC
# de archivos .wav en el directorio actual
# donde se corra este archivo y los guarda
# como imagen.
###

import librosa
import librosa.feature
import librosa.display
import sys
import os
import matplotlib.pyplot as plt

print("Corre este script en el directorio donde están tus archivos WAV.")
print("")

directory = os.getcwd()

# Generar MFCC
def save_mfcc(song):
	y, _ = librosa.load(song) # song directory
	mfcc = librosa.feature.mfcc(y)

	plt.figure(figsize = (10, 4))
	librosa.display.specshow(mfcc, x_axis = 'time', y_axis = 'mel') # spectrogram show
	plt.colorbar()
	plt.title(TITLE)
	plt.tight_layout()
	plt.savefig(TITLE + '.png') # CHANGE THE NAME OF THE OUTPUT FILE

for filename in os.listdir(directory):
	if filename.endswith(".wav"): 
		# print(os.path.join(directory, filename))
		TITLE = filename
		song_path = os.path.join(directory, filename)
		save_mfcc(song_path)
		continue
	else:
		continue