
def getCredentials(file_name):

    with open(file_name, "r") as f:
        
        credentials = f.readlines()
        nick = credentials[0].strip()
        password = cridentials[1].strip()

        return nick, password