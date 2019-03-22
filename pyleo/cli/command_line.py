import argparse
import time
import sys
from pyleo.cli.utils import progress
from pyleo.utils import get_or_create_node, TokenBucket


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
            bucket = TokenBucket(5, 1)
            print("Action: UPLOAD \nFile: {0} ".format(file_name))
            total = 10
            i = 0
            while i < total + 1:
                while True:
                    bucket.get_tokens()
                    if bucket.consume(2):
                        time.sleep(0.1)
                        progress(i, total, status='Uploading')
                        i += 1
                        continue
                    break

            print('\nDone')
        elif args.command == 'test':
            sys.stdout.write('test')
    else:
        print(file_name)


if __name__ == '__main__':
    main()
