#!/usr/local/bin/python3

import logging
from weaviate import Client, AuthClientSecret

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize Weaviate client
weaviate_url = "your-weaviate-url"
auth = AuthClientSecret("your-client-id", "your-client-secret")
client = Client(weaviate_url, auth)

# Define the Weaviate schema for video indexing
video_schema = {
    "classes": [
        {
            "class": "Video",
            "description": "Video files indexed from storage",
            "properties": [
                {
                    "name": "videoID",
                    "description": "Unique identifier for the video",
                    "dataType": ["int"]
                },
                {
                    "name": "filename",
                    "description": "Name of the video file",
                    "dataType": ["string"]
                },
                {
                    "name": "format",
                    "description": "Video format",
                    "dataType": ["string"]
                },
                {
                    "name": "sourcePath",
                    "description": "Path to the source video file",
                    "dataType": ["string"]
                },
                {
                    "name": "frames",
                    "description": "Extracted frames from the video",
                    "dataType": ["string"]
                }
            ]
        }
    ]
}

# Create schema in Weaviate
try:
    client.schema.create(video_schema)
    logging.info("Weaviate schema created successfully.")
except Exception as e:
    logging.error(f"Failed to create Weaviate schema: {e}")

if __name__ == "__main__":
    pass  # Add any additional setup or logging here
