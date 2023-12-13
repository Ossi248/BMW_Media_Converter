from typing import Callable, List
from os import walk, path
from converter.converter import extensionMap, convert_file
from multiprocessing import Process, Lock, Manager
from time import sleep


def convert_directory_parallel(src: str, dest: str, finish: Callable, progress: Callable[[int], None], workercount=4):
    if not path.exists(src):
        raise Exception("Input Path does not exist")
    inp = []
    for p, _, f in walk(src):
        inp.extend(tryCreateFileList(p, f, src, dest))
    w = split_up(workercount, inp)
    WorkerPool(w, len(inp), finish, progress)


def split_up(workerCount: int, paths: List[str]):
    res: List[List[str]] = []
    s = len(paths)
    chs = s // workerCount
    for i in range(0, s, chs):
        res.append(paths[i:i+chs])
    if len(res) != workerCount:
        x = res.pop()
        res[-1].extend(x)
    return res


def tryCreateFileList(d: str, files: List[str], src: str, out: str):
    res = []
    l = d.replace(src, '')[1:]
    for f in files:
        _, ext = path.splitext(f)
        try:
            extensionMap[ext]
            res.append((path.join(d, f), path.join(out, l)))
        except:
            pass
    return res


class WorkerPool:
    lock = Lock()
    manager = Manager()

    work = 0
    cbProgress: Callable[[int], None]

    def __init__(self, work: List[List[str]], workcount: int, finish: Callable, progress: Callable[[int], None]):
        workers = []
        self.done = self.manager.Value('i', 0)
        self.work = workcount
        self.cbProgress = progress

        for w in work:
            p = Process(target=self.worker, args=[w])
            p.start()
            workers.append(p)

        for p in workers:
            p.join()

        finish()

    def worker(self, work):
        for s, t in work:
            convert_file(s, t)
            with self.lock:
                self.done.value += 1
                self.cbProgress(self.done.value/self.work)
