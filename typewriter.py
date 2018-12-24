#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:21:09 2018

@author: kengo
"""

import sys, random, time

def print(message, end='\n'):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.randint(40, 100)/ 1000)
    sys.stdout.write(end)
