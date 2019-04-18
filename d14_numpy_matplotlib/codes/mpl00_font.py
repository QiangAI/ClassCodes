#!usr/bin/python
# coding=utf-8
import matplotlib as mpl
import matplotlib.font_manager as fm

# 1.得到配置文件目录，与matplotlib系统的数据存放目录
print(mpl.get_configdir())
print(mpl.matplotlib_fname())
# 上面第二个语句输出：/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc
# 其中/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/matplotlib/mpl-data/就是数据存放目录
# 假如：记matplotlib安装目录为：${MLP_HOME}，数据存放目录就是：${MLP_HOME}/mpl-data/
# 2.准备一个字体库文件，我找到的是msyh.ttf

# 3.把字体库拷贝到数据存放目录下的fonts/ttf目录，既：${MLP_HOME}/mpl-data/fonts/ttf

# 4.确认字库的字体名,可以根据经验，网络百度得到字体的family-name，下面使用代码获取
fp = fm.FontProperties(fname="msyh.ttf")
print(fp.get_family(), fp.get_name())

# 输出的字体名（fp.get_name（）函数的输出，get_family（）输出的配置的缺省family name）：Microsoft YaHei

# 5.修改配置文件：${MLP_HOME}/mpl-data/matplotlibrc
# 找到字体配置的位置：我的配置文件在195行,我增加一行196，配置family如下：
# 195 #font.family         : sans-serif
# 196 font.family         : Microsoft YaHei

# 6. 可以在程序中测试，某些环境可能因为缓冲滞后，只需要重启环境即可。
# |-比如：ipython就会因为缓冲而暂时没有效果，重启下即可。
