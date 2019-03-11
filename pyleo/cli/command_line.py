import argparse
import time
from pyleo.cli.utils import progress


def main():
    """
    Temporary stub
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, help='perform given action', choices=['upload', 'pass'])

    parser.add_argument('--file', '-f', type=str, action='store', help='csv file to upload')
    args = parser.parse_args()
    file_name = args.file
    if args.command:
        if args.command == 'upload':
            print("Action: UPLOAD \nFile: {0} ".format(file_name))

            total = 1000
            i = 0
            while i < total + 1:
                progress(i, total, status='Uploading')
                time.sleep(0.01)
                i += 1
            print('\nDone')
    else:
        print(file_name)


if __name__ == '__main__':
    main()
