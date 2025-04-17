import cv2
import os
import sys

def mp4_to_images(video_path, output_dir="image_frames"):
    if not os.path.isfile(video_path):
        print(f"File not found: {video_path}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        sys.exit(1)

    frame_num = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        filename = os.path.join(output_dir, f"{frame_num:04d}.png")
        cv2.imwrite(filename, frame)
        frame_num += 1

    cap.release()
    print(f"Saved {frame_num - 1} frames to '{output_dir}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mp4_to_images.py <input_video.mp4>")
        sys.exit(1)

    video_path = sys.argv[1]
    mp4_to_images(video_path)

