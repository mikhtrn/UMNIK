from pydub import AudioSegment
import os

this_dir = os.getcwd()

for dirs, folder, files in os.walk(this_dir):
    print('Выбранный директория: ', dirs)
    print('Вложенные папки: ', folder)
    break
print("Размер:", len(folder))

this_dir += "/"

for i in folder:
    if os.path.exists(this_dir + i + '/' + i + '.XLSX'):
        old_file = os.path.join(this_dir + i, i + ".XLSX")
        new_file = os.path.join(this_dir + i, i + ".xlsx")
        os.rename(old_file, new_file)
    else:
        continue

print(this_dir)