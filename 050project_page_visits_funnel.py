import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))

visits_cart = pd.merge(visits, cart, how = 'left')
print(len(visits_cart))

not_cart = visits_cart[visits_cart.cart_time.isnull()]
print(len(not_cart))
cart_percentage = len(not_cart) / len(visits_cart)
print(cart_percentage)

all_data = visits.merge(cart, how = 'left') \
                 .merge(checkout, how = 'left') \
                 .merge(purchase, how = 'left')
print(all_data.head())
not_purchse = all_data[all_data.purchase_time.isnull() & \
                      ~all_data.checkout_time.isnull()]
do_checkout  = all_data[~all_data.checkout_time.isnull()]
print(len(not_purchse)/len(do_checkout))

all_data['time_to_purchase'] = \
all_data.purchase_time -all_data.visit_time
print(all_data.time_to_purchase.head(5))
print (all_data.time_to_purchase.mean())
