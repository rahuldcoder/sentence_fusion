# sentence_fusion:
This repo deals with fusion of sentences based on cosine similarity


# input format:
The input format consists of pair of sentences one after the other for example if we needed to fuse two pairs like:

Pair 1:

Its Jallikattu day , at, the world famous Alanganallur

Jallikattu , at , Alanganallur the victory of youth

Pair 2:

Its Jallikattu day,at,the world famous Alanganallur

World Famous Alanganallur,Jallikattu,back after 3 years

Then our input txt file would be similar to "sample_input.txt" file
Kindly look at "sample_input.txt" file for reference

# threshold for fusion:
The default threshold value for fusion is 0.5 which can be adjusted by changing the 'thresh_merge' gloabal variable at the top.
