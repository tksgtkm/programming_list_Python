import shelve

db = shelve.open("class-shelve")

sue = db["sue"]
sue.giveRaise(0.25)
db["sue"] = sue

tom = db["tom"]
tom.giveRaise(0.20)
db["tom"] = tom
db.close()
