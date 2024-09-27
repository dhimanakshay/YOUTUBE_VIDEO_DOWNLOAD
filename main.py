import tkinter as tk
from tkinter import filedialog
import yt_dlp

# Function to download a YouTube video
def download_video(video_url, save_directory):
    try:
        # Set options for downloading the video
        download_options = {
            'format': 'best',  # Download the highest quality available
            'outtmpl': f'{save_directory}/%(title)s.%(ext)s',  # Define the saving pattern (title and extension)
        }

        # Using yt_dlp to handle the video download process
        with yt_dlp.YoutubeDL(download_options) as downloader:
            downloader.download([video_url])

        print("Download complete!")
    except Exception as error:
        print(f"An error occurred: {error}")

# Function to open a folder selection dialog
def choose_save_location():
    folder_path = filedialog.askdirectory()  # Open a dialog for the user to choose a folder
    if folder_path:
        print(f"Folder chosen: {folder_path}")
    return folder_path

# Main section of the program
if __name__ == "__main__":
    root = tk.Tk()  # Initialize the Tkinter window
    root.withdraw()  # Hide the main Tkinter window

    video_link = input("Enter the YouTube video link: ")  # Get the video URL from the user
    chosen_folder = choose_save_location()  # Ask the user to choose where to save the video

    if chosen_folder:  # Proceed only if a valid folder is selected
        print("Starting the download...")
        download_video(video_link, chosen_folder)
    else:
        print("No valid folder selected. Exiting...")
