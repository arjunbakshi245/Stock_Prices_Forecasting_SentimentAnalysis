# Stock_Prices_Forecasting_SentimentAnalysis
1. All plots     -  Graphical representation of results. Includes rpedictions as well as correlation matrixes
2. main          -  Contains final working code
3. Accuracy      -  Code for ccalculating accuracy, has all predicted datasets which are compared to the original.
4. Explainantion -  Contains presentations and other details.
5. Final Report  -  Full report with compiled results.


## Instruction for main file
1. Bert_9year_1-2week_weighted.csv is the final data set that we are using in the model.
2. bert_scores.csv is the dataset with bert scores column appened to it. The lag periods columns are added to this dataset through 
   created_lookbaks, creted_weighted_lookbacks.ipynb files

3. only_scores  -  dataset with bert_scores with unique dates(used to make the bert_scores.csv)

4. findscores.ipynb   =  uses BERT model fine tunes for financial text===> FinBERT(available on github)(https://github.com/ProsusAI/finBERT)
   Tooks 4hrs to run while predicting sentiment scores for each date.(CAUTION)

5. lstm_gru.ipynb  used for making predictions with varyin the lookbacak periods and changing the columns we use for training the model.
   results are doccumented in the Explainations folder along with all plots that are stored in the all plots folder.
   the GRU model is created by simply changeing 'LSTM' with 'GRU' in cell 21. line 2.

6. The Stockprices_prediction_without_truncating is same as lstm-gru. Here we dont check the result for error hence we predict prices that 
   we dont know the actual data of. Can be skiped. Not very Important.

7. Final-Report outside this folder also contains the literature Review of the reaseach along with the analysis of our results.

8. Remaining files are for the BERT model and fine tuning weights for FinBERT. Do not alter them

9. analyst_tone needs to be downloaded and added in this folder - drive link - https://drive.google.com/file/d/1ATcIeFeRlduXnYT6QX1xtS5R86bSEG3e/view?usp=sharing
