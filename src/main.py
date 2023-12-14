#
# BMW AudioConverter
#
# Authors: Colin Böttger
#

import converter

from gui.gui import GUI

from time import sleep

def done():
    print("DONE")


def main():
    gui = GUI('BR3/4/5 Converter', (500,400))
    join,abort= converter.convert_directory_parallel("./test", "./hallo", done, print, 4)
    print("Hallo")
    sleep(5)
    abort()
    join()
    print("test")

    
if __name__ == '__main__':
    main()
