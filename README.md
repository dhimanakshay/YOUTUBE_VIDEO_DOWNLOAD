YouTube Video Downloader
This is a Python-based YouTube video downloader that lets you save videos directly to your computer. It features a simple graphical interface for selecting where to save the video and uses the powerful yt-dlp library to ensure you get the best available video quality.

Features:
Download videos in the highest quality: Automatically downloads the best available resolution.
Choose where to save videos: You can select your preferred folder for saving the downloaded videos.
User-friendly interface: Uses a basic graphical file picker to choose the download location.
How to Use
Prerequisites:
Before running the program, you need to make sure you have Python installed. Also, install the required library by running:

bash
pip install yt-dlp
Running the Program:
Clone or download this repository to your local machine.
Open a terminal or command prompt and navigate to the folder where the script is located.
Run the script with Python:
bash
Copy code
python main.py
When prompted, paste the YouTube video URL.
A dialog box will pop up asking you to select the folder where you want to save the video.
The program will then download the video to the selected folder.
Example:
bash
Copy code
Please enter a YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Selected folder: C:/Users/YourName/Downloads
Started download...
Download complete!
Known Issues:
If the download fails, it's likely due to an unsupported video format or a change in YouTube's website. Make sure you have the latest version of yt-dlp installed by running:
bash

pip install --upgrade yt-dlp
Credits:
This project uses the yt-dlp library, which is an actively maintained tool for downloading YouTube content. Big thanks to the yt-dlp community for keeping this up to date!

License:
This project is open-source. Feel free to use, modify, and share it as you wish.
