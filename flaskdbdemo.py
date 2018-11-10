#!/usr/bin/env python
# -*- coding:utf-8 -*-
#encoding=utf-8
'''
@描述：PyCharm
@作者：hingbox
@邮箱：hingbox@163.com
@版本：V1.0
@文件名称 : flaskdbdemo.py
@创建时间：2018/11/10 20:16
'''
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, render_template
from pyecharts_javascripthon.api import TRANSLATOR
from pyecharts import Line
import MySQLdb

db=MySQLdb.connect(
    port=3306,
    host='127.0.0.1',
    db='pyecharts',
    user='root',
    passwd='root',
    charset='utf8'
)

cur = db.cursor()


sql=""" SELECT name_1 as '类型',formatr_1 as '型号',round(AVG(price),2) as '平均价格',DATE_FORMAT(time_1,'%Y-%m-%d')

 FROM gangcai_
 WHERE time_1>='2018-10-01' AND time_1<='2018-11-01' and name_1='螺纹钢' and area = '华南'
 and formatr_1='Ф16-25'
 and price > 1

 GROUP BY formatr_1,DATE_FORMAT(time_1,'%Y-%m-%d');"""

cur.execute(sql)
data=cur.fetchall()
price_date=[]
update_time=[]
for i in data:
    price_date.append(int(i[2]))
    update_time.append(str(i[3])[5:])

sql=""" SELECT name_1 as '类型',formatr_1 as '型号',round(AVG(price),2) as '平均价格',DATE_FORMAT(time_1,'%Y-%m-%d')

 FROM gangcai_
 WHERE time_1>='2018-10-01' AND time_1<='2018-11-01' and name_1='螺纹钢' and area = '华北'
 and formatr_1='Ф16-25'
 and price > 1

 GROUP BY formatr_1,DATE_FORMAT(time_1,'%Y-%m-%d');"""

cur.execute(sql)
data = cur.fetchall()
price_date_1 = []
update_time_1 = []
for i in data:
    price_date_1.append(int(i[2]))
    update_time_1.append(str(i[3])[5:])
#
# sql=""" SELECT name_1 as '类型',formatr_1 as '型号',round(AVG(price),2) as '平均价格',DATE_FORMAT(time_1,'%Y-%m-%d')
#
#  FROM gangcai_
#  WHERE time_1>='2018-05-01' AND time_1<='2018-06-01' and name_1='螺纹钢' and area = '华东'
#  and formatr_1='Ф16-25'
#  and price > 1
#
#  GROUP BY formatr_1,DATE_FORMAT(time_1,'%Y-%m-%d');"""
#
# cur.execute(sql)
# data=cur.fetchall()
# price_date_2=[]
# update_time_2=[]
# for i in data:
#     price_date_2.append(int(i[2]))
#     update_time_2.append(str(i[3])[5:])
# sql=""" SELECT name_1 as '类型',formatr_1 as '型号',round(AVG(price),2) as '平均价格',DATE_FORMAT(time_1,'%Y-%m-%d')
#
#  FROM gangcai_
#  WHERE time_1>='2018-05-01' AND time_1<='2018-06-01' and name_1='螺纹钢' and area = '华中'
#  and formatr_1='Ф16-25'
#  and price > 1
#
#  GROUP BY formatr_1,DATE_FORMAT(time_1,'%Y-%m-%d');"""
#
# cur.execute(sql)
# data=cur.fetchall()
# price_date_3=[]
# update_time_3=[]
# for i in data:
#     price_date_3.append(int(i[2]))
#     update_time_3.append(str(i[3])[5:])
#
# sql=""" SELECT name_1 as '类型',formatr_1 as '型号',round(AVG(price),2) as '平均价格',DATE_FORMAT(time_1,'%Y-%m-%d')
#
#  FROM gangcai_
#  WHERE time_1>='2018-05-01' AND time_1<='2018-06-01' and name_1='螺纹钢' and area = '东北'
#  and formatr_1='Ф16-25'
#  and price > 1
#
#  GROUP BY formatr_1,DATE_FORMAT(time_1,'%Y-%m-%d');"""
#
# cur.execute(sql)
# data=cur.fetchall()
# price_date_4=[]
# update_time_4=[]
# for i in data:
#     price_date_4.append(int(i[2]))
#     update_time_4.append(str(i[3])[5:])
#
#
#
# sql=""" SELECT name_1 as '类型',formatr_1 as '型号',round(AVG(price),2) as '平均价格',DATE_FORMAT(time_1,'%Y-%m-%d')
#
#  FROM gangcai_
#  WHERE time_1>='2018-05-01' AND time_1<='2018-06-01' and name_1='螺纹钢' and area = '西北'
#  and formatr_1='Ф16-25'
#  and price > 1
#
#  GROUP BY formatr_1,DATE_FORMAT(time_1,'%Y-%m-%d');"""
#
# cur.execute(sql)
# data = cur.fetchall()
# price_date_5 = []
# update_time_5 = []
# for i in data:
#     price_date_5.append(int(i[2]))
#     update_time_5.append(str(i[3])[5:])
#
# sql=""" SELECT name_1 as '类型',formatr_1 as '型号',round(AVG(price),2) as '平均价格',DATE_FORMAT(time_1,'%Y-%m-%d')
#
#  FROM gangcai_
#  WHERE time_1>='2018-05-01' AND time_1<='2018-06-01' and name_1='螺纹钢' and area = '西南'
#  and formatr_1='Ф16-25'
#  and price > 1
#
#  GROUP BY formatr_1,DATE_FORMAT(time_1,'%Y-%m-%d');"""
#
# cur.execute(sql)
# data = cur.fetchall()
# price_date_6 = []
# update_time_6 = []
# for i in data:
#     price_date_6.append(int(i[2]))
#     update_time_6.append(str(i[3])[5:])


db.close()

app = Flask(__name__)


@app.route("/")
def hello():

    _bar = bar_()
    javascript_snippet = TRANSLATOR.translate(_bar.options)
    return render_template(
            "mypyecharts.html",
            chart_id=_bar.chart_id,
            host='/static',
            renderer=_bar.renderer,
            my_width="100%",
            my_height=600,
            custom_function=javascript_snippet.function_snippet,
            options=javascript_snippet.option_snippet,
            script_list=_bar.get_js_dependencies(),
    )


def bar_():
    attr = update_time
    bar = Line("全国七大区")
    bar.add("2018年华南",
            attr,
            price_date,
            xaxis_interval=0,
            xaxis_rotate=30,
            yaxis_rotate=30,
            is_smooth=False,
            is_more_utils=True
            # is_label_show=True,
            )
    bar.add("2018年华北",
            attr,
            price_date_1,
            xaxis_interval=0,
            xaxis_rotate=30,
            yaxis_rotate=30,
            is_smooth=False,
            is_more_utils=True
            # is_label_show=True,
            )
    # bar.add("2018年华东",
    #         attr,
    #         price_date_2,
    #         xaxis_interval=0,
    #         xaxis_rotate=30,
    #         yaxis_rotate=30,
    #         is_smooth=False,
    #         # is_label_show=True,
    #         )
    # bar.add("2018年华中",
    #         attr,
    #         price_date_3,
    #         xaxis_interval=0,
    #         xaxis_rotate=30,
    #         yaxis_rotate=30,
    #         is_smooth=False,
    #         # is_label_show=True,
    #         )
    # bar.add("2018年东北",
    #         attr,
    #         price_date_4,
    #         xaxis_interval=0,
    #         xaxis_rotate=30,
    #         yaxis_rotate=30,
    #         is_smooth=False,
    #         # is_label_show=True,
    #         )
    # bar.add("2018年西北",
    #         attr,
    #         price_date_5,
    #         xaxis_interval=0,
    #         xaxis_rotate=30,
    #         yaxis_rotate=30,
    #         is_smooth=False,
    #         # is_label_show=True,
    #         )
    # bar.add("2018年西南",
    #         attr,
    #         price_date_6,
    #         xaxis_interval=0,
    #         xaxis_rotate=30,
    #         yaxis_rotate=30,
    #         is_smooth=False,
    #         # is_label_show=True,
    #         )
    return bar


if __name__ == "__main__":

    app.run(debug=True, host='127.0.0.1', port=8888)