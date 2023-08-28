#!/usr/local/bin/python3 

# Importing required libraries
import cv2
import numpy as np
import pandas as pd
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.models import Model
import os

# Create a directory for frames if it doesn't exist
if not os.path.exists("frames"):
    os.makedirs("frames")

# Initialize the ResNet50 model for feature extraction
base_model = ResNet50(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

# Function to get ResNet50 embeddings for an image
def get_resnet50_embeddings(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_array = np.array([img])
    img_array = preprocess_input(img_array)
    embeddings = model.predict(img_array)
    return embeddings.flatten()

# Placeholder function for GPT-3 Turbo embeddings
def get_gpt3turbo_embeddings(text):
    return "GPT-3 Turbo Embeddings Placeholder"

# Read the CSV
df = pd.read_csv("indexed-videos.csv", delimiter='|', error_bad_lines=False)
df['FramePath'] = None
df['ResNet50_Embeddings'] = None
df['GPT3Turbo_Embeddings'] = None

# Loop through each video for frame extraction and getting embeddings
for index, row in df.iterrows():
    video_path = row['Source Path']
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if ret:
        frame_path = f"frames/frame_{row['ID']}.jpg"
        cv2.imwrite(frame_path, frame)
        df.at[index, 'FramePath'] = frame_path
        resnet50_embeddings = get_resnet50_embeddings(frame_path)
        df.at[index, 'ResNet50_Embeddings'] = resnet50_embeddings
        gpt3turbo_embeddings = get_gpt3turbo_embeddings("Some Text")
        df.at[index, 'GPT3Turbo_Embeddings'] = gpt3turbo_embeddings
    cap.release()

# Save the updated DataFrame to a new CSV
df.to_csv("updated_indexed_videos.csv", index=False)
