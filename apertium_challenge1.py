import re


def head_label(sentence, word, function):
    head = word.split('\t')[6]
    head_index = int(head) - 1
    new_label = sentence[head_index].split('\t')[7]
    word = re.sub(function, new_label, word)
    return word


def flatten_conllu():
    with open('ru-ud-train.conllu', 'r', encoding='utf-8') as file:
        corpora = file.read().split('\n\n')

    with open('flat-ru-ud-train.conllu', 'w', encoding='utf-8') as file:
        for sentence in corpora:
            sentence = sentence.split('\n')

            for i in range(len(sentence)):
                if 'conj' in sentence[i]:
                    sentence[i] = head_label(sentence, sentence[i], 'conj')
                if 'parataxis' in sentence[i]:
                    sentence[i] = head_label(sentence, sentence[i], 'parataxis')

            sentence = '\n'.join(sentence)
            file.write(sentence)
            file.write('\n\n')


if __name__ == '__main__':
    flatten_conllu()
