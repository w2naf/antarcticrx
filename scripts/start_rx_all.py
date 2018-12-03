#!/usr/bin/env python
import os
from antarcticrx.config import working_dir, ringbuffer_size

def launch_separate_terminal(cmd):
    """Launches a terminal command in a new window."""
    cmd = '/usr/bin/terminator --command="/bin/bash -c \'{!s}; /bin/bash\'"'.format(cmd)
    print(cmd)
    os.system(cmd)

# Make sure the working directory is created.
data_dir = os.path.join(working_dir)
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Start the ringbuffer.
cmd = '/usr/local/bin/drf ringbuffer -z {!s} {!s}'.format(ringbuffer_size,working_dir)
launch_separate_terminal(cmd)

# Start the radio recorder.
cmd = '/usr/local/bin/rx_recorder.py'
launch_separate_terminal(cmd)

# Log GPS Time and Location.
cmd = '/usr/local/bin/gps_recorder.py'
launch_separate_terminal(cmd)
