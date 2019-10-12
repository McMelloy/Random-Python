import tkinter
import random


number = random.randint(0,100)
count = 0


def make_guess(event):
    global count
    guess = int(txt_guess.get())
    count+=1
    txt_guess.delete(0, "end")
    if guess < number:
        lbl_result["text"]="Number is bigger"
    elif guess > number:
        lbl_result["text"] = "Number is smaller"
    else:
        lbl_result["text"] = "Yay! You made "+str(count)+" tries"


def new_game():
    global number, count
    number = random.randint(0, 100)
    count = 0
    lbl_result["text"] = "New game"


root = tkinter.Tk()
root.wm_title("Guess game")

lbl_title = tkinter.Label(root, text = "The Guessing Game by Duke of Burritoshire")
lbl_title.grid(row=0, columnspan=2, padx =5)

lbl_result = tkinter.Label(root, text = "Good luck!")
lbl_result.grid(row=1, columnspan=2)

txt_guess = tkinter.Entry(width=10)
txt_guess.bind('<Return>', make_guess)
txt_guess.grid(row=2, columnspan=2)

btn_reset = tkinter.Button(root, text = "Reset", fg = "red", command=new_game)
btn_reset.grid(row=3, columnspan=2)


root.mainloop()
