from __future__ import division
from string import punctuation
import math
from collections import Counter
import math

SYMBOLS = '{}()[],:;+*|<>~$@$%^`%!'
# SYMBOLS = set(punctuation)
DIGITS = '1234567890'

def conseq_digits(token):
  max_occ = [0]
  curr = 0
  for ch in token:
    if ch in DIGITS:
      curr+=1
    else:
      max_occ.append(curr)
      curr = 0
  return max(max_occ)

def conseq_chars(token):
  max_occ = [0]
  curr = 0
  for ch in token:
    if ch not in DIGITS and ch not in SYMBOLS:
      curr+=1
    else:
      max_occ.append(curr)
      curr = 0
  return max(max_occ)

def conseq_symbols(token):
  max_occ = [0]
  curr = 0
  for ch in token:
    if ch in SYMBOLS:
      curr+=1
    else:
      max_occ.append(curr)
      curr = 0
  return max(max_occ)

def char_continuity_rate(url, len):
  return ((conseq_digits(url) + conseq_symbols(url) + conseq_chars(url)) / len)

def count_symbols(token):
  if len(token) == 0:
    return -1

  s = 0
  for ch in token:
    if ch in SYMBOLS:
      s+=1
  return s

def count_digits(token):
  s = 0
  for ch in token:
    if ch in DIGITS:
      s+=1
  return s

def get_params_len(query):
  len_ = 0
  # query_string = urlparse.urlparse(url) 
  for param in query:  
    len_ += len(param)
  return len_

def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'

# entropy calculation of a string
def shannon(string):
  "Calculates the Shannon entropy of a string"
  if len(string) == 0:
    return -1
  # get probability of chars in string
  prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

  # calculate the entropy
  entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

  return entropy