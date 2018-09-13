import numpy as np
import cv2
import time

#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



def TakeSnapshotAndSave():
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        x = 0
        y = 20
        text_color = (0,255,0)
        # write on the live stream video
        cv2.putText(frame, "Press q when ready", (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=2)


        # if you want to convert it to gray uncomment and display gray not fame
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        # press the letter "q" to save the picture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # write the captured image with this name
            cv2.imwrite('try.jpg',frame)
            break

    # When everything done, release the capture
    
    
    
    cap.release()
    cv2.destroyAllWindows()
    
    imagePath = 'try.jpg'
	


    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    if len(faces) == 1:
        print '1 face was found'



if __name__ == "__main__":
    TakeSnapshotAndSave()