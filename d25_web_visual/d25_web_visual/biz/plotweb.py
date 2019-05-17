# coding = utf-8

from d25_web_visual.visuals import plot3d
from django.shortcuts import HttpResponse  # 响应输出可视化matplotlib图形


def show_plot(request):
    data = plot3d.get_plot()  # 等系用来存放图像数据
    return HttpResponse(content=data, content_type='image/png')  # 二进制的图像输出
