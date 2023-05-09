import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/David Brum/Desktop/loljinha/imagem"

class FileEventHandler(FileSystemEventHandler):
    def on_created(Self, event):
        print("Ola, {event.src_path} foi criado")

    def on_created(Self, event):
        print("Papai amado alguem excluiu {event.src_path} agora fomos de base!")

    def on_created(Self, event):
        print("eae ze, {event.src_path} foi modificado")

    def on_created(Self, event):
        print("Eita rapaiz moveram, {event.src_path} para {event.dest_path}")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("Interrompido!")
    observer.stop()