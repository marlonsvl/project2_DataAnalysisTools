# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:08:05 2015

@author: marlon
"""

import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv('/Users/utpl/Documents/DataAnalysisTools/nesarc_pds.csv', low_memory=False)


#setting variables you will be working with to numeric

#HOW OFTEN USED SEDATIVES IN THE LAST 12 MONTHS
data['S3BD1Q2C'] = data['S3BD1Q2C'].replace('BL', numpy.nan)
data['S3BD1Q2C'] = data['S3BD1Q2C'].replace(' ', numpy.nan)
data['S3BD1Q2C'] = pandas.to_numeric(data['S3BD1Q2C']);
data['CHECK321'] = data['CHECK321'].replace('BL', numpy.nan)
data['CHECK321'] = data['CHECK321'].replace(' ', numpy.nan)
data['CHECK321'] = pandas.to_numeric(data['CHECK321']);
data['AGE'] = pandas.to_numeric(data['AGE']);

#DRUG ABUSE/DEPENDENCE (MEDICINE EXPERIENCES) HAPPEN IN THE LAST 12 MONTHS
data['S3CQ12B1'] = data['S3CQ12B1'].replace(9, numpy.nan)
data['S3CQ12B1'] = data['S3CQ12B1'].replace(' ', numpy.nan)
data['S3CQ12B1'] = pandas.to_numeric(data['S3CQ12B1']);


#subset data to young adults age 18 to 25 who have smoked in the past 12 months
sub1=data[(data['AGE']>=18) & (data['AGE']<=25) & (data['CHECK321']==1)]

#make a copy of my new subsetted data
sub2 = sub1.copy()


# recode missing values to python missing (NaN)
#sub2['S3BD1Q2C']=sub2['S3BD1Q2C'].replace(9, numpy.nan)

#recoding values for S3BD1Q2C into a new variable, USFREQMO
recode1 = {1: 365, 2: 264, 3: 168, 4: 72, 5: 30, 6: 12, 7:9, 8:4.5, 9:1}

sub2['USFREQMO']= sub2['S3BD1Q2C'].map(recode1)


# contingency table of observed counts
ct1=pandas.crosstab(sub2['S3CQ12B1'], sub2['USFREQMO'])
print (ct1)


# column percentages
colsum=ct1.sum(axis=0)
colpct=ct1/colsum
print(colpct)

# chi-square
print ('chi-square value, p value, expected counts')
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)


# set variable types 
sub2["USFREQMO"] = sub2["USFREQMO"].astype('category')

###############################################################

recode2 = {1: 365, 168:168}
sub2['COMP1v2']= sub2['USFREQMO'].map(recode2)

# contingency table of observed counts
ct2=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v2'])
print (ct2)

# column percentages
colsum=ct2.sum(axis=0)
colpct=ct2/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs2= scipy.stats.chi2_contingency(ct2)
print (cs2)


###############################################################
recode3 = {1: 365, 72:72}
sub2['COMP1v4']= sub2['USFREQMO'].map(recode3)

# contingency table of observed counts
ct3=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v4'])
print (ct3)

# column percentages
colsum=ct3.sum(axis=0)
colpct=ct3/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs3= scipy.stats.chi2_contingency(ct2)
print (cs3)


###############################################################
recode5 = {1: 365, 30:30}
sub2['COMP1v5']= sub2['USFREQMO'].map(recode5)

# contingency table of observed counts
ct5=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v5'])
print (ct5)

# column percentages
colsum=ct5.sum(axis=0)
colpct=ct5/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs5= scipy.stats.chi2_contingency(ct5)
print (cs5)

###############################################################

recode6 = {1: 365, 12:12}
sub2['COMP1v6']= sub2['USFREQMO'].map(recode5)

# contingency table of observed counts
ct6=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v6'])
print (ct6)

# column percentages
colsum=ct6.sum(axis=0)
colpct=ct6/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs6= scipy.stats.chi2_contingency(ct6)
print (cs6)


###############################################################

recode7 = {1: 365, 9:9}
sub2['COMP1v7']= sub2['USFREQMO'].map(recode7)

# contingency table of observed counts
ct7=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v7'])
print (ct7)

# column percentages
colsum=ct7.sum(axis=0)
colpct=ct7/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs7= scipy.stats.chi2_contingency(ct7)
print (cs7)


###############################################################

recode8 = {1: 365, 4.5:4.5}
sub2['COMP1v8']= sub2['USFREQMO'].map(recode8)

# contingency table of observed counts
ct8=pandas.crosstab(sub2['TAB12MDX'], sub2['COMP1v8'])
print (ct8)

# column percentages
colsum=ct8.sum(axis=0)
colpct=ct8/colsum
print(colpct)

print ('chi-square value, p value, expected counts')
cs8= scipy.stats.chi2_contingency(ct8)
print (cs8)



