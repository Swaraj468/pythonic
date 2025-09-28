usernames = ['swaraj09', 'swaraj07', 'swaraj07', 'swarajTheGoat', 'admin']
if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")