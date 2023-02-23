#block of code that are executed together

#functions use def keyword

def print_name():
    print("My name is clive ")
    print("I am a grease monkey")
    print("blogging is my thing")
    print("I am 18 yrs old ")
    print("my hobbies are, travelling ,playing video games")
#calling / invoking the function 
print_name()


def add_numbers(num1,num2):
    sum_num = num1 + num2
    print(sum_num)

add_numbers(10,10)
add_numbers(70,30) #pass the parameter
add_numbers(300,700)

#multiplying 
def mult_numbers(num1,num2):
    mult_num = num1 * num2
    print(mult_num)
    
mult_numbers(10,10)
mult_numbers(70,30) #pass the parameter
mult_numbers(300,700)

#subtraction
def sub_numbers(num1,num2):
    sub_num = num1 - num2
    print(sub_num)
    
sub_numbers(10,10)
sub_numbers(70,30) #pass the parameter
sub_numbers(300,700)
