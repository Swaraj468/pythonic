invitation_list = ['Andrew', 'Simon', 'Swaraj', 'Tanishq']
"""
This script manages a dinner invitation list. It demonstrates how to update, expand, and shrink the list of invitees based on changing circumstances:

- Initializes an invitation list with four guests.
- Handles a guest's inability to attend by replacing them.
- Expands the list when a bigger table is found, adding more guests at specific positions.
- Prints personalized invitation messages for each guest.
- Shrinks the list due to a table delay, removing guests one by one and notifying them.
- Confirms invitations to the remaining two guests.
- Cleans up the invitation list by deleting all entries.

The script showcases list operations such as insert, append, pop, and del, along with formatted string output for user notifications.
"""
print("Mr Simon can't make to dinner so we are inviting Mr Dhruv")
print("I have found a bigger table for more people, so we are inviting more people.")
invitation_list.insert(0, 'Anuska')
invitation_list.insert(3, 'Akanksha')
invitation_list.append('Ruhi')
invitation_list[2] = 'Dhruv'
print(f"Hi! {invitation_list[0]} you are invited for dinner") 
print(f"Hi! {invitation_list[1]} you are invited for dinner") 
print(f"Hi! {invitation_list[2]} you are invited for dinner") 
print(f"Hi! {invitation_list[3]} you are invited for dinner") 
print(f"Hi! {invitation_list[4]} you are invited for dinner") 
print(f"Hi! {invitation_list[5]} you are invited for dinner")
print(f"Hi! {invitation_list[6]} you are invited for dinner")
# print(invitation_list)  # Uncomment for debugging: shows the final empty invitation list
print("Sorry for inconvenience guys, the table I ordered is arriving late so there is space for only 2 people")
pop_andrew = invitation_list.pop(1)
print(f"Sorry {pop_andrew}, you are not invited for the dinner")
pop_anuska = invitation_list.pop(0)
print(f"Sorry {pop_anuska}, you are not invited for the dinner")
pop_dhruv = invitation_list.pop(2)
print(f"Sorry {pop_dhruv}, for the inconvenience you have not been invited for the dinner")
pop_Tanishq = invitation_list.pop(3)
print(f"Sorry {pop_Tanishq}, you are not invited for the dinner")
pop_Ruhi = invitation_list.pop(2)
print(f"Sorry {pop_Ruhi}, you are not invited for the dinner")
print(f"Hi! {invitation_list[0]}, you have been invited")
print(f"Hi! {invitation_list[1]}, you have been invited")
del invitation_list[0]
del invitation_list[0]
print(invitation_list)
length = len(invitation_list);
print(f"The number of people i invited is {length}")