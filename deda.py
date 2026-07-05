import matplotlib.pyplot as pns

class Deda:
    def __init__(self, age, body_count):
        self.age = [age]
        self.body_count = [body_count]
        
    def respawn(self):
        self.age.append(0)
        self.body_count.append(0)
        
    def kill_deda(self):
        print(f"{self.age[-1]} years old deda who killed {self.body_count[-1]} people is now dead")
        self.respawn()
        
    def howdeda(self):
        print(f"{self.age[-1]} years old deda who killed {self.body_count[-1]} people")
    
    def dedamurders(self):
        self.body_count.append(self.body_count[-1] + 1)
        print(f"treacherous deda has murdered another... now his body count grows to {self.body_count[-1]}")
        
    def switchage(self, newage):
        print(f"devilish deda bends time to his will and changes age from {self.age[-1]} to {newage}")
        self.age.append(newage)
    
    def achievements(self):
        pns.plot(self.age, self.body_count, marker="o")
        pns.xlabel("Age")
        pns.ylabel("Kills")
        pns.title("Lifetime kills of deda")
        pns.show()

# Example usage
d1 = Deda(12, 1)
d1.switchage(11)
d1.dedamurders()
d1.howdeda()
d1.achievements()
