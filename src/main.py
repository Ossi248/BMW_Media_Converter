#
# BMW AudioConverter
#
# Authors: Colin Böttger
#

import converter
from time import sleep

def done():
    print("DONE")


join,abort= converter.convert_directory_parallel("./test", "./hallo", done, print, 4)
print("Hallo")
sleep(5)
abort()
join()
print("test")
