import twint

c = twint.Config()
c.Search = "cancel culture"
c.Year = 2020
c.Store_json=True
c.Custom["tweet"] = ["id", "username", "tweet","date"]
c.Output="cancel_all.json"

# Run
twint.run.Search(c)
