import json, sys, struct, codecs, twint

c = twint.Config()
c.Search = "cancel culture"
c.Limit = 10
c.Store_csv=True
c.Output="cancel_att.csv"

# Run
twint.run.Search(c)
tlist = c.search_tweet_list
