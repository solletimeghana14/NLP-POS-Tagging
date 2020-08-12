import os
import sys
import re
import itertools
from collections import defaultdict


def NaiveBayes(inputsentence):
    sentences=[]
    first_tag=[]
    last_tag=[]
    words_pos=[]
    w_p=[]
    tags=[]
    tag_tag=[]
    tag_tag_count={}
    with open("NLP6320_POSTaggedTrainingSet-Unix.txt",'r') as file:
        data=file.read()
        sentences.extend(data.split('\n'))
        count_of_starttag=len(sentences)
        for i in range(len(sentences)-1):
            words=sentences[i].split()
            token = words[0].split('_')
            first_tag.append(token[1])
            tokens = words[len(words)-1].split('_')
            last_tag.append(tokens[1])
            tags_sentence=[]
            for w in words:
                t=w.split('_')
                w_p.append(t)
                words_pos.append(t[0]+" "+t[1])
                tags.append(t[1])
                tags_sentence.append(t[1])
            for k in range(len(tags_sentence)):
                if k!=len(tags_sentence)-1:
                    tag_tag = tags_sentence[k] + " " + tags_sentence[k+1]
                    if(tag_tag_count.get(tag_tag) != None):
                        tag_tag_count[tag_tag] = tag_tag_count.get(tag_tag)+1
                    else:
                        tag_tag_count[tag_tag] = 1
                
            
                    
    first_tag_count={}
    for i in first_tag:
        if i not in first_tag_count:
            first_tag_count[i]=1
        else:
            first_tag_count[i]=first_tag_count[i]+1

    last_tag_count={}
    for i in last_tag:
        if i not in last_tag_count:
            last_tag_count[i]=1
        else:
            last_tag_count[i]=last_tag_count[i]+1
            
    unique_words_pos=[]
    for i in w_p:
        if i not in unique_words_pos:
            unique_words_pos.append(i)
            
    word_tag_count={}
    for i in words_pos:
        if i not in word_tag_count:
            word_tag_count[i]=1
        else:
            word_tag_count[i]=word_tag_count[i]+1
            
    tag_count={}
    for i in tags:
        if i not in tag_count:
            tag_count[i]=1
        else:
            tag_count[i]=tag_count[i]+1
            
    word_tagslist = defaultdict(list) 
    for key, val in unique_words_pos: 
        word_tagslist[key].append(val) 
        
    word_sequence=inputsentence
    wos=word_sequence.split()
    list_tag_lists=[]
    for i in wos:
        list_tag_lists.append(word_tagslist[i])
    combinations = list(itertools.product(*list_tag_lists))
    
    maximum=0
    result=[]
    for ts in combinations:
        p=1
        for j in range(len(wos)):
            if j==0:
                p=p*(0 if word_tag_count.get(wos[j]+" "+ts[j]) is None else float(word_tag_count[wos[j]+" "+ts[j]])/tag_count[ts[j]])*(0 if first_tag_count.get(ts[j]) is None else float(first_tag_count.get(ts[j]))/(len(sentences)-1))
            elif j==(len(wos)-1):
                p=p*(0 if word_tag_count.get(wos[j]+" "+ts[j]) is None else float(word_tag_count[wos[j]+" "+ts[j]])/tag_count[ts[j]])*(0 if tag_tag_count.get(ts[j-1]+" "+ts[j]) is None else float(tag_tag_count[ts[j-1]+" "+ts[j]])/tag_count[ts[j-1]])*(0 if last_tag_count.get(ts[j]) is None else float(last_tag_count.get(ts[j]))/tag_count[ts[j]])
            else:
                p=p*(0 if word_tag_count.get(wos[j]+" "+ts[j]) is None else float(word_tag_count[wos[j]+" "+ts[j]])/tag_count[ts[j]])*(0 if tag_tag_count.get(ts[j-1]+" "+ts[j]) is None else float(tag_tag_count[ts[j-1]+" "+ts[j]])/tag_count[ts[j-1]])
        if p>=maximum:
            maximum=p
            result=ts

    print(maximum)
    print(result)

if __name__ == '__main__':

    arg_list = sys.argv
    sentence=str(arg_list[1])
    NaiveBayes(sentence)
