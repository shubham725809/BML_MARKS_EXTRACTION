import io
import os
import pandas as pd
from google.cloud import vision
from google.cloud.vision_v1 import types

# Set your environment variable for your GCP credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'circular-genius-402810-13afeaaa2b14.json'

# Initialize the Vision API client
client = vision.ImageAnnotatorClient()

# Load the image
with io.open('1.jpg', 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Create the text detection request
request = types.AnnotateImageRequest(
    image=image,
    features=[types.Feature(type='TEXT_DETECTION')]
)

# Send the request and get the response
response = client.annotate_image(request)

# Extract text blocks and their positions
text_blocks = []
for text_annotation in response.text_annotations:
    text_blocks.append({
        'text': text_annotation.description,
        'bounding_poly': text_annotation.bounding_poly,
    })

# Analyze text block positions to identify table structure
# (rows, columns, cell boundaries)

# Extract cell values and assign them to the table structure

# Create pandas DataFrame from the extracted cell values and table structure
df = pd.DataFrame(data=cell_values, columns=column_names)

# Print the pandas DataFrame
print(df)
df.to