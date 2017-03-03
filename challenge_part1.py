import re

def head_label(sentence, word, function):
    head = word.split('\t')[6]
    head_index = int(head) - 1
    new_label = sentence[head_index].split('\t')[7]
    word = re.sub(function, new_label, word)

    return word

def flatten_conllu():
    with open ('ru-ud-dev.conllu', 'r', encoding='utf-8') as file:
        text = file.read().split('\n\n')

    with open ('flattened2-ru-ud-dev.conllu.conllu', 'w', encoding='utf-8') as file:    
        for sentence in text:
            sentence = sentence.split('\n')
            for i in range (len(sentence)):
                if 'conj' in sentence[i]:
                    sentence[i] = head_label (sentence, sentence[i], 'conj')
                if 'parataxis' in sentence[i]:
                    sentence[i] = head_label (sentence, sentence[i], 'parataxis')

            sentence = '\n'.join(sentence)
            file.write(sentence)
            file.write('\n')
        '''for sentence in text:
            conj_words = re.findall ('\n[0-9]+\t.*?\t.*?\t.*?\t.*?\t.*?\t.*?\tconj\t.*?\t', sentence)
            parataxis_words = re.findall ('\n[0-9]+\t.*?\t.*?\t.*?\t.*?\t.*?\t.*?\tparataxis\t.*?\t', sentence)
            for word in conj_words:
                new_word = head_label(sentence, word, 'conj')
                sentence = re.sub(word, new_word, sentence)
            for word in parataxis_words:
                new_word = head_label(sentence, word, 'parataxis')
                sentence = re.sub(word, new_word, sentence)
            sentence = '\n'.join(sentence)
            file.write(sentence)
            file.write('\n')'''

if __name__ == '__main__':
    flatten_conllu()

           
