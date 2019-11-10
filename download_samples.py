from pytube import Playlist
import os
import ffmpeg

def makedirs(path):
    try:
        os.makedirs(path)
    except OSError as e:
        print(e)

def download_playlist(url, download_path):
    try:
        pl = Playlist(url)

        output = download_path + '/' + pl.title().lower()
        makedirs(output)

        pl.download_all(os.path.abspath(output))

    except Exception as e:
        print('Error downloading playlist.', e)

def change_format(format, path):
    try:
        output = os.path.splitext(os.path.basename(path))[0] + '.' + format
        output = os.path.dirname(path) + '/' + output

        audio = ffmpeg.input(path).audio
        audio = ffmpeg.output(audio, output)
        ffmpeg.run(audio)

        os.remove(path)
    except Exception as e:
        print('Error changing format.', e)

def change_format_recursive(format, path):
    path = os.path.abspath(path)

    if os.path.isdir(path):
        for file in os.listdir(path):
            change_format_recursive(format, path + '/' + file)
    else:
        change_format(format, path)

def main():
    playlists = []
    try:
        with open('./playlists') as file:
            playlists = file.readlines()
    except IOError as e:
        print(e)
        exit(1)

    for url in playlists:
        download_playlist(url, 'samples')

    change_format_recursive('wav', 'samples')

if __name__ == '__main__':
    main()
