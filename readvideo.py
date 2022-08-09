import cv2

cptr = cv2.VideoCapture("AnthonyShkraba.mp4")
print("opened !!")

if cptr.isOpened()==False:
    print("Unable to read the feed")

height = int(cptr.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cptr.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cptr.get(cv2.CAP_PROP_FPS))
print(fps)

size = (width,height)

out = cv2.VideoWriter("Projecttt.mp4",cv2.VideoWriter_fourcc(*"DIVX"),25,size)

while (True):
    ret,frame = cptr.read()
    cv2.imshow("Web cam",frame)
    if cv2.waitKey(25)==32:
        break
cptr.release()
out.release()
cv2.destroyAllWindows()
