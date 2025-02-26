#შექმენით ფუნქცია hello() სადაც print ფუნქციის გამოყენებით გამოიტანთ  "GOA Best!

#2
def hello():
    print("GOA Best!")
    
    hello("GOA Best" )

#3

# შექმენით ფუნქცია sum რომელიც მიიღებს ორ არგუმენთ მაგ: a , b  და შემდეგ print-ის გამოყენებით გამოიტანთ მათ ჯამს

def sum(b, a):
    result = 1 + 5
    print(result)


#4
# შექმენით ფუნქცია to_string რომელიც მიიღებს ერთ არგუმენტს მაგალითად value  რომელსაც დაბეჭდავთ სტრინგად str-ის გამოყენებით

def to_string(value):
    string_value = str(value)
    print(string_value)

to_string(True) 
#5
# შექმენით ფუნქცია print_type რომელიც მიიღებს ერთ არგუმენტს და შემდეგ built-in function  type() გამოყებით შეამოწმებთ მის მონაცემთა ტიპს და გამოიტანთ ეკრანზე

def print_type(value):
    value_type = type(value)
    print(value_type)

print_type("Hello")



