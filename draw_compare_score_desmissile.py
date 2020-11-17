import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
from extract_data import extract, extract_df, entity_analysis
from matplotlib import style
plt.style.use('ggplot')

# 比较的箱形图
def plot_compare_box(data, target_data, tag):
    # 数据
    if target_data == "destroyed_missile":
        t = -1
    if target_data == "score":
        t = 0
    y = [data[0].iloc[:, t], data[1].iloc[:, t], data[2].iloc[:, t]]
    print(y)
    # 图属性
    labels = [str(tag[0])+'_'+target_data, str(tag[1])+'_' +
              target_data, str(tag[2])+'_'+target_data]
    boxprops = {'facecolor': 'steelblue', 'color': 'steelblue'}
    whiskerprops = {'color': 'steelblue', 'linestyle': '--'}
    meanprops = {'linestyle': '-', 'linewidth': '1.8', 'color': 'orange'}
    medianprops = {'linestyle': '-', 'linewidth': '0', 'color': 'blue'}
    capprops = {'color': 'steelblue'}
    title = str(tag[0])+'_'+str(tag[1])+'_'+str(tag[2])+'_'+target_data
    #画图
    plt.figure()
    # plt.subplot(facecolor='white')
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
    # 地址
    saveto = "/home/iscas/2020_EXPDATA/"
    datapath1 = saveto+"Oct13-num-1500-variancexy50-count48-altitude3000-100/"
    datapath2 = saveto+"Oct13-num-1500-variancexy100-count48-altitude3000-100/"
    datapath3 = saveto+"oct13-num-1500-variancexy500-count48-altitude3000-100/"
    datapath = [datapath1, datapath2, datapath3]
    # 要取的数据
    col_list = ["score", "entity_count", "non_team_coll", "team_coll", "ground_coll", "defense_hit",
                "airport_plane_hit", "airport_plane_car_hit", "car_on_road_hit", "boat_along_coastline_hit"]

    # 比较数目，实验次数，比较的参数
    compare_num = 3
    exp_num = 100
    tag = [50, 100, 500]

    # 取数
    data = [1]*compare_num
    for i in range(compare_num):
        data[i] = extract_df(col_list, datapath[i], "/summary.csv", 3)

    for i in range(compare_num):
        entity_analysis(col_list, data[i], tag[i])

    # score比较图
    plot_compare_box(data, 'score', tag)
    # 剩下uav比较图
    plot_compare_box(data, 'destroyed_missile', tag)
