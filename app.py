from flask import Flask
import cv2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/Sample-generator')
def Sample_generator():
    # return render_template('sample-generator/index.html', title='Sample Generator')
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


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5001))
    app.run(debug=True)
    #    app.run() #host='0.0.0.0'
    #    host="0.0.0.0"
    #    debug=True
    #    app.run("localhost",port)
    #    app.run(debug=False)#host='0.0.0.0')
    #    app.run(host='0.0.0.0',port=8092)
    #    app.run(host='0.0.0.0',port=4367,#debug=True,use_re
    #            use_debugger=True,)
    #    app.run(host='0.0.0.0',port=4367,debug=True,use_re
    #            use_debugger=True,threaded=True)
