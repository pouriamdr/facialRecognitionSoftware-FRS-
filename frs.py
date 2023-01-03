import cv2
import sys, os
 
sources = os.listdir(sys.argv[1])
# Create the haar cascade
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
output = 'employee,gate,time\n'

for imageName in sources:
    image = cv2.imread("{}/{}".format(sys.argv[1], imageName) )
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
            gray_image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            #flags = cv2.CV_HAAR_SCALE_IMAGE
        )
    crop_img = None
    for (x, y, w, h) in faces:
        crop_img = gray_image[y:y+h, x:x+w]
        break
    histogram = cv2.calcHist([crop_img], [0],
                            None, [256], [0, 256])
    images = os.listdir(sys.argv[2])
    capacities = []
    histograms = []
    for img in images:
        try:
            image = cv2.imread(sys.argv[2] + "/" + img)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            histograms.append(cv2.calcHist([gray_image], [0],
                                    None, [256], [0, 256]))
            capacities.append(0)
        except:
            None
    row = 0
    for histogramX in histograms:
        i = 0
        try:
            while i<len(histogram) and i<len(histogramX):
                capacities[row]+=(histogram[i]-histogramX[i])**2
                i+= 1
            capacities[row] = capacities[row]**(1 / 2)
        except:
            None
        row += 1
    mostSimilarIndex = 0
    mostSimilar = 999999999999
    i = 0
    for c in capacities:
        if c < mostSimilar:
            mostSimilar = c
            mostSimilarIndex = i
        i += 1
    gate = imageName.split('-')
    gate = gate[0]
    employee = images[mostSimilarIndex].split('.')
    employee = employee[0]
    output += "{},{},{}\n".format(employee, gate ,sys.argv[1])
    print("{} was in {} on {}".format(employee, gate ,sys.argv[1]))
f = open(sys.argv[3],"w")
f.write(output)
f.close()
print("Output saved as {}".format(sys.argv[3]))