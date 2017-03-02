from AutoE import *
from utils import *


def setPara():
    para = {}
    para["learningRate"] = 0.001
    para["trainingEpochs"] = 1000
    para["batchSize"] = 1000
    para["beta"] = 15
    para["alpha"] = 1
    para["gamma"] = 5
    para['v'] = 0.1
    para["dbn_init"] = True
    para["sparse_dot"] = True
    return para

dataSet = "blogCatalog3.txt"

data = getData(dataSet)
para = setPara()
para["M"] = data["N"]
myAE = AutoE_sparse([data["N"],1000,100], para, data)    

if __name__ == "__main__":
    myAE.doTrain()
    embedding = myAE.getEmbedding(data["feature"])
    sio.savemat('embedding.mat',{'embedding':embedding})