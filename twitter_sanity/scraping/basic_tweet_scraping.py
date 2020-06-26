import pandas as pd
import twint 
import csv

class Tweet:
  def __init__(self,username,start_date,end_date):
    self.username= username
    self.start_date= start_date
    self.end_date= end_date

#To get followings of the user
  def get_followings(self):   
    c= twint.Config()
    c.Username= self.username
    c.Store_csv= True
    c.Output= self.username + '_Followings.csv'
    followings_list= twint.run.Following(c)
    return followings_list  


#To get tweets of user's followings for the mentioned dates.
  def following_tweets(self): 
    self.get_followings()
    
    c1= twint.Config()
    
    with open(self.username + '_Followings.csv') as csv1:
      followings = list(csv1)
    
    for name in followings:
      name.strip()
      c1.Username= name
      c1.Since = self.start_date
      c1.Until = self.end_date
      c1.Custom['tweet'] = ['date','time','username','name','tweet','retweets_count','likes_count']
      c1.Store_csv = True
      c1.Output = self.username + '_tweetData.csv'
      twint.run.Search(c1) 

#To get the tweets user retweeted between the mentioned dates
  def get_retweets(self):
    c = twint.Config()
    c.Username = self.username
    c.Since =  self.start_date
    c.Until = self.end_date
    c.Custom['tweet']=['date','time','username','name','tweet']
    c.Store_csv = True
    c.Native_retweets = True
    c.Output = self.username + "_retweets.csv"
    retweets = twint.run.Search(c)     

#To get the tweets liked by the user between the mentioned dates
  def get_likes(self):
    c= twint.Config()
    c.Username = self.username
    c.Since = self.start_date
    c.Until = self.end_date
    c.Store_csv = True
    c.Output = self.username + "_liked_data.csv"
    likes = twint.run.Favorites(c)

#To scrape all the data and store in csv files
  def scrape(self):
    self.following_tweets()
    self.get_retweets()
    

#Testing
d= Tweet('realDonaldTrump','2020-06-14 00:00:01', '2020-06-24 00:00:01')
d.scrape()

