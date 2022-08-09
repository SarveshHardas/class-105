import cv2
import os

path = "Images"
imgs=[]

for file in os.listdir(path):
    name,ext = os.path.splitext(file)

    if ext in [".gif",".jpg",".png",".jpeg",".jfif"]:
        file_name = path+"/"+file
        imgs.append(file_name)

count = len(imgs)

frame = cv2.imread(imgs[0])

height,width,channels = frame.shape

size = (width,height)

out = cv2.VideoWriter("Sunrise.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,size)

for i in range(count-1,0,-1):
    frame = cv2.imread(imgs[i])
    out.write(frame)

out.release()
print("Done!!")