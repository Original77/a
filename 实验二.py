import matplotlib.pyplot as plt  #导入matplotlib
import numpy as np 
x=np.linspace(0,4*np.pi,50)     #linspace限制x范围linspace（开始，结束，样本值）
y=np.sin(x)           #y函数

plt.rcParams['font.sans-serif']=['SimHei']  #显示中文
plt.rcParams['axes.unicode_minus']=False     #显示正负号  
plt.title(r'$y=sin(x)$')         #标题      
plt.plot(x,y)                   #plot画图函数
plt.show()                      #展示函数