"""
使用多个字段判断字符串前缀和后缀
"""
def example_1():
    text_1 = 'www.abc.com'
    text_2 = 'www.abc.cn'
    # 可以通过给endswith、startswith传一个元祖来支持多个字段匹配
    match = ('.com', '.cn')
    print(text_1.endswith(match))
    print(text_2.endswith(match))

# example_1()

"""
利用Shell通配符做匹配
"""
def example_2():
    from fnmatch import fnmatch
    print(fnmatch('a.jpg', '*.jpg'))
    # 需要注意的是fnmatch函数采用系统底层来决定是否忽略大小写，linux严格区分大小写，win则相反
    # 通过fnmatchcase来严格区分大小写，忽略系统差异


# example_2()

"""
正则非贪婪匹配
"""
def example_3():
    import re
    text = 'Computer says "no." Phone says "yes."'
    # 默认是贪婪匹配.*会匹配到多余字符串
    print(re.findall(r'\"(.*)\"', text))
    # 加一个？来限制贪婪匹配
    print(re.findall(r'\"(.*?)\"', text))

# example_3()
"""
字符串替换
"""
def example_4():
    # 简单的替换首选replace。高效
    print("abcd".replace('a', '1'))
    # 复杂规则可以使用translate通过建立对照表来替换
    # 对照表需要转换成ascii值
    table = {ord('a'): ord('1'),
             ord('b'): ord('2'),
             ord('c'): ord('3')}
    print("abcd".translate(table))
    # 使用maketrans生成对照表
    intab = "abc"
    outtab = "123"
    trantab = str.maketrans(intab, outtab)
    print("abcd".translate(trantab))

# example_4()

"""
format对齐字符串
"""

def example_5():
    # >右对齐 <左对齐 ^居中对齐
    # 使用format代替rjust() center()等
    # 使用=号填充20个字符
    print(format('hello world!', '=^20'))

# example_5()

"""
通过迭代器拼接字符串并限制返回最大值
"""

def example_6():
    def combine(source, maxsize):
        parts = []
        size = 0
        for part in source:
            parts.append(part)
            size += len(part)
            if size > maxsize or size == maxsize:
                yield ''.join(parts)
                parts = []
                size = 0
        yield ''.join(parts)

    for i in combine(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'], 5):
        print(i)

example_6()