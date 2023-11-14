import librosa
from pathlib import Path
import os


SAMPLE_RATE:int = 16100

class FilesIterator:
    def __init__(self, dir_path: Path):
        self.dir_path: Path = dir_path
        self.files: list = os.listdir(self.dir_path)
        self.file_max_number: int = len(self.files)
        self.current_file_number: int = 0

    def __iter__(self):
        return self
    
    def __next__(self) -> tuple:
        if self.current_file_number < self.file_max_number:
            return self._load_data(self.files[self.current_file_number])
        raise StopIteration

    def _load_data(self, file_path: Path) -> tuple:
        self.current_file_number += 1
        return librosa.load(self.dir_path / file_path, sr=SAMPLE_RATE)
