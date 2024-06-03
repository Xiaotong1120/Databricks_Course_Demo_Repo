# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World!"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title1
# MAGIC ## Title2
# MAGIC ### Title3

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

file = dbutils.fs.ls('/databricks-datasets')
print(file)

# COMMAND ----------

display(file)

# COMMAND ----------


