import argparse
import time
import sys
from pyleo.cli.utils import progress
from pyleo.utils import get_or_create_node


def main():
    """
    Temporary stub
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, help='perform given action', choices=['upload', 'test'])

    parser.add_argument('--file', '-f', type=str, action='store', help='csv file to upload')
    args = parser.parse_args()
    file_name = args.file
    if args.command:
        if args.command == 'upload':
            print("Action: UPLOAD \nFile: {0} ".format(file_name))

            total = 150
            i = 0
            while i < total + 1:
                progress(i, total, status='Uploading')
                time.sleep(0.01)
                i += 1
            print('\nDone')
        elif args.command == 'test':
            sys.stdout.write('test')
    else:
        print(file_name)


if __name__ == '__main__':
    main()
