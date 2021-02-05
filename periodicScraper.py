
# run this script to update and notify all users from config/users.txt file

import calendarSourceDownloader
from getCredentials import getCredentials
from sys import argv
import userNotifier

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


if __name__ == "__main__":
    
    user_list_file_name = argv[1]
    users = loadUserList(user_list_file_name)

    for user in users:
        userNotifier.checkNewEventsAndNotifyUser(user['credentials'], user['events_file_name'], user['email_address'])
