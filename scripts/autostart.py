#!/usr/bin/env python
import os

cmd = '/usr/bin/terminator --command="/bin/bash -c \'/usr/local/bin/start_rx_all.py; exit\'"'
print(cmd)
os.system(cmd)
