import itertools
import time
from multiprocessing import Pool

import requests

s = "adihgrtnsnd"
combinations = list(map(''.join, itertools.product(*zip(s.upper(), s.lower()))))

def process_youtube_ids(id):
    request = requests.get(f"http://noembed.com/embed?url=http%3A//www.youtube.com/watch%3Fv%3D{id}")
    with open("youtube_urls.txt", "a") as f:
        if "Bad Request" in request.content.decode("utf-8"):
            f.write(f"{id} Bad Request \n")
            print(f"Bad Request: {id} {request.content}")
        else:
            f.write(f"{id} {request.content} \n")
            print(f"Good Request: {id} {request.content}")

with Pool(5) as p:
    print(p.map(process_youtube_ids, combinations))