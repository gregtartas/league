import Tkinter
from Tkinter import *
import sys
import csv
import okno



class Liga:

    def __init__(self, master):
        
        self.master = master
        master.title("Liga W") #nazwa okna 

        #self.total = 0

        self.total_label_text = IntVar()
        #self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="gracze na turnieju:")

        vcmd = master.register(self.validate) 
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="ok", command=lambda: self.update("ok"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        
        if not new_text: 
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)   
            return True
        except ValueError:
            return False



    def update(self, method):
        
        if method == "ok":
            self.total = self.entered_number
            win = Toplevel()
            
            log = []
            afro = log
            new_text =  self.entered_number 
            for i in range(int(new_text)):
                log.append(i + 1)
                    
            ents = okno.makeform(win, afro) 
            root.bind('<Return>', (lambda event, e=ents: okno.fetch(e)))   
            b1 = Button(win, text='Zapisz',command=(lambda e=ents: okno.fetch(e)))
            b1.pack(side=LEFT, padx=3, pady=3)
            b2 = Button(win, text='Quit', command=root.quit)
            b2.pack(side=LEFT, padx=3, pady=3)
            b3 = Button(win, text='Zapisz turniej',command=okno.add_tournament())
            b3.pack(side=LEFT, padx=3, pady=3)
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

def add_tournament():
   
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
         players_tournament = entered_number
         valid = True
         if players_tournament > 0 :
            while players_tournament is not 0:
#----------------------------------
               name =  text
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




root = Tk()
my_gui = Liga(root)
root.mainloop()
