import pytube
import os
import subprocess

yt = pytube.YouTube("https://www.youtube.com/watch?v=AeXo05Iull0")
videos = yt.streams.all()

for item in range(len(videos)) :
    print(item, ',  ', videos[item])

down_dir = "D:\psp"

cNum = int(input("다운 받을 화질은?? (0~21)"))

videos[cNum].download(down_dir)

newFileName = input("변환 할 파일명은??")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
                 os.path.join(down_dir, oriFileName),
                 os.path.join(down_dir, newFileName)
])

print("동영상 다운로드 및 mp3 변환 완료!!!")
