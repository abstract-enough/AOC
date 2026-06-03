import cv2
import imageio
import math

file_name = "cardinal.mp4"

cap = cv2.VideoCapture("/content/drive/MyDrive/"+file_name)

frame_rate = math.ceil(cap.get(5))

frames = []

i=1
j=1
while True:

    ret, frame = cap.read()
    if ret:
      color_frame = cv2.cvtColor(frame,
cv2.COLOR_BGR2RGB)
      frames.append(color_frame)

      if i%(20*frame_rate) == 0:
        #write file
        imageio.mimsave("/content/drive/MyDrive/"+file_name[:-4]+"_"+str(j)+".mp4", frames, fps=frame_rate)
        frames = []
        j=j+1

      i=i+1

    if not ret:
        break
