import cv2
import numpy as np
from PIL import Image
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 840)

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input("Enter a Numeric USER ID here :   ")

print("Taking Samples please Look at the Camera......!")
count = 0

while True:

    ret, img = cam.read()
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_img, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

        cv2.imwrite("samples/face." + str(face_id)+'.' +
                    str(count)+".jpg", converted_img[y:y+h, x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff

    if k == 27:
        break
    elif count >= 10:
        print("Done! Time to Exit")
        break

print("Samples Taken Now closing the program....")
cam.release()
cv2.destroyAllWindows()


path = 'samples'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir
                  (path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids


print("Training Faces , It will take few seconds. Wait...")

faces, ids = Images_And_Labels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('trainer/trainer.yml')
print("Model trained, Now we can recognize your face")


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type


id = 5


names = ['', 'kiran', 'B kiran', 'pavan', 'Abdul',]


cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

# define the window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = true

while True:
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, accuracy = recognizer.predict(gray[y:y+h, x:x+w])
        if (accuracy <= 100):
            id = names[id]
            accuracy = "{0}%".format(round(100 - accuracy))

        else:
            id = "Unknown"
            accuracy = "{0}%".format(round(100 - accuracy))

        cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(accuracy), (x+5, y+h-5),
                    font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

    print("Thanks for using this program, Have a great DAY....")


cam.release()
cv2.destroyAllWindows()
