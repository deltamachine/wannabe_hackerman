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
        labels = []

        # fixing the register problem
        low_form_regexp = '\n[0-9]+\t' + \
            form.lower() + '\t.*?\t.*?\t.*?\t.*?\t.*?\t.*?\t'

        upper_form_regexp = '\n[0-9]+\t' + form[0].upper() + \
            form[1:] + '\t.*?\t.*?\t.*?\t.*?\t.*?\t.*?\t'

        words = re.findall(low_form_regexp, corpus)
        words += re.findall(upper_form_regexp, corpus)

        for word in words:
            label = word.split('\t')[7]
            labels.append(label)

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
