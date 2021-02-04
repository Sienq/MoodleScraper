import calendar_scraper

CRIDENTIALS_FILE = "cridentials.txt"

def getCridentials():

    with open(CRIDENTIALS_FILE, "r") as f:
        
        cridentials = f.readlines()
        nick = cridentials[0].strip()
        password = cridentials[1].strip()

        return nick, password

if __name__ == "__main__":

    cridentials = getCridentials()
    print(calendar_scraper.getEventsPageSource(cridentials))