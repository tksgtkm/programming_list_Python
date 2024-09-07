caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
cap2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]


def pleaseConformOpt(caps):
    start = 0
    forward = 0
    backward = 0
    intervals = []

    caps = caps + ["END"]
