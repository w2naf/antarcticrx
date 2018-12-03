import datetime

# WSPR Ham Radio Frequencies
#  1.8366 MHz
#  3.5686 MHz
#  5.2872 MHz
#  7.0386 MHz
# 10.1387 MHz
# 14.0956 MHz
# 18.1046 MHz
# 21.0946 MHz
# 24.9246 MHz
# 28.1246 MHz
# 50.2930 MHz

rxs = []
rxs.append({'label':  'CHU_3300',  'frequency':  3.3300e6})
rxs.append({'label': 'WSPR_3568',  'frequency':  3.5686e6})
rxs.append({'label':  'CHU_7850',  'frequency':  7.8500e6})
rxs.append({'label': 'WSPR_7038',  'frequency':  7.0386e6})
rxs.append({'label':  'CHU_14670', 'frequency': 14.6700e6})
rxs.append({'label': 'WSPR_14095', 'frequency': 14.0956e6})

rx_samp_rate    = 48000 # 48000, 96000, or 192000 kHz
metadata        = {'station':'MCM','rx':'Red Pitaya','ant':'DXE RF-PRO-1B'}

working_dir     = "/media/icerx/ICERX/hf_data"

ringbuffer_size = '900GB'
