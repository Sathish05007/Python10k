#For loop in list,string,set,tuple
list=["hello","sagar","good","morning"]
for i in list:
    print(i)
    print(list)
    print(i[0])

#revice a string,list,tuple,set use this metnod
list_1=["hi","hello","welcome","sagar","java","css","html"]

for i in range(len(list_1)-1,-1,-1): #last element start,stop at -1 to print index[0],step value -1
    print(list_1[i])

for i in range(1,len(list_1)-1):
    print(list_1[i]) #print the all elements expect first and last element


my_list=["king","queen","hors","bishp","elephent"]

for i in my_list:
    if(len(i)%2==0):
      print(f"the {i} is having length =",len(i))


info={
    "name":"sagar",
    "age":25,
    "gender":"male",
    "city":"hyd"
}

for i in info:
    # print(i)
    # print(info[i])
    print(f"{i}:{info[i]}")



students = [
    {"id": 1, "name": "Alice", "age": 20, "grade": "A"},
    {"id": 2, "name": "Bob", "age": 21, "grade": "B"},
    {"id": 3, "name": "Charlie", "age": 19, "grade": "A"},
    {"id": 4, "name": "David", "age": 22, "grade": "C"},
    {"id": 5, "name": "Eva", "age": 20, "grade": "B"},
    {"id": 6, "name": "Frank", "age": 23, "grade": "A"},
    {"id": 7, "name": "Grace", "age": 21, "grade": "B"},
    {"id": 8, "name": "Helen", "age": 20, "grade": "C"}
]
for i in students:
    # print(i)
    print(students["name"])

print(students[5])
   


ecommerce_data = [
    {
        "order_id": "ORD001",
        "customer_name": "Alice Johnson",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "quantity": 2,
        "price_per_unit": 599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD002",
        "customer_name": "Rajesh Kumar",
        "product": "Bluetooth Speaker",
        "category": "Electronics",
        "quantity": 1,
        "price_per_unit": 1999,
        "payment_method": "UPI",
        "delivery_status": "Shipped"
    },
    {
        "order_id": "ORD003",
        "customer_name": "Maria Fernandez",
        "product": "Leather Handbag",
        "category": "Fashion",
        "quantity": 1,
        "price_per_unit": 2499,
        "payment_method": "Cash on Delivery",
        "delivery_status": "Out for Delivery"
    },
    {
        "order_id": "ORD004",
        "customer_name": "John Smith",
        "product": "Running Shoes",
        "category": "Footwear",
        "quantity": 1,
        "price_per_unit": 3499,
        "payment_method": "Net Banking",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD005",
        "customer_name": "Anjali Mehta",
        "product": "Cotton Bedsheet Set",
        "category": "Home & Living",
        "quantity": 3,
        "price_per_unit": 899,
        "payment_method": "Credit Card",
        "delivery_status": "Cancelled"
    },
    {
        "order_id": "ORD006",
        "customer_name": "Samuel Lee",
        "product": "Smart Watch",
        "category": "Wearable Tech",
        "quantity": 1,
        "price_per_unit": 5299,
        "payment_method": "Debit Card",
        "delivery_status": "Delivered"
    },
    {
        "order_id": "ORD007",
        "customer_name": "Neha Sharma",
        "product": "Makeup Kit",
        "category": "Beauty",
        "quantity": 2,
        "price_per_unit": 1499,
        "payment_method": "UPI",
        "delivery_status": "Processing"
    },
    {
        "order_id": "ORD008",
        "customer_name": "David Brown",
        "product": "Office Chair",
        "category": "Furniture",
        "quantity": 1,
        "price_per_unit": 4599,
        "payment_method": "Credit Card",
        "delivery_status": "Delivered"
    }
]
   
for i in ecommerce_data:
    if(i["category"]=="Electronics"):
        print(i)
print(ecommerce_data[6]["customer_name"])        
   

     
tuple=("a","b","c","d","e","f","g","h","i")
for i in tuple:
    print(i)

# set={"sagar","laddu","ramesh","suresh"} #we dont use for loop for sets
# for i in set:
#     print(i)

#what is break,countines