import io
import os

from google.cloud import vision
from google.cloud.vision_v1 import types

# Set your environment variable for your GCP credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'circular-genius-402810-13afeaaa2b14.json'

# Initialize the Vision API client
client = vision.ImageAnnotatorClient()

# Load the image
with io.open('2.jpg', 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Create the text detection request
request = types.AnnotateImageRequest(
    image=image,
    features=[types.Feature(type='TEXT_DETECTION')]
)

# Send the request and get the response
response = client.annotate_image(request)

# Process the text annotations
for text_annotation in response.text_annotations:
    print('Text:', text_annotation.description)


