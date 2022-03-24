import os
import codecs
import shutil

fileObj = codecs.open( "names.txt", "r", "utf_8_sig")
name = fileObj.read().split('\r\n')
fileObj.close()

if os.path.exists('telegi'):
    pass
else:
    os.mkdir('telegi')

for n in name:
    if os.path.exists(f'telegi/{n}'):
        pass
    else:
        os.mkdir(f'telegi/{n}')

for n in name:
    shutil.copy('Telegram.exe', f'telegi/{n}')
