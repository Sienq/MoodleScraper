
def getCridentials(file_name):

    with open(file_name, "r") as f:
        
        cridentials = f.readlines()
        nick = cridentials[0].strip()
        password = cridentials[1].strip()

        return nick, password