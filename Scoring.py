import time
import random
from colorama import Fore, Style

# Dictionary notes, sebagai database notes
notes = {
    'T': {'good': 250, 'greatLow': 400, 'greatMid': 400, 'greatHigh': 400, 'perfectLow': 500, 'perfectHigh': 500, 'critical': 500},
    'HH': {'good': 500, 'greatLow': 800, 'greatMid': 800, 'greatHigh': 800, 'perfectLow': 1000, 'perfectHigh': 1000, 'critical': 1000},
    'SSS': {'good': 750, 'greatLow': 1200, 'greatMid': 1200, 'greatHigh': 1200, 'perfectLow': 1500, 'perfectHigh': 1500, 'critical': 1500},
    'BBBB' : {'good': 1000, 'greatLow': 1250, 'greatMid': 1500, 'greatHigh': 2000, 'perfectLow': 2500, 'perfectHigh': 2500, 'critical': 2500}
}

# Database chart lagu
charts = {
    'Hibana': {
        'Basic': ['BBBB', 'SSS', 'BBBB', 'T', 'SSS'],
        'Advanced': ['HH', 'SSS', 'BBBB', 'HH', 'SSS', 'T', 'T', 'SSS'],
        'Expert': ['HH', 'HH', 'HH', 'SSS', 'SSS', 'BBBB', 'HH', 'SSS', 'BBBB', 'SSS'],
        'Master': ['SSS', 'SSS', 'T', 'HH', 'HH', 'SSS', 'BBBB', 'T', 'SSS', 'SSS', 'SSS', 'SSS']
    },
    'Ghost Rule': {
        'Basic': ['SSS', 'T', 'SSS', 'BBBB', 'T'],
        'Advanced': ['SSS', 'SSS', 'SSS', 'BBBB', 'BBBB', 'HH', 'T', 'SSS'],
        'Expert': ['T', 'SSS', 'BBBB', 'HH', 'HH', 'HH', 'SSS', 'BBBB', 'T', 'HH'],
        'Master': ['HH', 'BBBB', 'BBBB', 'HH', 'SSS', 'T', 'T', 'T', 'HH', 'BBBB', 'SSS', 'BBBB']
    },
    'Daydream Cafe': {
        'Basic': ['HH', 'BBBB', 'T', 'SSS', 'BBBB'],
        'Advanced': ['SSS', 'SSS', 'BBBB', 'SSS', 'BBBB', 'HH', 'HH', 'HH'],
        'Expert': ['BBBB', 'T', 'SSS', 'T', 'T', 'SSS', 'T', 'BBBB', 'BBBB', 'SSS'],
        'Master': ['T', 'SSS', 'HH', 'BBBB', 'HH', 'HH', 'T', 'T', 'T', 'SSS', 'BBBB', 'HH']
    }
}

# Fungsi membuat chart random sementara sebagai pengganti chart lagu
def GenerateRandomList():
    noteSequence = ['T', 'HH', 'SSS', 'BBBB']
    randomChart = [random.choice(noteSequence) for _ in range(12)]
    print(randomChart)

# Fungsi pemberi warna supaya enak dipandang
def ColoredOutput(note):
    if note == 'T':
        return f"\033[38;2;200;0;150m{note}\033[0m"
    elif note == 'HH':
        return f"\033[38;2;255;182;193m{note}\033[0m"
    elif note == 'SSS':
        return f"\033[34m{note}\033[0m"
    elif note == 'BBBB':
        return f"\033[31m{note}\033[0m"
    else:
        return note  

# Load lagu dan difficulty
def LoadNotes(songChoice, diffChoice):
    songList = {1: 'Hibana', 2: 'Ghost Rule', 3: 'Daydream Cafe'}
    diffList = {1: 'Basic', 2: 'Advanced', 3: 'Expert', 4: 'Master'}
    
    songName = songList[songChoice]
    diffName = diffList[diffChoice]
    
    return charts[songName][diffName]

# Hitung total score point
def TotalBasePointChart(chart) :
    basePoint = 0
    for i in range (len(chart)) :
        if (chart[i] == 'T') :
            basePoint += 500
        elif (chart[i] == 'HH') :
            basePoint += 1000
        elif (chart[i] == 'SSS') :
            basePoint += 1500
        elif (chart[i] == 'BBBB') :
            basePoint += 2500
    return basePoint

def TotalBonusPointChart(chart) :
    bonusPoint = 0
    for i in range (len(chart)) :
        if (chart[i] == 'BBBB') :
            bonusPoint += 100
    return bonusPoint

# Fungsi permainan chart
def PlayChart(noteSequence):
    baseAchievement = 0
    bonusAchievement = 0
    
    # Mengecek setiap note
    for note in noteSequence:
        print(ColoredOutput(note))
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("!")
        
        startTime = time.time() 
        userInput = input(">> ")
        endTime = time.time()
        reactionTime = endTime - startTime
        
        # Menghitung Base Point
        if userInput == note:
            if 0 < reactionTime <= 0.4:
                print(f"{notes[note]['critical']}")
                baseAchievement += notes[note]['critical']
            elif 0.4 < reactionTime <= 0.7:
                print(f"{notes[note]['perfectHigh']}")
                baseAchievement += notes[note]['perfectHigh']
            elif 0.7 < reactionTime <= 1:
                print(f"{notes[note]['perfectLow']}")
                baseAchievement += notes[note]['perfectLow']
            elif 1 < reactionTime <= 1.2:
                print(f"{notes[note]['greatHigh']}")
                baseAchievement += notes[note]['greatHigh']
            elif 1.2 < reactionTime <= 1.4:
                print(f"{notes[note]['greatMid']}")
                baseAchievement += notes[note]['greatMid']
            elif 1.4 < reactionTime <= 1.5:
                print(f"{notes[note]['greatLow']}")
                baseAchievement += notes[note]['greatLow']
            elif 1.5 < reactionTime <= 1.7:
                print(f"{notes[note]['good']}")
                baseAchievement += notes[note]['good']
            else:
                print("0")
        else:
            print("0")
            
        # Menghitung break bonus point
        if userInput == 'BBBB':
            if 0 < reactionTime <= 0.4:
                print("100")
                bonusAchievement += 100
            elif 0.4 < reactionTime <= 0.7:
                print("75")
                bonusAchievement += 75
            elif 0.7 < reactionTime <= 1:
                print("50")
                bonusAchievement += 50
            elif 1 < reactionTime <= 1.2:
                print("40")
                bonusAchievement += 40
            elif 1.2 < reactionTime <= 1.4:
                print("40")
                bonusAchievement += 40
            elif 1.4 < reactionTime <= 1.5:
                print("40")
                bonusAchievement += 40
            elif 1.5 < reactionTime <= 1.7:
                print("30")
                bonusAchievement += 30
            else:
                print("0")
        
        # Newline
        print("")
        
    achievement = ((baseAchievement / TotalBasePointChart(noteSequence)) * 100) + (bonusAchievement / TotalBonusPointChart(noteSequence))
    
    # Debug baseAchievement dan bonusAchievement
    # print(f"Your base score is: {baseAchievement}")
    # print(f"Your bonus score is: {bonusAchievement}")
    
    # Print achievement
    print("Congratulations on finishing the chart!")
    print(f"Your score is: {achievement:.2f}%!\n")

# Ascii Art
def PrintArt():
    art = r'''
     _        _______ _________ _        _______ _________   ______           
    ( (    /|(  ___  )\__   __/( (    /|(  ___  )\__   __/  (  __  \ |\     /|
    |  \  ( || (   ) |   ) (   |  \  ( || (   ) |   ) (     | (  \  )( \   / )
    |   \ | || (___) |   | |   |   \ | || (___) |   | |     | |   ) | \ (_) / 
    | (\ \) ||  ___  |   | |   | (\ \) ||  ___  |   | |     | |   | |  ) _ (  
    | | \   || (   ) |   | |   | | \   || (   ) |   | |     | |   ) | / ( ) \ 
    | )  \  || )   ( |___) (___| )  \  || )   ( |___) (___  | (__/  )( /   \ )
    |/    )_)|/     \|\_______/|/    )_)|/     \|\_______/  (______/ |/     \|
                                                                          
    '''
    print(art)

# Main function
if __name__ == "__main__":
    
    # Buat random chart
    # GenerateRandomList()
    
    # Ascii Art pembuka
    PrintArt()
    
    # Username
    name = input("Enter your username: ")
    print(f"Welcome {name}!\n")
    
    # Sekali permainan maimai DX dapat bermain hingga 4 chart lagu
    for i in range (4) :
        print(f"GAME {i+1} / 4!\n")
        
        # Memilih lagu
        print("Select a song:")
        print("1. Hibana")
        print("2. Ghost Rule")
        print("3. Daydream Cafe")    
        song = int(input(">> "))
        print("")
        
        # Memilih kesulitan   
        print("Select a difficulty:")
        print("1. Basic")
        print("2. Advanced")
        print("3. Expert")
        print("4. Master")
        diff = int(input(">> "))
        print("")
        
        # Load chart
        chart = LoadNotes(song, diff)
        
        # Debug chart
        # print(chart)
        # print(LengthChart(chart))
        # print(LengthBreakChart(chart))
        
        # Play chart
        print("Turn on your capslock!")
        play = input("Ready to play? (Y/N) ")
        print()
        if (play == 'Y') :
            PlayChart(chart)
        else :
            print("You are skipping this song!")
        
    print("Thank you for playing!")

