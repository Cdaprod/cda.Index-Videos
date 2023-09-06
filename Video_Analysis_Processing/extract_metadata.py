from moviepy.editor import VideoFileClip

def extract_metadata(video_path):
    """
    Extracts metadata from a video file.
    
    Args:
        video_path (str): Path to the video file.
        
    Returns:
        dict: Metadata dictionary containing video length, frame rate, and resolution.
    """
    with VideoFileClip(video_path) as clip:
        video_length = clip.duration  # duration in seconds
        frame_rate = clip.fps  # frames per second
        resolution = clip.size  # (width, height)
    
    metadata = {
        "video_length": video_length,
        "frame_rate": frame_rate,
        "resolution": resolution
    }
    
    return metadata
