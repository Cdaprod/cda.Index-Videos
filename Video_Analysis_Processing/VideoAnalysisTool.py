from pydantic import BaseModel, Field
from typing import Optional
import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import asyncio

class VideoAnalysisInput(BaseModel):
    video_path: str = Field()
    n_frames: Optional[int] = Field(5)

class VideoAnalysisTool:
    name = "VideoAnalysis"
    description = "Tool for extracting video metadata and frames"
    args_schema = VideoAnalysisInput
    
    @staticmethod
    def extract_metadata(video_path: str):
        with VideoFileClip(video_path) as clip:
            video_length = clip.duration
            frame_rate = clip.fps
            resolution = clip.size
        
        return {
            "video_length": video_length,
            "frame_rate": frame_rate,
            "resolution": resolution
        }

    @staticmethod
    def extract_frames(video_path: str, n_frames=5):
        frames = []
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_indices = np.linspace(0, total_frames - 1, n_frames, dtype=int)
        
        for i in frame_indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if ret:
                frames.append(frame)
        
        cap.release()
        return frames

    @staticmethod
    async def run(video_path: str, n_frames=5):
        loop = asyncio.get_event_loop()
        metadata = loop.run_in_executor(None, VideoAnalysisTool.extract_metadata, video_path)
        frames = loop.run_in_executor(None, VideoAnalysisTool.extract_frames, video_path, n_frames)
        
        metadata, frames = await asyncio.gather(metadata, frames)
        return {"metadata": metadata, "frames": frames}

# You can add this class to your list of tools like this:  
# tools = [VideoAnalysisTool()]
# This should get you started on integrating the Flask server for asynchronous video processing