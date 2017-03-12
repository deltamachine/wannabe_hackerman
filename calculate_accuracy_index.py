import sys
from collections import Counter


def parse_sf_labels(input_train):
    with open(input_train, 'r', encoding='utf-8') as file:
        corpus = file.readlines()

    freq_table = {}

    for line in corpus:
        if line.strip('\n') == '':
            continue
        if line[0] == '#':
            continue

        word = line.strip('\n').split('\t')
        form = word[1]
        label = word[7]

        if form in freq_table.keys():
            freq_table[form].append(label)
        else:
            freq_table[form] = []
            freq_table[form].append(label)

    return freq_table


def accuracy_index(input_dev, freq_table):
    with open(input_dev, 'r', encoding='utf-8') as file:
        dev_corpus = file.readlines()

    c = 0
    t = 0

    for line in dev_corpus:
        if line.strip('\n') == '':
            continue
        if line[0] == '#':
            continue

        word = line.strip('\n').split('\t')
        form = word[1]
        label = word[7]
        t += 1

        try:
            train_form = freq_table[form]
            if label == train_form[0]:
                c += 1
        except Exception:
            t -= 1

    accuracy_index = c / t

    print(accuracy_index)


input_train = sys.argv[1]
input_dev = sys.argv[2]

freq_table = parse_sf_labels(input_train)
accuracy_index(input_dev, freq_table)
