def feet_to_steps(user_feet):
   #write your code here
   rawSteps = user_feet / 2.5
   return (int(rawSteps))

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    
    #print your steps here
    print(str(feet_to_steps(float(input()))))
    