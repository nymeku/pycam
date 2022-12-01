import cv2

canva = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
# cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    # play video in specific window
    # cv2.imshow("preview", frame)
    # rval, frame = vc.read()
    # frame = cv2.flip(frame,1)
    # key = cv2.waitKey(20)
    
    for x in range(0,100-1):
        for y in range(0,100-1):
            # if key == 27: # exit on ESC
            #     break
            v=frame[y,x]
            print("Pixel : [{},{}], Value: {}".format(x,y,v))

    # if key == 27: # exit on ESC
    #         break
    

vc.release()
# cv2.destroyAllWindows()
cv2.destroyWindow("preview")