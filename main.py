
import calendar_source_downloader
from get_credentials import getCredentials
from sys import argv
import user_notifier

def loadUserList(file_name):

    users = []

    with open(file_name, "r") as f:

        all_data = f.read().split()

        for i in range(0, len(all_data), 3):

            user = [all_data[i], all_data[i+1], all_data[i+2]] # credentials file, user events file, address
            users.append(user)
    
    return users


if __name__ == "__main__":
    
    user_list_file_name = argv[1]
    users = loadUserList(user_list_file_name)

    for user in users:

        credentials_file = user[0]
        credentials = getCridentials(credentials_file)
        events_file = user[1]
        email_address = user[2]

        user_notifier.checkNewEventsAndNotifyUser(credentials, events_file, email_address)
