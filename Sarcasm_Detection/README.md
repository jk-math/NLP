# Sarcasm Detection in News articles

Kaggle dataset: https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection/home

Use urls provided in Kaggle dataset to pull headline and paragraphs contents from news articles

Some of the urls failed to open, but many of them were legitimate web addresses that had the HuffPost web address appended to the front. The Recover failed links notebook strips the HuffPost address from the front and attempts to access the websites. This recovered many of the failed urls

Train a simple LSTM model to detect sarcasm using the first 200 words of the article (headline plus some text from the beginning of the article).

Once the model is trained, a function at the end of the notebook allows one to provide a url and the model will return a prediction of whether or not the article is sarcastic
