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
image_extensions = [".jpg", ".png", ".svg", ".gif", ".jpeg"]
documents_extensions = [".ppt", ".docx", ".xls", ".md", ".html", ".xml"]


def is_music(filename: str) -> bool:
    for extension in music_extensions:
        if filename.endswith(extension):
            return True
        else:
            continue
    return


def is_video(filename: str) -> bool:
    for extension in video_extensions:
        if filename.endswith(extension):
            return True
        else:
            continue
    return


def is_ebook(filename: str) -> bool:
    for extension in ebook_extensions:
        if filename.endswith(extension):
            return True
        else:
            continue
    return


def is_image(filename: str) -> bool:
    for extension in image_extensions:
        if filename.endswith(extension):
            return True
        else:
            continue
    return



def is_document(filename: str) -> bool:
    for extension in documents_extensions:
        if filename.endswith(extension):
            return True
        else:
            continue
    return


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
                        shutil.move(f"{path}/{filename}",
                                    "/home/victorchiaka/Music/")
                    except FileNotFoundError:
                        print(f"The {filename} file does does not exist")

                elif is_video(filename):
                    try:
                        shutil.move(f"{path}/{filename}",
                                    "/home/victorchiaka/Videos/")
                    except FileNotFoundError:
                        print(f"The {filename} file does does not exist")

                elif is_image(filename):
                    try:
                        shutil.move(f"{path}{filename}",
                                    "/home/victorchiaka/Pictures/")
                    except FileNotFoundError:
                        print(f"The {filename} file does does not exist")
                        
                elif is_ebook(filename):
                    try:
                        shutil.move(f"{path}/{filename}",
                                    "/home/victorchiaka/my-books/")
                    except FileNotFoundError:
                        print(f"The {filename} file does does not exist")


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
