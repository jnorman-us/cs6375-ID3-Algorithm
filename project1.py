import math
import numpy as np
import pandas as pd
import argparse

# used to determine if the leaf partition should be expanded further (i.e. if entropy is 0, no need to expand)
def calculatePreviousEntropy(rows):
    target = rows.columns[len(rows.columns) - 1]
    classes = {}

    for index, row in rows.iterrows():
        targ_value = row[target]
        if targ_value not in classes:
            classes[targ_value] = 0
        classes[targ_value] += 1

    entropySum = 0
    for key in classes:
        prob = classes[key] / len(rows)
        if prob != 0:
            entropySum += prob * math.log(1 / prob, 2)
    return entropySum


def calculateEntropy(rows, attribute):
    target = rows.columns[len(rows.columns) - 1]
    occurences = {}
    counts = {}
    partition = {}

    for index, row in rows.iterrows():
        attr_value = row[attribute]
        targ_value = row[target]
        if attr_value not in occurences:
            occurences[attr_value] = {}
            counts[attr_value] = 0
            partition[attr_value] = []
        if targ_value not in occurences[attr_value]:
            occurences[attr_value][targ_value] = 0
        occurences[attr_value][targ_value] += 1
        counts[attr_value] += 1
        partition[attr_value].append(index)

    entropySum = 0
    for key in occurences:
        count = counts[key]
        subProbSum = 0
        for attr_value in occurences[key]:
            occs = occurences[key][attr_value]
            prob = occs / count
            if prob != 0:
                subProbSum += prob * math.log(1 / prob, 2)
        entropySum += (count / len(rows)) * subProbSum

    partition = list(partition.values())
    return (entropySum, partition)

def cal_best_partition(df, partition):
    # TO DO, partition the data based on the entropy of the selected arguments (picking the max split possible).
    min_part = None
    min_attribute = None
    min_entropy = 1000
    min_calculatedPartition = None

    for part in partition:
        entries = np.array(partition[part]) - 1
        rows = df.loc[entries, :]

        for attribute_i in range(len(df.columns)):
            attribute = df.columns[attribute_i]
            if attribute_i == len(df.columns) - 1: # skip over the target attribute
                continue

            prevEntropy = calculatePreviousEntropy(rows)
            if prevEntropy == 0:
                continue # this node is a leaf and cannot be expanded further

            entropy, calculatedPartition = calculateEntropy(rows, attribute)
            print(part, attribute, prevEntropy, entropy, calculatedPartition)

            if prevEntropy != entropy and entropy < min_entropy:
                min_part = part
                min_attribute = attribute
                min_entropy = entropy
                min_calculatedPartition = calculatedPartition

    if min_part is not None:
        output_text = 'Partition ' + min_part + ' was replaced with partition '
        del partition[min_part]
        for i in range(len(min_calculatedPartition)):
            newPartitionName = min_part + "" + str(i + 1)
            partition[newPartitionName] = np.array(min_calculatedPartition[i]) + 1
            output_text += newPartitionName + (',' if i < len(min_calculatedPartition) - 1 else '')
        output_text += ' using Feature ' + min_attribute
        print(output_text)
    else:
        print("No partitions created")

    return partition

if __name__ == "__main__":
    # Read user input
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type = str, default = 'dataset-1.csv', help = "Input csv file name of dataset")
    parser.add_argument("--input", type = str, default = 'partition-2.txt', help = "Input partition")
    parser.add_argument("--output", type = str, default = 'partition-3.txt', help = "Output partition")
    args = parser.parse_args()
    dataset = args.dataset
    input_partition_filename = args.input
    output_partition_filename = args.output

    # Read input dataset and partition
    df = pd.read_csv(dataset)
    outfile = open(output_partition_filename,"w")
    partition = {}
    with open(input_partition_filename) as f:
        for line in f.readlines():
            word = line.split(' ')
            key = word[0]
            value =[]
            for i in range(1,len(word)):
                value.append(int(word[i]))
            partition[key] = value

    # processing
    result_partition = cal_best_partition(df, partition)

    # writing output
    for key, value in result_partition.items():
        value_str=''
        for val in value:
            value_str = value_str+' '+ str(val)
        line = str(key)+''+value_str+'\n'
        outfile.writelines(line)
    outfile.close()