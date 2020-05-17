import twint

# This function gets the list of people the user was following
def get_following(username):
    c = twint.Config()
    c.Username = username
    c.Pandas = True
    twint.run.Following(c)
    Following_df = twint.storage.panda.Follow_df
    list_of_following = Following_df['following'][username]
    return list_of_following

# This function gets a list of tweets made by people the user follows over the past week
def following_tweets(list_of_following):
    for i in range(len(list_of_following)):
        c = twint.Config()
        c.Username = list_of_following[i]
        c.Since =  "2020-05-05 00:00:01" # need to make this dynamic
        c.Custom["tweet"] = ["date","id", "username","tweet"]
        c.Output = "tweets.csv"
        c.Store_csv = True
        followingtweets = twint.run.Search(c)
    return followingtweets
    
# This function gets the tweets the user retweeted over the past week
def get_retweets(username):
    c = twint.Config()
    c.Username = 'elonmusk'
    c.Since =  "2020-05-05 00:00:01" # need to make this dynamic
    c.Custom["tweet"] = ["date","id", "username","tweet"]
    c.Output = "rt.csv"
    c.Store_csv = True
    c.Native_retweets = True
    retweets = twint.run.Search(c)
    return retweets
    
# This function gets the tweets the user liked over the past week
def get_likes(username):
    c = twint.Config()
    c.Username = 'elonmusk'
    c.Since =  "2020-05-05 00:00:01"
    c.Custom["tweet"] = ["date","id", "username","tweet"]
    c.Store_csv = True
    c.Output = "fav.csv"
    likes = twint.run.Favorites(c)
    return likes

# Testing
if __name__ == '__main__':
   username = 'elonmusk'
   list_of_following = get_following(username)
   followingtweets = following_tweets(list_of_following)
   retweets = get_retweets(username)
   likes = get_likes(username)
