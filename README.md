## Easy-Wav2Lip improves Wav2Lip video lipsyncing making it:

## Easier:
* Simple setup and execution - locally and via colab.
     * no messing around manually downloading and installing prerequesits
     * Google Colab has only 2 cells to execute
     * Windows users only need one file to install, update and run.
* Well documented options below.
     * No more wondering what anything does!

## Faster:
For my 9 second 720p 60fps test clip via Colab T4:
| Original Wav2Lip | Easy-Wav2Lip |
|:-------|:-----|
| Execution time: 6m 53s | Execution time: 56s |

That's not a typo! My clip goes from almost 7 minutes to under 1 minute!

The tracking data is saved between generations of the same video, saving even more time:
| Easy-Wav2Lip on the same video again |
|:-----|
| Execution time: 25s |

## Better looking:

Easy-Wav2Lip fixes visual bugs on the lips:

[![Comparison gif](https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/wav2lipcomparison.gif)](https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/wav2lipcomparison.gif)

3 Options for Quality:
* Fast: Wav2Lip
* Improved: Wav2Lip with a feathered mask around the mouth to restore the original resolution for the rest of the face
* Enhanced: Wav2Lip + mask + GFPGAN upscaling done on the face

[![Comparison gif](https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/JPComparison.gif)](https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/JPComparison.gif)


# Installation:

### For the easiest and most compatible way to use this tool, use the Google Colab version:

### Google Colab:
[https://colab.research.google.com/github/anothermartz/Easy-Wav2Lip/blob/v8.1/Easy_Wav2Lip_v8.1.ipynb](https://colab.research.google.com/github/anothermartz/Easy-Wav2Lip/blob/v8.1/Easy_Wav2Lip_v8.1.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anothermartz/Easy-Wav2Lip/blob/v8.1/Easy_Wav2Lip_v8.1.ipynb)

### For the easiest way to install locally on Windows 10 or 11, 64-Bit with a non-ARM processor and an NVIDIA GPU:

1. Download [Easy-Wav2Lip.bat](https://github.com/anothermartz/Easy-Wav2Lip/releases/download/v8.1_release/Easy-Wav2Lip_v8.1.bat)
2. Place it in a folder on your PC (EG: in Documents)
3. Run it and follow the instructions.

Make sure your Nvidia drivers are up to date or you may not have Cuda 12.

[Easy-Wav2Lip.bat](https://github.com/anothermartz/Easy-Wav2Lip/releases/download/v8.1_release/Easy-Wav2Lip_v8.1.bat) will automatically check for and install the required software, download and install Easy-Wav2Lip, then run it in a loop of configuration and processing until you close it. It will also check for updates to Easy-Wav2Lip.

_If anyone is able to convert Easy-Wav2Lip.bat to work on linux, it will very appreciated!_

### For other configurations (untested!) or just to manually install:
1. Make sure the following are installed and can be accessed via your terminal:
      * Python (I have only tested 3.10.11 - other versions may not work!)
      * Git
      * ffmpeg, ffplay, ffprobe
      * Visual Studio Build Tools C++ module
      * Cuda (Just having the latest Nvidia drivers will do this, I have only tested 12.2)
2. Run the following in your terminal:
```
git clone https://github.com/anothermartz/Easy-Wav2Lip.git
cd Easy-Wav2Lip
pip install -r requirements.txt
python install.py
```
Then:
Linux:
`./run_loop.sh`

Windows:
`call run_loop.bat`

Please let me know if you have success running this on Linux, an AMD GPU or an ARM proessor and if you did or didn't do anything special to get it working.

## Usage:
* Once everything is installed, a file called config.ini should pop up.
* Add the path(s) to your video and audio files here and configure the settings to your liking.
     * Pro Tip:
     * On Windows Hold shift when right clicking on the file you want to use, then press "a" or click "copy as path" and that'll get the path that you can paste as video_file or vocal_file.
       
* Save config.ini and close it, this will start the Wav2Lip process and your file will be saved in the same directory as your video_path file.
* config.ini will open again and you can change inputs and settings.
* See [Advanced Tweaking](https://github.com/anothermartz/Easy-Wav2Lip/blob/v8/README.md#advanced-tweaking) below for the explanation of the settings not already explained in config.ini

# Credits:
* [The Original Wav2Lip](https://github.com/Rudrabha/Wav2Lip) of course.
* The huge speed increase and improved base quality comes from [cog-Wav2Lip](https://github.com/devxpy/cog-Wav2Lip).
* Code to upscale with [GFPGAN](https://github.com/TencentARC/GFPGAN) mainly came from [wav2lip-hq-updated-ESRGAN](https://github.com/GucciFlipFlops1917/wav2lip-hq-updated-ESRGAN).
* I couldn't have done this without AI assistance; Before making this I had very minimal python experience! LLM of choice: **Bing Chat.**
* Thanks to [JustinJohn](https://github.com/justinjohn0306) for making the [Wav2Lip_simplified](https://colab.research.google.com/github/justinjohn0306/Wav2Lip/blob/master/Wav2Lip_simplified_v5.ipynb) colabs which inspired me to make my own, even simpler version.

# Support
I've been offering some support in this discord:<br>
Invite link: https://discord.gg/FNZR9ETwKY<br>
Wav2Lip channel: https://discord.com/channels/667279414681272320/1076077584330280991

# Best practices:
* The best results come from lining up the speech to the actions and expressions of the speaker before you send it through wav2lip!

Video files:
* Must have a face in all frames or Wav2Lip will fail
* Crop or mask out faces you don't want to lipsync or it'll choose randomly.
* Use h264 .mp4 - other file types may be supported but this is what it outputs as
* Images are currently untested.
* Use a small file in every way (try <720p, <30 seconds, 30fps <b></b> etc. - Bigger files may work but are usually the reason it fails)
* For your first try, use a really tiny clip just to get used to the process, only once you're familiar should you try bigger files to see if they work.

Audio files:
* Save as .wav and the same length as your input video.
* NOTE: I've noticed that about 80ms gets cut from the processed video/audio and I'm not sure how to fix this, so make sure you have a little extra than what you actually need!
* You can just encode it into your video file and leave vocal_path blank, but this will add a couple of seconds to the processing time as it splits the audio from the video
* <b>OR</b>
* Select your audio file separately
* I'm not certain what filetypes are supported, at least .wav and .mp3 work.

# Advanced Tweaking:
## wav2lip_version:
| Option | Pros | Cons |
|:-------|:-----|:-----|
| Wav2Lip | + More accurate lipsync <br> + Attempts to keep the mouth closed when there is no sound | - Sometimes produces missing teeth (uncommon) |
| Wav2Lip_GAN | + Looks nicer <br> + Keeps the original expressions of the speaker more | - Not as good at masking the original lip movements, especially when there is no sound |

I suggest trying Wav2Lip first and switching to the GAN version if you experience an effect where it looks like the speaker has big gaps in their teeth.

### nosmooth:
* When enabled, wav2lip will crop the face on each frame independently.
  * Good for fast movements or cuts in the video.
  * May cause twitching if the face is on a weird angle.

* When disabled, wav2lip will blend the detected position of the face between 5 frames.
  * Good for slow movements, especially for faces on an unusual angle.
  * Mouth can be offset when the face moves within the frame quickly, looks horrible between cuts.

## Padding:
This option controls how many pixels are added or removed from the face crop in each direction.

| Value | Example | Effect |
|:------|:--------|:-------|
| U | U = -10 | Removes 5 pixels from the top of the face |
| D | D = 10 | Adds 10 pixels to the bottom of the face |
| L | L = 0 | No change to the left of the face |
| R | R = 15 | Adds 15 pixels to the right of the face |

Padding can help remove hard lines at the chin or other edges of the face, but too much or too little padding can change the size or position of the mouth. It's common practice to add 10 pixels to the bottom, but you should experiment with different values to find the best balance for your clip.

## Mask:
This option controls how the processed face is blended with the original face. This has no effect on the "Fast" quality option.

* **size** will increase the size of the area that the mask covers.
* **feathering** determines the amount of blending between the centre of the mask and the edges.
* **mouth_tracking** will update the position of the mask to where the mouth is on every frame (slower)
*   * Note: The mouth position is already well approximated due to the frame being cropped to the face, enable this only if you find a video where the mask doesn't appear to follow the mouth.
* **debug_mask** will make the background grayscale and the mask in colour so that you can easily see where the mask is in the frame.

# Other options:

# Batch processing:
This option allows you to process multiple video and/or audio files automatically. 
* Name your files with a number at the end, eg. Video1.mp4, Video2.mp4, etc. and put them all in the same folder.
* Files will be processed in numerical order starting from the one you select. For example, if you select Video3.mp4, it will process Video3.mp4, Video4.mp4, and so on.
* If you select numbered video files and a non-numbered audio file, it will process each video with the same audio file. Useful for making different images/videos say the same line.
* Likewise, if you select a non-numbered video file and numbered audio files, it will use the same video for each audio file. Useful for making the same image/video say different things.

### output_suffix:
This adds a suffix to your output files so that they don't overwite your originals.

### include_settings_in_suffix:
Adds what settings were used - good for comparing different settings as you will know what you used for each render.
Will add: Qualty_resolution_nosmooth_pads-UDLR
EG: _Enhanced_720_nosmooth1_pads-U15D10L-15R30
pads_UDLR will not be included if they are set to 0.
resolution will not be included if it output_height is set to full resolution

### preview_input
Displays the input video/audio before processing so you can check to make sure you chose the correct file(s). It may only work with .mp4, I just know it didn't work on an .avi I tried.
Disabling this will save a few seconds of processing time for each video.

### preview_settings
This will render only 1 frame of your video and display it at full size, this is so you can tweak the settings without having to render the entire video each time.
frame_to_preview is for selecting a particular frame you want to check out - may not be completely accurate to the actual frame.
