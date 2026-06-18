orders=[
    {
        "order_id":1,
        "customer":"rishabh",
        "items":[("phone",1,50000),("keyboard",2,20000),("mouse",3,18000)],
        "status":"deliverd"
    },
    {
        "order_id":2,
        "customer":"nikhl",
        "items":[("laptop",1,700000),("keyboard",1,15000),("mouse",3,18000)],
        "status":"deliverd"
    },
    {
        "order_id":3,
        "customer":"piyush",
        "items":[("phone",1,50000)],
        "status":"pending"
    }
   
]
total_revenue=0
spending_money={}
for order in orders:
    if order["status"]=="deliverd":
        customer=order["customer"]
        order_total=0
        for item,quantity,price in order["items"]:
            order_total+=(quantity*price)
        total_revenue+=order_total
        if customer in spending_money:
          spending_money[customer]+=order_total
        else:
          
          spending_money[customer]=order_total
top_customer=None
max_spent=-1
for customer,spent in spending_money.items():
    if spent>max_spent:
        max_spent=spent
        top_customer=customer
print(f"total revenue:{total_revenue}")
print(f"top spender:{top_customer}")
print(f"amount_spent:{max_spent}")
        
    
        
        