# Name: Dwight Dart
# Prog Purpose: This program finds a random number for our C.E. Project topic
#       "A" means the topic is available
#       "U" means the topic is unavailable

import random

TOTAL_TOPICS = 40 #test this program with 5 topics before changing to 40

#define variables
topics = []     #create an empty list to hold the topic codes
num_used_topics = 0
generate_another_randnumber = True  #boolean variable to control the outer loop
continue_search = True  #boolean to control the inner loop

for i in range(TOTAL_TOPICS):
    topics.append("A")  #add another item to the list and insert an "A" in it

while generate_another_randnumber:
    continue_search = True

    while continue_search:
        randnumber = random.randint(0, TOTAL_TOPICS-1) #items in list start with 0, not 1
        if topics[randnumber] == "A":
            topics[randnumber] = "U"
            num_used_topics +=1
            continue_search = False
    
    print("\nRandom Topic Number: " + str(randnumber+1)) #items in list start with 0, so add 1

    print("\nList of topic availability by number:")
    for i in range(TOTAL_TOPICS):
        print("\t" + str(i+1) + ". " + topics[i])

    if num_used_topics == TOTAL_TOPICS:
        print("There are no more topics available at this time.")

    else:
        answer = input("\n\nWhould you like another random number? Y/N: ")
        if answer.upper() != "Y":
            generate_another_randnumber = False


