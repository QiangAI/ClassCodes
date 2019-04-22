#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt

'''
矩形图形绘制--Axes除了使用add_artist添加构造好的图形外，还可以使用一系列函数直接绘制
    |-Axes.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, data=None)
        返回值：
            |-patches : list
                matplotlib.patches.Wedge对象的列表
            |-texts : list
                matplotlib.text.Text对象列表
            |-autotexts : list
                标签的Text对象，当autopct非None的时候返回.
        |-x : array-like
            |-饼图上的数据份额，最后自定转换成百分比。
        |-explode : array-like, optional, default: None
            |-控制饼图中，每个饼偏离中心的距离
        |-labels : list, optional, default: None
            |-每个饼对应的文字标签（可显示）
        |-colors : array-like, optional, default: None
            |-每个饼对应的颜色
        |-autopct : None (default), string, or function, optional
            |-现在在饼内的文本,如果有%字符格式，会自定填充饼的百分比。
        |-pctdistance : float, optional, default: 0.6
            |-autopct与中心点的距离
        |-shadow : bool, optional, default: False
            |-是否绘制阴影
        |-labeldistance : float, optional, default: 1.1
            |-标签到中心点的距离
        |-startangle : float, optional, default: None
            |-开始角度（单位：角度，非弧度）
        |-radius : float, optional, default: None
            |-饼的半径
        |-counterclock : bool, optional, default: True
            |-饼的绘制方向（顺时针False））
        |-wedgeprops : dict, optional, default: None
            |-使用字典设置边界属性
            |-字典的key，需要参考wedge object对象的帮助文档(在patch模块Wedge类中)
        |-textprops : dict, optional, default: None
            |-文本属性，可以参考Text的官方文档。(在matplotlib.text.Text中有描述)
        |-center : list of float, optional, default: (0, 0)
            |-中心点（注意：frame=True，center改变不了比例尺）
        |-frame : bool, optional, default: False
            |-显示坐标轴
        |-rotatelabels : bool, optional, default: False
            |-对labels的文本进行对应的旋转。
    注意:这个函数也支持data替代x。
'''
figure = plt.figure(1, figsize=(4, 4))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# 1. pie
# -------------------------------
pe = ax.pie(
    x=[3, 2, 2],
    explode=[0.01, 0.01, 0.01],
    labels=['第一个饼', '第二个饼', '第三个饼'],
    colors=['r', 'g', 'b'],
    autopct='份额:%8.2f%%',
    pctdistance=1.3,
    shadow=False,
    labeldistance=0.5,
    startangle=45,
    radius=0.5,
    counterclock=False,
    wedgeprops={
        'linewidth': 1,
        'edgecolor': (1, 1, 0, 1),
        'hatch': '.'
    },
    textprops={
        'color': (0, 1, 1, 1)
    },
    center=(0.5, 0.5),  # 外观上位置都在窗体中间，可以设置为（500，500）但改变了坐标轴的参照点（可以使用光标观察坐标变化）
    frame=True,
    rotatelabels=True
)
# -------------------------------
figure.show(warn=False)
plt.show()
