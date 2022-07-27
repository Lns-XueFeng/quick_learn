import sqlite3
import sys
from quick_start.quick_start import QuickStart, warn, diy_open


if __name__ == "__main__":
    # 内置默认需要打开的网址
    quick_start_urls = [("个人网站", "http://codechangeworld.cn/"),
                        ("Python_Doc", "https://docs.python.org/zh-cn/3.7/"),
                        ("Python_Library", "https://docs.python.org/zh-cn/3.7/library/index.html"),
                        ("Python HowTo", "https://docs.python.org/zh-cn/3.7/howto/index.html"),
                        ("MDN", "https://developer.mozilla.org/zh-CN/"),
                        ("Flask", "https://dormousehole.readthedocs.io/en/latest/index.html"),
                        ("StackOverFlow", "https://stackoverflow.com/"),
                        ("Bing", "https://cn.bing.com/?mkt=zh-CN"), ]

    from quick_start.db import create_table, check_all, insert_many

    try:
        create_table()
    except sqlite3.OperationalError:
        pass

    values = check_all()   # 获得数据库中的urls
    if len(values) == 0:
        insert_many(quick_start_urls)
        warn = warn()
        raise "初始化成功，请再次启动程序打开默认webs\n" + warn

    # 获得数据库中的urls
    values = check_all()
    # 获得命令行参数列表
    argv = sys.argv
    # 实例化quick_start
    quick_start = QuickStart(values)

    # 如果输入参数为: python main.py 则打开默认web页面
    if len(argv) == 1:
        if argv[0] == "main.py":
            quick_start.quick_open()

        else:
            warn = warn()
            print(warn)

    elif len(argv) == 2:
        if argv[1] == "checkall":
            urls = sorted(values)
            for url in urls:
                print(url[1:])

    elif len(argv) == 3:
        # 如果输入参数为: python main.py -open url=... 则自定义打开页面
        if argv[1] == "open" and "url" in argv[2]:
            url = argv[2].split("=")[1]
            end = diy_open(url)
            print(end)

        # 如果输入参数为：python main.py add name
        elif argv[1] == "add" and argv[2]:
            from quick_start.db import insert_one
            name = argv[2]
            url = input("请输入网站地址：")
            insert_one(name, url)
            print("插入成功")

        # 如果输入参数为：python main.py delete name
        elif argv[1] == "delete" and argv[2]:
            from quick_start.db import delete_one
            name = argv[2]
            delete_one(name)
            print("删除成功")

        # 如果输入参数为：python main.py update name
        elif argv[1] == "update" and argv[2]:
            from quick_start.db import update_url
            name = argv[2]
            url = input("请输入修改后的网站地址：")
            update_url(name, url)
            print("更新成功")

        # 如果输入参数为：python main.py check name
        elif argv[1] == "check" and argv[2]:
            from quick_start.db import check_one
            name = argv[2]
            result = check_one(name)
            try:
                print(result[2])
            except TypeError:
                print("没有此网站")

        else:
            warn = warn()
            print(warn)

    else:
        warn = warn()
        print(warn)
