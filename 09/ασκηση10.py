#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

N = 194749497518847283
if N > 1:
   # check for factors
  if N > 1:
   # check for factors
   for i in range(2,N):
       if (N % i) == 0:
           print(i,"is p",N//i,"is q")
           break
   else:
       print(N,"is a prime number")
       