''' TO-DO:
screenshot capture/saving feature
could/should refactor card_list creation
keyboard shortcuts
'''


from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title('test2')
root.geometry('1100x700')

#------functions to change menubutton background colors-------
def changeColor_red(mb_object):
    mb_object.configure(bg='#f21515')
def changeColor_green(mb_object):
    mb_object.configure(bg='#35e805')
def changeColor_light_red(mb_object):
    mb_object.configure(bg='#e5b0a6')
def changeColor_light_green(mb_object):
    mb_object.configure(bg='#b5f9a2')


#---------create Menubutton function------------
def createMenubutton(mb_name, mb_text, row_num, col_num):
    mb_name = Menubutton(root, text=mb_text, height='2', width='5', bg='#77a6c6',activebackground='#f7ffb3',relief=RAISED)
    mb_name.menu = Menu(mb_name, tearoff=OFF)
    mb_name['menu'] = mb_name.menu
    mb_name.menu.add_command(label='C1', background='#f21515', command=lambda: changeColor_red(mb_name))
    mb_name.menu.add_command(label='C2', background='#35e805', command=lambda: changeColor_green(mb_name))
    mb_name.menu.add_command(label='C3', background='#e5b0a6', command=lambda: changeColor_light_red(mb_name))
    mb_name.menu.add_command(label='C4', background='#b5f9a2', command=lambda: changeColor_light_green(mb_name))
    mb_name.grid(row=row_num, column=col_num)

#------list of text for menubuttons----------
card_list = ['AA','AKs','AQs','AJs','ATs','A9s','A8s','A7s','A6s','A5s','A4s','A3s','A2s',
            'AKo','KK', 'KQs','KJs','KTs','K9s','K8s','K7s','K6s','K5s','K4s','K3s','K2s',
            'AQo','KQo','QQ', 'QJs','QTs','Q9s','Q8s','Q7s','Q6s','Q5s','Q4s','Q3s','Q2s',
            'AJo','KJo','QJo','JJ', 'JTs','J9s','J8s','J7s','J6s','J5s','J4s','J3s','J2s',
            'ATo','KTo','QTo','JTo','TT', 'T9s','T8s','T7s','T6s','T5s','T4s','T3s','T2s',
            'A9o','K9o','Q9o','J9o','T9o','99', '98s','97s','96s','95s','94s','93s','92s',
            'A8o','K8o','Q8o','J8o','T8o','98o','88', '87s','86s','85s','84s','83s','82s',
            'A7o','K7o','Q7o','J7o','T7o','97o','87o','77', '76s','75s','74s','73s','72s',
            'A6o','K6o','Q6o','J6o','T6o','96o','86o','76o','66', '65s','64s','63s','62s',
            'A5o','K5o','Q5o','J5o','T5o','95o','85o','75o','65o','55', '54s','53s','52s',
            'A4o','K4o','Q4o','J4o','T4o','94o','84o','74o','64o','54o','44', '43s','42s',
            'A3o','K3o','Q3o','J3o','T3o','93o','83o','73o','63o','53o','43o','33', '32s',
            'A2o','K2o','Q2o','J2o','T2o','92o','82o','72o','62o','52o','42o','32o', '22',
            ]

#---------menubutton grid layout creation------------
x = 0
for i in range(13):
    for j in range(13):
        createMenubutton('menub1', card_list[x], i, j)
        x += 1


class Card:
    def __init__ (self, value, suit):   #correct value parameter will be 0-12, suit will be 0-3
        self.value = value
        self.suit = suit

    def __repr__(self):
            value_name = ""
            suit_name = ""
            if self.value == 0:
                value_name = "2"
            if self.value == 1:
                value_name = "3"
            if self.value == 2:
                value_name = "4"
            if self.value == 3:
                value_name = "5"
            if self.value == 4:
                value_name = "6"
            if self.value == 5:
                value_name = "7"
            if self.value == 6:
                value_name = "8"
            if self.value == 7:
                value_name = "9"
            if self.value == 8:
                value_name = "10"
            if self.value == 9:
                value_name = "jack"
            if self.value == 10:
                value_name = "queen"
            if self.value == 11:
                value_name = "king"
            if self.value == 12:
                value_name = "ace"
            if self.suit == 0:
                suit_name = "diamonds"
            if self.suit == 1:
                suit_name = "clubs"
            if self.suit == 2:
                suit_name = "hearts"
            if self.suit == 3:
                suit_name = "spades"


            return value_name + '_of_' + suit_name   # or could use: return 'a {self.color} of'.format(self=self)      

comm_cards = []


class Deck(list):  
    def __init__(self):
        super().__init__()
        suits = list(range(4))          #creates a list variable named suits with length of 4 elements
        values = list(range(13))
        for j in suits:
            for i in values:
                self.append(Card(i,j))

    def __repr__(self):
        return f"{len(self)} cards remaining in deck."

    def shuffle(self):
        random.shuffle(self)

    def deal_comm_cards(self):
        for i in range(5):
            comm_cards.append(self.pop(0))

    def burn(self):
        self.pop(0)

def PokerGame():
    deck = Deck()
    deck.shuffle()
    deck.deal_comm_cards()

PokerGame()

my_img1 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[0]) + ".png").resize((100,155))) 
my_img2 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[1]) + ".png").resize((100,155)))
my_img3 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[2]) + ".png").resize((100,155)))
my_img4 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[3]) + ".png").resize((100,155)))
my_img5 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[4]) + ".png").resize((100,155)))


my_label = Label(image=my_img1)
my_label.grid(row=8, column=15,rowspan=5 )

my_label2 = Label(image=my_img2)
my_label2.grid(row=8, column=16,rowspan=5 )

my_label3 = Label(image=my_img3)
my_label3.grid(row=8, column=17,rowspan=5 )

my_label4 = Label(image=my_img4)
my_label4.grid(row=8, column=18, rowspan=5 )

my_label5 = Label(image=my_img5)
my_label5.grid(row=8, column=19, rowspan=5 )

def updateCommCards():

    comm_cards.clear()

    global my_label
    global my_label2
    global my_label3
    global my_label4
    global my_label5

    global my_img1
    global my_img2
    global my_img3
    global my_img4
    global my_img5

    PokerGame()

    my_img1 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[0]) + ".png").resize((100,155))) 
    my_img2 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[1]) + ".png").resize((100,155)))
    my_img3 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[2]) + ".png").resize((100,155)))
    my_img4 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[3]) + ".png").resize((100,155)))
    my_img5 = ImageTk.PhotoImage(Image.open("cards/" + str(comm_cards[4]) + ".png").resize((100,155)))

    my_label = Label(image=my_img1)
    my_label.grid(row=8, column=15,rowspan=5 )

    my_label2 = Label(image=my_img2)
    my_label2.grid(row=8, column=16,rowspan=5 )

    my_label3 = Label(image=my_img3)
    my_label3.grid(row=8, column=17,rowspan=5 )

    my_label4 = Label(image=my_img4)
    my_label4.grid(row=8, column=18, rowspan=5 )

    my_label5 = Label(image=my_img5)
    my_label5.grid(row=8, column=19, rowspan=5 )


deal_button = Button(root, text='Deal board')
deal_button.grid(row=6, column= 16 )
show_button = Button(root, text='Update board', command=updateCommCards)
show_button.grid(row=6, column= 18 )


root.mainloop()





