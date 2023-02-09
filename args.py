import getopt
import sys
import qrcode
import time
import calendar

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hco:"

# Long options
long_options = ["Help", "Create", "Output="]


def get_time() -> str:
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    return str(time_stamp)


def generate_qrcode(text=None):  # todo: make this ask for dir
    # if text is None:  # del this
    #     text = sys.argv  # try: if text is None
    qr = qrcode.make(text)
    qr_name = f"qrcode{text}{get_time()}.jpg"
    qr.save(qr_name)
    print(f"created {qr_name}")


try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print("Displaying Help")

        elif currentArgument in ("-c", "--Create"):
            print("creating", sys.argv[2] if sys.argv[1] == "-c" else "todo")
            generate_qrcode(sys.argv[2])

        elif currentArgument in ("-o", "--Output"):
            print("Enabling special output mode (% s)" % currentValue)

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))

# todo make this main
