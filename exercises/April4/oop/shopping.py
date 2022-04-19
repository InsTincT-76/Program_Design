from product import Product

shopping_list= {
    Product("Converse Shoes", "Tan and Black walking shoes", 29.99),
    Product("Baby Doll", "Walking and Talking fun Doll", 19.99),
    Product("Gym Bag", "Green duffel bag", 45.99),

    
}

total_cost=0

for product in shopping_list:
    product.display()
    total_cost += product.get_total_price()
    
print(f"Total cost : $ {round(total_cost, 2)}")
    
