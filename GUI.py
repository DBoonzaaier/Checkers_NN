import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from CheckersV4 import Checkers
import math
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.board = Canvas(self)

        self.click1 = 0
        self.click2 = 0
        self.jump_coords = [0, 0]
        self.move_no = 1                                # A check that goes with the one below.  If on a move greater than 1 do the check below.
        self.pre_move = 0                               # A check to see whether the next move is correct if there are multiple jumps.

        self.board_index_from = 0
        self.board_index_to = 0

        self.indexDictionary = {}
        self.setup_Dictionary()

        self.playableSquares = []
        self.pieces = []
        self.play_as = ""
        self.play_against = ""

        self.mesText = StringVar()
        self.mesBox = Label(self)

        self.errorText = StringVar()
        self.errorBox = Label(self)

        self.status = Listbox(self, height=25)               # Status box
        self.status_scroll = ttk.Scrollbar(self, orient=VERTICAL, command=self.status.yview)
        self.status['yscrollcommand'] = self.status_scroll.set
        self.status_index = 0

        Label(self, text="Play as White or Red?", font=("Times New Roman", 30)).grid(row=0, column=0, pady=(150, 20), padx=(110, 1), columnspan=3)

        self.white = tk.Button(self, text="White", font=("Times New Roman", 16), command=self.white_click)
        self.origi_color = self.white.cget("background")
        self.white.grid(row=1, column=0, padx=(115, 1), pady=20, ipadx=10, ipady=5)

        self.red = tk.Button(self, text="Red", font=("Times New Roman", 16), command=self.red_click)
        self.red.grid(row=1, column=2, padx=(1, 20), ipadx=20, ipady=5)

        self.start = tk.Button(self, text="Start", font=("Times New Roman", 16), command=self.say_hi)
        self.start.grid(row=2, column=1, pady=10, ipadx=20, ipady=5)

        self.quit = tk.Button(self, text="QUIT", font=("Times New Roman", 16), command=self.exit_game)
        self.quit.grid(row=3, column=1, pady=5, ipadx=15, ipady=5)

    def say_hi(self):
        gameBrain.set_gui_player(self.play_as)              # Sets the player in the Checkers Class.

        for element in self.grid_slaves():
            if element.grid_info()["row"] != 3:
                element.grid_forget()
        self.quit.grid(column=0, columnspan=5)

        self.mesBox.grid(row=0, column=0, columnspan=5)
        self.mesText.set(self.play_as+"'s Turn.")           # Text for top of GUI.
        self.mesBox.config(padx=20, pady=20, font=("Times New Roman", 20), text=self.mesText.get())

        self.errorBox.grid(row=2, column=0, columnspan=5)
        self.errorText.set("Go For IT !!")                  # Text for bottom of GUI.
        self.errorBox.config(padx=20, pady=10, font=("Times New Roman", 14), text=self.errorText.get())

        self.status.grid(row=1, column=4, rowspan=1, padx=(5,1), sticky=(N,W,E,S))
        self.status_scroll.grid(row=1, column=5, rowspan=1, sticky=(N,W,E,S))

        self.board.config(width=420, height=420, bg="white")
        self.board.grid(row=1, column=0, columnspan=3)
        self.board.bind("<Button-1>", self.mouse_click)

        #self.board.create_text(50, 50, text=self.play_as)
        self.createBoard()
        self.setPieces()

    def mouse_click(self, event):
        self.errorText.set("You Can Do IT!!")
        self.errorBox.config(text=self.errorText.get())
        #print("clicked", event.x, event.y, event.widget.find_overlapping(event.x, event.y, event.x, event.y),"\n")

        if self.click1 == 0 and self.click2 == 0:
            self.click1 = event.widget.find_overlapping(event.x, event.y, event.x, event.y)
            self.board_index_from = self.click1[0]                       # move piece from this board index.
            if len(self.click1) == 2:
                self.click1 = self.click1[1]
            else:
                self.click1 = self.click1[0]
            self.jump_coords[0] += event.x
            self.jump_coords[1] += event.y
        elif self.click1 != 0 and self.click2 == 0:
            self.click2 = event.widget.find_overlapping(event.x, event.y, event.x, event.y)
            self.board_index_to = self.click2[0]                         # to this board index.
            if len(self.click2) == 2:
                self.click2 = self.click2[1]
            else:
                self.click2 = self.click2[0]
            self.jump_coords[0] += event.x
            self.jump_coords[1] += event.y

            self.jump_coords[0] //= 2
            self.jump_coords[1] //= 2

            #print("from", self.click1, "to", self.click2)
            coordsToMove = self.board.coords(self.click2)
            #print("click 2 from coords", self.click2, "\n")

            coordsToMove[0] += 5
            coordsToMove[1] += 5
            coordsToMove[2] -= 5
            coordsToMove[3] -= 5

            #print("board index to", self.board_index_to, "click 1", self.click1, "click 2", self.click2)
            if self.click1 > 65 and self.click2 <= 65:
                more_jumps = True
                while more_jumps:
                    #print("more_jumps =", more_jumps)
                    try:
                        brainMove = [self.indexDictionary[self.board_index_from], self.indexDictionary[self.board_index_to]]
                        if self.play_as == "White":
                            acceptance, more_jumps = gameBrain.gui_check(self.status_index+1, brainMove)
                        else:
                            acceptance, more_jumps = gameBrain.gui_check(self.status_index, brainMove)
                        #print("acceptance =", acceptance, "more_jumps =", more_jumps)
                    except KeyError:
                        self.errorText.set("Move Impossible.")
                        self.errorBox.config(text=self.errorText.get())
                        break

                    if acceptance:
                        self.mesText.set(self.play_against+"'s Turn.")           # Text for top of GUI.
                        self.mesBox.config(text=self.mesText.get())

                        piece_to_take = math.fabs(self.indexDictionary[self.board_index_from] - self.indexDictionary[self.board_index_to]) > 6
                        more_jumps = more_jumps and piece_to_take               # Determines if there is a jump and whether the previous move was also a jump.

                        #print("move no.", self.move_no, "\nclick 1.", self.click1, "\nprev move", self.pre_move)
                        if self.move_no < 2:
                            self.move_no += 1
                            self.pre_move = self.click1                             # For jumping checks.
                            self.board.coords(self.click1, coordsToMove)            # Move piece from one place to another.
                            if (3 <= self.click2 <= 9) and self.play_as == "White":
                                self.board.itemconfigure(self.click1, width=5, outline="red")           # Turn piece into King.
                            elif (58 <= self.click2 <= 64) and self.play_as == "Red":
                               self.board.itemconfigure(self.click1, width=5, outline="white")           # Turn piece into King.
                        else:
                            if self.click1 == self.pre_move:
                                self.board.coords(self.click1, coordsToMove)            # Move piece from one place to another.
                                if (3 <= self.click2 <= 9) and self.play_as == "White":
                                    self.board.itemconfigure(self.click1, width=5, outline="red")       # Turn piece into King.
                                elif (58 <= self.click2 <= 64) and self.play_as == "Red":
                                    self.board.itemconfigure(self.click1, width=5, outline="white")           # Turn piece into King.
                            else:
                                self.errorText.set("Move Impossible. Complete Jump Path.")
                                self.errorBox.config(text=self.errorText.get())
                                break

                        if piece_to_take:
                            remove_piece = self.board.find_overlapping(self.jump_coords[0], self.jump_coords[1], self.jump_coords[0], self.jump_coords[1])[1]
                            self.board.delete(remove_piece)
                            to_ins = str(self.status_index+1) + " - J - " + str(self.indexDictionary[self.board_index_from]) + " to " + str(self.indexDictionary[self.board_index_to]) + " - " + self.play_as
                            self.status.insert(END, to_ins)
                        else:
                            to_ins = str(self.status_index+1) + " - " + str(self.indexDictionary[self.board_index_from]) + " to " + str(self.indexDictionary[self.board_index_to]) + " - " + self.play_as
                            self.status.insert(END, to_ins)

                        if not more_jumps:
                            self.status_index += 1
                        else:
                            self.move_no += 1
                        self.board.update()
                        #print("move from", self.board_index_from, self.indexDictionary[self.board_index_from], "to", self.board_index_to, self.indexDictionary[self.board_index_to])
                    else:
                        if self.move_no > 3:
                            self.errorText.set("Move Impossible.")
                            self.errorBox.config(text=self.errorText.get())
                        elif not more_jumps:
                            if self.move_no == 1:
                                self.errorText.set("Move Impossible.")
                                self.errorBox.config(text=self.errorText.get())
                            elif self.move_no == 3:
                                self.move_no += 1
                            break
                        self.errorText.set("Move Impossible.")
                        self.errorBox.config(text=self.errorText.get())

                    self.exit_game_result()             # Check for end of game.

                    # Opponant  neural network plays. ##################################################################
                    if acceptance and ((self.status_index+1) % 2 == 0):
                        self.move_no = 1
                        if self.play_as == "White":
                            opponants_move = gameBrain.gui_check(self.status_index+1, "NULL")
                        else:
                            opponants_move = gameBrain.gui_check(self.status_index, "NULL")

                        self.exit_game_no_move(opponants_move)

                        if type(opponants_move[0]) != list:
                            opp_move_idex1 = self.key_from_Dict(opponants_move[0])      # Index (Item specifier) of square on GUI for NN given move index.
                            opp_move_idex2 = self.key_from_Dict(opponants_move[1])      # Index (Item specifier) of square on GUI for NN given move index.

                            coords_mi1 = self.board.coords(opp_move_idex1)              # Coords of square for corresponding idex.
                            coords_mi2 = self.board.coords(opp_move_idex2)              # Coords of square for corresponding idex.

                            cmi1_x1, cmi1_y1, cmi1_x2, cmi1_y2 = coords_mi1             # Coords for piece to move.
                            cmi2_x1, cmi2_y1, cmi2_x2, cmi2_y2 = coords_mi2             # Coords to move piece to.

                            # Obtaining the Item specifier for the piece to move.
                            opp_piece = self.board.find_overlapping(cmi1_x1+10, cmi1_y1+10, cmi1_x2-10, cmi1_y2-10)[1]
                            self.board.coords(opp_piece, [cmi2_x1+5, cmi2_y1+5, cmi2_x2-5, cmi2_y2-5])
                            if (58 <= opp_move_idex2 <= 64) and self.play_as == "White":
                                self.board.itemconfigure(opp_piece, width=5, outline="white")           # Turn piece into King.
                            elif (3 <= self.click2 <= 9) and self.play_as == "Red":
                               self.board.itemconfigure(self.click1, width=5, outline="red")           # Turn piece into King.

                            to_ins = str(self.status_index+1) + " - " + str(opponants_move[0]) + " to " + str(opponants_move[1]) + " - " + self.play_against
                            self.status.insert(END, to_ins)
                            self.status_index += 1
                            self.mesText.set(self.play_as+"'s Turn.")           # Text for top of GUI.
                            self.mesBox.config(text=self.mesText.get())
                        else:
                            for jump in opponants_move:
                                opp_move_idex1 = self.key_from_Dict(jump[0])      # Index (Item specifier) of square on GUI for NN given move index.
                                opp_move_idex2 = self.key_from_Dict(jump[1])      # Index (Item specifier) of square on GUI for NN given move index.

                                coords_mi1 = self.board.coords(opp_move_idex1)              # Coords of square for corresponding idex.
                                coords_mi2 = self.board.coords(opp_move_idex2)              # Coords of square for corresponding idex.

                                cmi1_x1, cmi1_y1, cmi1_x2, cmi1_y2 = coords_mi1             # Coords for piece to move.
                                cmi2_x1, cmi2_y1, cmi2_x2, cmi2_y2 = coords_mi2             # Coords to move piece to.

                                opp_piece = self.board.find_overlapping(cmi1_x1+10, cmi1_y1+10, cmi1_x2-10, cmi1_y2-10)[1]
                                self.board.coords(opp_piece, [cmi2_x1+5, cmi2_y1+5, cmi2_x2-5, cmi2_y2-5])
                                if (58 <= opp_move_idex2 <= 64) and self.play_as == "White":
                                    self.board.itemconfigure(opp_piece, width=5, outline="white")           # Turn piece into King.
                                elif (3 <= opp_move_idex2 <= 9) and self.play_as == "Red":
                                    self.board.itemconfigure(opp_piece, width=5, outline="red")             # Turn piece into King.

                                # Coordinates to find the piece to be taken.
                                oj_coords = [(cmi1_x1 + cmi2_x1)//2, (cmi1_y1 + cmi2_y1)//2, (cmi1_x2 + cmi2_x2)//2, (cmi1_y2 + cmi2_y2)//2]
                                # Item specifier for piece to be taken.
                                remove_piece_opp = self.board.find_overlapping(oj_coords[0]+20, oj_coords[1]+20, oj_coords[2]-20, oj_coords[3]-20)[1]
                                self.board.delete(remove_piece_opp)

                                to_ins = str(self.status_index+1) + " - J - " + str(jump[0]) + " to " + str(jump[1]) + " - " + self.play_against
                                self.status.insert(END, to_ins)
                                self.mesText.set(self.play_as+"'s Turn.")           # Text for top of GUI.
                                self.mesBox.config(text=self.mesText.get())
                                self.board.update()
                                time.sleep(1)                                       # Delay the taking of the next piece so the player can see what is happening.
                            self.status_index += 1

                    if self.play_as == "White":
                        no_move_check = gameBrain.gui_check(self.status_index+1, "NULL")
                    else:
                        no_move_check = gameBrain.gui_check(self.status_index, "NULL")
                    self.exit_game_no_move(no_move_check)                           # Check for end of game due to no further available moves.
                    self.exit_game_result()                                         # Check for end of game.
            else:
                self.errorText.set("Move Impossible.")
                self.errorBox.config(text=self.errorText.get())

            self.click1 = 0
            self.click2 = 0
            self.board_index_from = 0
            self.board_index_to = 0
            self.jump_coords[0], self.jump_coords[1] = [0, 0]

            #print("Ending Click Move\n")

    def exit_game_result(self):
        victory = gameBrain.gui_Victory_Check(self.status_index)
        if victory == 'w':
            if self.play_as == "White":
                messagebox.showinfo("VICTORY !!", "CONGRATULATIONS, YOU WIN !!!")
            else:
                messagebox.showinfo("OOPS", "SORRY, YOU LOSE.")
        elif victory == 'b':
            if self.play_as == "Red":
                messagebox.showinfo("VICTORY !!", "CONGRATULATIONS, YOU WIN !!!")
            else:
                messagebox.showinfo("OOPS", "SORRY, YOU LOSE.")
        elif victory == 'd':
            messagebox.showinfo("DRAW", "THE GAME ENDS IN A DRAW. 100 TURNS HAVE BEEN MADE.")

        if victory:
            sys.exit()

    # If there are no further moves to make with pieces still on the board then display winner and exit.
    def exit_game_no_move(self, vic):
        if vic == 'b':
            if self.play_as == "Red":
                messagebox.showinfo("VICTORY !!", "CONGRATULATIONS, YOU WIN !!!  No more moves available.")
            elif self.play_as == "White":
                messagebox.showinfo("OOPS", "SORRY, YOU LOSE.  No more moves available.")
            sys.exit()
        elif vic == 'w':
            if self.play_as == "White":
                messagebox.showinfo("VICTORY !!", "CONGRATULATIONS, YOU WIN !!!  No more moves available.")
            elif self.play_as == "Red":
                messagebox.showinfo("OOPS", "SORRY, YOU LOSE.  No more moves available.")
            sys.exit()

    def exit_game(self):
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            root.destroy()

    def white_click(self):
        self.white.config(bg="yellow", relief="sunken")
        self.red.config(bg=self.origi_color, relief="raised")
        self.play_as = "White"
        self.play_against = "Red"

    def red_click(self):
        self.red.config(bg="yellow", relief="sunken")
        self.white.config(bg=self.origi_color, relief="raised")
        self.play_as = "Red"
        self.play_against = "White"

    def createBoard(self):
        self.board.create_rectangle(10, 10, 410, 410)
        b = 10
        d = 60
        for i in range(8):
            a = 10
            c = 60
            for j in range(8):
                if (i+j)%2 == 1:
                    usablesquare = self.board.create_rectangle(a, b, c, d, fill="black")
                    self.playableSquares.append(usablesquare)
                else:
                    self.board.create_rectangle(a, b, c, d, fill="#FFB05F")
                a += 50
                c += 50
            b += 50
            d += 50

    def setPieces(self):
        # Red Pieces
        b = 15
        d = 55
        for i in range(2):
            a = 65
            c = 105
            for j in range(4):
                self.board.create_oval(a, b, c, d, fill="#D50000")
                a += 100
                c += 100
            b += 100
            d += 100

        a = 15
        b = 65
        c = 55
        d = 105
        for i in range(4):
            self.board.create_oval(a, b, c, d, fill="#D50000")
            a += 100
            c += 100

        # White Pieces
        b = 265
        d = 305
        for i in range(2):
            a = 15
            c = 55
            for j in range(4):
                self.board.create_oval(a, b, c, d, fill="#F1F1F1")
                a += 100
                c += 100
            b += 100
            d += 100

        a = 65
        b = 315
        c = 105
        d = 355
        for i in range(4):
            self.board.create_oval(a, b, c, d, fill="#F1F1F1")
            a += 100
            c += 100

    def setup_Dictionary(self):
        self.indexDictionary = {}
        num1 = 58
        num2 = 0
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1
        num1 = 51
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1
        num1 = 42
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1
        num1 = 35
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1
        num1 = 26
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1
        num1 = 19
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1
        num1 = 10
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1
        num1 = 3
        for i in range(4):
            self.indexDictionary[num1] = num2
            num1 += 2
            num2 += 1

    def key_from_Dict(self, v):
        for key, value in self.indexDictionary.items():
            if v == value:
                return key


root = tk.Tk()
root.wm_title("Checkers Game")
root.geometry("575x620")

gameBrain = Checkers(True)

app = Application(master=root)
app.mainloop()
