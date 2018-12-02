#!/usr/bin/env python
import os
from antarcticrx.config import working_dir, ringbuffer_size

#cmd = '/usr/bin/terminator --command="/bin/bash -c \'/usr/local/bin/drf ringbuffer -z 800GB /media/icerx/icerx/hf_data; /bin/bash\'"'
cmd = '/usr/bin/terminator --command="/bin/bash -c \'/usr/local/bin/drf ringbuffer -z {!s} {!s}; /bin/bash\'"'.format(ringbuffer_size,working_dir)
print(cmd)
os.system(cmd)
