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


example_2()