# listen for simple changes in the downloads folder, changes are new file(s) added
# detect the type of event that is going on
# check the extension of the file to detemine the file type
# depending on the file type, move it to a more likely directory

# clean up the code and improve on it


# to resolve my issue with the shifting of files : https://stackoverflow.com/questions/60695881/how-to-check-if-the-file-is-completely-downloaded-in-a-folder-using-python

import os
import time
import shutil
from watchdog.events import FileSystemEventHandler
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

music_extensions = [
    ".mp3", ".wav", ".wma", ".aac", ".flac", ".ogg", ".pcm", ".aiff", ".alac"]
video_extensions = [".mp4", ".mov", ".avi", ".avchid",
                    ".flv", ".f4v", ".swf", ".mkv", ".webm", ".mpeg-2"]
ebook_extensions = [".pdf", ".epub"]
# image_extensions = [".svg", ".gif", ".jpeg", ".jpg", ".png"]
image_extensions = [".jpg", ".png",".svg", ".gif", ".jpeg"]
documents_extensions = [".ppt", ".docx", ".xls", ".md", ".html", ".xml"]


def is_music(filename: str) -> bool:
    for extension in music_extensions:
        return filename.endswith(extension)


def is_video(filename: str) -> bool:
    for extension in video_extensions:
        return filename.endswith(extension)


def is_ebook(filename: str) -> bool:
    for extension in ebook_extensions:
        return filename.endswith(extension)


def is_image(filename: str) -> bool:
    for extension in image_extensions:
        return filename.endswith(extension)



def is_document(filename: str) -> bool:
    for extension in documents_extensions:
        return filename.endswith(extension)


# This class handles the events when it detects an even in the directory, the class will be passed as a parameter to the observer.schedule() in the top code


class MyEventHandler(FileSystemEventHandler):

    path = "/home/victorchiaka/Downloads/"

    def is_download_completed(path: str, filename: str) -> bool:
        file_size = -1
        while True:
            file_size = os.stat(path + filename)
            time.sleep(2)
            if file_size == file_size:
                return True
            else:
                return False
            
    def on_created(self, event):
        
        for root, dirs, files in os.walk(path):
            for filename in files:

                if is_music(filename):
                    try:
                        shutil.move(path + filename,
                                    "/home/victorchiaka/Music/")
                    except FileNotFoundError:
                        logging.warning(
                            f"file {path + filename} does not exist")

                elif is_video(filename):
                    try:
                        shutil.move(path + filename,
                                    "/home/victorchiaka/Videos/")
                    except FileNotFoundError:
                        logging.warning(
                            f"file {path + filename} does not exist")

                elif is_image(filename):
                    try:
                        shutil.move(path + filename,
                                    "/home/victorchiaka/Pictures/")
                    except FileNotFoundError:
                        logging.warning(
                            f"file {path + filename} does not exist")
                        
                elif is_ebook(filename):
                    try:
                        shutil.move(path + filename,
                                    "/home/victorchiaka/my-books/")
                    except FileNotFoundError:
                        logging.warning(
                            f"file {path + filename} does not exist")

                # else:
                #     logging.info(
                #         f"this file {filename} does not have a folder for the filetype"
                #     )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "/home/victorchiaka/Downloads/"
    event_handler = LoggingEventHandler()
    observer = Observer()

    my_handler = MyEventHandler()

    observer.schedule(my_handler, path, recursive=True)
    time.sleep(10)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
