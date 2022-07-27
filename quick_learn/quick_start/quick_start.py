import webbrowser


def warn():
    return """你可能需要帮助：
    python main.py               -> 运行程序并快速打开默认网站
    python main.py checkall      -> 查询数据库中所有数据
    python main.py open url=...  -> 自定义打开某网站
    python main.py add name      -> 添加新网站
    python main.py delete name   -> 删除某网站
    python main.py update name   -> 更新某网站
    python main.py check name    -> 查询某网站是否在数据库中 """


def diy_open(url):
    webbrowser.open_new_tab(url)
    return "{}：打开成功".format(url)


class QuickStart:
    def __init__(self, quick_start_urls):
        self.quick_start_urls = quick_start_urls

    def quick_open(self):
        bool_lis = [webbrowser.open_new_tab(key[2]) for key in self.quick_start_urls]

        if all(bool_lis):
            for key in self.quick_start_urls:
                print("{}: Success!".format(key))

        else:
            count = 0
            for b in bool_lis:
                if b is False:
                    keys = self.quick_start_urls.keys()
                    current_false_key = list(keys)[count]
                    print("{0}打开失败, 请手动打开{0}: {1}"
                          .format(current_false_key, self.quick_start_urls[current_false_key]))
                count += 1


"""
运行命令：
    python main.py             -> 运行程序并快速打开默认网站
    python main.py -o url=...  -> 自定义打开某网站
    python main.py add name    -> 添加新网站
    python main.py delete name -> 删除某网站
    python main.py update name -> 更新某网站
    python main.py check name  -> 查询某网站是否在数据库中
"""
