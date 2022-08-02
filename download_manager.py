#!/usr/local/bin/python3
import os
import shutil
import time

import magic
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

DOWNLOADS_DIR_PATH = "/Users/klemen/Downloads"


class Watcher:
    dir_to_watch: str
    observer: Observer

    def __init__(self, dir_to_watch: str) -> None:
        self.dir_to_watch = dir_to_watch
        self.observer = Observer()

    def run(self) -> None:
        event_handler = Handler()
        self.observer.schedule(event_handler, self.dir_to_watch, recursive=False)
        self.observer.start()
        while True:
            time.sleep(2)

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == "created":
            if event.is_directory:
                dir_name = event.src_path.split("/")[-1]
                os.makedirs(f"{DOWNLOADS_DIR_PATH}/downloaded_folders", exist_ok=True)
                shutil.move(event.src_path, f"{DOWNLOADS_DIR_PATH}/downloaded_folders/{dir_name}")
                return None
            filename = event.src_path.split("/")[-1]
            if filename.startswith(".") or filename.endswith(".crdownload"):
                return
            if "TMPtmp" in filename:
                shutil.move(event.src_path, f"/tmp/{filename}")
            else:
                filetype = mime.from_file(event.src_path)
                file_dir = f"{filetype.split('/')[0]}s"
                os.makedirs(f"{DOWNLOADS_DIR_PATH}/{file_dir}", exist_ok=True)
                shutil.move(event.src_path, f"{DOWNLOADS_DIR_PATH}/{file_dir}/{filename}")


if __name__ == "__main__":
    mime = magic.Magic(mime=True)
    w = Watcher(dir_to_watch=DOWNLOADS_DIR_PATH)
    w.run()
