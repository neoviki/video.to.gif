## Video to GIF Converter

A simple 3-step semi-automated utility to convert any `.mp4` video into a clean, customized GIF.

### Step 0: Install dependencies

Before you begin, run:

```bash
chmod +x ./install.dependencies.sh;./install.dependencies.sh
```

This will install all the necessary Python and system dependencies needed for the scripts to run.

---

## Step 1: Convert video to image frames

```bash
./step.1.video.to.image.frame <input_video.mp4>
```

This will extract frames from the video and save them in the `image_frames/` folder as numbered '.png' files (`0001.png`, `0002.png`, etc.).

---

## Step 2: Choose your image frames

```bash
./step2.choose.image.frames.sh
```

Follow the steps and delete the image frames you **don’t want** as part of the final GIF. Keep only the ones you want in the animation. This step gives you manual control over the final result.

---

## Step 3: Generate the GIF

```bash
./step.3.image.frame.to.gif <duration_in_ms>
```

This script uses the images from `image_frames/` and creates an animated GIF called `animation.gif`.

You can choose how long each frame should play. Recommended durations:
- 150ms (fast)
- 300ms (medium)
- 400ms (slow)

Example:

```bash
./step.3.image.frame.to.gif 250
```

You can run without argument ( in this case the default duration is 100 milliseconds )

Example: Without argument 

```bash
./step.3.image.frame.to.gif
```

---

## Output

The final animated GIF is saved as:

```
animation.gif
```

---

## Tips

- Default folder for frames: `image_frames/`
- Missing image files (e.g. `0003.png`) are skipped automatically
- Try different frame durations until the animation looks just right
- default frame duration is 100 milliseconds

