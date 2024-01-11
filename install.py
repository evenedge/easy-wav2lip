version = 'v8.1'
import os
import re
import argparse
import shutil
from IPython.display import clear_output
from easy_functions import (format_time,
                            load_file_from_url,
                            load_model,
                            load_predictor)
from enhance import load_sr

parser = argparse.ArgumentParser(description='Install Easy-Wav2Lip')

parser.add_argument('--ver', type=str,  default=version,
                    help='Which branch to install', required=False)

args = parser.parse_args()

working_directory = os.getcwd()

#download and initialize both wav2lip models
print('downloading wav2lip essentials')
load_file_from_url(
  url='https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/Wav2Lip_GAN.pth',
  model_dir='checkpoints', progress=True, file_name='Wav2Lip_GAN.pth')
model = load_model(os.path.join(working_directory,'checkpoints','Wav2Lip_GAN.pth'))
print('wav2lip_gan loaded')
load_file_from_url(
  url='https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/Wav2Lip.pth',
  model_dir='checkpoints', progress=True, file_name='Wav2Lip.pth')
model = load_model(os.path.join(working_directory,'checkpoints','Wav2Lip.pth'))
print('wav2lip loaded')

#download gfpgan files
print("downloading gfpgan essentials")
load_file_from_url(
  url='https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/GFPGANv1.4.pth',
  model_dir='checkpoints', progress=True, file_name='GFPGANv1.4.pth')
load_sr()

#load face detectors
print('initializing face detectors')
load_file_from_url(
  url='https://github.com/anothermartz/Easy-Wav2Lip/releases/download/Prerequesits/shape_predictor_68_face_landmarks_GTX.dat',
  model_dir='checkpoints', progress=True, file_name='shape_predictor_68_face_landmarks_GTX.dat')

load_predictor()

#write a file to signify setup is done
with open('installed.txt', 'w') as f:
    f.write(args.ver)
print("Installation complete!")
print('If you just updated from v8 - make sure to download the updated Easy-Wav2Lip.bat too!')
