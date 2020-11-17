import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

#取出一列数据
def extract(other_file_num, datapath, filename, target_data):
    extract_datas = []
    pathDir = os.listdir(datapath)
    pathDir.sort(key=lambda x :x.split('_')[-1])
    lenth = len(pathDir)
    pathDir = pathDir[0:lenth-other_file_num]
    pathDir.sort(key=lambda x :int(x.split('_')[-1]))
    for allDir in pathDir:      
        if os.path.isdir(datapath + allDir) and allDir !=  'missions' and allDir !=  'logs' :
            data = pd.read_csv(datapath + allDir + filename)
            extract_data = round(data[target_data][0],2)
            extract_datas.append(extract_data)
            extract_data_df = pd.DataFrame(extract_datas,columns=[target_data])
    if target_data == 'score':
        max_experiment_num = extract_data_df[target_data].idxmax()+1
        print(target_data+" max_exp_num:"+str(max_experiment_num))
    return extract_data_df

#取出所需列数据并合并为一个df,取出的数为25%-75%
def extract_df(col_list,datapath,file_name,other_file_num):
    y=pd.DataFrame([])
    for i in range(len(col_list)):
        col_data =pd.DataFrame([])
        col_data = extract(other_file_num,datapath,file_name,col_list[i])
        y = pd.concat([y,col_data],axis=1)
    l= len(y)
    index_25 = int(l * 0.25)
    index_75 = int(l*0.75)
    y=y.sort_values(by='score')[index_25:index_75]
    return y

#计算destroyed missile，用于几个实验的比较
def entity_analysis(col_list,data,tag):
    data[str(tag)+'_destroyed_missile']=data['entity_count']- data.iloc[:,2:len(col_list)].sum(axis=1)
    return data

#计算hit和destroy的均值
def cal_mean(data):
    mean = data.mean()
    mean_hit_des = pd.DataFrame(mean[1:len(mean)-2]).values
    # mean_coll = pd.DataFrame(mean[len(mean)-2:len(mean)])
    y1 = mean_hit_des.reshape((5,2))
    # y2 = mean_coll
    return y1