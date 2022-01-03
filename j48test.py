import sys
import weka.core.jvm as jvm
import csv
import math
import weka.core.serialization as serialization
from weka.classifiers import Classifier
from weka.core.dataset import Instances
from weka.core.converters import Loader


jvm.start()

objects = serialization.read_all("3fmodel.model")
cls = Classifier(jobject=objects[0])
print(cls)
data = Instances(jobject=objects[1])
trainCl = data.class_attribute.values

loader = Loader(classname="weka.core.converters.CSVLoader")
data2 = loader.load_file("5rf32.csv")
data2.class_is_last()
#print(data2)
co = 0
itr = 0
for index, inst in enumerate(data2):
    itr +=1
    if itr>40:
        break
    act = inst.get_value(82)
    actCl = inst.class_attribute.values[int(act)] # value at that index
    pred = cls.classify_instance(inst)
    predCl = trainCl[int(pred)]
    print pred,predCl,trainCl,act,actCl,inst.class_attribute.values
    dist = cls.distribution_for_instance(inst)
    if predCl == actCl:
        co = co + 1
    print dist
print co
jvm.stop()
