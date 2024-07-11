from flask import Flask, request, jsonify,render_template
import base64
from PIL import Image
from io import BytesIO
from imgProcessing import preprocess_image
from prediction import predictionGarbage

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/classifier.html')
def classifier():
    return render_template('classifier.html')

@app.route('/craft.html')
def craft():
    return render_template('craft.html')


def predict(image):
    processedImg = preprocess_image(image)
    result = predictionGarbage(processedImg)
    return result

@app.route('/predict', methods=['POST'])
def predict_image():
    data = request.get_json()
    image_data = data['image_data']
    # Remove the 'data:image/jpeg;base64,' prefix from the base64 string
    image_data = image_data.replace('data:image/jpeg;base64,', '')
    # Decode the base64 string to image
    img = Image.open(BytesIO(base64.b64decode(image_data)))
    # Get the prediction
    prediction = predict(img)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
