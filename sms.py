from __future__ import print_function
from __future__ import print_function
import requests




def send_sms1(mobile, msg, sender="PHLKDM"):
    authkey =  '125195AnE7snTWFepK5925ea7c'
    url = 'http://api.msg91.com/api/sendhttp.php?authkey=' + authkey + '&mobiles='
    url += mobile
    url += '&message=' + msg
    url += '&sender=' + sender + '&route=4'
    print(url)
    print(requests.request('GET', url))


