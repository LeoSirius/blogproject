import random

# adj list
adjs = ['white', 'black', 'ugly', 'beautiful', 'big', 'great', 'fancy']
# job list
jobs = ['soldier', 'emperor', 'robber', 'ranger', 'hunter', 'sailor']
# location list
locs = ['London', 'China', 'Sparta', 'Rome']

name_set = set()

def gen_triple_name():
    """
    设计思路：
    基本思路是不断枚举，用hash表防止重复

    1. 先在名字三部分的索引范围内生成三个随机索引p1, p2, p3
    2. 如果有重复的，则p1,p2,p3分别加1

    这样最多可以生成len(adjs) * len(jobs) * len(locs)个不同的名字
    """
    global name_set
    adj_size, job_size, loc_size = len(adjs), len(jobs), len(locs)
    p1 = random.randint(0, adj_size-1)
    p2 = random.randint(0, job_size-1)
    p3 = random.randint(0, loc_size-1)
    name = f'{adjs[p1]} {jobs[p2]} from {locs[p3]}'

    try_circle = 0
    while name in name_set:

        if try_circle == 0:
            p1 = (p1 + 1) % adj_size
        elif try_circle == 1:
            p2 = (p2 + 1) % job_size
        elif try_circle == 2:
            p3 = (p3 + 1) % loc_size
        try_circle = (try_circle + 1) % 3
        name = f'{adjs[p1]} {jobs[p2]} from {locs[p3]}'

    name_set.add(name)
    return name

if __name__ == "__main__":
    for i in range(99):
        print(gen_triple_name())
