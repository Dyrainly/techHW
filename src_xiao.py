import pandas
import pickle
from pyecharts.charts import Bar
from pyecharts import options as opts

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
data = pandas.read_csv("cooked.csv")

###统计分析设备使用情况
def getDeviceUse():
    device_use = {"电视": 0, "台式电脑": 0, "平板": 0, "手机": 0, "音频": 0, "纸质学习资料": 0}
    dict = {"电视":"2","台式电脑":"3","平板":"4","手机":"5","音频":"6","纸质学习资料":"7"}
    for key in dict.keys():
        device_use[key] = data[dict[key]].tolist().count(1)/len(data[dict[key]])
    X = device_use.keys()
    Y = device_use.values()
    plt.bar(X, Y)
    for a, b in zip(X,Y):
        plt.text(a, b , '{:.2%}'.format(b), ha='center', va='bottom', fontsize=7)
    plt.title("设备使用比例统计")
    plt.show()

def getFunctionUse():
    TOTAL_COUNT = data.shape[0]
    ###线上平台功能使用情况
    functions_use = {"回看课程视频":0,"作业提交":0,"随堂测试":0,"视频会议":0,
                     "作业批改反馈":0,"课堂发言":0,"班级通知":0,"班级圈":0,
                     "优秀作业查看":0,"学科竞赛游戏":0,"屏幕共享":0,"弹幕":0,"讨论":0}
    dict_function_use = {"回看课程视频":"8","作业提交":"9","随堂测试":"10","视频会议":"11",
                 "作业批改反馈":"12","课堂发言":"13","班级通知":"14","班级圈":"15",
                 "优秀作业查看":"15","学科竞赛游戏":"16","屏幕共享":"17","弹幕":"18","讨论":"19"}

    for key in functions_use.keys():
        functions_use[key] = data[dict_function_use[key]].tolist().count(1)/TOTAL_COUNT
    X = functions_use.keys()
    Y = functions_use.values()
    plt.bar(X,Y)
    for a, b in zip(X,Y):
        plt.text(a, b , '{:.2%}'.format(b), ha='center', va='bottom', fontsize=7)
    plt.title("线上平台设备使用情况")
    print(functions_use)
    ax = plt.subplot(111)
    ax.set_xlabel(..., fontsize=10)
    plt.show()


###最长上课时长分析
def getCourseTimeAnalysis():
    course_time_list = data["21"].to_list()
    dict = {}
    for i in course_time_list:
        if dict.get(i)==None:
            dict[i]=1
        else:
            dict[i]+=1
    keys = list(dict.keys())
    for key in keys:
        dict[str(key)+"h"] = dict.pop(key)
    plt.pie(dict.values(),labels=dict.keys(),autopct='%1.1f%%')
    plt.title("最长上课时长")
    plt.show()

getDeviceUse()
getFunctionUse()
getCourseTimeAnalysis()
