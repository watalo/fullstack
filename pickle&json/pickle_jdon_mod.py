#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/7

import pickle
d = {
    "name":"watalo",
    "role":"police",
    "blood":76,
    "weapon":"AK47"
}

alive_players = ["watalo","alex","rain"]

# f = open("game.txt","w")
# f.write(d)

d_dump = pickle.dumps(d)   #序列化
print(pickle.loads(d_dump))#反序列化

f = open("game.pkl","wb")
# f.write(d_dump) 可以用，但是pickle 有命令可用

pickle.dump(d,f)   #First in First out FIFO
pickle.dump(alive_players,f)
