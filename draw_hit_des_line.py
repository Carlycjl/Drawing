import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
from extract_data import extract, extract_df
from matplotlib import style
plt.style.use('seaborn-white')

# 画各类别hit和destroy的6个图,tag为比较的变量的数值
def plot_hit_des(y):
    y11 = y['defense_hit']
    y12 = y['defense_destroy']
    y21 = y['airport_plane_hit']
    y22 = y['airport_plane_destroy']
    y31 = y['airport_plane_car_hit']
    y32 = y['airport_plane_car_destroy']
    y41 = y['car_on_road_hit']
    y42 = y['car_on_road_destroy']
    y51 = y['boat_along_coastline_hit']
    y52 = y['boat_along_coastline_destroy']
    y61 = y['team_coll']
    y62 = y['ground_coll']
    y63 = y61+y62

    x1 = range(0, len(y11))

    fig = plt.figure(figsize=(20, 15))
    # bgcolor = fig.patch
    # bgcolor.set_facecolor("white")

    plt.subplot(231,facecolor = 'white')
    plt.plot(x1, y11, label="hit",linestyle='-')
    plt.plot(x1, y12, label="destroy",linestyle='--')
    plt.title("defense")
    plt.xlabel('experiment')
    plt.ylabel('num')

    plt.subplot(232,facecolor = 'white')
    plt.plot(x1, y21, label="hit",linestyle='-',)
    plt.plot(x1, y22, label="destroy",linestyle='--')
    plt.title("airport_plane")
    plt.xlabel('experiment')

    plt.subplot(233,facecolor = 'white')
    plt.plot(x1, y31, label="hit",linestyle='-')
    plt.plot(x1, y32, label="destroy",linestyle='--')
    plt.legend(bbox_to_anchor=(1.1, 0), loc=3, borderaxespad=0)
    plt.title("airport_car_plane")
    plt.xlabel('experiment')

    plt.subplot(234,facecolor = 'white')
    plt.plot(x1, y41,label="hit",linestyle='-')
    plt.plot(x1, y42, label="destroy",linestyle='--')
    plt.title("car_on_road")
    plt.xlabel('experiment')
    plt.ylabel('num')

    plt.subplot(235,facecolor = 'white')
    plt.plot(x1, y51, label="hit",linestyle='-')
    plt.plot(x1, y52, label="destroy",linestyle='--')
    plt.title("boat_along_coastline")
    plt.xlabel('experiment')

    plt.subplot(236,facecolor = 'white')
    plt.plot(x1, y61,  label="team_coll",linestyle='--')
    plt.plot(x1, y62,  label="ground_coll",linestyle='-')
    plt.plot(x1, y63,  label="all_coll",linestyle='-')
    plt.legend(bbox_to_anchor=(0.7, 0.85), loc=3, borderaxespad=0)
    plt.title("coll")
    plt.xlabel('experiment')
    plt.savefig(saveto+"des_hit折线图.jpg")

    plt.show()

if __name__ == '__main__':
    #参数：地址、要取的数据
    saveto = "/home/iscas/2020_EXPDATA/"
    datapath14 = saveto+"oct13-num-1500-variancexy500-count48-altitude1000-100/"
    col_list = ["score", "defense_destroy", "defense_hit", "airport_plane_destroy", "airport_plane_hit", "airport_plane_car_destroy", "airport_plane_car_hit",
                 "boat_along_coastline_destroy", "boat_along_coastline_hit", "car_on_road_destroy", "car_on_road_hit", "team_coll", "ground_coll"]

    #取数
    y = extract_df(col_list, datapath14, "/summary.csv", 3)
    #画hit和destroy图
    plot_hit_des(y)