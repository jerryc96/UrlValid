from extract.extractCSV import *
from transform.transform import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urlFrame = readCSV()
    checkValidUrls(urlFrame)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
