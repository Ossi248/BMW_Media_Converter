#
# BMW AudioConverter
#
# Authors: Colin Böttger
#

import converter

from gui.gui import GUI


def done():
    print("DONE")


def main():
    gui = GUI('BR3/4/5 Converter', (500,400))
    converter.convert_directory_parallel("./test", "./hallo", done, print, 4)

if __name__ == '__main__':
    main()