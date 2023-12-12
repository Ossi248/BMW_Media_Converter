from typing import Callable

from converter.converter import convert_file

def convertDirectoryAsync(src:str,dest:str,finish: Callable,progress:Callable[[int],None]):
    pass