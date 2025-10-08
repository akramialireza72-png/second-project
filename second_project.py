def check_again():
    question1=input("Do you want try again? yes/no ").lower()
    if question1 == "yes":
        return True
    else:
        return False
def check_rude(person_count , list , rude_person):
    if person_count == 1: # for just one
        list.remove(rude_person)
        return list
    else:
        for item in list: # for all
            if item == rude_person:
                list.remove(item)
        return list
normal_line= []
super_line= []
count= 0
# To collect passenger information for queue management
while count < 9:
    passengers_name=input("Enter your name: ").lower()
    while True:
        queue_input=int(input("Enter your ticket number: "))
        if queue_input == 0 or queue_input == 1:
            if queue_input == 0:
                normal_line.append(passengers_name)
                print("Successfully completed.")
                break
            else:
                super_line.append(passengers_name)
                print("you're very welcome.")
                break
        # Make sure the user enters a valid input
        else:
            print("Please enter the number 1 or 0")
            continue
    count += 1
print(",".join(normal_line))
print(",".join(super_line))
customer_try= 0
while True:
    late_person=input("What is your name? ").lower()
    person_friend_late=input("Enter your friend's name: ").lower()
    # Checking whether the person's name is on the list
    if person_friend_late in normal_line:
        missing= normal_line.index(person_friend_late)
        normal_line.insert(missing+1 , late_person)
        print("Successfully completed.")
        break
    elif person_friend_late in super_line:
        missing= super_line.index(person_friend_late)
        super_line.insert(missing + 1 , late_person)
        print("you're very welcome.")
        break
    # If their name isn’t on the list, they can check again through the function.
    else:
        print("Your friend wasn't in list" )
        Customer_response= check_again()
        if Customer_response == True:
            customer_try += 1
            if customer_try == 3: # The customer cannot attempt more than three times.
                print("You have exceeded the maximum number of attempts.")
                break
            else:
                continue
        else:
            break
print(",".join(normal_line))
print(",".join(super_line))
customer_try= 0
rude_list= []
list_all= normal_line + super_line
while True:
    undisciplined_person=input("Hello, Mr. Guard. Who has been undisciplined? ").lower()
    if undisciplined_person in normal_line or undisciplined_person in super_line:
        while True:
            # This enables the removal of either one name or the entire list.
            bad_count=input("All of them or just one person? 1/All ").lower()
            if bad_count == '1':
                int_bad_count= int(bad_count)
                rude_list= check_rude(int_bad_count, list_all , undisciplined_person)
                break
            elif bad_count == 'all':
                rude_list= check_rude(bad_count, list_all, undisciplined_person)
                break
            if customer_try == 3:
                print("You have exceeded the maximum number of attempts.")
                break
            else:
                print("Please enter 1 or all.")
                customer_try += 1
                continue
        break
    else:
        if customer_try == 3:
            print("You have exceeded the maximum number of attempts.")
            break
        else:
            print("That person is not on the list, officer.\n please try again.")
            customer_try += 1
            continue

print(f"polite people: {",".join(rude_list)}")