import Tkinter as tk
from Tkinter import *
import sys
import csv
global new_text

class Liga:

    def __init__(self, master):
        self.master = master
        master.title("Liga")

        self.total = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="gracze na turnieju:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="ok", command=lambda: self.update("ok"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2, sticky=W+E)


class Application(Frame):

    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent

        self.add_numbers_of_players()
        self.add_tournament()
        self.remove_player()
        
    def add_number_of_players(self):
        import nowe_okno
        pip = nowe_okno.root()


#======================================
#join with okno 
#======================================

    def add_tournament(self):

        global players_tournament
        valid = False
        filename = 'warzone_players.csv'

        with open(filename) as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    warzone_playerlist.append( Warzone_player((row[0]), int(row[1]), int(row[2])) )
            except csv.Error as e:
                sys.exit('file {}, line {} {}'.format(filename, reader.line_num, e))

        while valid == False:
            try:
                players_tournament = int (raw_input ("ile graczy: ")) 
                valid = True
                if players_tournament > 0 :
                    while players_tournament is not 0:
                        #----------------------------------
                        name = raw_input("wpisz gracza: ")
                        score = players_tournament
                        
                        on_the_list = False
                        for player in warzone_playerlist:
                            if player.name == name:
                                if player in warzone_playerlist:
                                    player.score = player.score + players_tournament
                                    player.battle = player.battle+1
                                on_the_list = True
                                break
                        if not on_the_list:
                            warzone_playerlist.append(Warzone_player(name, score, 1 )) 
                        #----------------------------------
                        players_tournament -=1
                else:
                    print "wrong number try again"
                    break
                    
            except ValueError:
                print "must be numeric"
        


        filename = 'warzone_players.csv'
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for row in warzone_playerlist :
                writer.writerow([row.name, row.score, row.battle])
        print sorted (warzone_playerlist, key=getKey, reverse=True)
#==========================================================
        
    def remove_player(self):
        """
        Label (master, text = "wpisz gracza: ").grid(row=0)
        e1 = Entry(master)
        e1.grid(row = 0, column = 1)
        player_to_remove = e1.get()

        need to change in this direction
        """

        player_to_remove = raw_input ("wpisz gracza: ")

        filename = 'warzone_players.csv'
        on_the_list = False
        with open(filename) as f:
            reader = csv.reader(f)
            try:
                #tutaj nie powinno nadpisywac
                for row in reader:
                    warzone_playerlist.append( Warzone_player((row[0]), int(row[1]), int(row[2])) )
            except csv.Error as e:
                sys.exit('file {}, line {} {}'.format(filename, reader.line_num, e))

        while on_the_list == False:
            try:
                for player in warzone_playerlist:
                    if player.name == player_to_remove:
                        on_the_list = True
                        warzone_playerlist.remove(player)
                        break
                    else:
                        print "error this player is not in ranking"
                        on_the_list = True
            except ValueError:
                print "must be ---"
        filename = 'warzone_players.csv'
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for row in warzone_playerlist :
                writer.writerow([row.name, row.score, row.battle])
        print sorted (warzone_playerlist, key=getKey, reverse=True)

#-----------------------------------------------      
    def create_widgets(self):
           
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        #self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "bottom"})
#-----------------------------------------------

        self.add2 =Button(self)
        self.add2["text"] = "add players"
        self.add2["command"] = self.add_tournament

        self.add2.pack({"side": "bottom"})

#-----------------------------------------------
        
        self.add = Button(self)
        self.add["text"] = "add tournament players"
        self.add["command"] = self.add_number_of_players

        self.add.pack({"side": "left"})
#-----------------------------------------------
        self.remove = Button(self)
        self.remove["text"] = "remove player"
        self.remove["command"] = self.remove_player

        self.remove.pack({"side": "left"})
#-----------------------------------------------
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
#-----------------------------------------------

#lista i klasa gracza
#============================

        
class Warzone_player(object):
    def __init__(self, name, score, battle):
        self.name = name
        self.score = score
        self.battle = battle
        
    def __repr__(self):
        return'{} {} {}'.format(self.name, self.score, self.battle)

warzone_playerlist = []

#====================
def getKey(Warzone_player):
    return Warzone_player.score
print sorted (warzone_playerlist, key=getKey, reverse=True)
#============================

def main():
  
    root = Tk()
    app = Application(master=root)
    root.geometry("500x500+300+300")
    root.mainloop()
    root.destroy()


if __name__ == '__main__':
    main()  

