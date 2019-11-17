#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
#date: 2019/11/7

import pickle

f = open("game.pkl","rb")
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

