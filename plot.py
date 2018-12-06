#!/usr/bin/env python3
import os
import datetime

path        = '/media/icerx/ICERX/hf_data'
center_freq = 3568600
sTime       = datetime.datetime(2018,12,6,3,58)
secs        = 60
samp_rate   = 48000
samp_1      = samp_rate*secs

#cmd = 'drf_plot.py -i /home/icerx-vm/ICERX/hf_data -a 2018-12-04T20:08:00 -o 14095000 -p specgram -c WSPR_14095 -r 0:8000000 -b 1024 -l -s specgram.png'
cmd = 'drf_plot.py -i {!s} -a {!s} -o {:.0f} -p specgram -c {:.0f} -r 0:{:.0f} -b 1024 -l -s specgram.png'.format(
        path,sTime.isoformat(),center_freq,center_freq,samp_1)
os.system(cmd)
