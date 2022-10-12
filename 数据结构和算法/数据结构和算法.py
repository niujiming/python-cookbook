"""
保存指定长度的历史记录
比如一个文件：
1
2
3
python
4
5
6
可以指定匹配字段python，指定长度为2，就可以输出2、3、python。
"""
from collections import deque


def search(lines, pattern, history=5):
    # 实例化一个指定长度的队列
    previous_lines = deque(maxlen=history)
    for _line in lines:
        if pattern in _line:
            # 匹配时，返回当前匹配line以及队列
            yield _line, previous_lines
        # 不匹配指定字段时，将当前line加入队列
        previous_lines.append(_line)


def example_1():
    with open('test') as f:
        for line, prev_lines in search(f, 'python', 5):
            # 匹配后打印队列里的值
            for prev_line in prev_lines:
                print(prev_line, end='')
            # 打印匹配行
            print(line, end='')


# example_1()
"""
deque，一个两端都可以操作的队列
使用appendleft()、popleft()可以操作队列左侧
实例化时使用maxlen:int 指定长度

通过yield将处理搜索过程的函数和使用搜索结果的函数解耦
"""

##############################################################################################
"""
返回队列、复杂数据的最大最小的N个数
"""
import heapq


def example_2():
    nums = [1, 2, 3, 4, 5, 6]
    # 找出最大的三个数
    print(heapq.nlargest(3, nums))
    # 找出最小的三个数
    print(heapq.nsmallest(3, nums))
    dic = {'k1': {'num': 1},
           'k2': {'num': 2},
           'k3': {'num': 3},
           'k4': {'num': 4},
           'k5': {'num': 5},
           'k6': {'num': 6}}
    # 可以指定参数key处理复杂数据，lambda参数s为,dic的key，通过lambda返回需要筛选的key
    # 注意实际返回为dic 的key，即k1、k2..
    print(heapq.nlargest(3, dic, key=lambda s: dic[s]['num']))


# example_2()

"""
优先级队列，根据优先级pop优先级最高的值
"""


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # (-priority, self._index, item) 队列已元祖形式组成
        # priority取负值保证队列是以从大到小排练，默认heapq排列是从小到大。
        # 引入 self._index用于处理相同优先级的值进行比较的情况，优先级相同时会按照self._index进行比较。
        # item为实际的值
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def example_3():
    queue = PriorityQueue()
    queue.push('k4', 4)
    queue.push('k1', 1)
    queue.push('k3', 3)
    queue.push('k2', 2)
    queue.push('k5', 5)
    print(queue.pop())
    print(queue.pop())


# example_3()

##############################################################################################

"""
字典上的键映射到多个值（list、tuple）
"""

from collections import defaultdict


def example_4():
    # 使用defaultdict创建字典可以自动初始化第一个值
    # 自动将值初始化为一个列表
    d = defaultdict(list)
    # 直接使用列表方法
    d['k1'].append(1)
    d['k1'].append(11)
    d['k2'].append(2)
    print(d['k1'])


# example_4()

##############################################################################################

"""
对字典值进行操作
"""


def example_5():
    d = {'k1': 789,
         'k2': 321,
         'k3': 456}
    # zip接收可迭代对象，并将所有值打包成元祖返回一个可迭代对象。
    t = zip(d.values(), d.keys())
    # 注意如果要进行排序、取最大最小值等操作时先转换为列表
    t_list = list(t)
    print(min(t_list))
    print(sorted(t_list))
    # 除了使用zip函数，还可以通过min、max的key参数来指定需要进行计算的值
    # 此处通过lambda将字典的值作为比较对象
    # 返回值最小的键
    print(min(d, key=lambda key: d[key]))


# example_5()

##############################################################################################

"""
在两个字典中寻找相同点
"""


def example_6():
    d1 = {'k1': 1,
          'k2': 1,
          'k3': 1}
    d2 = {'k3': 1,
          'k4': 1,
          'k5': 1}
    # 字典的键是可以进行集合操作的
    # items()也支持，但是注意value()方法不支持，因为值可能不是唯一的。
    print(d1.keys() & d2.keys())


# example_6()

##############################################################################################

"""
统计重复元素出现的次数。
"""


def example_7():
    from collections import Counter
    _list = ['a', 'a', 'a', 'b', 'b', 'c']
    # 返回字典
    _count = Counter(_list)
    print(_count.most_common(1))


# example_7()

##############################################################################################


"""
利用itemgetter排序字典
"""


def example_8():
    from operator import itemgetter
    t1 = [{'key': 'k3', 'value': 3},
          {'key': 'k1', 'value': 1},
          {'key': 'k2', 'value': 2}]
    # 通过itemgetter 根据字典中对应的键来排序
    # 前面示例使用了lambda，对于公共键（键名相同）来说，使用itemgetter速度更快
    print(sorted(t1, key=itemgetter('value')))
    print(itemgetter('value'))


# example_8()

##############################################################################################


"""
对无法原生支持的类型排序
"""


def example_9():
    from operator import attrgetter
    class User(object):
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return f'user id : {self.user_id}'

    users = [User(13), User(2), User(20)]
    # 利用attrgetter函数来获得对象的类属性来进行排序
    print(sorted(users, key=attrgetter('user_id')))
    # 使用lambda效果一样
    print(sorted(users, key=lambda s: s.user_id))


# example_9()

##############################################################################################

"""
根据指定的字段值进行分组处理
"""

def example_10():
    from operator import itemgetter
    from itertools import groupby
    from collections import defaultdict
    rows = [{'id': 0, 'date': '2022:09:17'},
            {'id': 1, 'date': '2022:09:17'},
            {'id': 2, 'date': '2022:10:15'},
            {'id': 3, 'date': '2022:10:15'},
            {'id': 4, 'date': '2022:08:27'}]

    rows_by_date = defaultdict(list)
    # 创建一个新的字典（默认值为一个列表）按日期来存放数据
    for row in rows:
        # 以date的值做为键，值为默认的list，相同日期的数据都会加到同一列表
        rows_by_date[row['date']].append(row)
    # print(rows_by_date['2022:10:15'])

    # 利用groupby将相同值进行分组（groupby返回一个迭代器）处理数据量大的时候比较好用
    # 首先要对groupby的值进行排序
    rows.sort(key=itemgetter('date'))
    # 使用key关键字对指定键分组
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(i)

# example_10()


"""
筛选序列元素
"""

def example_11():
    values = ['4', '5', 'aaa', None]
    def is_int(val):
        try:
            int(val)
            return True
        except (ValueError, TypeError):
            return False
    # 通过filter实现自定复杂过滤规则函数。
    int_value = filter(is_int, values)
    print(list(int_value))
    # 简单的过滤也可通过列表推导式来实现
    values = [4, 5, 0]
    print([i for i in values if i > 0])

example_11()