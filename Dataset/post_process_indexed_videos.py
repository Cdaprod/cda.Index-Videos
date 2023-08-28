
import cv2
import numpy as np
import pandas as pd
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

# Initialize ResNet50 model for feature extraction
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Function to extract ResNet50 embeddings for a given frame
def get_resnet50_embedding(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = np.expand_dims(frame, axis=0)
    frame = preprocess_input(frame)
    return model.predict(frame).flatten()

# Function to extract key frames and their embeddings
def get_key_frame_embeddings(video_path):
    cap = cv2.VideoCapture(video_path)
    key_frame_embeddings = []
    
    ret, frame = cap.read()
    last_key_frame = frame
    last_embedding = get_resnet50_embedding(frame)
    
    key_frame_diff_threshold = 0.2  # Threshold for key frame difference
    
    while ret:
        ret, frame = cap.read()
        if not ret:
            break
        
        current_embedding = get_resnet50_embedding(frame)
        diff = np.linalg.norm(current_embedding - last_embedding)
        
        if diff > key_frame_diff_threshold:
            key_frame_embeddings.append(current_embedding)
            last_key_frame = frame
            last_embedding = current_embedding

    cap.release()
    return np.array(key_frame_embeddings)

# Read indexed-videos.csv
df = pd.read_csv('indexed-videos.csv', delimiter='|')

# Add new columns if they don't exist
if 'Extracted_Frame_Path' not in df.columns:
    df['Extracted_Frame_Path'] = ''
if 'Embedding_File' not in df.columns:
    df['Embedding_File'] = ''

# Loop through each video to update the new columns
frames_dir = 'frames/'  # Assuming 'frames' directory exists in cwd

for index, row in df.iterrows():
    video_path = row['Source Path']
    video_id = row['ID']
    
    embeddings = get_key_frame_embeddings(video_path)
    frame_file = f"{frames_dir}frames_{video_id}.npy"
    embedding_file = f"{frames_dir}embedding_{video_id}.npy"
    
    # Save extracted frames and embeddings (placeholder for frames as they are not saved here)
    np.save(embedding_file, embeddings)
    
    df.at[index, 'Extracted_Frame_Path'] = frame_file
    df.at[index, 'Embedding_File'] = embedding_file

# Save the updated DataFrame back to indexed-videos.csv
df.to_csv('indexed-videos.csv', index=False, sep='|')
