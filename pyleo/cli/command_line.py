import argparse
import csv
import sys
from pyleo.cli.utils import progress
from pyleo.utils import TokenBucket
from pyleo.api import LeoApi


def main():
    """
    Process upload action
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, help='perform given action', choices=['upload', 'test'])

    parser.add_argument('--file', '-f', type=str, action='store', help='csv file to upload')
    parser.add_argument('--user', '-u', type=str, action='store', help='LinguaLeo username')
    parser.add_argument('--password', '-p', type=str, action='store', help='LinguaLeo password')

    args = parser.parse_args()
    file_name = args.file
    user_name = args.user
    password = args.password

    api_instance = LeoApi(user_name, password)
    if api_instance.need_auth:
        api_instance.auth()

    if args.command:
        if args.command == 'upload':
            bucket = TokenBucket(5, 1)
            print("Action: UPLOAD \nFile: {0} ".format(file_name))

            with open(file_name, newline='') as f:
                total = sum(1 for line in f) - 1

            with open(file_name, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(reader, None)  # skip headers

                for idx, row in enumerate(reader, start=1):
                    while True:
                        if bucket.consume(2):
                            api_instance.add_word(row[0], row[1].split(',')[0]).decode('utf-8')
                            progress(idx, total, status='Uploading')
                            continue
                        break
                print('\nDone')

        elif args.command == 'test':
            sys.stdout.write('test')
    else:
        print(file_name)


if __name__ == '__main__':
    main()
