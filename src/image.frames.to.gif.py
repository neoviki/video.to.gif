import os
import sys
import argparse
from PIL import Image

def generate_gif_from_images(image_folder, output_gif="animation.gif", duration=100):
    # List and sort all 'png' files in the folder
    image_files = sorted(
        [f for f in os.listdir(image_folder) if f.endswith(".png")],
        key=lambda x: int(os.path.splitext(x)[0])
    )

    if not image_files:
        print("No 'png' images found in the folder.")
        return

    # Load images
    images = [Image.open(os.path.join(image_folder, f)) for f in image_files]

    # Save as GIF
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0,
        optimize=False
    )

    print(f"GIF saved as '{output_gif}' with {len(images)} frames.")
    print(f"Frame duration: {duration} ms per frame.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a GIF from numbered image frames.")
    parser.add_argument("-d", "--directory", required=True, help="Directory containing image frames (e.g., 0001.png to 1000.png).")
    parser.add_argument("-i", "--interval-between-frames", type=int, default=100, help="Duration of each frame in milliseconds (default: 100ms).")

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory.")
        sys.exit(1)

    generate_gif_from_images(args.directory, duration=args.interval_between_frames)

