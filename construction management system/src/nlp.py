import  requests

from src.dbconnection import iud


def sent(k):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(k)
    print("outttt",ss)

    emo="Neutral"
    rating = 2.5
    if (ss['neu'] > ss['pos'] and ss['neu'] > ss['neg']):
        pass
    elif (ss['neg'] > ss['pos']):
        emo="Negative"
    else:
        emo="Positive"
    return emo
