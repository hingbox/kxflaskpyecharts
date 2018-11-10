#encoding=utf-8
from flask import Flask
import random
from pyecharts import Scatter3D
#from pyecharts.constants import DEFAULT_HOSTS
from flask import Flask, render_template
from pyecharts import Bar
app = Flask(__name__)

REMOTE_HOST = "https://pyecharts.github.io/assets/js"
@app.route('/')
def hello_world():
    s3d = scatter3d()
    return render_template(
        "pyecharts.html",
        myechart=s3d.render_embed(),
        host=REMOTE_HOST,
        script_list=s3d.get_js_dependencies(),
    )

def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ]
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D

def generate_3d_random_point():
    return [
        random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
    ]

@app.route('/one')
def app_1():
    bar = Bar("一周邮件量", "海南邮政数据中心")
    bar.add("当日递", ["周一", "周二", "周三", "周四", "周五", "周六","周日"], [5, 20, 36, 10, 75, 90,28])
    bar.add("次日递", ["周一", "周二", "周三", "周四", "周五", "周六","周日"], [25, 10, 56, 70, 25, 40,88])
    ret_html = render_template('pyecharts.html',
                           myechart=bar.render_embed(),
                               mytitle=u"数据演示",
                           host='/static',
                       script_list=bar.get_js_dependencies())
    return ret_html
@app.route('/two')
def app_2():
    from pyecharts import Gauge
    gauge = Gauge("业务量完成情况","函件",width=600, height=300)
    gauge.add("海口", "", 86.66,scale_range=[0,100],angle_range=[180,0])

    gauge1 = Gauge("业务收入完成情况","函件",width=600, height=300)
    gauge1.add("海口", "", 88.99)
    ret_html = render_template('pyecharts.html',
                           myechart=gauge.render_embed()+gauge1.render_embed(),
                               mytitle=u"数据演示",
                           host='/static',
                           script_list=gauge.get_js_dependencies())
    return ret_html


if __name__ == '__main__':
    app.run(port=9999)
