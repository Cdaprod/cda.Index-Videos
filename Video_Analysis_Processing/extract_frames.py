import cv2
import numpy as np

def extract_frames(video_path, n_frames=5):
    """
    Extracts frames from a video file.
    
    Args:
        video_path (str): Path to the video file.
        n_frames (int): Number of frames to extract.
        
    Returns:
        list: List of frames as NumPy arrays.
    """
    frames = []
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Select n_frames evenly spaced frames to extract
    frame_indices = np.linspace(0, total_frames - 1, n_frames, dtype=int)
    
    for i in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        
        if ret:
            frames.append(frame)
    
    cap.release()
    return frames
