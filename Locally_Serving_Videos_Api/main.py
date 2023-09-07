from flask import Flask, jsonify, send_from_directory, Response
from flask_idempotent import Idempotent
import logging
import os

# Initialize Flask app
app = Flask(__name__, static_folder='/volume1/')

# Initialize Flask-Idempotent
Idempotent(app)

# Initialize logging
logging.basicConfig(filename='flask_serve_videos_api.log', level=logging.DEBUG)

# Placeholder function for Supabase connection
def create_supabase_conn():
    logging.info('Supabase connection created.')
    conn = psycopg2.connect(
        dbname="",
        user="",
        password="",
        host="",
        port="5432"
    )
    return supabase_conn

# Placeholder function for Weaviate connection
def create_weaviate_conn():
    logging.info('Weaviate connection created.')
    # Replace with actual Weaviate connection code
    pass

@app.route('/api/v1/videos/<int:index_number>', methods=['GET'])
def get_video(index_number):
    try:
        # Connect to Supabase to get the source path
        conn = create_supabase_conn()  # Changed from supabase_conn to conn
        cursor = conn.cursor()
        cursor.execute("SELECT src_path FROM video_files WHERE id = %s", (index_number,))
        result = cursor.fetchone()

        if result:
            src_path = result[0]
        else:
            logging.warning(f'No video found with index_number {index_number}.')
            return Response("Video not found.", status=404)

        # Connect to Weaviate to get enriched metadata
        weaviate_conn = create_weaviate_conn()
        # Placeholder: Replace with actual query to Weaviate
        metadata = "example_metadata"

        logging.info(f'Video {index_number} retrieved successfully.')
        return jsonify({
            "index_number": index_number,
            "src_path": src_path,
            "metadata": metadata
        })
        
    except Exception as e:
        logging.error(f'An error occurred while retrieving video {index_number}: {str(e)}')
        return Response("An error occurred.", status=500)

@app.route('/videos/<path:path>', methods=['GET'])
def serve_video(path):
    try:
        # Serving video from Synology NAS
        logging.info(f'Serving video from path: {path}')
        return send_from_directory(app.static_folder, path)
        
    except Exception as e:
        logging.error(f'An error occurred while serving the video from path {path}: {str(e)}')
        return Response("An error occurred.", status=500)

if __name__ == '__main__':
    app.run(debug=True)
