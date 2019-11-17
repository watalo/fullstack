#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/7

import json

# d = {
#     "name":"watalo",
#     "role":"police",
#     "blood":76,
#     "weapon":"AK47"
# }
#
# alive_players = ["watalo","alex","rain"]
#
# print(json.dumps(d))
#
# f = open("game.json","w")
# json.dump(d,f)
# json.dump(alive_players,f)

f = open("game.json","r")
print(json.load(f))

