class Player:

    def __init__(self): 
        self.gesture = ["Rock", "Scissors", "Paper" , "Lizard", "Spock"]
        self.player_point = 0
        

    def choose_gesture(self):
     while True:
        self.gesture = ("Rock, Scissors, Paper, Lizard, Spock") 
        input("Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")

        if self.gesture == "0":
            print(f"You have chosen {self.gesture[0]}")
        if self.gesture == "1":
            print(f"You have chosen {self.gesture[1]}")
        if self.gesture == "2": 
            print(f"You have chosen {self.gesture[2]}")
        if self.gesture == "3":        
            print(f"You have chosen {self.gesture[3]}")
        if self.gesture == "4":        
            print(f"You have chosen {self.gesture[4]}")
        if self.gesture() not in self.gesture['0','1', '2', '3', '4']:
            print("Please try again and Enter 0 for Rock, 1 for Scissors, 2 for Paper, 3 for Lizard, 4 for Spock")
        else:
            break