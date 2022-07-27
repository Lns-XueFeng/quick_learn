import sqlite3


def create_table():
    # 连接数据库(如果不存在则创建)
    conn = sqlite3.connect('../task.db')
    cursor = conn.cursor()

    sql = 'CREATE TABLE task(id integer PRIMARY KEY autoincrement, name, url)'
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()


def insert_one(name, url):
    """往数据库中插入一条数据
    :param name: 网站名称
    :param url: 网站链接
    :return: None
    """
    conn = sqlite3.connect("../task.db")
    cur = conn.cursor()

    data = (name, url)
    sql = "INSERT INTO task(name, url) VALUES(?, ?)"
    cur.execute(sql, data)

    conn.commit()
    cur.close()
    conn.close()


def insert_many(li):
    """往数据库中插入多条数据
    :param li: 由列表包裹的多个元组
    :return: None
    """
    conn = sqlite3.connect("../task.db")
    cur = conn.cursor()

    sql = "insert into task(name, url) values(?,?)"
    cur.executemany(sql, li)

    conn.commit()
    cur.close()
    conn.close()


def update_url(name, url):
    """更新网站名字以及url
    :param name: 网站名称
    :param url: 网站网址
    :return: None
    """
    delete_one(name)
    insert_one(name, url)


def delete_one(name):
    """删除一条数据
    :param name: 网站名称
    :return: None
    """
    conn = sqlite3.connect('../task.db')
    cur = conn.cursor()

    data = (name,)   # 逗号不能省，元组元素只有一个的时候一定要加逗号,将删除name
    sql = "delete from task where name=?"
    cur.execute(sql, data)

    conn.commit()
    cur.close()
    conn.close()


def check_one(name):
    """查询指定的数据
    name: 网站名称
    :return:
    """
    conn = sqlite3.connect('../task.db')
    cur = conn.cursor()

    sql = "select * from task where name=?"
    values = cur.execute(sql, (name,))
    for tur in values:
        if name in tur:
            conn.commit()
            cur.close()
            conn.close()
            return tur

    conn.commit()
    cur.close()
    conn.close()
    return None


def check_all():
    """
    :return:
    """
    conn = sqlite3.connect('../task.db')
    cur = conn.cursor()

    sql = "select * from task"
    values = cur.execute(sql)
    li = []
    for i in values:
        li.append(i)

    conn.commit()
    cur.close()
    conn.close()

    return li
