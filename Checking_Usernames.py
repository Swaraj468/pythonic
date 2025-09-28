current_users = ['swaraj09', 'swaraj07', 'swaraj08', 'swarajTheGoat', 'admin']
new_users = ['Admin', 'Swaraj07', 'legend27', 'pythonPro', 'swaraj10']
if new_users:
    for new in new_users:
        if new.lower() in current_users:
            print(f"Username, {new} already exist")
        else:
            print(f"Username, {new} is available.")
