import sys


def head_label(sentence, word):
    head = word[6]
    head_index = int(head) - 1
    new_label = sentence[head_index][7]
    return new_label


def flatten(input_conllu):
    with open(input_conllu, 'r', encoding='utf-8') as file:
        corpus = file.read().split('\n\n')

    with open(input_conllu, 'w', encoding='utf-8') as file:
        for part in corpus:
            part = part.split('\n')
            sentence = []

            for line in part:
                if line == '':
                    file.write('%s\n' % (line))
                elif line[0] == '#':
                    file.write('%s\n' % (line))
                else:
                    word = line.split('\t')
                    sentence.append(word)

            for word in sentence:
                if word[7] == 'conj' or word[7] == 'parataxis':
                    word[7] = head_label(sentence, word)

                word = '\t'.join(word)
                file.write('%s\n' % (word))

            file.write('\n')


input_conllu = sys.argv[1]
flatten(input_conllu)
