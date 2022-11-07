#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:00:19 2020

@author: almaaune
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# import data
df = pd.read_csv('aritzia-conversions - visits.csv')


# convert to date
#df['date'] = pd.to_datetime(df['date'], format = %m/%d/%Y)
print(df.info())
print(df['date'].head())


# what is the weekly conversion rate?
transactions = df['transactions'].sum()
print('conversions: ', transactions/len(df))
# 9.33%

# how many unique visitors?
print('unique visitors:')
print(df['visitorid'].nunique())


# total conversions per day
#conversions = df.groupby('date')['transactions'].sum()
conversions = df.groupby('date').sum()
conversions = conversions.reset_index()
conversions = conversions.drop(['visitorid', 'visitid'], axis = 1)
conversions['rate'] = (conversions['transactions'] / conversions['visits']).round(4)
print(conversions)

# average daily conversion: 
print('average daily conversion: ', conversions['rate'].mean())
# 8.43% , note that average daily conversion rate is different than weekly conversion calculations


plt.figure(figsize = (11,6))
plt.subplot(1,2,1)
sns.barplot(x='date', y='transactions', data=conversions)
plt.xticks(rotation=45)
plt.title('Total Conversions by Date')

plt.subplot(1,2,2)
sns.barplot(x='date', y = 'rate', data=conversions)
plt.xticks(rotation = 45)
plt.title('Conversion Rate by Date')

# split data into US and CA for further segmenting
ca = df[df['country'] == 'canada']
us = df[df['country'] == 'usa']

# daily conversion rate for each country
ca_conv = ca.groupby('date').sum()
ca_conv = ca_conv.reset_index()
ca_conv = ca_conv.drop(['visitorid', 'visitid'], axis =1)
ca_conv['rate'] = (ca_conv['transactions'] / ca_conv['visits']).round(4)

us_conv = us.groupby('date').sum()
us_conv = us_conv.reset_index()
us_conv = us_conv.drop(['visitorid', 'visitid'], axis =1)
us_conv['rate'] = (us_conv['transactions'] / us_conv['visits']).round(4)

ca_trans = ca['transactions'].sum()
us_trans = us['transactions'].sum()

print('ca weekly conversion rate: ', ca_trans / len(ca) )
print('us weekly conversion rate: ', us_trans / len(us))


plt.figure(figsize = (11,6))
plt.subplot(1,2,1)
sns.barplot(x='date', y='rate', data =ca_conv )
plt.xticks(rotation=45)
plt.title('Conversion Rate by Date (CA)')

plt.subplot(1,2,2)
sns.barplot(x='date', y='rate', data =us_conv )
plt.xticks(rotation=45)
plt.title('Conversion Rate by Date (US)')

# country
country = df.groupby('country').sum()
country = country.reset_index()
country = country.drop(['visitorid','visitid'], axis=1)
country['rate'] = country['transactions'] / country['visits']
print(country)


# traffic source
print('trafficSource')

ca_traffic_source = ca.groupby('trafficSource').sum()
ca_traffic_source = ca_traffic_source.reset_index()
ca_traffic_source = ca_traffic_source.drop(['visitorid','visitid'], axis=1)
ca_traffic_source['rate'] = ca_traffic_source['transactions'] / ca_traffic_source['visits']
print(ca_traffic_source)

us_traffic_source = us.groupby('trafficSource').sum()
us_traffic_source = us_traffic_source.reset_index()
us_traffic_source = us_traffic_source.drop(['visitorid','visitid'], axis=1)
us_traffic_source['rate'] = us_traffic_source['transactions'] / us_traffic_source['visits']
print(us_traffic_source)

plt.figure(figsize = (11,6))
plt.subplot(1,2,1)
sns.barplot(x='trafficSource', y = 'rate', data=ca_traffic_source)
plt.xticks(rotation = 45)
plt.title('Conversion Rate by Traffic Source (CA)')

plt.subplot(1,2,2)
sns.barplot(x='trafficSource', y = 'rate', data = us_traffic_source)
plt.xticks(rotation=45)
plt.title('Conversion rate by Traffic Source (US)')

# deviceCategory
print('deviceCategory:')
ca_device = ca.groupby('deviceCategory').sum()
ca_device = ca_device.reset_index()
ca_device = ca_device.drop(['visitorid','visitid'], axis=1)
ca_device['rate'] = ca_device['transactions'] / ca_device['visits']
print(ca_device)

us_device = us.groupby('deviceCategory').sum()
us_device = us_device.reset_index()
us_device = us_device.drop(['visitorid','visitid'], axis=1)
us_device['rate'] = us_device['transactions'] / us_device['visits']
print(us_device)


plt.figure(figsize = (11,6))
plt.subplot(1,2,1)
sns.barplot(x='deviceCategory', y = 'rate', data=ca_device)
plt.xticks(rotation = 45)
plt.title('Conversion rate by Device (CA)')

plt.subplot(1,2,2)
sns.barplot(x='deviceCategory', y = 'rate', data = us_device)
plt.xticks(rotation=45)
plt.title('Conversion rate by Device (US)')



# region
print('region')
ca_map = {'british columbia': 'R1',
          'alberta': 'R2',
          'saskatchewan': 'R2',
          'ontario':'R3',
          'manitoba' : 'R3',
          'quebec' : 'R4'}

ca['new_region'] = ca['region'].map(ca_map)
ca_region = ca.groupby('new_region').sum()
ca_region = ca_region.reset_index()
ca_region = ca_region.drop(['visitorid', 'visitid'], axis=1)
ca_region['rate'] = ca_region['transactions'] / ca_region['visits']
print(ca_region)

us_map = {'california': 'west',
          'colorado': 'central' ,
          'connecticut' : 'east',
          'illinois' : 'central',
          'new york' : 'east',
          'oregon' : 'west',
          'pennsylvania' :'east' ,
          'texas' : 'south',
          'washington' : 'west'}

us['new_region']= us['region'].map(us_map)
us_region = us.groupby('new_region').sum()
us_region = us_region.reset_index()
us_region = us_region.drop(['visitorid', 'visitid'], axis=1)
us_region['rate'] = us_region['transactions'] / us_region['visits']
print(us_region)


plt.figure(figsize = (11,6))
plt.subplot(1,2,1)
sns.barplot(x='new_region', y = 'rate', data=ca_region)
plt.xticks(rotation = 45)
plt.title('Conversion Rate by Region (CA)')


plt.subplot(1,2,2)
sns.barplot(x='new_region', y = 'rate', data = us_region)
plt.xticks(rotation=45)
plt.title('Conversion Rate by Region (US)')


# further segmenting - by device and by traffic source

ca_d = ca[ca['deviceCategory'] == 'desktop']
ca_m = ca[ca['deviceCategory'] == 'mobile']
ca_t = ca[ca['deviceCategory'] == 'tablet']

us_d = us[us['deviceCategory'] == 'desktop']
us_m = us[us['deviceCategory'] == 'mobile']
us_t = us[us['deviceCategory'] == 'tablet']

# -- canada
ca_d_ts = ca_d.groupby('trafficSource').sum()
ca_d_ts = ca_d_ts.reset_index()
ca_d_ts = ca_d_ts.drop(['visitorid', 'visitid'], axis=1)
ca_d_ts['rate'] = ca_d_ts['transactions'] / ca_d_ts['visits']

print('desktop (CA)- traffic source')
print(ca_d_ts)

ca_m_ts = ca_m.groupby('trafficSource').sum()
ca_m_ts = ca_m_ts.reset_index()
ca_m_ts = ca_m_ts.drop(['visitorid', 'visitid'], axis=1)
ca_m_ts['rate'] = ca_m_ts['transactions'] / ca_m_ts['visits']

print('mobile (CA) - traffic source')
print(ca_m_ts)

ca_t_ts = ca_t.groupby('trafficSource').sum()
ca_t_ts = ca_t_ts.reset_index()
ca_t_ts = ca_t_ts.drop(['visitorid', 'visitid'], axis=1)
ca_t_ts['rate'] = ca_t_ts['transactions'] / ca_t_ts['visits']

print('tablet (CA) - traffic source')
print(ca_t_ts)

# -- usa
us_d_ts = us_d.groupby('trafficSource').sum()
us_d_ts = us_d_ts.reset_index()
us_d_ts = us_d_ts.drop(['visitorid', 'visitid'], axis=1)
us_d_ts['rate'] = us_d_ts['transactions'] / us_d_ts['visits']

print('desktop (US)- traffic source')
print(us_d_ts)

us_m_ts = us_m.groupby('trafficSource').sum()
us_m_ts = us_m_ts.reset_index()
us_m_ts = us_m_ts.drop(['visitorid', 'visitid'], axis=1)
us_m_ts['rate'] = us_m_ts['transactions'] / us_m_ts['visits']

print('mobile (US) - traffic source')
print(us_m_ts)

us_t_ts = us_t.groupby('trafficSource').sum()
us_t_ts = us_t_ts.reset_index()
us_t_ts = us_t_ts.drop(['visitorid', 'visitid'], axis=1)
us_t_ts['rate'] = us_t_ts['transactions'] / us_t_ts['visits']

print('tablet (US) - traffic source')
print(us_t_ts)



# PAGES VIEWED

df2 = pd.read_csv('aritzia-conversions - pages viewed.csv')

print(df2.head())
print(df2.info())


# unique visits
print('unique visits: ', df2['visitid'].nunique())

# unique visitors: 
print('unique visitors: ', df2['visitorid'].nunique())

# bounce rate
visits = df2['visitid'].nunique()
freq = df2.groupby('visitid')['visitid'].count().tolist()
print(freq)
bounce = 0
for i in freq:
    if i == 1:
        bounce +=1
print('bounce rate: ', bounce/visits)


# pages per session 
print('pages per session: ', (np.mean(freq)).round(2))


# abandon cart rate 
print('abandon cart rate')
add_to_cart = df2[df2['eventAction'] == 'add-to-bag']
initiated_transactions = add_to_cart['visitid'].nunique()
print(initiated_transactions)
#print(add_to_cart_count)
# assume that a visit only has 1 transaction

# total conversions
conversions = len(df2[df2['eventAction'] == 'purchase'])
print(conversions)

print('abandon cart rate: ', (initiated_transactions - conversions)/initiated_transactions)












