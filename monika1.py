from faker import Faker
import pandas as pd
from datetime import datetime


fake = Faker()
a=1
b=2
c=3
a=1


def get_most_frequent_email_domain():
    """
    Generate fake profiles and return the most frequent  email domain
    """
    now = datetime.now() #placeholder code for the review to detect
    profiles = [fake.profile() for i in range(100)]
    data = pd.DataFrame(profiles)
    data['domain'] = data['mail'].str.split('@', expand=True).iloc[:,1]
    most_frequent_domain = data['domain'].mode()[0]
#     print('done')
    return most_frequent_domain



if __name__ == '__main__':
    print(get_most_frequent_email_domain())
    
print("hello world") 
print("hello world") 

def setdefault_example():
    std_dict = dict()
    for k, v in enumerate(range(5)):
        std_dict.setdefault(k, []).append(v)
    return std_dict

if a==1:
    if b==2:
        if c==3:
            return true
        else:
            return false
        if a==1:
            return true 
        else
        
        operations_count = 0
 
def main():
    ask_again = True
    while(ask_again):
        a = input("Enter the numerator: ")
        b = input("Enter the denominator: ")
        result = perform_division(a,b)
        print(result)
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if(ask_again == 'yes'):
            ask_again = True
        else:
            ask_again = False
            print("You performed " + str(operations_count) + " operations, bye!")
 
 
def perform_division(a,b):
    global operations_count
    try:
        operations_count += 1
        return int(a)/int(b)
    except Exception as e:
        pass
 
 
main()
    
    

