# data

This repository contains the Development languages for SIGMORPHON 2020 Task 0.  
Surprise language data will be released here later during the Generalization Phase.  

We additionally provide WALS features for those who choose to use them (allowed for both constrained and unconstrained submissions).  


## Evaluation

The official evaluation script `evaluate.py` lives in this directory.
You may run the evaluation script as shown in the example below.

```
python3 evaluate.py --hyp lang.hyp --ref lang.dev

accuracy:	67.30
levenshtein:	0.93
```
