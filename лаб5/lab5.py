
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import sqlalchemy
import pytest
import yaml
from flask import Flask
import pyttsx3

def use_requests():
    try:
        resp = requests.get('https://httpbin.org/get')
        print("requests status:", resp.status_code)
    except Exception as e:
        print("requests error:", e)

def use_numpy():
    try:
        arr = np.array([1,2,3,4,5])
        print("numpy mean:", arr.mean())
    except Exception as e:
        print("numpy error:", e)

def use_pandas():
    try:
        df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
        print("pandas df:\n", df)
    except Exception as e:
        print("pandas error:", e)

def use_matplotlib():
    try:
        plt.plot([1,2,3],[4,5,6])
        plt.title("Simple plot")
        # plt.show()  # optional
        print("matplotlib plotted a simple graph")
    except Exception as e:
        print("matplotlib error:", e)

def use_beautifulsoup():
    try:
        html = '<html><body><h1>Hello World</h1></body></html>'
        soup = BeautifulSoup(html, 'html.parser')
        print("beautifulsoup found:", soup.h1.text)
    except Exception as e:
        print("beautifulsoup error:", e)

# Ви можете додати ще 5 бібліотек, але використовувати лише 5 у блоках try.
# Решта імпортів залишити для повноти бібліотек у requirements.

if __name__ == "__main__":
    use_requests()
    use_numpy()
    use_pandas()
    use_matplotlib()
    use_beautifulsoup()