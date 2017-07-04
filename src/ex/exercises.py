'''
Created on Mar 16, 2017

@author: maint
'''
from __builtin__ import str

"""  Exercise 4 """
from random import random
def divisors():
    num = int(input("Enter a number to find its divisors: "))
    potentials = range(1, num+1)
    answer = []
    for x in potentials:
        if num % x == 0:
            answer.append(x)
    print answer


"""  Exercise 5 """
import random  

def list_overlap():
    len1 = random.randint(1,100)
    len2 = random.randint(1,100)
    print"first list with ", len1, "elements"
    print"second list with ", len2, "elements"
    
    
    def fill_with_random(length):
        lst = []
        while(length>0):
            lst.append(random.randint(1,1000))
            length = length-1
        return lst
    
    def cacl_list_overlap(list1, list2):
        return [x for x in list1 if list2.__contains__(x)]  
            
    list1 = fill_with_random(len1)
    print "list1 = " , list1
    list2 = fill_with_random(len2)
    print "list2 = " , list2
    print "\nOverlapping part is :", cacl_list_overlap(list1, list2)
            

"""  Exercise 6 """

def is_palindrome():
    word = input("Enter a word: ")
    length = word.__len__()
    iterations = int(length / 2)
    i = 0
    while (i < iterations):
        if word[i] != word[length-1-i]:
            print word, " is not a palindrome "
            exit(0)
        i= i+1
    print word, " is a palindrome"
            
    

"""  Exercise 8 """
def play():
    play_options = ["Rock", "Paper", "Scissors"]
    input_options = ["Quit"]
    input_options.extend(play_options)
    selection_msg = "select : " + str(input_options)+ " "
    
    def prompt():
        input1 = input(selection_msg)
        print "You chose", input1
        return input1
    
    def win(a, b):
        if a.__eq__(play_options[0]) and b.__eq__(play_options[2]):
            return True
        if a.__eq__(play_options[1]) and b.__eq__(play_options[0]):
            return True
        if a.__eq__(play_options[2]) and b.__eq__(play_options[1]):
            return True
        return False
        
    player = prompt()
    while (player != "Quit"):
        if not player in input_options:
            print "Invalid option"
        else:    
            my = random.sample(play_options, 1)[0]
            print "I chose", my
            if win(player, my):
                print "You win!"
            elif win(my, player):
                print "I win!"
            else:
                print "It's a tie"
        player = prompt()        
            

"""  Exercise 15 """
def reverse_words():
    
    def get_words():
        input_str = input("Please enter your sentence: ")
        return input_str
    
    def nice_print_list(a_list):
        sep = " "
        nice = sep.join(a_list)
        print nice
    
    def reverse(sentence):
        word_list = sentence.split()
        reversed_list = word_list[::-1]
        return reversed_list
    
    nice_print_list(reverse(get_words()))    


def main():
#    divisors()
#    list_overlap()
#    is_palindrome()
#    play() 
    reverse_words()
    
if __name__ == "__main__":
    main()
        
                