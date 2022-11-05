#!/usr/bin/env python3

"""
Assignment 3 Task 1
Team-ID : BD1_616_659_661_667

Dataset Observations
- Contains NaN values
- Duplicate Rows


Query: (For original dataset)

df_view - generated after removing nan/duplicate rows

SELECT DISTINCT d1.`Ticket number` FROM df_view d1
WHERE `Fine amount` >
(SELECT AVG(d2.`Fine amount`) FROM df_view d2 WHERE d1.`RP State Plate`=d2.`RP State Plate`)
AND
d1.Color="WH"
ORDER BY d1.`Ticket number`;
"""

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import DoubleType

INPUT_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]

s_context = SparkSession.builder.config("spark.master", "local").appName("a3t1").getOrCreate()
s_context.sparkContext.setLogLevel("OFF")

df = s_context.read.options(header="true").csv(INPUT_PATH)

# Drop NaN values
df = df.na.drop()

# Drop Duplicates
df = df.distinct()

df = df.withColumn("Fine amount", col("Fine amount").cast(DoubleType()))
df = (
    df.withColumnRenamed("RP State Plate", "RP_State_Plate")
    .withColumnRenamed("Fine amount", "fine_amount")
    .withColumnRenamed("Ticket number", "ticket_number")
)

df.createOrReplaceTempView("df_table")
avg_table = s_context.sql(
    "SELECT AVG(fine_amount) AS fine_amount,RP_State_Plate FROM df_table GROUP BY RP_State_Plate"
)
avg_table.createOrReplaceTempView("avg_table")
avg_table = s_context.sql(
    "SELECT round(fine_amount,2) AS fine_amount,RP_State_Plate FROM avg_table"
)
avg_table.createOrReplaceTempView("avg_table")
tkt_color = s_context.sql(
    """SELECT df_table.ticket_number,df_table.color FROM df_table,avg_table
    WHERE df_table.RP_State_Plate=avg_table.RP_State_Plate
    AND
    df_table.fine_amount >= avg_table.fine_amount"""
)

tkt_color.createOrReplaceTempView("tkt_color_table")
output_df = s_context.sql(
    """SELECT DISTINCT ticket_number FROM tkt_color_table

    WHERE tkt_color_table.color='WH' ORDER BY ticket_number"""
)
output_df.write.option("header", False).csv(OUTPUT_PATH)
