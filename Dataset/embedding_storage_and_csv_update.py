
import numpy as np
import pandas as pd

# Assuming 'frames' directory exists in the cwd
frames_dir = 'frames/'

# Read the existing CSV into a DataFrame
df = pd.read_csv('indexed-videos.csv', delimiter='|')

# Add a new column for Embedding_File if it doesn't exist
if 'Embedding_File' not in df.columns:
    df['Embedding_File'] = ''

# Loop through each row to update the Embedding_File column
for index, row in df.iterrows():
    video_id = row['ID']
    video_path = row['Source Path']
    
    # Assuming a function get_key_frame_embeddings(video_path) exists that returns embeddings for key frames
    embeddings = get_key_frame_embeddings(video_path)
    
    # Save embeddings to a .npy file
    embedding_file = f"{frames_dir}embedding_{video_id}.npy"
    np.save(embedding_file, embeddings)
    
    # Update the DataFrame
    df.at[index, 'Embedding_File'] = embedding_file

# Save the updated DataFrame back to the CSV file
df.to_csv('indexed-videos.csv', index=False, sep='|')
