import customtkinter
import tkinter
import os
import random
import requests
import json
import pprint
import asyncio
import threading
import time
import traceback
import pyrebase
from concurrent.futures import ThreadPoolExecutor
from PIL import Image


config = {
  "apiKey": "AIzaSyBqT2XnKRXee2wIQBVeU7SV46WML9uHg08",
  "authDomain": "claneye.firebaseapp.com",
  "databaseURL": "https://claneye-default-rtdb.firebaseio.com/",
  "storageBucket": "claneye.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

urlArray = [
    "https://www.roblox.com/games/155615604/Prison-Life-Cars-fixed",
    "https://www.roblox.com/games/5841467683/Glacian-Factory-RAID",
    "https://www.roblox.com/games/5361853069/Auroras-Dam-RAID",
    "https://www.roblox.com/games/6101349068/Blizzard-Outfall-RAID",
    "https://www.roblox.com/games/5014397267/RAID-Reversal-Compound",
    "https://www.roblox.com/games/6565314611/RAID-Unity-Outfall",
    "https://www.roblox.com/games/8771989818/RAID-Reversal-Compound-Remastered",
    "https://www.roblox.com/games/10141792191/RAID-The-Graveyard",
    "https://www.roblox.com/games/5847686787/SWORD-Tafes-Pass",
    "https://www.roblox.com/games/7257291581/RAID-The-Collective",
    "https://www.roblox.com/games/1427493600/WIJ-Outpost-Indigo-II",
    "https://www.roblox.com/games/1427580544/WIJ-Outpost-Cerulean-II",
    "https://www.roblox.com/games/5257899796/WIJ-Marrs-Communications-Relay-FAIRZONE",
    "https://www.roblox.com/games/4652767371/Raidable-Docks-Fairzone",
    "https://www.roblox.com/games/2007110262/Port-Maersk-EASY-MODE",
    "https://www.roblox.com/games/7775216059/RAID-Armageddon-Shipyard",
    "https://www.roblox.com/games/8249245310/RAID-Vulturist-Tower",
    "https://www.roblox.com/games/11401909704/RAID-Pride-of-Altaris",
    "https://www.roblox.com/games/11412621623/RAID-Starfall-Station",
    "https://www.roblox.com/games/9166246939/RAID-Malora-District",
    "https://www.roblox.com/games/11117968023/6v6-NEW-Crown-of-Polaris",
    "https://www.roblox.com/games/8152027924/RSF-Winter-Arvore-II#!/about",
    "https://www.roblox.com/games/9726482460/Installation-Anchorage",
    "https://www.roblox.com/games/8046351934/RAID-Dawn-Under-Heaven",
    "https://www.roblox.com/games/8254413158/Blacksite-Ares"
]

imgArr = [
    "https://tr.rbxcdn.com/d7c01ebfc7d898dff08ffedc4b68250f/768/432/Image/Png",
    "https://tr.rbxcdn.com/03a2f2f0dba2241cf291965879914676/768/432/Image/Png",
    "https://tr.rbxcdn.com/e6d91b528f99087113ff582b9e5349ad/768/432/Image/Png",
    "https://tr.rbxcdn.com/e9c71a7684c8e65257a04d4fd4b8c449/768/432/Image/Png",
    "https://tr.rbxcdn.com/2396c7bb94d7c63f38ded1328f82eaa5/768/432/Image/Png",
    "https://tr.rbxcdn.com/965465bfea5161e703010834a53e3577/768/432/Image/Png",
    "https://t7.rbxcdn.com/5c66ba63087a3dd4cfa7b5c4717f6065",
    "https://tr.rbxcdn.com/bab82f223d8d05f7068cc0e2b168a411/768/432/Image/Png",
    "https://tr.rbxcdn.com/1f89fc2b5c0234f5c3871a2405aa8a26/768/432/Image/Png",
    "https://tr.rbxcdn.com/f27bca028fdbdaaae5e14561599d2bfb/768/432/Image/Png",
    "https://tr.rbxcdn.com/808605d3b34c74bf02c7115585340e35/768/432/Image/Png",
    "https://tr.rbxcdn.com/9844e6883685d0e9ac8f69739f89cecc/768/432/Image/Png",
    "https://tr.rbxcdn.com/997960976f37f8d23a631c591620cd4a/768/432/Image/Png",
    "https://tr.rbxcdn.com/c03068cc7a411ab374df6bd0bc69671e/768/432/Image/Png",
    "https://tr.rbxcdn.com/41efc88d9796fa4b480e985c2245a836/768/432/Image/Png",
    "https://tr.rbxcdn.com/9966c1b993205996f1453a9e66a7a5f3/768/432/Image/Png",
    "https://tr.rbxcdn.com/b17e86f05e9c9e8123c8f1e5f779e4ee/768/432/Image/Png",
    "https://tr.rbxcdn.com/e68faf5a3a2080f27467306f4486ff0f/768/432/Image/Png",
    "https://t2.rbxcdn.com/45b31d4505d514928adfca9a7271d55e",
    "https://t7.rbxcdn.com/5c66ba63087a3dd4cfa7b5c4717f6065",
    "https://t1.rbxcdn.com/162138bbcfc4f93e3f26c790c6813acc",
    "https://tr.rbxcdn.com/5d3294f63bf1f9ac268799cc4d1f56da/768/432/Image/Png",
    "https://tr.rbxcdn.com/b83523c44c362851ca976aeb47711b04/768/432/Image/Png",
    "https://tr.rbxcdn.com/71ee13ad60ecb7cecda73e695ec58a7a/768/432/Image/Png",
]

gameIdArr = [
    155615604,
    5841467683,
    5361853069,
    6101349068,
    5014397267,
    6565314611,
    8771989818,
    10141792191,
    5847686787,
    7257291581,
    1427493600,
    1427580544,
    5257899796,
    4652767371,
    2007110262,
    7775216059,
    8249245310,
    11401909704,
    11412621623,
    9166246939,
    11117968023,
    8152027924,
    9726482460,
    8046351934,
    8254413158
]

locArr = [
    "Prison Life",
    "Glacian Factory",
    "Aurora's Dam",
    "Blizzard Outfall",
    "Reversal Compound",
    "Unity Outfall",
    "Reversal Compound 2",
    "Graveyard",
    "Tafes Pass",
    "Collective",
    "Indigo 2",
    "Cerulean 2",
    "Marrs Relay",
    "Docks",
    "Port Maersk",
    "Armageddon Shipyard",
    "Vulturist Tower",
    "Pride of Altaris",
    "Starfall Station",
    "Malora District",
    "Crown of Polaris",
    "Arvore 2",
    "Installation Anchorage",
    "Dawn Under Heaven",
    "Blacksite Ares"
]

newUrlArr = []
toRemove = []
toRemoveSpar = []

raidSearchLoc = []
raidSearchPlayer = []

serverType = 0
sortOrder = 2
excludeFullGames = False
limit = 10
searching = False
searchingSpar = False

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.quit_me)
        self.title("ClanEye Client - by haypro")
        self.iconbitmap('test_images\ClanEyeT.ico')
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ClanEyeT.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner.png")), size=(500, 150))
        self.banner2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner2.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "RaidEyeT.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "PracEyeT.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  ClanEye", image=self.logo_image,
                                                            compound="left", anchor="center", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=0, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="RaidEye",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="center", command=self.home_button_event)
        self.home_button.grid(row=1, column=0)

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="PracEye",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="center", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0)


        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="MANUAL RAID CHECK", corner_radius=5, font=('Calibri', 12), command=self.initial_test)
        # self.home_frame_button_1.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="ENABLE AUTO CHECK", corner_radius=5, font=('Calibri', 12), command=self.start_in_bg)
        self.home_frame_button_2.grid(row=1, column=1, padx=90, pady=10, sticky="W")
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="DISABLE AUTO CHECK", corner_radius=5, font=('Calibri', 12), command=self.end_loop)
        self.home_frame_button_3.grid(row=1, column=0, padx=10, pady=10, sticky="E")

        # self.new_label = customtkinter.CTkLabel(self.home_frame, text=f'', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.new_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.search_label = customtkinter.CTkLabel(self.home_frame, text=f'Waiting for search to start...', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.search_label.grid(row=2, column=0, columnspan=3, padx=10, pady=0)


        self.prac_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.prac_frame.grid_columnconfigure(0, weight=1)

        self.prac_frame_large_image_label = customtkinter.CTkLabel(self.prac_frame, text="", image=self.banner2)
        self.prac_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.prac_frame_button_1 = customtkinter.CTkButton(self.prac_frame, text="ENABLE AUTO CHECK", corner_radius=5, font=('Calibri', 12), command=self.start_in_bg_spar)
        self.prac_frame_button_1.grid(row=1, column=1, padx=90, pady=10, sticky="W")
        self.prac_frame_button_2 = customtkinter.CTkButton(self.prac_frame, text="DISABLE AUTO CHECK", corner_radius=5, font=('Calibri', 12), command=self.end_in_bg_spar)
        self.prac_frame_button_2.grid(row=1, column=0, padx=10, pady=10, sticky="E")

        self.search_label_spar = customtkinter.CTkLabel(self.prac_frame, text=f'Waiting for search to start...', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.search_label_spar.grid(row=2, column=0, columnspan=3, padx=10, pady=0)


        self.select_frame_by_name("home")

    def quit_me(self):
        print('quit')
        self.quit()
        self.destroy()

    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "prac" else "transparent")

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "prac":
            self.prac_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.prac_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("prac")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def destroy_labels(self):
        for label in toRemove:
            label.destroy()
        toRemove.clear()
        print("success!")

    def destroy_labels_spar(self):
        for label in toRemoveSpar:
            label.destroy()
        toRemoveSpar.clear()
        print("success spar!")

    def loop_check(self):
        global searching
        global toRemove
        if searching == True:
            return
        self.destroy_labels()
        searching = True
        self.search_label.configure(text="Initializing search...")
        gridRow = 3
        for i in range(0, len(gameIdArr)):

            if searching == False:
                self.destroy_labels()
                break

            placeId = gameIdArr[i]
            gameServerList = f"https://games.roblox.com/v1/games/{placeId}/servers/{serverType}?sortOrder={sortOrder}&excludeFullGames={excludeFullGames}&limit={limit}"

            headers = {
                "accept": "application/json"
            }

            response = requests.get(gameServerList, headers=headers)
            data = json.dumps(response.json())
            check = json.loads(data)

            try:
                playerCount = check['data'][0]['playing']
                print(f'{locArr[i]}: {playerCount}')
                if playerCount > 0:
                    raidSearchPlayer.append(check['data'][0]['playing'])
                    raidSearchLoc.append(locArr[i])
                i += 1
                time.sleep(0.2)
            except Exception:
                print(f'{locArr[i]}: 0')
                i += 1
                time.sleep(0.2)

        for checkVal in range(0, len(raidSearchPlayer)):

            if searching == False:
                self.destroy_labels()
                break

            self.new_label = customtkinter.CTkLabel(self.home_frame, text=f'{raidSearchLoc[checkVal]}: {raidSearchPlayer[checkVal]} player(s)', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.new_label.grid(row=gridRow, column=0, columnspan=3, padx=10, pady=0)
            toRemove.append(self.new_label)
            gridRow += 1

        self.search_label.configure(text="Currently searching for raids...")

        while searching == True:

            raidSearchPlayer.clear()
            raidSearchLoc.clear()

            if searching == False:
                self.destroy_labels()
                break

            gridRow = 3
            for i in range(0, len(gameIdArr)):
                if searching == False:
                    self.destroy_labels()
                    break

                placeId = gameIdArr[i]
                gameServerList = f"https://games.roblox.com/v1/games/{placeId}/servers/{serverType}?sortOrder={sortOrder}&excludeFullGames={excludeFullGames}&limit={limit}"

                headers = {
                    "accept": "application/json"
                }

                response = requests.get(gameServerList, headers=headers)
                data = json.dumps(response.json())
                check = json.loads(data)

                try:
                    playerCount = check['data'][0]['playing']
                    if playerCount > 0:
                        raidSearchPlayer.append(check['data'][0]['playing'])
                        raidSearchLoc.append(locArr[i])
                    i += 1
                    time.sleep(0.2)
                except Exception:
                    i += 1
                    time.sleep(0.2)

            self.destroy_labels()

            for checkVal in range(0, len(raidSearchPlayer)):

                if searching == False:
                    self.destroy_labels()
                    break

                self.new_label = customtkinter.CTkLabel(self.home_frame, text=f'{raidSearchLoc[checkVal]}: {raidSearchPlayer[checkVal]} player(s)', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
                self.new_label.grid(row=gridRow, column=0, columnspan=3, padx=10, pady=0)
                toRemove.append(self.new_label)
                gridRow += 1
            time.sleep(10)

        self.destroy_labels()


    
    def end_loop(self):
        global searching
        searching = False
        for label in toRemove: 
            label.destroy()
        toRemove.clear()
        self.search_label.configure(text="Waiting for search to start...")

    def start_in_bg(self):
        checkThread = threading.Thread(target=self.loop_check)
        checkThread.start()

    def start_in_bg_spar(self):
        sparThread = threading.Thread(target=self.loop_check_spar)
        sparThread.start()
    
    def loop_check_spar(self):
        global searchingSpar

        if searchingSpar == True:
            return

        callData = db.child("first").get()
        callDataVal = callData.val()
        callData2 = db.child('second').get()
        callData2Val = callData2.val()
        callData3 = db.child('third').get()
        callData3Val = callData3.val()

        self.first_label = customtkinter.CTkLabel(self.prac_frame, text=f'{callDataVal}', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.first_label.grid(row=3, column=0, columnspan=3, padx=10, pady=0)
        self.second_label = customtkinter.CTkLabel(self.prac_frame, text=f'{callData2Val}', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.second_label.grid(row=4, column=0, columnspan=3, padx=10, pady=0)
        self.third_label = customtkinter.CTkLabel(self.prac_frame, text=f'{callData3Val}', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.third_label.grid(row=5, column=0, columnspan=3, padx=10, pady=0)
        
        searchingSpar = True
        self.search_label_spar.configure(text="Currently searching for spars...")
        while searchingSpar == True:
            callData = db.child("first").get()
            callDataVal = callData.val()
            callData2 = db.child('second').get()
            callData2Val = callData2.val()
            callData3 = db.child('third').get()
            callData3Val = callData3.val()

            self.first_label.configure(text=callDataVal)
            self.second_label.configure(text=callData2Val)
            self.third_label.configure(text=callData3Val)


            time.sleep(10)


    def end_loop_spar(self):
        global searchingSpar
        searchingSpar = False
        for label in toRemoveSpar:
            label.destroy()
        toRemoveSpar.clear()
        self.search_label_spar.configure(text="Waiting for search to start...")

    def start_in_bg_spar(self):
        checkThreadSpar = threading.Thread(target=self.loop_check_spar)
        checkThreadSpar.start()

    def end_in_bg_spar(self):
        endSparThread = threading.Thread(target=self.end_loop_spar)
        endSparThread.start()


    def initial_test(self):

        self.home_frame.children.clear()
        newItems = []
        i = 0
        headers = { "accept": "application/json", 'User-agent': 'ClanEye 1.0' }

        for i in range(0, len(gameIdArr)):
            newUrlArr.append(f"https://games.roblox.com/v1/games/{gameIdArr[i]}/servers/{serverType}?sortOrder={sortOrder}&excludeFullGames={excludeFullGames}&limit={limit}")

        with ThreadPoolExecutor(max_workers=5) as pool:
            iterator = pool.map(requests.get, newUrlArr)
            
        for item in iterator:
            newItems.append(item.json())

        with ThreadPoolExecutor(max_workers=100) as pool2:
            iterator2 = pool2.map(json.dumps, newItems)

        with ThreadPoolExecutor(max_workers=100) as pool3:
            iterator3 = pool3.map(json.loads, iterator2)

        i = 0
        gridRow = 2
        for response in iterator3:
            print(response)
            loc = locArr[i]
            try:
                playerCount = response['data'][0]['playing']
                i += 1
                try:
                    self.new_label = customtkinter.CTkLabel(self.home_frame, text=f'{loc}: {playerCount} players', compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
                    self.new_label.grid(row=gridRow, column=0, columnspan=3, padx=10, pady=0)
                    gridRow += 1
                    # self.new_label.configure(text=f'{loc}: {playerCount}')
                except Exception:
                    print(i)
                    traceback.print_exc()
                    continue
            except:
                i += 1
                continue
        i = 0
        
        # print(newUrlArr)
        # for i in range(len(gameIdArr)):
        #     # randomIndex = random.randint(0, len(gameIdArr) - 1)
        #     placeId = gameIdArr[i]
        #     gameServerList = f"https://games.roblox.com/v1/games/{placeId}/servers/{serverType}?sortOrder={sortOrder}&excludeFullGames={excludeFullGames}&limit={limit}"

        #     headers = { "accept": "application/json" }

        #     response = requests.get(gameServerList, headers=headers)
        #     data = json.dumps(response.json())
        #     check = json.loads(data)
            
        #     try:
        #         print(f"{locArr[i]}: {check['data'][0]['playing']}")
        #     except:
        #         continue

if __name__ == "__main__":
    app = App()
    app.mainloop()

    