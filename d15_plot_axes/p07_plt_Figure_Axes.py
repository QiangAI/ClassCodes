import matplotlib.pyplot as plt

figure = plt.figure(
    num='坐标演示案例',
    figsize=(8, 6),
    dpi=100,
    facecolor='gray'
)

# a = figure.subplots(2, 2)
# print(a)

# ax = figure.gca()
# print(ax)
#
# ax = figure.get_axes()
# ax = figure.add_subplot(222,facecolor='red',label='A', title='AA',position=[0.5,0.5,0.3,0.3])
# ax = figure.add_subplot(221,facecolor='green',label='B',title='Bb')
# ax = figure.add_subplot(224)

ax = plt.Axes(
    figure,
    rect=[0.1, 0.1, 0.8, 0.8]
)
figure.add_axes(ax)

# -------------
ax.set_position([0.2, 0.2, 0.6, 0.6])
ax.set_xlabel(
    xlabel='x坐标',
    fontdict={
        'fontsize': 8,
        'fontweight': 'bold',
        'fontstyle': 'italic',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center',
        'color': (1, 1, 0, 1)
    }
)
ax.set_ylabel(
    ylabel='y坐标',
    fontdict={
        'fontsize': 8,
        'fontweight': 'bold',
        'fontstyle': 'italic',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center',
        'color': (1, 1, 0, 1)
    }
)

# ax.set_xbound(lower=0,upper=100)
# ax.set_ybound(lower=-100,upper=100)
#
# ax.set_xlim(left=0,right=10)

# ax.set_xscale('linear')
ax.set_xticks(
    ticks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    minor=True
)

ax.set_xticklabels(
    labels=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
    fontdict={
        'fontsize': 8,
        'fontweight': 'bold',
        'fontstyle': 'italic',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center',
        'color': (1, 0, 1, 1)
    },
    minor=True)
# -------------
ax.plot(
    [0, 1, 2, 3, 6, 7, 8, 9, 10],
    [0.5, 0, 1, 1, 0, 1, 0, 1, 0],
    linewidth=1,
    linestyle='--',
    marker='o',
    markerfacecolor='red',
    markersize=15,
    color=(1, 1, 0, 1),
    markeredgecolor=(0, 0, 1, 1),
    markeredgewidth=2,
    markerfacecoloralt=(1, 0, 1, 1)
)
# ax.plot(
#     [0,  1,  2 , 3,   6,   7,   8,  9, 10],
#     [0.5, 0, 1,  1,   0,   1,   0,  1, 0],
#     'g--'
# )
# -------------
ax.legend()
# figure.legend()  # 绘制主题：图中存在Artist的时候才能绘制
figure.show()
figure.savefig('a.png')

plt.show()
