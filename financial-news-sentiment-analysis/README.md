# Financial news sentiment analysis

## Description

This projects implements a simple sentiment analysis tool for financial news headlines.
Given a file containing financial headlines, the program loops over each headlines and classifies it as negative, neutral or positive based on sentiment polarity.
The dataset consists of a small collection of financial news headlines collected from publicly available Reuters finance articles. 
Only the headline text is used. The dataset is intended for demonstration and learning purposes. 

## Getting Started

### Dependencies

* Libraries used: sys, TextBlob

### Executing program

* Headlines are read from a text file
* Basic text preprocessing is applied:
  * lowercasing
  * removal of punctuation
* Each headline is analyzed using TextBlob
* Sentiment polarity scores are used to categorize headlines into:
  * Negative (polarity < 0)
  * Neutral (polarity = 0)
  * Positive (polarity > 0)
* The final output shows the total number of negative, neutral and positive headlines
* To run the code in the command line:
```
python sentiment_analysis.py headlines.csv
```
* Example output:
```
This is the number of negative, neutral and positive headlines respectively: (1, 12, 8)
```
