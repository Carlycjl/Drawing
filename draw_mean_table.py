import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
from extract_data import extract, extract_df,cal_mean
from matplotlib import style
plt.style.use('ggplot')
import matplotlib as mpl

mpl.rcParams[u'font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False

# 画各类别hit_destroy的表的均值
def plot_hit_des_table(mean_hit_des,value):
    #取数
    y = [[0 for c in range(5)] for r in range(6)]
    values=value*mean_hit_des
    for i in range(5):
        for j in range(2):
            y[i][j]=round(mean_hit_des[i][j],2)
            y[i][j+2]=round(values[i][j],2)
        y[i][4]=round(values[i][0]+values[i][1],2)
    for j in range(5):
        for i in range(5):
            y[5][j]= round(y[i][j]+y[5][j],2)

    #表属性
    col_labels = ['被击毁数量(均值)', '被击中次数(均值)',
                  '击毁价值（均值）', '击中价值（均值）','价值（均值）',]
    row_labels = ['防空系统', '地面固定飞机', '地面移动飞机（拖车）',
                  '小艇', '行驶车辆', '合计']
    cellColours=[["white" for c in range(5)] for r in range(6)]
    colColours = ["white"] * 5
    rowColours=["white"] * 6
    colWidths=[0.07]*6
    title= "des_hit表"

    #画表
    fig = plt.figure(figsize=(18, 8))
    fig.add_subplot(111, frameon=False, xticks=[], yticks=[])
    table1 = plt.table(cellText=y, rowLabels=row_labels, colLabels=col_labels,
                       rowColours=rowColours, colColours=colColours,
                       cellColours=cellColours, colWidths=colWidths,
                       loc='best', cellLoc='center')
    table1.set_fontsize(20)
    table1.scale(2, 3)
    plt.savefig(saveto+title+".jpg")

#画collision表
def plot_coll_table(y):
    #取数
    y1=y['team_coll'].mean()
    y2=y['ground_coll'].mean()
    y3=round(y1+y2,2)
    vals2 = [[y1,y2,y3]]
    #表属性
    col_labels = ['组内碰撞', '地形碰撞', '合计']
    row_labels = ['均值']
    colWidths=[0.07]*6 
    loc='center'
    cellLoc='center'
    rowColours=["white"]
    colColours=["white"] * 3
    cellColours=[["white" for c in range(3)] for r in range(1)]
    
    #画表
    fig = plt.figure(figsize=(18, 8))
    fig.add_subplot(111, frameon=False, xticks=[], yticks=[])
    table1 = plt.table(cellText=vals2, loc=loc, cellLoc=cellLoc,
                    rowLabels=row_labels, colLabels=col_labels,
                    colWidths=colWidths, cellColours=cellColours,
                    rowColours=rowColours,colColours=colColours)
    table1.set_fontsize(20)
    table1.scale(2, 3)
    plt.savefig(saveto+"coll表.jpg")

if __name__ == '__main__':
    #地址
    saveto = "/home/iscas/2020_EXPDATA/"
    datapath14 = saveto+"Oct13-num-1500-variancexy100-count48-altitude3000-100/"
    #要取的数据
    col_list = ["score", "defense_destroy", "defense_hit", "airport_plane_destroy", "airport_plane_hit", "airport_plane_car_destroy", "airport_plane_car_hit",
                 "boat_along_coastline_destroy", "boat_along_coastline_hit", "car_on_road_destroy", "car_on_road_hit", "team_coll", "ground_coll"]
    #损失单价
    value = np.array([[200,40],[100,50],
                [100,50],[30,15],[50,25]])
    #数据特征
    # tag = 500  #altitude:500

    #取数，计算剩余uav均值
    y = extract_df( col_list, datapath14, "/summary.csv", 3)
    mean_hit_des = cal_mean(y)

    #画图
    plot_hit_des_table(mean_hit_des,value)
    plot_coll_table(y)
    

    


