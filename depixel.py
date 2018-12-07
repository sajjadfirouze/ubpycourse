import os
import sys

# sys.argv = list(map(str, input().split())) # if you want run in pycharm
for i in sys.argv[1:]:
    os.system("potrace -b svg -b pdf " + i)
