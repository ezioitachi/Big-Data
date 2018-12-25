# python3
import heapq


class Worker:

    def __init__(self, thread_id, release_time=0):
        self.id = thread_id
        self.time = release_time

    def __lt__(self, other):           #自定义大小比较
        if other.time == self.time:
            return self.id < other.id
        return self.time < other.time

    def __gt__(self, other):
        if other.time == self.time:
            return self.id > other.id
        return self.time > other.time


class JobQueue:

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.result = []
        assert m == len(self.jobs)

    def write_response(self):
        for i in self.result:
            print(i[0], i[1])

    def assign_jobs(self):
        
        self.assigned_workers = [Worker(i)for i in range(self.num_workers)]

        for job in self.jobs:
            worker = heapq.heappop(self.assigned_workers)   #数组中取出最小值
            self.result.append((worker.id, worker.time))
            worker.time += job
            heapq.heappush(self.assigned_workers, worker)   #将item压入到数组中

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
