from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy import read
#import matplotlib.pyplot as plt   # matplotlib and its pyplot sub-package is used for plotting
#import numpy as np                # numpy is used for numerical computing and with arrays

client = Client("GFZ")

t1 = UTCDateTime.now()

start = t1 - 60*60*12
endtime = start + 60*60*12

try:
 wave1 = client.get_waveforms('PM', 'ROSA', '--', 'BHZ', start.replace(minute=0, second=1), endtime)
 wave1.filter('highpass', freq=0.2, corners=2, zerophase=True)
 #wave1.filter("bandpass", freqmin=0.12, freqmax=25.00, corners=3, zerophase=False)
 wave1.detrend(type='demean')
 wave1.detrend(type='linear')
 wave1.plot(type="dayplot", interval=30, size=(1360, 800), dpi=164, number_of_ticks=6, tick_rotation=45,
        right_vertical_labels=True,
        vertical_scaling_range=6e3, one_tick_per_line=True,
        color=['k', 'r', 'b', 'g'], show_y_UTC_label=True,
        outfile='PM/ROSA/PM_12H_ROSA_BHZ.png')
except Exception as e:
 print('Error while fetching: ', e)
