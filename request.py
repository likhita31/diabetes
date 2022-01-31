# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 23:26:20 2020

@author: user
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'pregnancies':1, 'glucose':85, 'bpressure':66, 'skinfold':29, 'insulin':0, 'bmi':26.6, 'pedigree':0.351, 'age':31})

print(r.json())