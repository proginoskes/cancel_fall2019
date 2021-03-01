import twint

c = twint.Config()
c.Search = "cancel culture"
c.Year = 2020
c.Verified = True
c.Store_json=True
c.Custom["tweet"] = ["id", "username", "tweet","date"]
c.Output="cancel_v_all.json"

# Run
twint.run.Search(c)
