class IPL:
    def __init__(self,Team, Captain, Vice_Captain, Owner):
        self.Team = Team
        self.Captain = Captain
        self.Vice_Captain = Vice_Captain
        self.Owner = Owner
    def Team_info(self):
        print(f"Team: {self.Team}")
        print(f"Captain: {self.Captain}")
        print(f"Vice_Captain: {self.Vice_Captain}")
        print(f"Owner: {self.Owner}")
    def change_New_Captain(self, New_Captain):
        print(f"Captain {self.Captain} changed to {New_Captain}")
        self.Captain = New_Captain
    def change_New_Vice_Captain(self, New_Vice_Captain):
        print(f"Vice_Captain {self.Vice_Captain} changed to {New_Vice_Captain}")
        self.Vice_Captain = New_Vice_Captain
    def change_New_Owner(self, New_Owner):
        print(f"Owner {self.Owner} changed to {New_Owner}")
        self.Owner = New_Owner
# OBJECTS
# Initial team information for Chennai
Team_1=IPL("Chennai","Dhoni","Jadeja","N.Srinivasan")
print(Team_1.Team_info())

# Initial team information for Mumbai
Team_2=IPL("Mumbai","Rohit","Suryakumar","Neeta Ambani")
Team_2.Team_info()
# Changing captain and vice-captain for Mumbai
Team_2.change_New_Captain("Suryakumar")
Team_2.change_New_Vice_Captain("Hardik")
Team_2.Team_info()
