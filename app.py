import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verify', methods=['POST'])
def process_image():
    result = predict()
    return result

@app.route('/')
def index():
    return "FLASK APP IS WORKING YIPEEEEEEEE :333333"

base_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_path, "LLMModels", "keras_model.h5")
labels_path = os.path.join(base_path, "labels", "labels.txt")

model = load_model(model_path, compile=False)
with open(labels_path, "r") as file:
    class_names = [line.strip() for line in file.readlines()]

def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected for uploading'}), 400

    try:
        # Preprocess the image
        image = Image.open(BytesIO(file.read())).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        # Make prediction
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        return jsonify({'class': class_name, 'confidence': float(confidence_score)})
    except Exception as e:
        return jsonify({'error': f'Error processing the image: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True)