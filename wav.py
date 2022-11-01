from pydub import AudioSegment
import os

path = 'C:/Users/mikhail/Desktop/test3'
for dirs, folder, files in os.walk(path):
    print('Выбранный директория: ', dirs)
    print('Вложенные папки: ', folder)
    break
print("Размер:", len(folder))
for i in folder:
    if os.path.exists('C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.mp3'):
        sound = AudioSegment.from_mp3('C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.mp3')
        sound.export('C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav', format='wav')

        sound = AudioSegment.from_file('C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav', format='wav', frame_rate=44100, channels=2)
        sound = sound.set_frame_rate(8000).set_channels(1)
        sound.export('C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav', format='wav')

        print(i)
    else:
        continue


for j in folder:
    print(j)
    filename = 'C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav'
    myaudio = AudioSegment.from_file(filename)
    print(myaudio.frame_rate)
