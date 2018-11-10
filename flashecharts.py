#encoding=utf-8
from flask import Flask
import random
from pyecharts import Scatter3D
#from pyecharts.constants import DEFAULT_HOSTS
from flask import Flask, render_template
from pyecharts_javascripthon.api import TRANSLATOR
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

@app.route('/three')
def app_3():
    _bar = bar_chart()
    javascript_snippet = TRANSLATOR.translate(_bar.options)
    return render_template(
            "mypyecharts.html",
            chart_id=_bar.chart_id,
            host=REMOTE_HOST,
            renderer=_bar.renderer,
            my_width="100%",
            my_height=600,
            custom_function=javascript_snippet.function_snippet,
            options=javascript_snippet.option_snippet,
            script_list=_bar.get_js_dependencies(),
    )

def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    # bar.use_theme('dark')
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    bar.add(
        "商家A", attr, [5, 20, 36, 10, 75, 90],is_more_utils=True
    )
    bar.add(
        "商家B", attr, [5, 20, 36, 10, 75, 90],is_more_utils=True
    )
    return bar


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9999)
