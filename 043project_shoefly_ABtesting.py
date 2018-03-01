import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(5))

ad_platform = \
ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(ad_platform)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head(5))

clicks_by_source = \
ad_clicks.groupby(['utm_source', 'is_click']) \
.user_id.count().reset_index()
clicks_pivot = clicks_by_source \
.pivot(index='utm_source',
       columns='is_click',
       values='user_id').reset_index()
clicks_pivot['percent_clicked'] = \
clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

AB_ad = ad_clicks.groupby(['experimental_group', 'is_click']) \
.user_id.count().reset_index()
AB_pivot = AB_ad \
.pivot(index='experimental_group',
       columns='is_click',
       values='user_id').reset_index()
AB_pivot['percent_clicked'] = \
AB_pivot[True] / (AB_pivot[True] + AB_pivot[False])
print(AB_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
a_dayclicks = a_clicks.groupby(['day', 'is_click']) \
.user_id.count().reset_index()
b_dayclicks = b_clicks.groupby(['day', 'is_click']) \
.user_id.count().reset_index()
a_day_pivot = a_dayclicks \
.pivot(index='day',
       columns='is_click',
       values='user_id').reset_index()
a_day_pivot['percent_clicked'] = \
a_day_pivot[True] / (a_day_pivot[True] + a_day_pivot[False])
b_day_pivot = b_dayclicks \
.pivot(index='day',
       columns='is_click',
       values='user_id').reset_index()
b_day_pivot['percent_clicked'] = \
b_day_pivot[True] / (b_day_pivot[True] + b_day_pivot[False])
print(a_day_pivot)
print(b_day_pivot)
