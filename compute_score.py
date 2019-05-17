import collections
import numpy as np
import re
import io

path = "samples.txt"
def tokenize_string(sample):
    return tuple(sample.lower().split(' '))

def load_dataset(path, max_length=10, tokenize=False, max_vocab_size=2048):
    
    lines = {}

    with io.open(path, 'r', encoding="ISO-8859-1") as f:
        i = 0
        for line in f:
            line = line[:-1]
            # right pad with ` character

            if line not in lines:
                lines[line] = i
            i+=1

    return lines

num_dict = load_dataset(path)


score_dict =  {}
with io.open("rockyou.txt", 'r', encoding="ISO-8859-1") as f:
    for line in f:
        line = line[:-1]
        if line in num_dict:
            num = num_dict[line]
            score_dict[line] = num

import json


json = json.dumps(score_dict)
f = open("results.json","w")
f.write(json)
f.close()

            
