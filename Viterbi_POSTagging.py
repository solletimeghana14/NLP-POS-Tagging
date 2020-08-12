import os
import sys

def Viterbi(sentence):
    words=sentence.split()
    tags=('NNP','MD','VB','JJ','NN','RB','DT')
    start_probabilities = {'NNP': 0.2767, 'MD': 0.0006, 'VB': 0.0031, 'JJ': 0.0453, 'NN': 0.0499, 'RB': 0.0510,'DT': 0.2026}
    HMM_transition_probability = {
        'NNP':{'NNP': 0.3777, 'MD': 0.0110, 'VB': 0.0009, 'JJ': 0.0084, 'NN': 0.0584, 'RB': 0.0090, 'DT': 0.0025},
        'MD': {'NNP': 0.0008, 'MD': 0.0002, 'VB': 0.7968, 'JJ': 0.0005, 'NN': 0.0008, 'RB': 0.1698, 'DT': 0.0041},
        'VB': {'NNP': 0.0322, 'MD': 0.0005, 'VB': 0.0050, 'JJ': 0.0837, 'NN': 0.0615, 'RB': 0.0514, 'DT': 0.2231},
        'JJ': {'NNP': 0.0366, 'MD': 0.0004, 'VB': 0.0001, 'JJ': 0.0733, 'NN': 0.4509, 'RB': 0.0036, 'DT': 0.0036},
        'NN': {'NNP': 0.0096, 'MD': 0.0176, 'VB': 0.0014, 'JJ': 0.0086, 'NN': 0.1216, 'RB': 0.0177, 'DT': 0.0068},
        'RB': {'NNP': 0.0068, 'MD': 0.0102, 'VB': 0.1011, 'JJ': 0.1012, 'NN': 0.0120, 'RB': 0.0728, 'DT': 0.0479},
        'DT': {'NNP': 0.1147, 'MD': 0.0021, 'VB': 0.0002, 'JJ': 0.2157, 'NN': 0.4744, 'RB': 0.0102, 'DT': 0.0017},
    }
    HMM_output_probability = {
                          'NNP':{'Janet': 0.000032, 'will': 0, 'back': 0, 'the': 0.000048, 'bill': 0},
                          'MD': {'Janet': 0, 'will': 0.308431, 'back': 0, 'the': 0, 'bill': 0},
                          'VB': {'Janet': 0, 'will': 0.000028, 'back': 0.000672, 'the': 0, 'bill': 0.000028},
                          'JJ': {'Janet': 0, 'will': 0, 'back': 0.000340, 'the': 0, 'bill': 0},
                          'NN': {'Janet': 0, 'will': 0.000200, 'back': 0.000223, 'the': 0, 'bill': 0.002337},
                          'RB': {'Janet': 0, 'will': 0, 'back': 0.010446, 'the': 0, 'bill': 0},
                          'DT': {'Janet': 0, 'will': 0, 'back': 0, 'the': 0.506099, 'bill': 0},
                          }
    
    
    rows=len(tags) 
    cols=len(words)
    V = [[0 for i in range(cols)] for j in range(rows)]
    B=  [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
          V[i][0]=start_probabilities[tags[i]]*HMM_output_probability[tags[i]][words[0]]
            
    for i in range(1,cols):
        for j in range(rows):
            maximum=0
            prev=-1
            for t in range(rows):
                if HMM_output_probability[tags[j]][words[i]]!=0:
                    value=V[t][i-1]*HMM_transition_probability[tags[t]][tags[j]]
                    if value>maximum:
                        maximum=value
                        prev=t
                    V[j][i]=V[prev][i-1]*HMM_transition_probability[tags[prev]][tags[j]]*HMM_output_probability[tags[j]][words[i]]   
                    B[j][i]=prev
                    
    T=["" for i in range(cols)] 
    ma=0
    tag_index=0
    for j in range(rows):
        if V[j][cols-1]>ma:
            ma=V[j][cols-1]
            tag_index=B[j][cols-1]
            T[cols-1]=tags[j] 
    Observation_Probability_Sequence=ma

    for i in range(cols-2,0,-1):
        T[i]=tags[tag_index]
        tag_index=B[tag_index][i]
    T[0]=tags[tag_index] 

    print("Observation Probability of Sequence:",Observation_Probability_Sequence)
    print("Tag sequence of given observation:",T)

if __name__ == '__main__':
    arg_list = sys.argv
    sentence=str(arg_list[1])
    Viterbi(sentence)
