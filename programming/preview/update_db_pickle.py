import pickle

dbfile = open("people-pickle", "rb")
db = pickle.load(dbfile)
dbfile.close()

db["sue"]["pay"] *= 1.10
db["tom"]["name"] = "Jerry"

dbfile = open("people-pickle", "wb")
pickle.dump(db, dbfile)
dbfile.close()
