import datetime

# WSPR Ham Radio Frequencies (For reference only)
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

# CHU Radio Frequencies (For reference only)
#  3.3300 MHz
#  7.8500 MHz
# 14.6700 MHz

# Receiver list in Hz; List up to 7 center frequencies.
rxs = [] 
rxs.append( 3.3300e6) # 80 m CHU
rxs.append( 3.5686e6) # 80 m Ham-WSPR
rxs.append( 7.8500e6) # 40 m CHU
rxs.append( 7.0386e6) # 40 m Ham-WSPR
rxs.append(14.6700e6) # 20 m CHU
rxs.append(14.0956e6) # 20 m Ham-WSPR

rx_samp_rate    = 48000 # 48000, 96000, or 192000 kHz

# You can put as many metadata key:value pairs here as you like.
metadata        = {'station':'MCM','rx':'Red Pitaya','ant':'DXE RF-PRO-1B'}

# This is where the data is stored.
working_dir     = "/media/icerx/ICERX/hf_data"

# Maximum size of the ringbuffer.
ringbuffer_size = '900GB'
