import cv2
def take_image():
    vid=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vid.read()
        cv2.imwrite("my_image.jpg",frame)
        result=False
    vid.release()
    cv2.destroyAllWindows()
take_image()        