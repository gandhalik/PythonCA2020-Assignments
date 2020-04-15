import sys

for file in sys.argv[1:]:
    try:
        f = open(file, 'r')
    except IOError:
        print('cannot open', file)