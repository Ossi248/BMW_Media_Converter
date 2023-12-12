from typing import Callable, List
from os import walk, path
from converter.converter import extensionMap
from multiprocessing import Process
from time import sleep


def convert_directory_parallel(src: str, dest: str, finish: Callable, progress: Callable[[int], None]):
    if not path.exists(src):
        raise Exception("Input Path does not exist")
    inp = []
    for p, _, f in walk(src):
        inp.extend(tryCreateFileList(p, f))
    worker = split_up(4, inp)
    execute_worker(worker, dest, finish, progress)
    pass


def worker(id: int, work: List[List[str]], target, progress: Callable[[int], None]):
    for w in work:
        sleep(1)
        progress(id)
        print(w)
    pass


def execute_worker(work: List[List[str]], target: str, finish: Callable, progress: Callable[[int], None]):
    workers = []
    for i, w in enumerate(work):
        p = Process(target=worker, args=[i, w, target, progress])
        p.start()
        workers.append(p)
    for p in workers:
        p.join()
    finish()
    pass


def split_up(workerCount: int, paths: List[str]):
    res: List[List[str]] = []
    s = len(paths)
    chs = s // workerCount
    print(s)
    print(chs)
    for i in range(0, s, chs):
        res.append(paths[i:i+chs])
    if len(res) != workerCount:
        x = res.pop()
        res[-1].extend(x)
    return res


def tryCreateFileList(dir: str, files: List[str]):
    res = []
    for f in files:
        _, ext = path.splitext(f)
        try:
            extensionMap[ext]
            res.append(dir+f)
        except:
            pass
    return res
