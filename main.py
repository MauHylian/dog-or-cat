from pytube import YouTube
import subprocess
import sys
import os
import librosa
import librosa.feature
import librosa.display
import glob
import numpy as np
import matplotlib.pyplot as plt

# Descargar video
search = input("Introduce el enlace del video: ")
yt = YouTube(str(search))
title = yt.title
TITLE = title.replace(" ", "_")
print(title)
t = yt.streams.filter(only_audio=True).all()
print(t)
t[0].download()

# Convertir a .wav
def convert_video(video_input, video_output):
	cmds = ['ffmpeg', '-i', video_input, video_output]
	subprocess.Popen(cmds)

convert_video(title + '.mp4', TITLE + '.wav')

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

def isdir(dir):
    return os.path.isdir(dir)

def save_mfcc_recursive(path):
    files = os.listdir(path)
    for file in files:
        absolute_path = path + '/' + file
        if isdir(absolute_path):
            save_mfcc_recursive(absolute_path)
        elif file.endswith('.wav'):
            save_mfcc(absolute_path)

save_mfcc_recursive('./samples')
# save_mfcc('path/to/song.wav') # .wav file path

# https://www.youtube.com/watch?v=IwqylziCavQ