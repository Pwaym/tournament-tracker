participants = input(
    "Welcome to the Tournament Tracker!\r\n"
    "==================================\r\n"
    "Enter the number of participants:"
)
print("\r\nThere are",participants,"participant slots ready for sign-ups.\r\n")

global tempstr
tempstr = []
for i in range(1,int(participants)+1):
    tempstr.append(f"{i}: None")

def signup(participantname, desiredslot):
    if int(desiredslot) in range(1,int(participants)):
        if "None" in tempstr[int(desiredslot)-1]:
            tempstr[int(desiredslot)-1] = f"{desiredslot}: {participantname}"
            print("Successfully updated participants\r\n")
        else:
            print("That slot is full! Choose another slot or remove existing participant.\r\n")
    else:
        print("That slot does not exist!\r\n")

def cancel(participantname, startingslot):
    if int(startingslot) in range(1,int(participants)):
        if participantname in tempstr[int(startingslot)-1]:
            tempstr[int(startingslot)-1] = f"{startingslot}: None"
            print("Successfully updated participants\r\n")
        else:
            print(f"{participantname} is not in that starting slot.\r\n")
    else:
        print("That slot does not exist!\r\n")

def view(startingslot):
    if int(startingslot) in range(1,int(participants)):
        for k in range(int(startingslot)-6,int(startingslot)+5):
            if k in range(int(participants)):
                print(f"{tempstr[k]}")
            else:
                pass
    else:
        print("That slot does not exist!\r\n")

def save(confirm):
    if confirm == "y":
        finalstr = ','.join(tempstr)
        f = open("participants.csv","w")
        f.write(finalstr)
        print("Your changes have been saved\r\n")
    else:
        print("Your changes have not been saved\r\n")

while True:
    menuselect = input(
        "\r\nParticipant Menu\r\n"
        "================\r\n"
        "1. Sign Up\r\n2. Cancel Sign Up\r\n3. View Participants\r\n4. Save Changes\r\n5. Exit\r\n"
        "Input a number 1-5 to select:"
    )
    if menuselect == "5":
        print("Exit")
        print("====")
        exitprompt = input("Any unsaved changes will be lost.\r\nAre you sure you want to exit? [y/n]")
        if exitprompt == "y":
            break
        else:
            pass
    elif menuselect == "1":
        print("Participant Sign Up")
        print("===================")
        participantname = input("Input participant name:")
        desiredslot = input(f"Input desired slot [1-{participants}]:")
        signup(participantname, desiredslot)
    elif menuselect == "2":
        print("Participant Cancellation")
        print("========================")
        startingslot = input(f"Input starting slot [1-{participants}]:")
        participantname = input("Input participant name:")
        cancel(participantname, startingslot)
    elif menuselect == "3":
        print("View Participants")
        print("=================")
        startingslot = input(f"Input starting slot [1-{participants}]:")
        view(startingslot)
    elif menuselect == "4":
        print("Save Changes")
        print("============")
        confirm = input("Would you like to save your changes to CSV? [y/n]")
        save(confirm)
    else:
        pass
        