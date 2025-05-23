#!/usr/bin/env python
# coding: utf-8
# @author: Alejandro Morales Fernández. Banco de España.


## Merge both GLEIF and National datasets and creates the report in Excel.
## Example of use for Spain and three identifiers: python National Identfier matcher.py ES 3


__author__ = "Alejandro Morales Fernández"
__version__ = "2.0"

import matcher
import os

match = matcher.Matcher(
    input_dir = os.getcwd(), output_dir = os.getcwd()
)

match.run_matcher()
