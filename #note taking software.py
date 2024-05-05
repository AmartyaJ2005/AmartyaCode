#note taking software 
import os
import whisper
import time as time
import pyautogui as pt
import subprocess 
from pydub import AudioSegment
import shutil
import csv


model = whisper.load_model("medium")
recordings = "Library/Application Support/com.apple.voicememos/Recordings"
folder = "Amartyag"
destination = "Transcripts"
backup = "Backup"
recs = os.listdir(recordings)
for i in recs:
    if (".m4a" in i ):
        shutil.move(os.path.join(recordings, i), os.path.join(folder, i))
        shutil.copyfile(os.path.join(recordings, i), os.path.join(backup, i))
files = os.listdir(folder)
files = [os.path.join(folder, f) for f in files] # add path to each file
for f in files:
    os.rename(f,f.replace("m4a","wav"))
files = os.listdir(folder)
files = [os.path.join(folder, f) for f in files] # add path to each filenformation is
for i in files:
    t = 10 * 60 * 1000
    if ".wav" not in i:
        continue
    t1 = 0 #Works in milliseconds
    t2 = t
    print(i)
    try:
        newAudio = AudioSegment.from_wav(i)
    except:
        newAudio = AudioSegment.from_file(i, format="mp4")
    print(len(newAudio))
    for j in range(int(len(newAudio)/t)):
        newAudio1 = newAudio[t1:t2]
        newAudio1.export(i.replace(".wav", str(j)) + ".wav", format="wav")
        t1 += t
        t2 += t

files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
for i in files:
    if not ".wav" in i:
        continue
    result = model.transcribe(i)
    with open(os.path.join(destination, i[len(folder)+1:(len(i)-3)]+"txt"), "w") as f:
        f.write(result["text"])
    print(result["text"])
    os.remove(i)

files1 = os.listdir(destination)
files1 = [os.path.join(destination, f) for f in files1] # add path to each file
files1.sort(key=lambda x: os.path.getmtime(x))

for i in range (11):
    with open(files1[i], encoding='windows-1252') as f:
        contents = f.read()
        print(contents)
        time.sleep(4)
        subprocess.run("pbcopy", text=True, input=contents)
    os.remove(files1[i])
    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Google Chrome.app"])
    time.sleep(2)
    pt.click(x=723, y=539)
    time.sleep(5)
    pt.click(x=306, y=545)
    time.sleep(5)
    pt.hotkey('command', 't')
    time.sleep(5)
    pt.typewrite("chat")
    time.sleep(5)
    pt.press('return')
    time.sleep(10)
    pt.hotkey('command','v')
    time.sleep(15)
    pt.typewrite("summarise the following  lecture in a manner in which all details regarding are captured in great thoroughly. Further, make sure that the information is recorded as a smooth-flowing narrative that retains all the meaning and suppositions of the original transcript while also being easy to understand for me, the student. Lastly, add in any information you think will help enhance the narrative and fill in the gaps to make excellent notes and leave nothing unexplained such that a student gains mastery of the material discussed in the transcript. Don't forget to add heading and let the information flow like a narrative and ensure that it is understandable to a student of the subject  ")
    time.sleep(15)
    pt.click(x=1203, y=830)
    time.sleep(200)
    pt.click(x=813, y=593)
    time.sleep(15)
    pt.click(x=813, y=593)
    time.sleep(5)
    pt.scroll(-500)
    time.sleep(10)
    pt.click(x=999, y=749)
    time.sleep(5)
    pt.click(x=525, y=757)
    time.sleep(10)
    pt.hotkey('command', 't')
    time.sleep(5)
    pt.typewrite("docs.google.com")
    time.sleep(5)
    pt.press('return')
    time.sleep(10)
    pt.click(x=31, y=136)
    time.sleep(5)
    pt.click(x=481, y=727)
    time.sleep(10)
    pt.hotkey('command','v')
    time.sleep(10)
    pt.click(x=31, y=136)
    time.sleep(5)
    pt.hotkey('command', 'shift', 'w')
    time.sleep(20)#end




