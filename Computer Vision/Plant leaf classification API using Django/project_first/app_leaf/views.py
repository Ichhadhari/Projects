import tensorflow as tf
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


model = tf.keras.models.load_model('app_leaf/keras_model.h5')

@csrf_exempt
def classify_image(request):
    # code to process the image and make predictions
    #prediction = model.predict(request.file)

    #my
    if request.method == 'POST':
        print(request.FILES)

        if 'image.' in request.FILES:
            print("get")
            image = request.FILES['image.']

            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            #path = request.FILES['image'].read()

            image = Image.open(image).convert("RGB")

            # resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

            # turn the image into a numpy array
            image_array = np.asarray(image)

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # Predicts the model
            prediction = model.predict(data)

            class_names=['Alstonia Scholaris (P2)','Arjun (P1)','Basil (P8)','Chinar (P11)','Gauva (P3)','Jamun (P5)','Jatropha (P6)','Lemon (P10)','Mango (P0)','Pomegranate (P9)','Pongamia Pinnata (P7)']

            #index = np.argmax(prediction)
            #class_name = class_names[index]

            output_dic = {}

            for i in range(0, len(prediction[0])):
                prediction[0][i] = float("{:.2f}".format(prediction[0][i] * 100))  # todo
                output_dic[class_names[i]] = prediction[0][i]

            sorted_dict = dict(sorted(output_dic.items(), key=lambda x: x[1], reverse=True))
            sorted_keys = list(sorted_dict.keys())
            sorted_values = list(sorted_dict.values())

            result = ""

            for i in range(0, 5):
                result = result + sorted_keys[i] + "  :  " + str(sorted_values[i]) + "/n"


            # return prediction as a JSON response
            return JsonResponse({'prediction': result})

        return JsonResponse({'prediction': "image not get"})


# Create your views here.
