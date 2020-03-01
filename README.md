# Data

This repository contains the Development languages for SIGMORPHON 2020 Task 0.  
Surprise language data will be released here later during the Generalization Phase.  


All data files are in canonicalized format (see tags.yaml for possible tags): tags start with POS, and features follow lexicographic order. 

Tags follow [UniMorph schema](https://unimorph.github.io/) that was slightly extended with a few new tags (such as ``1+INCL''; due to new languages). 

We additionally `provide' WALS features [here](https://wals.info/download) for those who choose to use them (allowed for both constrained and unconstrained submissions).


## Evaluation

The official evaluation script `evaluate.py` lives in this directory.
You may run the evaluation script as shown in the example below.

```
python3 evaluate.py --hyp lang.hyp --ref lang.dev

accuracy:	67.30
levenshtein:	0.93
```
