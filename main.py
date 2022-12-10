import json
import pandas as pd
from tqdm import tqdm
from timestamp.scripts.TimestampEstimator import find_tweet_timestamp
from datetime import datetime

def read_data():
    with open('data/likes.json', 'r') as f:
        tweets = json.load(f)

    tweet_texts = []
    tweet_urls = []
    tweet_times = []
    for tweet in tqdm(tweets):
        if 'fullText' not in tweet['like']:
            continue
        if 'You’re unable to view this Tweet' in tweet['like']['fullText']:
            continue
        if 'Tweet is from a suspended account' in tweet['like']['fullText']:
            continue

        tstamp = find_tweet_timestamp(int(tweet['like']['tweetId']))
        utcdttime = datetime.utcfromtimestamp(tstamp / 1000)
            
        tweet_texts.append(tweet['like']['fullText'])
        tweet_urls.append(tweet['like']['expandedUrl'])
        tweet_times.append(utcdttime)

    df = pd.DataFrame({'text': tweet_texts, 'url': tweet_urls, 'time': tweet_times})
    df = df.sort_values(by='time', ascending=False)
    return df

def filter_by_date(df, start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print('Invalid date format. Please use YYYY-MM-DD.')
        return None

    print(start_date, end_date)
    return df[(df['time'] >= start_date) & (df['time'] <= end_date)]

def main():
    df = read_data()
    df = filter_by_date(df, '2021-06-01', datetime.today().strftime('%Y-%m-%d'))
    print(df.head())

if __name__ == '__main__':
    main()