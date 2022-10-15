num_of_ppl = int(input("Enter the numbers of People available on the meeting scheduler: "))

list_ppl = {}
meeting = []
busy = []

def main():
    
    for i in range(num_of_ppl):
        temp = input("Enter the name: ")
        list_ppl[temp] = "a"
        
    wtd = input("\nDo you want to schedule a meeting? Y or N: ")
    if wtd == "Y":
        print("\nThe following People are available: ")
        for name, avl in list_ppl.items():
            if avl == "a":
                print(name)
        
        add = input("\nEnter Persons Name(seperated with',' without space) to add: \n")
        mems = add.split(",")
        
        for i in mems:
            for name,  avl in list_ppl.items():
                if i != name:
                    meeting.append(i)
                else: print(name, "is busy")
            
            
        print("Meeting created!")
        print("People in meeting: ",meeting)
            
        
        
        # for name in range(len(busy)):
        #     for ppl in range(len(meeting)):
        #         if meeting[ppl] == name:
        #             print(name," is busy")
        
        wtd = input("Restart App? Y or N: ")
        if wtd =="Y":
            main()
        else: pass
            
    else:
        wtd = input("Restart App? Y or N: ")
        if wtd =="Y":
            main()
        else: pass


main()
