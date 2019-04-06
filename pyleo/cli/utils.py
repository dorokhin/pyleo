import sys


def progress(count, total, status='', bar_len=60):
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    if count == total:
        percents = 100.0
    bar = '█' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[{bar}] {percent} %   {status}\r'.format(bar=bar, percent=percents, status=status))
    sys.stdout.flush()
