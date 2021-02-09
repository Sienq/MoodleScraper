from getCredentials import getCredentials


def loadUserList(file_name):

    users = []

    with open(file_name, "r") as f:

        all_data = f.read().split()

        for i in range(0, len(all_data), 4):

            user = dict()
            user['discord_id'] = all_data[i]
            user['credentials'] = getCredentials(all_data[i+1])
            user['events_file_name'] = all_data[i+2]
            user['email_address'] = all_data[i+3]
            
            users.append(user)
    
    return users


def getUserWithID(list_, user_id):

    for u in list_:
        
        if u['discord_id'] == str(user_id):
            return u
    
    return None
