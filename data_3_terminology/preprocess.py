import os

script_dir = os.path.dirname(__file__) 
train_path = os.path.join(script_dir, "../data_2_terminology/train.tsv")
test_path = os.path.join(script_dir, "../data_2_terminology/test.tsv")
dev_path = os.path.join(script_dir, "../data_2_terminology/dev.tsv")
new_train_path = os.path.join("train.tsv")
new_test_path = os.path.join("test.tsv")
new_dev_path = os.path.join("dev.tsv")

train = open(train_path, 'r')
new_train = open(new_train_path, 'w')
train_list = []
lines = train. readlines()
for line in lines:
    l = line.split('\t')
    if abs(len(l[0].split()) - len(l[1].split()))< 15:
        train_list.append(line)

new_train.writelines(train_list)

test = open(test_path, 'r')
new_test = open(new_test_path, 'w')
test_list = []
lines = test. readlines()
for line in lines:
    l = line.split('\t')
    if abs(len(l[0].split()) - len(l[1].split()))< 15:
        test_list.append(line)

new_test.writelines(test_list)

dev = open(dev_path, 'r')
new_dev = open(new_dev_path, 'w')
dev_list = []
lines = dev. readlines()
for line in lines:
    l = line.split('\t')
    if abs(len(l[0].split()) - len(l[1].split()))< 15:
        dev_list.append(line)

new_dev.writelines(dev_list)
