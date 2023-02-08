import calendar

import qrcode
import sys
import time


def get_time() -> str:
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    return str(time_stamp)


def generate_qrcode(text=None):
    if text is None:
        text = sys.argv
    qr = qrcode.make(sys.argv)
    qr.save(f"qrcode{get_time()}.jpg")


generate_qrcode()
