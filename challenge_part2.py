import re
from collections import Counter
from streamparser import parse

def parse_surface_forms():
    surface_forms = []
    apertium_string = ('^i/*i$ ^hoped/hope<vblex><past>/hope<vblex><pp>$ ^you/prpers<prn><subj><p2><mf><sp>/prpers<prn><obj><p2><mf><sp>$ ^are/be<vbser><pres>$ ^nice/nice<adj><sint>$')
    parsed_string = parse(apertium_string)

    for word in parsed_string:
        surface_forms.append(word.wordform)

    return surface_forms

def count_labels(surface_forms):
    with open ('C:/Users/Анна/Desktop/UD_English/en-ud-dev.conllu', 'r', encoding='utf-8') as file:
        corpus = file.read()

    for form in surface_forms:
        labels = []
        regexp = '\n[0-9]+\t' + form + '\t.*?\t.*?\t.*?\t.*?\t.*?\t.*?\t'
        words = re.findall(regexp, corpus)

        for word in words:
            label = word.split('\t')[7]
            labels.append(label)

        most_frequent_label = Counter(labels).most_common(1)

        if most_frequent_label != []:
            print ('%s: %s, %s times' %(form, most_frequent_label[0][0], most_frequent_label[0][1]))
        else:
            print (form, ': not found in corpus')

def main():
    surface_forms = parse_surface_forms()
    count_labels(surface_forms)

if __name__ == '__main__':
    main()
        

