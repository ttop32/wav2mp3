import os
import sys
os.environ['PATH'] += ";"+os.path.join(os.path.abspath("."), "ffmpeg/bin/")    
from pydub import AudioSegment
from glob import glob
from send2trash import send2trash
from tqdm import tqdm



#convert file and wav to trash
def convertFile(filePath):
    filename, file_extension = os.path.splitext(filePath)
    AudioSegment.from_file(filePath).export(filename+".mp3", format="mp3")
    send2trash(filePath)


if __name__ == '__main__':
    os.makedirs("input", exist_ok=True)
    fileList=glob("input/**/*.wav", recursive=True,)
    fileList = [f for f in fileList if os.path.isfile(f)]

    print(fileList)
    for i in tqdm(fileList):
        convertFile(i)

