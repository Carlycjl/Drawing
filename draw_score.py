import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

from extract_data import extract
from matplotlib import style
plt.style.use('ggplot')

# 画折线图
def plot_line(data):
    #     data=data.sort_values(by='score')[25:75]
    # max_experiment_num = data['score'].idxmax()+1
    # max_score = data['score'].max()
    y = data
    x = range(0, len(y))
    # notestr = '('+str(max_experiment_num)+', '+str(max_score)+')'
    # noteloc = (max_experiment_num,max_score)

    plt.figure()
    plt.plot(x, y, c='steelblue')
    # plt.annotate(notestr,color='black'
    # ,xy=noteloc,xytext=noteloc,)
    plt.title("Scores")
    plt.xlabel('experiment')
    plt.ylabel('score')
    plt.savefig(saveto+"Scores折线图.jpg")
    plt.show()

# 画箱型图
def plot_box(data, partdata):
    #取数
    data = pd.DataFrame(data)
    l = len(data)
    flag = "Alldata"
    if partdata:
        data = data.sort_values(by='score')[int(0.25*l):int(0.75*l)]
        flag = "Partdata"
    y=data['score']
    #属性-
    labels = list(data)
    boxprops = {'facecolor': 'steelblue', 'color': 'steelblue'}
    whiskerprops = {'color': 'steelblue', 'linestyle': '--'}
    meanprops = {'linestyle': '-', 'linewidth': '1.8', 'color': 'orange'}
    medianprops = {'linestyle': '-', 'linewidth': '0', 'color': 'blue'}
    capprops = {'color': 'steelblue'}
    title=flag+"_"+"Scores"

    #画图
    plt.figure()
    plt.boxplot(y, showmeans=True, meanline=True,
                patch_artist=True, vert=True, labels=labels,
                medianprops=medianprops, meanprops=meanprops,
                whiskerprops=whiskerprops, capprops=capprops,
                boxprops=boxprops)
    plt.title(title)
    plt.grid(axis="x", ls=":", lw=1, color="gray", alpha=1)
    plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=1)
    plt.savefig(saveto+title+".jpg")
    plt.show()


if __name__ == '__main__':
    # 地址oct13-num-850-variancexy500-count48-100
    saveto = "/home/iscas/2020_EXPDATA/"
    datapath1 = saveto+"nov7-num-1100-variancexy500-count64-alititude3000-2group-120s-300/"
    # 取数
    score1 = extract(3, datapath1, "/summary.csv", "score")
    # 当前数据
    # tag = "500"
    # 画折线图
    plot_line(score1)
    # 画全部数据箱型图
    plot_box(score1,0)
    # 画25%-75%数据箱型图
    plot_box(score1, 1)
