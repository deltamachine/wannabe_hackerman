import re
import sys
from collections import Counter
from streamparser import parse


def parse_surface_forms(apertium_string):
    surface_forms = []
    parsed_string = parse(apertium_string)

    for word in parsed_string:
        surface_forms.append(word.wordform)

    return surface_forms


def count_labels(surface_forms, input_conllu):
    with open(input_conllu, 'r', encoding='utf-8') as file:
        corpus = file.read()

    for form in surface_forms:
        form_regexp = '\n[0-9]+\t' + \
            form + '\t.*?\t.*?\t.*?\t.*?\t.*?\t(.*?)\t'

        labels = re.findall(form_regexp, corpus, flags = re.IGNORECASE)
        most_frequent_label = Counter(labels).most_common(1)

        if most_frequent_label != []:
            print(
                '%s: %s, %s times' %
                (form,
                 most_frequent_label[0][0],
                 most_frequent_label[0][1]))
        else:
            print(form, ': not found in corpus')


def main():
    apertium_string = sys.argv[1]
    input_conllu = sys.argv[2]

    surface_forms = parse_surface_forms(apertium_string)
    count_labels(surface_forms, input_conllu)


if __name__ == '__main__':
    main()
