import pandas as pd
import numpy as np
import scipy.spatial.distance as dist
import random
np.set_printoptions(threshold=np.inf)
graphPath = 'G:/ml-latest-small/graph.csv'  #读入文件，在此我导入的是csv文件，改csv文件由两列组成，分别是source节点和target节点
graphDF = pd.read_csv(graphPath,index_col=None)
adjaMatrix=np.zeros((34,34))
i=np.arange(0,34,1)
adjaMatrix[i, i]=1
for i in range(0,graphDF.shape[0]) :  #利用邻接矩阵A来存储网络，其中A_{ij}表示第i个节点与第j个节点的是否有边相互链接，1表示i与j相互连接，0表示i与j没有相互连接。
    source=graphDF.loc[[i],['source']].values[0]
    target=graphDF.loc[[i],['target']].values[0]
    adjaMatrix[int(source)-1][int(target)-1]=1
    adjaMatrix[int(target) - 1][int(source) - 1] = 1
#print(adjaMatrix[1][8])


def S():     #计算每两点之间的jaccard距离，输出为34*34的矩阵
    Sadj=np.zeros((34,34))
    for i in range(0,34):
        for j in range(0,34):
            a=adjaMatrix[i]
            b=adjaMatrix[j]
            Sadj[i][j]=1-dist.pdist([a,b], 'jaccard')

    return Sadj





def changeC(Sadj):
    x = np.arange(0, 34, 1)
    x = x.tolist()
    #rand = random.choice(x)
    set=[[],[]]
    min=1
    rand = 0      #第一类中心
    for i in range(0,34):
        if(Sadj[0][i]<min):
            rand2=i     #第二类中心

    set[0].append(rand)
    set[1].append(rand2)

    x.remove(rand)
    x.remove(rand2)
    for i in range(0,2):
        j=33   #遍历所有节点
        while(j>0):
            maxvalue=0.19     #设置阈值，若大于阈值则有效，否则无效
            for m in range(0, 34):
                if(m in x):     #防止一个点被加入多次
                    tempmaxvalue = 0
                    for ii in range(0, len(set[i]) ):
                        tempmaxvalue += Sadj[set[i][ii]][m]  # 计算节点m到聚类list1中所有节点的杰卡德距离

                        if (tempmaxvalue/len(set[i]) > maxvalue):
                            maxvalue = tempmaxvalue/len(set[i])
                            maxnode = m  # 选取相似度最大的节点m

            adjaMatrix[rand][maxnode] = 1   #以下步骤是更新相似度矩阵
            adjaMatrix[maxnode][rand] = 1
            a = adjaMatrix[rand]
            b = adjaMatrix[maxnode]
            Sadj[rand][maxnode] = 1 - dist.pdist([a, b], 'jaccard')
            Sadj[maxnode][rand] = 1 - dist.pdist([a, b], 'jaccard')
            if maxnode in x:
                x.remove(maxnode)

                set[i].append(maxnode)  # 节点m添加到聚类set中
            j = j - 1  # 循环次数减1

        x.append(set[i][-1])
        set[i].pop()
    

    for i in range(0, len(x)):   #对于在上面步骤中尚未分类的节点
        post = x[i]
        setvalue1=0
        setvalue2=0
        for ii in range(0, len(set[0])):   #计算它更属于哪一类并加入
            setvalue1 += Sadj[set[0][ii]][post]
        for ii in range(0, len(set[1])):
            setvalue2 += Sadj[set[1][ii]][post]
        if(setvalue1>setvalue2):
            set[0].append(post)
        else:
            set[1].append(post)

    set[0] = [x + 1 for x in set[0]]
    set[1] = [x + 1 for x in set[1]]
    print('分组1为： '+str(set[0]))
    print('分组2为： '+str(set[1]))


Sadj=S()
changeC(Sadj)


