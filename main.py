#!/usr/local/bin/python3


import os
import logging
from supabase_py import create_client

# Constants
VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mov', '.h264']

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Helper function to check if a file is a video
def is_video(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower() in VIDEO_EXTENSIONS

# Initialize Supabase client
supabase_url = "your-supabase-url"
supabase_key = "your-supabase-key"
supabase = create_client(supabase_url, supabase_key)

def generate_video_index_supabase(root_directory):
    logging.info("Generating video index...")
    video_id = 1  # Initialize video ID
    rows = supabase.table("video-index").select("Source Path").execute()
    existing_records = {row['Source Path'] for row in rows['data']}
    
    for root, _, files in os.walk(root_directory):
        for filename in files:
            if is_video(filename):
                src_path = os.path.join(root, filename)
                if src_path not in existing_records:
                    video_format = os.path.splitext(filename)[1][1:]
                    
                    # Insert into Supabase table
                    supabase.table("video-index").insert([{
                        'ID': video_id,
                        'Filename': filename,
                        'Format': video_format,
                        'Source Path': src_path
                    }]).execute()
                    
                    existing_records.add(src_path)
                    video_id += 1

# Main function to orchestrate the task
def main():
    root_directory = '/volume1/'  # Update this to your root directory
    
    generate_video_index_supabase(root_directory)
    logging.info("Process completed.")

if __name__ == "__main__":
    main()