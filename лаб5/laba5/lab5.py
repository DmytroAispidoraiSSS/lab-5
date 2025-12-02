import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random2
import pyfiglet
from colorama import Fore, Style
from faker import Faker
import pytz
from dateutil import parser

# 1. requests
try:
    r = requests.get("https://api.github.com")
    print("Requests OK:", r.status_code)
except Exception as e:
    print("Requests error:", e)

# 2. numpy
try:
    arr = np.array([1, 2, 3])
    print("Numpy sum =", np.sum(arr))
except Exception as e:
    print("Numpy error:", e)

# 3. pandas
try:
    df = pd.DataFrame({"a": [1, 2, 3]})
    print("Pandas head:\n", df.head())
except Exception as e:
    print("Pandas error:", e)

# 4. pyfiglet
try:
    ascii_art = pyfiglet.figlet_format("Lab 5")
    print(ascii_art)
except Exception as e:
    print("Pyfiglet error:", e)

# 5. colorama + faker
try:
    fake = Faker()
    print(Fore.GREEN + "Fake name:", fake.name())
    print(Style.RESET_ALL)
except Exception as e:
    print("Faker/colorama error:", e)
