import calendar
import qrcode
import sys
import time


def get_time() -> str:
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    return str(time_stamp)


def generate_qrcode(text=None):  # todo: make this ask for dir
    if text is None:
        try:
            text = sys.argv
        except:
            print("Something went wrong")
        finally:
            print("The 'try except' is finished")
    qr = qrcode.make(text)
    qr.save(f"{text}qrcode{get_time()}.jpg")
    print("generated")
    # resolve this


class QrGenerator:
    def __init__(self):
        print("init")

    # add text on bottom of qrcode


generate_qrcode()
