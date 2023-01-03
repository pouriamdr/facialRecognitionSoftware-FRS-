import cv2
import sys, os

# Create the haar cascade
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

images = os.listdir(sys.argv[1])
for img in images:
    print(img)
    try:
        # Read the image
        image = cv2.imread("{}/{}".format(sys.argv[1],img))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            #flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        print("Found {0} faces!".format(len(faces)))

        # Draw a rectangle around the faces
        i = 1
        for (x, y, w, h) in faces:
            crop_img = image[y:y+h, x:x+w]
            cv2.imwrite("{}/{}".format(sys.argv[2], img), crop_img)
            i+=1
    except:
        None