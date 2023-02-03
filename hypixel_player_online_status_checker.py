from mojang import MojangAPI
from time import sleep
from datetime import datetime
import requests
import os

def clear_console():
    """
    Allows the resetting of the console.
    (Clear the screen).
    """
    print("\n")
    os.system("cls||clear")

def get_player_online_status():
    person_of_intrest = input(
        "Please type the name of the player that you want to check:" 
        )
    key = input(
        """
        Please type in your hypixel-api-key.
        If you don't have this special key, 
        log in to the hypixel server 
        and use the command 'api' to get your key.
        The key is 36 characters long
        with a combination of letters, numbers, and hyphens:
        """
        )
    if len(key) != 36:
        print("Error, the length of your key is incorrect!")
        get_player_online_status()
    ping_delay = int(input(
        """
        Please type in a number that represents the ping delay.
        For example, 100 would mean a 100-second delay per ping.
        Please note, the fastest ping rate is every 61 seconds.
        The reason for this is because of the API rules found here:
        https://api.hypixel.net/#section/Introduction/Rules
        Going faster than every 61 seconds may be a violation of the rules.
        Moreover, it is unnecessary to access the server's info that often.
        Altering this in any shape or form is ill-advised.
        """
        ))
    if ping_delay < 61:
        ping_delay = 61

    clear_console()
    
    while True:
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M:%S")

        uuid = MojangAPI.get_uuid(person_of_intrest)
        requestlink = f"https://api.hypixel.net/player?key={key}&uuid={uuid}"

        hypixeldata = requests.get(requestlink).json()

        try:
            player = hypixeldata["player"]["displayname"]
        except: # Error b/c there is no data on that player or on that key
            print(
                """
                Sorry, but this player has never been on the server.
                OR, your inputted API key is incorrect. 
                Please double-check that your API key is correct.
                """
                )
            get_player_online_status()
            
        try:
            logouttime = hypixeldata['player']['lastLogout']
            logintime = hypixeldata['player']['lastLogin']
        except: # Error b/c some players disable their API status online.
            print("Sorry, but the player has made their status private.")
            get_player_online_status()

        if logouttime < logintime:
            print(f'{player} IS ONLINE! -> pinged at ' + current_time)
        else:
            print(f'{player} is offline -> pinged at ' + current_time)
        sleep(ping_delay)
get_player_online_status()