from ntplib import *
from time import ctime

ntp_client = NTPClient()
attempts = 0

# Get the right time from (local) NTP server
while attempts < 3:
    try:
        response = ntp_client.request('pool.ntp.org')
        print (ctime(response.tx_time))
        break
    except:
        attempts += 1
        print('Fetching ntp failed.')

# Get configured times
times_file = open('times.txt', 'r')
times = times_file.readlines()

# Get next closest time.

# Calculate time remaining in seconds.

# Loop
    # Display time remaining in gpio ports.

    # wait one second and decrease time left with 1 second

    # Is minutes and seconds 00 00?
    #   TRY to Recalculate time remaining based on NTP time.