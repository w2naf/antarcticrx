#!/usr/bin/env python
import os

cmd = '/usr/bin/terminator --command="/bin/bash -c \'/usr/local/bin/rx_recorder.py; /bin/bash\'"'
print(cmd)
os.system(cmd)
