from PIL import Image
import numpy as np

def preprocess_image(image):
    # Convert the image to a numpy array
    image_np = np.array(image)
    # Normalize pixel values
    image_normalized = image_np / 255.0
    # Resize the image to match the model's input shape
    image_resized = np.resize(image_normalized, (224, 224, 3))
    # Convert the resized image back to a PIL image
    # image_pil = Image.fromarray(np.uint8(image_resized * 255))
    # Add batch dimension
    image_batched = np.expand_dims(image_resized, axis=0)
    return image_batched




