from files_iterator.files_iterator import FilesIterator
from argparse import ArgumentParser
from pathlib import Path


class AudioPreprocessing:
    def __init__(self, parsed_data: dict):
        self.data = FilesIterator(parsed_data.get('data_input'))
    
    def preprocess(self):
        for audio in self.data:
            print(audio)

def parse_input():
    parser = ArgumentParser()
    parser.add_argument('-i', '--data_input', dest='data_input', type=str, required=True)
    arguments = parser.parse_args()

    return {
        'data_input': Path(arguments.data_input)
    }

if __name__ == '__main__':
    preprocessor = AudioPreprocessing(parse_input())
    preprocessor.preprocess()
