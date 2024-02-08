class Person:
    def __init__(self, last_name, first_name, DOB):
        self.lname = last_name
        self.fname= first_name
        self.age= 2023-DOB

    def method1(self):
        print(self.lname)
    

man = Person("Cyiza", "Kenny", 2006)
woman= Person("Rwibutso", "Delice", 2004)

man.method1()


class Player:
    def __init__(self, name, game, team):
        self.player_name= name
        self.player_game= game
        self.player_team= team
    
    def printing(self):
        print(self.player_name, self.player_game, self.player_team)
    

player_one= Player("Ancra_Messi", "Football", "Fc PSG")
player_two= Player("Ronaldo_Christiano", "Football","United_States_Arabs")

player_one.printing()
player_two.printing()

print("{} plays {}".format(player_one.player_name, player_two.player_game))