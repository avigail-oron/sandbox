""" Problem 1"""

import math

def prob_1():
    divisors = [x for x in range(1000) if x%3 == 0 or x%5 ==0]
    print (int(math.fsum(divisors)))
    

""" Problem 2 """

def prob_2():
    fibbn1 = 1
    fibbn2 = 2
    curr = fibbn2
    even_sum = 0 
    
    def next(curr, fibbn1, fibbn2):
        curr = fibbn1+fibbn2
        fibbn1 = fibbn2
        fibbn2 = curr
        return curr, fibbn1, fibbn2
        
    while (curr < 4* math.pow(10, 6)):
    #while (curr < 90):
        if curr%2 == 0: #sum only even elements
            even_sum = even_sum+curr
            print (even_sum)
        curr, fibbn1, fibbn2 = next(curr, fibbn1, fibbn2)
        print (curr, fibbn1, fibbn2)
        
    print (even_sum)
        
        
    
def prob_3():
    
    def is_prime(num):
        factorials = [x for x in range(2, num) if num % x == 0]
        return factorials.__len__() == 0
    
    number = 600851475143
    max_fact = 0
    x=2
    #number = 1082
    while x < number:
        if number % x == 0 and is_prime(x) and x > max_fact:
            max_fact = x
            print (max_fact)
        x = x+1    
    return max_fact


def prob_4():
    
    def is_palindrome(number):
        str_num = str(number)
        rev_str_num = str_num[::-1]
        return str_num.__eq__(rev_str_num)
    
    def check_all_products():
        max_product = 0
        mp_x = 0
        mp_y = 0
        for x in range(999, 100, -1):
            for y in range (999, 100, -1):
                product = x*y
                if is_palindrome(product) and product > max_product:
                   max_product = product 
                   mp_x = x
                   mp_y = y
        return max_product, mp_x, mp_y           
    
    max_product, x, y = check_all_products()
    print ("Max product: ", max_product, " multipliers are: ", x, " and ", y)          
        
        
""" problem 5 """
def prob_5():
    
    def is_div_1_20(number):
        for div in range(1, 20):
            if number % div != 0:
                return False
        return True
    
    x = 20
    while True:
       if is_div_1_20(x):
           break
       x = x +1
    print (x)   
    
    
""" problem 6 """
def prob_6():
    
    def sq_of_sum(number):
        return math.pow(sum(range(1, number+1)), 2)
        
    def sum_of_sq(number):
        return sum([x*x for x in range(1, number+1)])
     
    print  (sq_of_sum(100))
    print  (sum_of_sq(100))
    print  (sq_of_sum(100)- sum_of_sq(100))
    
       
""" problem 7 """
def prob_7():
    def is_pita(a, b, c):
        return a*a+b*b == c*c
            
    def find_pita():
        for a in range(1,999):
            for b in range (a, 999):
                c = 1000-a-b
                if is_pita(a, b, c):
                    return a, b, c  
     
    print (find_pita())                          
                
            




def main():
    prob_7()
    
if __name__ == "__main__":
    main()