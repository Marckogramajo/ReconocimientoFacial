from django.shortcuts import render, redirect
import cv2
import numpy as np
import logging
from sklearn.model_selection import train_test_split
from . import dataset_fetch as df
from . import cascade as casc
from PIL import Image

from time import time
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pickle

from settings import BASE_DIR
# crear vistas
def index(request):
    return render(request, 'index.html')
def errorImg(request):
    return render(request, 'error.html')

def agregar_persona(request):
    #obtner id
    userId = request.POST['userId']
    print cv2.__version__
    # Detectar el rostro
    #Crear el clasificador con imagnes en cascada
    faceDetect = cv2.CascadeClassifier(BASE_DIR+'/ml/haarcascade_frontalface_default.xml')
    #capturar imagen desde la camara web
    cam = cv2.VideoCapture(0)

    id = userId
    font = cv2.FONT_HERSHEY_SIMPLEX

     # Contador para nombrar las imagnes
    contador = 0
    # Capturar rostro de uno en uno
    while(True):
        # Capturar la imagen que captura la camara
        ret, img = cam.read()
        #Convertir la imagen en escala de gris
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #obtinen las coordenadas de los rostros
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        #crea un rectangulo en el rostro detectado en la imagen.
        for(x,y,w,h) in faces:
            # increnta en 1 el contador
            contador = contador+1
            # se guarda la imagen 
            cv2.imwrite(BASE_DIR+'/ml/dataset/user.'+str(id)+'.'+str(contador)+'.jpg', gray[y:y+h,x:x+w])
            cv2.imwrite(BASE_DIR+'/static/img/'+str(id)+'.jpg', gray[y:y+h,x:x+w])
            #http://127.0.0.1:8000/static/img/55.jpg
            #cv2.imwrite(BASE_DIR+'/static/img/.'+str(id)+'.jpg')
            #configuracion del rectangulo
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 3)
            cv2.putText(img, str(contador)+"/100",(x,y+h), font, 1, (0,0,255),2)
            # pausa 
            cv2.waitKey(50)

        #mostrar una ventana con la imagen de la camara web
        cv2.imshow("Captura de Rostro",img)
        #espera sino da error cv
        cv2.waitKey(1)
        #fin del ciclo al capturar 35 rostros
        if(contador>100):
            break
    # desactivar la camara
    cam.release()
    # cerrar ventana 
    cv2.destroyAllWindows()

    return redirect('/admin')

def trainer(request):

    import os
    from PIL import Image

    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    path = BASE_DIR+'/ml/dataset'

    
    def getImagesWithID(path):
        
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] #concatinate the path with the image name
       
        faces = []
        Ids = []
        for imagePath in imagePaths:
           
            faceImg = Image.open(imagePath).convert('L') #convert it to grayscale
        
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1]) # -1 so that it will count from backwards and slipt the second index of the '.' Hence id
            
            faces.append(faceNp)
           
            Ids.append(ID)
            
            cv2.imshow("Entrenamiento", faceNp)
            cv2.waitKey(10)
        return np.array(Ids), np.array(faces)

  
    ids, faces = getImagesWithID(path)

    
    recognizer.train(faces, ids)

    
    recognizer.save(BASE_DIR+'/ml/recognizer/trainingData.yml')
    cv2.destroyAllWindows()

    return redirect('/')


def detect(request):
    faceDetect = cv2.CascadeClassifier(BASE_DIR+'/ml/haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
  
    rec = cv2.face.LBPHFaceRecognizer_create();
   
    rec.read(BASE_DIR+'/ml/recognizer/trainingData.yml')
    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    userId = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)

            getId,conf = rec.predict(gray[y:y+h, x:x+w]) 
            if conf<35:
                userId = getId
                cv2.putText(img, "Detectado",(x,y+h), font, 1, (0,255,0),2)
            else:
                cv2.putText(img, "Desconocido",(x,y+h), font, 1, (0,0,255),2)

            

        cv2.imshow("Camara",img)
        if(cv2.waitKey(1) == ord('q')):
            break
        elif(userId != 0):
            cv2.waitKey(1000)
            cam.release()
            cv2.destroyAllWindows()
            return redirect('/records/details/'+str(userId))

    cam.release()
    cv2.destroyAllWindows()
    return redirect('/')
