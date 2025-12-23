# Ecampus Management system

events =[]
participants={}
attendence={}

def add_event():
    """Add a new event"""
    eid=int(input("Enter Event Id:"))
    name=input("Enter Name :")
    date= input("Enter date (DD-MM-YYYY):")
    age_limit=int(input("Enter Age: "))
    club=input("Enter Club Organize:")
    
    event=(eid,name,date,age_limit,club)
    events.append(event)
    attendence[eid]=[]
    print("Event added successfully!")
    print(f"ID:{eid},Name:{name},Date:{date},Age Limit:{age_limit},Club:{club}\n")

def show_events():
    """Display all events"""
    if not events:
        print("No events available.")
        return
    print("Available Events:")
    for e in events:
        print(f"ID: {e[0]}, Name: {e[1]}, Date: {e[2]}, Age Limit: {e[3]}, Club: {e[4]}")
        print()

# Participant management Funnctions
def register_participant():
    """Register a participant for an events"""
    pid=int(input("Enter Participant Id:"))
    name=input("Enter name:")
    age=int(input("Enter Age:"))

    if pid in participants:
        print("Parcipants already is registered")
        return
    else:
        participants[pid]={"name":name, "age":age}
        print(f"particpant '{name}' registered successfully with Id ! {pid}")

def show_participants():
    """diaplay all participants"""
    if not participants:
        print("NO participants registered.")
        return
    print("registered participants:")
    for pid,details in participants.items():
        print(f"Id: {pid},Name: {details['name']},age:{details['age']}")
        print()

# Attendence Managment function

def mark_attendence():
    """mark attendence for an event"""
    eid=int(input("enterevent id :"))
    pid=int(input("enter participant id :"))
    if eid not in attendence:
        print("Event no foundeed!")
        return
    if pid not in participants:
        print("participant not registered for the events !")
        return 

    attendence[eid].append(pid)
    print(f"attendence marked for {participants [pid] ['name']} In event {eid}.") 

def show_attendence():
    """display attendence for an event"""
    eid = int(input("Enter event id:"))
    if eid not in attendence:
        print("Event not founded!")
        return
    print(f"Attendence for event {eid}:")
    if not attendence[eid]:
        print("NO participants Attendeed the event yet.")
        return
    for pid in attendence[eid]:
        print(f"{participants[pid]['name']} (Id : {pid})")
        print()

def generate_report():
    """Generate a report of all events, participants, and attendence"""
    print("participants Report:")
    for event in events:
        eid,name, _, _, _=event
        count =len(attendence[eid])
        print(f"Event : {name} {count} participants attended.")
        print()

# Main Menu

def main():
    while True:
        print("Ecampus Management System")
        print("1. Add Event")
        print("2. Show Events")
        print("3. Register Participant")
        print("4. Show Participants")
        print("5. Mark Attendence")
        print("6. Show Attendence")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_event()
        elif choice == '2':
            show_events()
        elif choice == '3':
            register_participant()
        elif choice == '4':
            show_participants()
        elif choice == '5':
            mark_attendence()
        elif choice == '6':
            show_attendence()
        elif choice == '7':
            generate_report()
        elif choice == '8':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")


# Run the program
if __name__ == "__main__":
    main()


