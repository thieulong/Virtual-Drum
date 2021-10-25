# Virtual-Drum# Sleep-Prevention
A program using your device's webcam to track your fingertip as a drumstick and you'll be able to play the drum virtually through the video from your webcam.
### 1. Clone the project
You'll first need to clone this project by running the following command  

`git clone https://github.com/thieulong/Virtual-Drum.git`  

**Note**: Make sure you have Github installed on your system. If not, check out [***this site***](https://gist.github.com/derhuerst/1b15ff4652a867391f03)  

### 2. Install requirements
To run the code file, some of the requirements need to be installed, run this command (in this Github directory) to install all of the neccessary requirements.  
  
`pip3 install -r requirements.txt`
  
### 3. Run the project
Navigate to this Github directory, run  

`python3 virtual_drum.py`  

and the project will start using your device's webcam to track your fingertip, remember to show your hand in the webcam range.
  
**Note**: If you encounter a *Can't open camera by index* error, try to change the camera index base on your device's webcam index (Usually happends when you have another plug-in webcam)
  
Change the camera index (line 10) in *virtual_drum.py* file. If you have no idea what your camera index is, try to replace 0 with any number from 1 and going up.
  
You can minimize the tracking window while you're working. Stop the program by pressing the ESC button.
