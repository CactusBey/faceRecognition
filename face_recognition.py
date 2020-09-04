import face_recognition as fr
import os 
import cv2
import numpy as np

if not os.path.exists("photos"):
    os.mkdir("photos")
os.chdir("photos")

def faceReceg():
    acces = False
    encodePhoto  = {}
    for photo in os.listdir():
        imageRGB = fr.load_image_file(photo)
        faceLocation = fr.face_locations(imageRGB)
        encode = fr.face_encodings(imageRGB,faceLocation)
        ıd = photo[:-4]
        encodePhoto[ıd] = encode[0]
    faces = list(encodePhoto.values())
    names = list(encodePhoto.keys())

    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        frame = cam.read()[-1]
        locations = fr.face_locations(frame)
        encodeFace = fr.face_encodings(frame,locations)

        for location, encodeA in zip(locations, encodeFace):
            distances = fr.face_distance(faces,encodeA)
            if np.any(distances <= 0.6):
                print(f"Access accepted {ıd}")
                global user
                user = ıd
                acces = True
                global acceS
                acceS = acces
        cv2.imshow("frame", frame)
        k = cv2.waitKey(10) & 0xFF
        if k== ord("q") or acces == True : 
            break

    cam.release()
    cv2.destroyAllWindows()

def takePhoto():
    name = input("What is your name? ")
    surName = input("What is yout surname? ")
    print("Please look at the camera\nPress s to take photo ")
    camera = cv2.VideoCapture(0)
    while True:
        _,image = camera.read()
        if cv2.waitKey(1)& 0xFF == ord('s'):
            cv2.imwrite('photos/'+ name + " "+surName+".jpg",image)
            break
        cv2.imshow('image',image)            
        camera.release()
        cv2.destroyAllWindows()

print("Hello welcome to face recognition system")

while True:
    try:
        userInput = int(input("1: Sign in to the system  \n2: Register to the system\n3: Quit system\nChoose action: "))
    except ValueError:
        print("------------------\nPlease only number")
    else:
        if userInput >= 4:
            print("--------------------\nEnter valid number")
        elif userInput == 1:
            faceReceg()
            if acceS:
                print(f"Welcome the system {user}")
                break
        elif userInput == 2:
            takePhoto()
        else:
            break
        
