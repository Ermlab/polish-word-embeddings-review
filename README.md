# Polish Word Embeddings Review

Evaluation of polish word embeddings prepared by various research groups. Evaluation is done by words analogy task

## Used word embeddings
### Word2Vec Format
IPIPAN Models:
- http://dsmodels.nlp.ipipan.waw.pl/

Facebook FastText:
- https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pl.300.vec.gz

Embeddings from https://github.com/Kyubyong/wordvectors
Fasttext
- https://www.dropbox.com/s/cibxhnsqk6gn1d8/pl.tar.gz?dl=0

Word2Vec
- https://drive.google.com/file/d/0B0ZXk88koS2KbFlmMy1PUHBSZ0E/view

Embeddings from Sławomir Dadas (embeddings in results with sdadas prefix):
* https://github.com/sdadas/polish-nlp-resources

### Pre-Trained Models

* https://clarin-pl.eu/dspace/handle/11321/442
* https://clarin-pl.eu/dspace/handle/11321/606
* https://clarin-pl.eu/dspace/handle/11321/600
* https://clarin-pl.eu/dspace/handle/11321/327
* http://vectors.nlpl.eu/repository (id: 62,167)
* https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pl.300.bin.gz



## Evaluation procedure

To evaluate the word embedding, we use the function evaluation_word_pairs and assessment_word_analogies provided by gensim.

For analogue testing, a file provided by facebook fastext is used, a link to it can be found in References. To evaluate the similarity in word embedding, the Polish version of SimLex999, made available by IPIPAN, is used, but we had to adjust it to the function by removing the column with the row identifier (first collumn) and the entire relatedness column (last column). A link to the version provided by IPIPAN can be found in References.

## Results

|  name | vocab size | vector size | Total analogy accuracy | pearson | spearman | out of vocab |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  facebook_fastext-300.txt | 2000000 | 300 | 0,66 | 0,369 | 0,3934 | 4,004 |
|  nkjp+wiki-lemmas-restricted-300-skipg-ns.txt | 1407762 | 300 | 0,62 | 0,3875 | 0,4444 | 1,6016 |
|  nkjp+wiki-lemmas-all-300-skipg-ns.txt | 1549322 | 300 | 0,61 | 0,3973 | 0,4567 | 1,6016 |
|  nkjp+wiki-lemmas-restricted-300-cbow-ns.txt | 1407762 | 300 | 0,59 | 0,4132 | 0,4541 | 1,6016 |
|  nkjp-lemmas-restricted-300-skipg-ns.txt | 1162845 | 300 | 0,58 | 0,4031 | 0,4508 | 1,6016 |
|  wiki-lemmas-restricted-300-skipg-ns.txt | 446608 | 300 | 0,58 | 0,3311 | 0,3893 | 2,1021 |
|  wiki-lemmas-all-300-skipg-ns.txt | 473000 | 300 | 0,56 | 0,3456 | 0,4025 | 2,1021 |
|  nkjp-lemmas-all-300-skipg-ns.txt | 1282621 | 300 | 0,56 | 0,4127 | 0,4634 | 1,6016 |
|  wiki-lemmas-restricted-300-cbow-ns.txt | 446608 | 300 | 0,55 | 0,3647 | 0,4044 | 2,1021 |
|  wiki-lemmas-restricted-100-skipg-ns.txt | 446608 | 100 | 0,53 | 0,3008 | 0,348 | 2,1021 |
|  nkjp+wiki-lemmas-all-300-cbow-ns.txt | 1549322 | 300 | 0,53 | 0,4085 | 0,4578 | 1,6016 |
|  nkjp-lemmas-restricted-300-cbow-ns.txt | 1162845 | 300 | 0,53 | 0,4108 | 0,4524 | 1,6016 |
|  nkjp+wiki-lemmas-restricted-300-skipg-hs.txt | 1407762 | 300 | 0,52 | 0,3182 | 0,3785 | 1,6016 |
|  nkjp+wiki-lemmas-all-300-cbow-ns-50.txt | 294182 | 300 | 0,52 | 0,4092 | 0,46 | 1,6016 |
|  wiki-lemmas-restricted-300-skipg-hs.txt | 446608 | 300 | 0,52 | 0,2811 | 0,3374 | 2,1021 |
|  wiki-lemmas-all-300-cbow-ns.txt | 473000 | 300 | 0,51 | 0,3634 | 0,4104 | 2,1021 |
|  wiki-lemmas-all-300-skipg-hs.txt | 473000 | 300 | 0,51 | 0,2861 | 0,3425 | 2,1021 |
|  nkjp+wiki-lemmas-restricted-100-skipg-ns.txt | 1407762 | 100 | 0,50 | 0,3436 | 0,3937 | 1,6016 |
|  nkjp+wiki-lemmas-pos-all-300-skipg-ns.txt | 1686208 | 300 | 0,50 | -0,1073 | -0,3 | 99,4995 |
|  nkjp+wiki-lemmas-pos-all-300-cbow-hs.txt | 1686208 | 300 | 0,50 | -0,1167 | -0,3 | 99,4995 |
|  wiki-lemmas-all-100-skipg-ns.txt | 473000 | 100 | 0,50 | 0,3054 | 0,3558 | 2,1021 |
|  nkjp+wiki-lemmas-all-300-skipg-hs.txt | 1549322 | 300 | 0,50 | 0,3319 | 0,3937 | 1,6016 |
|  nkjp+wiki-lemmas-restricted-100-cbow-ns.txt | 1407762 | 100 | 0,49 | 0,368 | 0,4123 | 1,6016 |
|  nkjp-lemmas-restricted-300-skipg-hs.txt | 1162845 | 300 | 0,48 | 0,3493 | 0,4042 | 1,6016 |
|  nkjp+wiki-forms-restricted-300-skipg-ns.txt | 1982479 | 300 | 0,48 | 0,3833 | 0,4406 | 1,3013 |
|  wiki-lemmas-restricted-100-cbow-ns.txt | 446608 | 100 | 0,48 | 0,3321 | 0,3725 | 2,1021 |
|  nkjp-lemmas-all-300-cbow-ns.txt | 1282621 | 300 | 0,48 | 0,4057 | 0,4544 | 1,6016 |
|  kyubyong_fasttext.txt | 50036 | 300 | 0,48 | 0,3114 | 0,3879 | 41,4414 |
|  nkjp-lemmas-restricted-100-skipg-ns.txt | 1162845 | 100 | 0,47 | 0,3613 | 0,403 | 1,6016 |
|  nkjp+wiki-lemmas-all-100-skipg-ns.txt | 1549322 | 100 | 0,46 | 0,3524 | 0,4054 | 1,6016 |
|  nkjp+wiki-forms-all-300-skipg-ns.txt | 2123132 | 300 | 0,46 | 0,3881 | 0,4388 | 1,3013 |
|  nkjp-forms-restricted-300-skipg-ns.txt | 1713738 | 300 | 0,46 | 0,3937 | 0,4446 | 1,3013 |
|  nkjp-lemmas-all-300-skipg-hs.txt | 1282621 | 300 | 0,46 | 0,3603 | 0,4166 | 1,6016 |
|  nkjp-forms-all-300-skipg-ns.txt | 1832700 | 300 | 0,45 | 0,3924 | 0,4405 | 1,3013 |
|  nkjp+wiki-forms-all-300-skipg-ns-50.txt | 556932 | 300 | 0,45 | 0,3856 | 0,438 | 1,3013 |
|  nkjp-lemmas-all-100-skipg-ns.txt | 1282621 | 100 | 0,44 | 0,3673 | 0,4111 | 1,6016 |
|  nkjp-lemmas-restricted-100-cbow-ns.txt | 1162845 | 100 | 0,43 | 0,3661 | 0,4102 | 1,6016 |
|  wiki-lemmas-all-100-cbow-ns.txt | 473000 | 100 | 0,43 | 0,3292 | 0,3794 | 2,1021 |
|  wiki-lemmas-restricted-100-skipg-hs.txt | 446608 | 100 | 0,42 | 0,2547 | 0,3011 | 2,1021 |
|  nkjp+wiki-forms-restricted-300-cbow-ns.txt | 1982479 | 300 | 0,42 | 0,3631 | 0,3917 | 1,3013 |
|  nkjp+wiki-forms-restricted-300-skipg-hs.txt | 1982479 | 300 | 0,41 | 0,3415 | 0,4033 | 1,3013 |
|  nkjp+wiki-lemmas-restricted-100-skipg-hs.txt | 1407762 | 100 | 0,40 | 0,2828 | 0,3358 | 1,6016 |
|  nkjp-forms-restricted-300-cbow-ns.txt | 1713738 | 300 | 0,40 | 0,3623 | 0,3884 | 1,3013 |
|  nkjp+wiki-lemmas-all-100-cbow-ns.txt | 1549322 | 100 | 0,40 | 0,3657 | 0,4166 | 1,6016 |
|  nkjp+wiki-forms-all-300-cbow-ns.txt | 2123132 | 300 | 0,40 | 0,3452 | 0,3709 | 1,3013 |
|  wiki-lemmas-all-100-skipg-hs.txt | 473000 | 100 | 0,40 | 0,2646 | 0,3133 | 2,1021 |
|  nkjp+wiki-forms-all-300-skipg-hs.txt | 2123132 | 300 | 0,39 | 0,34 | 0,3975 | 1,3013 |
|  nkjp+wiki-forms-all-300-cbow-ns-50.txt | 556932 | 300 | 0,39 | 0,3442 | 0,3683 | 1,3013 |
|  nkjp+wiki-forms-restricted-100-skipg-ns.txt | 1982479 | 100 | 0,39 | 0,333 | 0,3819 | 1,3013 |
|  nkjp-forms-restricted-300-skipg-hs.txt | 1713738 | 300 | 0,38 | 0,3404 | 0,387 | 1,3013 |
|  nkjp-forms-restricted-100-skipg-ns.txt | 1713738 | 100 | 0,38 | 0,3399 | 0,3803 | 1,3013 |
|  nkjp-forms-all-300-cbow-ns.txt | 1832700 | 300 | 0,38 | 0,3481 | 0,3714 | 1,3013 |
|  nkjp+wiki-forms-all-300-skipg-hs-50.txt | 556932 | 300 | 0,38 | 0,3448 | 0,4021 | 1,3013 |
|  nkjp+wiki-forms-all-100-skipg-ns.txt | 2123132 | 100 | 0,37 | 0,3421 | 0,3854 | 1,3013 |
|  nkjp-forms-all-300-skipg-hs.txt | 1832700 | 300 | 0,37 | 0,3503 | 0,3906 | 1,3013 |
|  nkjp-lemmas-restricted-100-skipg-hs.txt | 1162845 | 100 | 0,37 | 0,3153 | 0,3612 | 1,6016 |
|  nkjp+wiki-lemmas-all-100-skipg-hs.txt | 1549322 | 100 | 0,36 | 0,2931 | 0,3468 | 1,6016 |
|  nkjp-forms-all-100-skipg-ns.txt | 1832700 | 100 | 0,36 | 0,3508 | 0,3879 | 1,3013 |
|  nkjp-lemmas-all-100-cbow-ns.txt | 1282621 | 100 | 0,35 | 0,3624 | 0,4124 | 1,6016 |
|  nkjp+wiki-lemmas-restricted-300-cbow-hs.txt | 1407762 | 300 | 0,35 | 0,415 | 0,46 | 1,6016 |
|  nkjp+wiki-forms-restricted-100-cbow-ns.txt | 1982479 | 100 | 0,33 | 0,3106 | 0,3421 | 1,3013 |
|  wiki-lemmas-restricted-300-cbow-hs.txt | 446608 | 300 | 0,32 | 0,361 | 0,3986 | 2,1021 |
|  nkjp-lemmas-all-100-skipg-hs.txt | 1282621 | 100 | 0,32 | 0,3227 | 0,3716 | 1,6016 |
|  wiki-forms-restricted-300-skipg-ns.txt | 698304 | 300 | 0,32 | 0,3388 | 0,4053 | 5,2052 |
|  wiki-forms-all-300-skipg-ns.txt | 724756 | 300 | 0,31 | 0,3321 | 0,3884 | 5,5055 |
|  nkjp-forms-restricted-100-cbow-ns.txt | 1713738 | 100 | 0,31 | 0,311 | 0,3409 | 1,3013 |
|  nkjp+wiki-forms-restricted-100-skipg-hs.txt | 1982479 | 100 | 0,30 | 0,2989 | 0,351 | 1,3013 |
|  wiki-forms-all-100-skipg-ns-30-it100.txt | 226396 | 100 | 0,30 | 0,2748 | 0,3476 | 8,6086 |
|  nkjp-forms-restricted-100-skipg-hs.txt | 1713738 | 100 | 0,29 | 0,3057 | 0,3441 | 1,3013 |
|  nkjp+wiki-forms-all-100-skipg-hs.txt | 2123132 | 100 | 0,28 | 0,3035 | 0,3544 | 1,3013 |
|  wiki-forms-restricted-300-skipg-hs.txt | 698304 | 300 | 0,28 | 0,2656 | 0,3379 | 5,2052 |
|  nkjp-lemmas-restricted-300-cbow-hs.txt | 1162845 | 300 | 0,28 | 0,4121 | 0,4563 | 1,6016 |
|  nkjp+wiki-forms-all-100-cbow-ns.txt | 2123132 | 100 | 0,28 | 0,2975 | 0,3263 | 1,3013 |
|  wiki-forms-restricted-100-skipg-ns.txt | 698304 | 100 | 0,28 | 0,3016 | 0,3657 | 5,2052 |
|  wiki-forms-all-100-skipg-ns.txt | 724756 | 100 | 0,28 | 0,3028 | 0,3687 | 5,5055 |
|  nkjp+wiki-lemmas-all-300-cbow-hs.txt | 1549322 | 300 | 0,28 | 0,4071 | 0,4597 | 1,6016 |
|  wiki-forms-all-300-skipg-hs.txt | 724756 | 300 | 0,28 | 0,2767 | 0,343 | 5,5055 |
|  wiki-lemmas-all-300-cbow-hs.txt | 473000 | 300 | 0,27 | 0,362 | 0,4056 | 2,1021 |
|  wiki-forms-restricted-300-cbow-ns.txt | 698304 | 300 | 0,27 | 0,2795 | 0,315 | 5,2052 |
|  nkjp-forms-all-100-skipg-hs.txt | 1832700 | 100 | 0,26 | 0,3091 | 0,3436 | 1,3013 |
|  nkjp-forms-all-100-cbow-ns.txt | 1832700 | 100 | 0,26 | 0,3019 | 0,3305 | 1,3013 |
|  wiki-lemmas-restricted-100-cbow-hs.txt | 446608 | 100 | 0,26 | 0,3215 | 0,3575 | 2,1021 |
|  wiki-forms-all-300-cbow-ns-30.txt | 226396 | 300 | 0,26 | 0,2828 | 0,3201 | 8,6086 |
|  nkjp-lemmas-all-300-cbow-hs.txt | 1282621 | 300 | 0,24 | 0,4085 | 0,4582 | 1,6016 |
|  wiki-forms-all-300-cbow-ns.txt | 724756 | 300 | 0,24 | 0,2791 | 0,3138 | 5,5055 |
|  nkjp+wiki-forms-restricted-300-cbow-hs.txt | 1982479 | 300 | 0,23 | 0,2974 | 0,3147 | 1,3013 |
|  nkjp-forms-restricted-300-cbow-hs.txt | 1713738 | 300 | 0,23 | 0,3061 | 0,322 | 1,3013 |
|  kyubyong_word2vec.txt | 50035 | 300 | 0,23 | 0,2544 | 0,3087 | 41,4414 |
|  nkjp-lemmas-restricted-100-cbow-hs.txt | 1162845 | 100 | 0,22 | 0,3503 | 0,3967 | 1,6016 |
|  wiki-forms-restricted-100-skipg-hs.txt | 698304 | 100 | 0,22 | 0,2594 | 0,3215 | 5,2052 |
|  nkjp-forms-all-300-cbow-hs.txt | 1832700 | 300 | 0,22 | 0,2962 | 0,311 | 1,3013 |
|  wiki-forms-all-100-cbow-ns-30-it100.txt | 226396 | 100 | 0,21 | 0,2643 | 0,3052 | 8,6086 |
|  wiki-forms-restricted-100-cbow-ns.txt | 698304 | 100 | 0,21 | 0,259 | 0,2936 | 5,2052 |
|  nkjp+wiki-forms-all-300-cbow-hs.txt | 2123132 | 300 | 0,21 | 0,2924 | 0,3065 | 1,3013 |
|  wiki-forms-all-100-skipg-hs.txt | 724756 | 100 | 0,21 | 0,2675 | 0,3276 | 5,5055 |
|  nkjp+wiki-lemmas-all-100-cbow-hs.txt | 1549322 | 100 | 0,21 | 0,3471 | 0,3984 | 1,6016 |
|  nkjp+wiki-forms-all-300-cbow-hs-50.txt | 556932 | 300 | 0,20 | 0,2942 | 0,3104 | 1,3013 |
|  nkjp-lemmas-all-100-cbow-hs.txt | 1282621 | 100 | 0,19 | 0,3556 | 0,4072 | 1,6016 |
|  wiki-lemmas-all-100-cbow-hs.txt | 473000 | 100 | 0,19 | 0,3189 | 0,3634 | 2,1021 |
|  wiki-forms-all-100-cbow-ns.txt | 724756 | 100 | 0,19 | 0,255 | 0,2936 | 5,5055 |
|  nkjp+wiki-forms-restricted-100-cbow-hs.txt | 1982479 | 100 | 0,18 | 0,242 | 0,2639 | 1,3013 |
|  nkjp-forms-restricted-100-cbow-hs.txt | 1713738 | 100 | 0,18 | 0,2537 | 0,2748 | 1,3013 |
|  nkjp+wiki-forms-all-100-cbow-hs.txt | 2123132 | 100 | 0,15 | 0,2437 | 0,2688 | 1,3013 |
|  nkjp-forms-all-100-cbow-hs.txt | 1832700 | 100 | 0,15 | 0,2493 | 0,2733 | 1,3013 |
|  wiki-forms-restricted-300-cbow-hs.txt | 698304 | 300 | 0,13 | 0,2496 | 0,2816 | 5,2052 |
|  wiki-forms-all-300-cbow-hs-30.txt | 226396 | 300 | 0,13 | 0,2626 | 0,2916 | 8,6086 |
|  wiki-forms-all-300-cbow-hs.txt | 724756 | 300 | 0,13 | 0,2636 | 0,2925 | 5,5055 |
|  wiki-forms-restricted-100-cbow-hs.txt | 698304 | 100 | 0,09 | 0,2162 | 0,2427 | 5,2052 |
|  wiki-forms-all-100-cbow-hs.txt | 724756 | 100 | 0,08 | 0,2294 | 0,2611 | 5,5055 |
|sdadas_word2vec_100_3_polish.bin|1934030|100|0,33|0,3961|0,4616|1,1011|
|sdadas_word2vec_300_3_polish.bin|1934028|300|0,41|0,442 |0,5005|1,1011|
|sdadas_fasttext_100_3_polish.bin|2488306|100|0,23|0,3532|0,4092|1,1011|
|sdadas_glove_100_3_polish.txt   |1926320|100|0,54|0,3128|0,3705|1,1011|
|sdadas_glove_300_3_polish.txt   |1926319|300|0,62|0,351 |0,4027|1,1011|
|sdadas_glove_500_3_polish.txt   |1926319|500|0,61|0,3493|0,3987|1,1011|
|sdadas_glove_800_3_polish.txt   |1926319|800|0.57|0.3401|0.3911|1,1011|

## References
Polish Word Analogy: 

https://dl.fbaipublicfiles.com/fasttext/word-analogies/questions-words-pl.txt

MSimLex999 Polish:

http://zil.ipipan.waw.pl/CoDeS?action=AttachFile&do=view&target=MSimLex999_Polish.zip
