#
# BMW AudioConverter
#
# Authors: Colin Böttger
#

import converter


def done():
    print("DONE")


converter.convert_directory_parallel("./test", "./hallo", done, print, 4)
