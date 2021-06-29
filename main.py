
import collections
import json
#import re


def print_hi(name):

    import cx_Oracle

    # dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')  # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
    # conn = cx_Oracle.connect(user='system', password='yourdbpassword', dsn=dsn_tns)  # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

    conn = cx_Oracle.connect('system/n00b12345@//localhost:1521/orcl')  # To handle assignment error of 'conn'

    try:
        conn = cx_Oracle.connect('system/n00b12345@//localhost:1521/orcl')
    except Exception as err:
        print('Cannot create connection')
    else:
        print(conn.version)
        c = conn.cursor()
        c.execute('SELECT * FROM chart')  # use triple quotes if you want to spread your query across multiple lines
        row = c.fetchall()
        print(row)

        c.execute('SELECT * FROM chart')
        rows = c.fetchall()

        d = collections.OrderedDict() #To handle assignment error of 'd'

        obj_list = []
        for row in rows:
            d = collections.OrderedDict()
            d["Russia"] = row[0]
            d["US"] = row[1]
            d["Venezuela"] = row[2]
            d["India"] = row[3]
            obj_list.append(d)

        test = ""
        i = 0
        for key, value in d.items():
            if (i > 0):
                test = test + ",\n"
            test = test + "{" + '"label": "{}", "value": "{}"'.format(key, value) + "}"
            i = i + 1

        print('{"data": [' + test + "]}")

        f = open("FusionChartsProject/test.json", "w")
        f.write('{"data": [' + test + "]}")
        f.close()

        t = open("FusionChartsProject/data.json", "r")
        u = open("FusionChartsProject/test.json", "r")
        j = json.load(t)
        k = json.load(u)
        print(k)
        t.close()

    finally:
        conn.close()


if __name__ == '__main__':
    print_hi('lol')