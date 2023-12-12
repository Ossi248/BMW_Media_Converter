from os import path, remove

extensionMap = {
    ".mp3": ".br4",
    ".br4": ".mp3"
}


def convert_file_bitwise(src: str, dest: str):
    if not path.exists(src):
        raise Exception(f"The File {src} does not exitst")
    try:
        tar = open(dest, "+bw")
        with open(src, "rb") as file:
            byte = file.read(1024)
            while byte:
                arr = bytearray(byte)
                for i in range(len(arr)):
                    arr[i] ^= 0xFF
                tar.write(arr)
                byte = file.read(1)
        tar.close()
    except Exception as e:
        remove(dest)
        raise e


def convert_file(src: str, dest: str):
    name, ext = path.splitext(src)
    try:
        result = f"{dest}{path.basename(src).replace(ext,extensionMap[ext])}"
    except Exception as e:
        print(e)
        raise Exception(f"Unkown extension {ext}")
    convert_file_bitwise(src, result)
