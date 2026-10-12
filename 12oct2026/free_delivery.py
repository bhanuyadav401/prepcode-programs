order_amount = 850
is_premium_member = True
free_delivery = (order_amount >= 1000) or is_premium_member
print("qualifies for free delivery:", free_delivery)