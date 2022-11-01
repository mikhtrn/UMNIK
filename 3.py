from pydub import AudioSegment
import os

path = 'C:/Users/mikhail/Desktop/test3'
for dirs, folder, files in os.walk(path):
    print('Выбранный директория: ', dirs)
    print('Вложенные папки: ', folder)
    break
print("Размер:", len(folder))
for i in folder:
    wav_file = AudioSegment.from_file(file='C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav',
                                      format="wav")
    framerate = wav_file.frame_rate
    if framerate == 44100:
        sound = AudioSegment.from_file('C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav', format='wav', frame_rate=44100)
        sound = sound.set_frame_rate(8000)
        sound.export('C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav', format='wav')
    else:
        continue


for j in folder:
    print(j)
    filename = 'C:/Users/mikhail/Desktop/test3/' + i + '/' + i + '.wav'
    myaudio = AudioSegment.from_file(filename)
    print(myaudio.frame_rate)