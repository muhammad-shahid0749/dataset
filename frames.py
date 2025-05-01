import cv2
import os

def video_to_frames(video_path, output_dir, frame_interval=1):
    """
    Convert a video file to individual frames (images)
    
    Parameters:
    video_path (str): Path to input video file
    output_dir (str): Directory to save output frames
    frame_interval (int): Save every nth frame (default: 1)
    """
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file")
        return
    
    # Initialize variables
    frame_count = 0
    saved_count = 0
    pic_num=60000
    while True:
        # Read next frame
        success, frame = cap.read()
        
        # If frame couldn't be read (end of video)
        if not success:
            break
            
        # Only process frames at specified interval
        if frame_count % frame_interval == 0:
            # Save frame as JPEG file
            frame_file = os.path.join(output_dir, f"00{pic_num:05d}.jpg")
            cv2.imwrite(frame_file, frame)
            saved_count += 1
            pic_num +=1
            
            # Print progress every 100 frames
            if saved_count % 100 == 0:
                print(f"Saved {saved_count} frames...")
        
        frame_count += 1
    
    # Release video capture object
    cap.release()
    
    print(f"Finished processing. Total frames: {frame_count}")
    print(f"Saved frames: {saved_count} to directory: {output_dir}")


# Example usage
if __name__ == "__main__":
    video_path = "v6.mp4"  # Change to your video path
    output_dir = "v6"    # Change to desired output directory
    frame_interval = 1              # Save every frame
    
    video_to_frames(video_path, output_dir, frame_interval)