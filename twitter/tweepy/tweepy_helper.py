import pandas as pd

def tweets_to_df(tweets):
    """Converteer tweets object van Tweepy (Response) naar Pandas DataFrame.

    Parameters
    ----------
    tweets : tweepy.client.Response
        Response van Twitter API.

    Returns
    -------
    pandas.DataFrame
        Tweets in Pandas Dataframe. Let op, kan dubbele tweets bevatten
        als er meerdere context annotations zijn.
    """
    df = pd.DataFrame(
        tweets.data[0].data,
        index = [i for i in range(len(tweets.data[0].data['context_annotations']))])
    j = 1
    for i in range(1, len(tweets.data)):
        data = tweets.data[i].data
        data['text'] = data['text'].replace("\n"," ")
        index = [j]
        
        if "context_annotations" in data:
            index = range(j, j+len(data['context_annotations']))
            j+=len(data['context_annotations'])
        else:
            j+=1
        df = pd.concat([df, pd.DataFrame(data, index=index)])# vervangen voor concat want deprecated
    print("Let op: kan dubbele tweets bevatten door context annotations")
    return df