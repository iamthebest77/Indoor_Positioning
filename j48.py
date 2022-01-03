import sys
import weka.core.jvm as jvm
import csv
import math
import weka.core.serialization as serialization
from weka.core.dataset import Instances

jvm.start()

#data_dir = "data/"

#Load dataset and print it

cl = []
with open('5rf31.csv', 'rb') as csvfile:
     value = csv.reader(csvfile, delimiter=',')
     for row in value:
         if row[-1] not in cl:
             cl.append(row[-1])
cl = cl[1:]
print cl


from weka.core.converters import Loader
loader = Loader(classname="weka.core.converters.CSVLoader")
data = loader.load_file("3ftraindata.csv")
data.class_is_last()
trainCl = data.class_attribute.values
#print(data)
#Build classifier on dataset, output predictions

from weka.classifiers import Classifier
cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.25","-M","2"])
cls.build_classifier(data)
print(cls)
serialization.write_all("3fmodel.model",[cls,Instances.template_instances(data)])

data2 = loader.load_file("5rf33.csv")
data2.class_is_last()
#print(data2)
co = 0
itr = 0
for index, inst in enumerate(data2):
    itr +=1
    #if itr>40:
    #    break
    act = inst.get_value(82)
    actCl = inst.class_attribute.values[int(act)] # value at that index
    pred = cls.classify_instance(inst)
    predCl = trainCl[int(pred)]
    print pred,predCl,trainCl,act,actCl,inst.class_attribute.values
    dist = cls.distribution_for_instance(inst)
    if predCl == actCl:
        co = co + 1
print co*100/index
jvm.stop()
