#!/usr/bin/env python

#day 2 homework

#1. Make boxplot of top/middle/bottom 1/3rd FPKMs -- for SRR072893, SRR072915
#summary: sorting by percent of the total range isn't really useful as almost all of the data for both sets is in the bottom 1/3. Nevertheless this code works for the bottom and top thirds (not for the middle) of both data sets.

import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
df = pd.read_table(cufflinks_output)
cufflinks_output_2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df2 = pd.read_table(cufflinks_output_2)

df_sorted = df.sort(["FPKM"])
df_sorted_bottom = df_sorted[df_sorted["FPKM"]<(14405.2/3)]
#print df_sorted_bottom
df_sorted_top    = df_sorted[df_sorted["FPKM"]>(28810.4/3)]
#print df_sorted_top
#df_sorted_middle = df_sorted[ df_sorted["FPKM"] < (28810.4/3) and > (14405.2/3)]  - didn't work, incorrect syntax
#df_sorted_middle = df_sorted[ df_sorted["FPKM"] < (28810.4/3) and ["FPKM"] > (14405.2/3)] - didn't work, valueerror
#df_sorted_middle = df_sorted[ df_sorted["FPKM"] < (28810.4/3) and df_sorted["FPKM"] > (14405.2/3)] - didn't work valueerror

data = [df_sorted_bottom["FPKM"], df_sorted_top["FPKM"]]
#print data

plt.figure()
plt.boxplot(data)
plt.savefig("boxplot_male.png")

df2_sorted = df2.sort(["FPKM"])
#print df2_sorted
df2_sorted_bottom = df2_sorted[ df2_sorted["FPKM"]<(24267.2/3) ]
df2_sorted_top    = df2_sorted[ df2_sorted["FPKM"]>(48534.4/3) ]
#df_sorted_middle = df_sorted[ df_sorted["FPKM"] < (24267.2/3) and df_sorted["FPKM"] > (48534.4/3)] - didn't work

data2 = [df2_sorted_bottom["FPKM"], df2_sorted_top["FPKM"]]
#print data2

plt.figure()
plt.boxplot(data2)
plt.savefig("boxplot_female.png")