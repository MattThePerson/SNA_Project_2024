

def track_progress(total, progress, text='progress:', inc=1):
    a, b = progress, total
    perc = ((a+1) / b * 100)
    if a%inc == 0 or progress == total-1:
        print("\r {} {:_}/{:_} ({:.5f}%)".format( text, (a+1), b, perc ), end='')
    a += 1
    return a, perc



def get_filtered_tweets_dataframe(dataset_fn):
    import time
    import pandas as pd
    
    # Import dataset from tsv file
    #dataset_fn = "../dataset/TweetsCOV19.tsv"
    header = ["Tweet Id", "Username", "Timestamp", "Followers", "Friends", "Retweets", "Favorites", "Entities", "Sentiment", "Mentions", "Hashtags", "URLs", "EXTRA"]
    dtype = {"Tweet Id":"string", "Username":"string", "Timestamp":"string", "Followers":int, "Friends":int, "Retweets":int, "Favorites":int, "Entities":"string", "Sentiment":"string", "Mentions":"string", "Hashtags":"string", "URLs":"string", "EXTRA":"string"}
    print("Importing dataset from tsv file ...", end='')
    start = time.time()
    df = pd.read_csv(dataset_fn, sep='\t', names=header, on_bad_lines='warn', dtype=dtype)
    end = time.time()
    print("read {:_} lines (took {:.1f}s)".format(len(df), end-start))
    df.set_index('Tweet Id', inplace=True)

    # Convert timestamp column to Timestamp object
    print("Converting timestamp column")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%a %b %d %H:%M:%S %z %Y')

    # Filter columns and timestamp
    print("Filtering desired columns and between desired dates ... ", end='')
    dff = df[["Username", "Timestamp", "Sentiment", "Hashtags"]]
    start_date =    pd.to_datetime('2019-12-01 00:00:00 +0000')
    end_date =      pd.to_datetime('2020-03-01 00:00:00 +0000')
    dff = dff[(dff['Timestamp'] >= start_date) & (dff['Timestamp'] < end_date)]
    print("{:_} rows in dataframe".format(len(df)))

    # Parse hashtags tab into array
    print("Parsing hashtags and positive/negative sentiments")
    dff['Hashtags'] = dff['Hashtags'].str.split().apply(lambda x: [name for name in x if name != "null;"] if isinstance(x, list) else [])

    # Split positive and negative sentiments into own columns (and convert to int type)
    dff[['Sentiment_pos', 'Sentiment_neg']] = dff['Sentiment'].str.split(" ", expand=True)
    dff['Sentiment_pos'], dff['Sentiment_neg'] = dff['Sentiment_pos'].astype(int), dff['Sentiment_neg'].astype(int)
    dff.drop("Sentiment", axis=1, inplace=True)

    # Filter rows with mentions (and less that outlier mentions)
    print("filtering for tweets that contain hashtags ... ", end='')
    ht = dff[dff['Hashtags'].apply(lambda x: len(x) > 0 and len(x) < 60)]
    print("{:_} rows in dataframe".format(len(df)))

    return ht