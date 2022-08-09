import cv2

cptr = cv2.VideoCapture(0)
print("opened !!")

if cptr.isOpened()==False:
    print("Unable to read the feed")

height = int(cptr.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cptr.get(cv2.CAP_PROP_FRAME_WIDTH))

size = (width,height)

out = cv2.VideoWriter("Project.mp4",cv2.VideoWriter_fourcc(*"DIVX"),25,size)

while (True):
    ret,frame = cptr.read()
    cv2.imshow("Web cam",frame)
    if cv2.waitKey(25)==32:
        break
cptr.release()
out.release()
cv2.destroyAllWindows()
