from flask import Flask, jsonify, request
import VideoAnalysisTool

app = Flask(__name__)

@app.route('/api/v1/video_analysis', methods=['POST'])
async def video_analysis():
    data = request.get_json()
    video_path = data['video_path']
    n_frames = data.get('n_frames', 5)
    
    analysis_tool = VideoAnalysisTool()
    result = await analysis_tool.run(video_path, n_frames)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
