import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

from extract_data import extract, extract_df, entity_analysis
from matplotlib import style
plt.style.use('ggplot')

def plot_box(data):
    #取数
    y = data

    #属性
    boxprops = {'facecolor': 'steelblue', 'color': 'steelblue'}
    whiskerprops = {'color': 'steelblue', 'linestyle': '--'}
    meanprops = {'linestyle': '-', 'linewidth': '1.8', 'color': 'orange'}
    medianprops = {'linestyle': '-', 'linewidth': '0', 'color': 'blue'}
    capprops = {'color': 'steelblue'}
    title="destroyed_missile"

    #画图
    plt.figure()
    plt.boxplot(y, showmeans=True, meanline=True,
                patch_artist=True, vert=True,labels=[title],
                medianprops=medianprops, meanprops=meanprops,
                whiskerprops=whiskerprops, capprops=capprops,
                boxprops=boxprops)
    plt.title(title)
    # plt.xlabel(title)
    plt.grid(axis="x", ls=":", lw=1, color="gray", alpha=1)
    plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=1)
    plt.savefig(saveto+title+".jpg")
    plt.show()


if __name__ == '__main__':
    # 地址
    saveto = "/home/iscas/2020_EXPDATA/"
    datapath = saveto + "Oct13-num-1500-variancexy100-count48-altitude3000-100/"
    col_list = ["score", "entity_count", "non_team_coll", "team_coll", "ground_coll", "defense_hit",
                "airport_plane_hit", "airport_plane_car_hit", "car_on_road_hit", "boat_along_coastline_hit"]

    data = extract_df(col_list, datapath, "/summary.csv", 3)
    data = entity_analysis(col_list, data, 64)
    data1 =data['64_destroyed_missile']
    plot_box(data1)