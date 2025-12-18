from textblob import TextBlob
import sys

def get_lines(path):
    with open(path, 'r') as f:
        headline = f.readlines()
        headline = [x.strip(".,;:!?").lower() for x in headline]
        return headline
    
def get_sentiment(text):
    count_negatives = 0
    count_neutrals = 0
    count_positives = 0
    for headline in text:
        blob = TextBlob(headline)
        sentiment = blob.sentiment
        if sentiment.polarity < 0:
            count_negatives += 1
        elif sentiment.polarity == 0:
            count_neutrals += 1
        else:
            count_positives += 1 
    return count_negatives, count_neutrals, count_positives

    
def main():
    headlines = get_lines(sys.argv[1])
    sentiment = get_sentiment(headlines)
    print(f"This is the number of negative, neutral and positive headlines respectively: {sentiment}")
main()
