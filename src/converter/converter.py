from os import path , remove

def convert_file_bitwise(src:str, dest:str):
    if not path.exists(src):
        raise Exception(f"The File {src} does not exitst")
    try:
        tar = open(dest,"+bw") 
        with open(src, "rb") as file:
            byte = file.read(1)
            while byte:
                tar.write(~byte)
                byte = file.read(1)
        tar.close()
    except Exception as e:
        remove(dest)
        raise e
    
def convert_file(src:str, dest:str):
    print(path.splitext(src))
    