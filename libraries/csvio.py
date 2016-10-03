# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:22:17 2016

@author: efron
"""
from typing import Tuple
from csv import reader
def read_csv_into_memory(filename: str) -> Tuple[str]:
    # reads the entire contents of a CSV into memory
    with open(filename) as file:
        asCSV = reader(file)
        contents = (item for line in asCSV for item in line)
        return tuple(contents)
