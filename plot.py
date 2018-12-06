#!/usr/bin/env python3
import os
import datetime

path        = '/home/icerx-vm/ICERX/hf_data'
samp_rate   = 48000
center_freq = 14095600
channel     = 'WSPR_14095'
sTime       = datetime.datetime(2018,12,4,20,8,50)
secs        = 8
samp_1      = samp_rate*secs

#cmd = 'drf_plot.py -i /home/icerx-vm/ICERX/hf_data -a 2018-12-04T20:08:00 -o 14095000 -p specgram -c WSPR_14095 -r 0:8000000 -b 1024 -l -s specgram.png'
cmd = 'drf_plot.py -i {!s} -a {!s} -o {:.0f} -p specgram -c {!s} -r 0:{:.0f} -b 1024 -l -s specgram.png'.format(path,sTime.isoformat(),center_freq,channel,samp_1)
os.system(cmd)
