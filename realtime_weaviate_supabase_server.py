#!/usr/local/bin/python3

import logging
from weaviate import Client, AuthClientSecret
from supabase_py import create_client
from flask import Flask, jsonify

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize Weaviate client
weaviate_url = "your-weaviate-url"
auth = AuthClientSecret("your-client-id", "your-client-secret")
weaviate_client = Client(weaviate_url, auth)

# Initialize Supabase client
supabase_url = "your-supabase-url"
supabase_key = "your-supabase-key"
supabase = create_client(supabase_url, supabase_key)

# Initialize Flask app
app = Flask(__name__)

@app.route('/sync', methods=['GET'])
def sync_to_weaviate():
    try:
        # Fetch data from Supabase table
        rows = supabase.table("video-index").select("*").execute()
        
        for row in rows['data']:
            # Prepare data for Weaviate
            weaviate_data = {
                "videoID": row['ID'],
                "filename": row['Filename'],
                "format": row['Format'],
                "sourcePath": row['Source Path']
            }
            
            # Add to Weaviate
            weaviate_client.data_object().create(weaviate_data, "Video")
        
        return jsonify({"status": "success"}), 200

    except Exception as e:
        logging.error(f"Failed to sync: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
