from ntplib import *
from time import ctime

ntp_client = NTPClient()
attempts = 0

while attempts < 3:
    try:
        response = ntp_client.request('pool.ntp.org')
        print (ctime(response.tx_time))
        break
    except:
        attempts += 1
        print('Fetching ntp failed.')

times_file = open('times.txt', 'r')
times = times_file.readlines()
