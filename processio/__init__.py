from multiprocessing import Pool
import multiprocessing


class ProcessIO:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.pool = Pool(processes=1)
        self.process = self._start_process()

    def _start_process(self):
        return self.pool.apply_async(self.func, args=self.args, kwds=self.kwargs)

    def doing_work(self):
        if not self.process.ready():
            return True
        return False

    def result(self):
        return self.process.get()


class ParseIO:
    def __init__(self, func, items, processes=False):
        if not processes:
            processes = multiprocessing.cpu_count() - 1
        self.func = func
        self.items = items
        self.processes = processes
        self.pool = Pool(processes=processes)
        self.workers = []
        self.amount = int(len(items) / processes)
        self.end = self.amount
        self.start = 0
        self.job_result = []
        self.start_work = self._run()

    def _run(self):
        for i in range(self.processes):
            if i + 1 == int(self.processes):
                self.end = len(self.items)
            worker = self.pool.apply_async(self.func, [self.items[self.start:self.end]])
            self.workers.append(worker)
            self.start += self.amount
            self.end += self.amount
        return True

    def status(self, string=True, json=False):
        active = 0
        for worker in self.workers:
            if not worker.ready():
                active += 1

        if json:
            return {'active': active, 'total': self.processes}

        if string:
            return f'{active} of {self.processes} threads working'

    def doing_work(self):
        for worker in self.workers:
            if not worker.ready():
                return True
        return False

    def result(self) -> list:
        for worker in self.workers:
            res = worker.get()
            self.job_result.append(res)

        self.pool.close()

        return self.job_result
