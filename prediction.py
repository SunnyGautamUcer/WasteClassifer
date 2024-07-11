from keras.models import load_model
import numpy as np
from imgProcessing import preprocess_image

pathM = 'C:\\Users\\somes\\OneDrive\\Desktop\\DemoProject\\model\\keras_model.h5'

model = load_model(pathM)

classDic = {0: 'Non-Recyclable', 1: 'Recyclable',2: 'Non-Recyclable'}
def predictionGarbage(image):
    image = preprocess_image(image)
    prediction = model.predict(image)
    class_index = np.argmax(prediction)
    print(class_index)
    return classDic[class_index]
    

