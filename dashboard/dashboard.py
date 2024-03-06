import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns, streamlit as st, os, datetime

bike_df = pd.read_csv("day.csv", parse_dates=['dteday'], index_col='dteday')
bike_df.rename(columns={'instant':'rec_id','dteday':'datetime','yr':'year','mnth':'month','weathersit':'weather_condition',
                       'hum':'humidity','cnt':'total_count'},inplace=True)

columns = ['season', 'year', 'month', 'holiday', 'weekday', 'workingday', 'weather_condition']

for col in columns:
  bike_df[col] = bike_df[col].astype("category")

total_df = bike_df[['total_count']]
total_df = total_df.resample('M').mean()

weather_df = bike_df.groupby(by=['season', 'holiday']).agg({
    "total_count":"sum",
})

condition_df = bike_df.groupby(by=['month','holiday']).agg({
    'total_count': 'sum'
})

with st.container():
  st.title('Total Rental Bikes Last 2 Years per Months')
  fig, ax = plt.subplots(figsize=(10,5))
  sns.lineplot(x='dteday', y='total_count', data=total_df, ax=ax)
  ax.set_xlabel("Date")
  ax.set_ylabel("Customers")
  st.pyplot(fig)
  plt.show()

with st.container():
  st.title('Total Rental Bikes Every Seasons in Holiday')
  fig, ax = plt.subplots(figsize=(10,5))
  sns.barplot(x='season', y='total_count', data=weather_df, hue='holiday', ax=ax)
  ax.set_title('Total Rental Bikes Every Seasons in Holiday')
  ax.set_xlabel("Season")
  ax.set_ylabel("Customers")
  st.pyplot(fig)
  plt.show()

with st.container():
  st.title('Total Rental Bikes Every Months in Holiday')
  fig, ax = plt.subplots(figsize=(10,5))
  sns.barplot(x='month', y='total_count', data=condition_df, hue='holiday', ax=ax)
  ax.set_xlabel("Months")
  ax.set_ylabel("Customers")
  st.pyplot(fig)
  plt.show()