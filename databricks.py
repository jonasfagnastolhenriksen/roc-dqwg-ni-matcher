# Databricks notebook source
# databricks.py

dbutils.widgets.text("input_path", "")
dbutils.widgets.text("output_path", "")

input_path = dbutils.widgets.get("input_path")
output_path = dbutils.widgets.get("output_path")




# COMMAND ----------

# MAGIC %load_ext autoreload

# COMMAND ----------

# MAGIC %autoreload 2

# COMMAND ----------

# Kjør scriptet (forutsetter at filen er i samme repo eller lastet opp)
# print pythonpath
import sys, os

if "matcher" in sys.modules:
    del sys.modules["matcher"]

#import matcher 
#import importlib
#importlib.reload(matcher)
import matcher 

print(sys.path)

sys.path.append(os.getcwd())
print(sys.path)

matchobj = matcher.Matcher()
matchobj.run_matcher()

# common.test_function(input_var="hei")



# COMMAND ----------


