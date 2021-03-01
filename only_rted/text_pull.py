import twint

c = twint.Config()
c.Search = "cancel culture"
c.Year = 2020
c.Min_retweets = 1
c.Store_json=True
c.Custom["tweet"] = ["id", "username", "tweet","date","retweet"]
c.Output="cancel_r1_all.json"

# Run
twint.run.Search(c)
