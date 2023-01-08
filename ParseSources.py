import glob
from pprint import pprint as pp
import re

patern = '["<](.+?)[>"]'

prefix = '..\\my\\'
headers = glob.glob(prefix +"*.h")
sources = glob.glob(prefix +"*.cpp")

hdr_set = {hdr.removeprefix(prefix).lower() for hdr in headers}
src_set = {src.removeprefix(prefix) for src in sources }

for src in sources:
    print(src.removeprefix(prefix))
    with open(src) as file:
        lines = [line.strip() for line in file]
        for l in lines:
            if l.startswith('#include'):
                inc = l.removeprefix('#include').strip()
                f = re.search(patern, inc)
                if f:
                    inc = f.group(1)
                else:
                    print('\t*** \t Error in #include\a', inc)

                if inc.lower() not in hdr_set:
                    print('\t', inc)

print('\t\a')
