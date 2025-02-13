#!/home/codespace/.python/current/bin/python3

import os

FAV_SPORTS = input('What is your favorite sports team?')
FAV_PLACE = input('Where is your favorite place to visit?')
FAV_SHOW = input('What is your favorite show?')

os.environ["FAV_SPORTS"] = "Baltimore Ravens"
os.environ["FAV_PLACE"] = "New York City"
os.environ["FAV_SHOW"] = "Criminal Minds"

FAV_SPORTS_ENV = os.getenv("FAV_SPORTS")
FAV_PLACE_ENV = os.getenv("FAV_PLACE")
FAV_SHOW_ENV = os.getenv("FAV_SHOW")

print(FAV_SPORTS_ENV)
print(FAV_PLACE_ENV)
print(FAV_SHOW_ENV)