GSoC 2017: coding challenges
=====================

###Apertium challenges:

* _flatten_conllu.py:_ A script that takes a dependency treebank in UD format and "flattens" it, that is, applies the following transformations:
 * Words with the @conj relation take the label of their head
 * Words with the @parataxis relation take the label of their head

* _calculate_accuracy_index.py:_ A script that does the following:
 * Takes -train.conllu file and calculates the table: surface_form - label - frequency
 * Takes -dev.corpus and for each token assigns the most frequent label from the table
 * Calculates the accuracy index

* _label_asf:_ A script that takes a sentence in Apertium stream format and for each surface form applies the most frequent label from the labelled corpus.
```cmd
$ python "string in Apertium stream format" labelled-corpus.conllu
```
