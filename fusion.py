from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import scipy.spatial as sp
print("Import Successful")
print("Threshold for merging set at 0.5")

print("------------------------")

thresh_merge = 0.5

def split_comma_separated(sentence):
    sentence = sentence.split(',')
    new_sentence = []
    for frame in sentence:
        frame = frame.strip()
        new_sentence.append(frame)
    return new_sentence


def remove_newline(frame):
    frame = frame.strip('\n')
    return frame

def create_corpus(first_frames,second_frames):
    corpus = [frame for frame in first_frames]
    for frame_element in second_frames:
        corpus.append(frame_element)
    return corpus

def sentence_compactor(cosine_sim_matrix,first_sentence,second_sentence):
    mapping = dict()
    index = cosine_sim_matrix.argmax(axis=1)
    for i in range(len(index)):
        if cosine_sim_matrix[i][index[i]]>=thresh_merge:
            mapping[first_sentence[i]]=second_sentence[index[i]]
        else:
            mapping[first_sentence[i]]=''
            mapping[second_sentence[index[i]]]=''
    
    for i in range(len(second_sentence)):
        if i not in index:
            mapping[second_sentence[i]]=''
    
    return mapping   

def sentence_fusion(mapping):
    final_fused_sen = []
    for u,v in mapping.items():
        
        if len(u)>=len(v):
            final_fused_sen.append(u)
        
        else:
            final_fused_sen.append(v)
    
    return final_fused_sen

def main_util(sentence1,sentence2):
    first_sentence = split_comma_separated(sentence1)
    second_sentence = split_comma_separated(sentence2)
    last_frame = first_sentence[-1]
    first_sentence[-1] = remove_newline(last_frame)
    first_frames = first_sentence
    second_frames = second_sentence
    corpus = create_corpus(first_frames,second_frames)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    X = X.toarray()
    first_sen_vec = X[0:len(first_frames)]
    second_sen_vec = X[len(first_frames):]  
    cosine_sim_matrix = 1 - sp.distance.cdist(first_sen_vec, second_sen_vec, 'cosine')
    mapping = sentence_compactor(cosine_sim_matrix,first_sentence,second_sentence)
    print(sentence_fusion(mapping))
    print("------------------------")

def main():
    print("Please Enter the filename")
    filename = input()
    with open(filename,'r') as file_handler:
        sentences = file_handler.readlines()
    num_of_pairs = len(sentences)/2
    counter = 0
    
    for _ in range(int(num_of_pairs)):
        i=counter
        j=i+1
        
        print("Output for pair starting at line number ",counter+1)
        main_util(sentences[i],sentences[j])
        counter = counter + 2
        
if __name__=="__main__":
    main()
   

