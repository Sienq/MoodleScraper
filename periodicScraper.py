
# run this script to update and notify all users from config/users.txt file

import calendarSourceDownloader
from getCredentials import getCredentials
from sys import argv
import userNotifier
import time
from singleInstanceLock import *
import userslist


LOCK_FILE_NAME = "single_scraper_lock"


if __name__ == "__main__":
    
    waitAndLock(LOCK_FILE_NAME)

    user_list_file_name = argv[1]
    users = userslist.loadUserList(user_list_file_name)

    for user in users:
        userNotifier.checkNewEventsAndNotifyUser(user['credentials'], user['events_file_name'], user['email_address'], user['discord_id'])
    
    removeLock(LOCK_FILE_NAME) # lock will not be removed if scraping fails to prevent next launch
