rxs = []
rxs.append({'label': 'CHU_3300',  'frequency':  3.330e6})
rxs.append({'label': 'HAM_3596',  'frequency':  3.596e6})
rxs.append({'label': 'CHU_7850',  'frequency':  7.096e6})
rxs.append({'label': 'HAM_7096',  'frequency':  7.096e6})
rxs.append({'label': 'CHU_14670', 'frequency': 14.670e6})
rxs.append({'label': 'HAM_14096', 'frequency': 14.096e6})
rxs.append({'label': 'WWV_10050', 'frequency': 10.050e6})

rx_samp_rate    = 192000
metadata        = {'call':'W2NAF','grid':'<6-digit-grid>','rx':'Red Pitaya','ant':'DXE RF-PRO-1B'}

working_dir     = "/media/icerx/icerx/"
ringbuffer_size = '800GB'
