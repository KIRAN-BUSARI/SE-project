import cv2
import face_recognition

# Load the trained recognizer (trainer.yml)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# Load the face detection model from face_recognition library
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
video_capture = cv2.VideoCapture(0)

video_capture.set(3, 640)
video_capture.set(4, 480)

minW = 0.1*video_capture.get(3)
minH = 0.1*video_capture.get(4)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(int(minW), int(minH)))

    # Process each detected face
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]

        # Recognize the face using the trained recognizer
        label, confidence = recognizer.predict(face_roi)
        print("Label:", label, "Confidence:", confidence)

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the label and confidence
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'kiran: {label}',
                    (x, y-10), font, 0.9, (0, 255, 0), 2)

        # cv2.putText(frame, str(label), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(frame, str(confidence), (x+5, y+h-5),
                    font, 1, (255, 255, 0), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
