# tic tac toe

import tkinter as tk
from tkinter import ttk
from functools import partial
x='X'
def game():
   global x
   def reset():
      win.destroy()
      game()
   def end():
      b2=ttk.Button(win,text='Reset',command=reset)
      b2.grid(row=10,column=0)
   def check(x):
      q=1
      #print(f" if(({l[0][0]}=={l[0][1]}and {l[0][1]}=={l[0][2]}) or ({l[2][0]}=={l[2][1]}and {l[2][1]}=={l[2][2]}) or ({l[1][0]}=={l[1][1]}and {l[1][1]}=={l[1][2]})):")
      if((l[0][0]==l[0][1]and l[0][1]==l[0][2]) or (l[2][0]==l[2][1]and l[2][1]==l[2][2]) or (l[1][0]==l[1][1]and l[1][1]==l[1][2])):
         q=x
      elif((l[0][0]==l[1][0] and l[1][0]==l[2][0]) or (l[0][1]==l[1][1] and l[1][1]==l[2][1]) or (l[0][2]==l[1][2] and l[1][2]==l[2][2]) ):
         q=x
      elif((l[0][0]==l[1][1] and l[1][1]==l[2][2]) or (l[0][2]==l[1][1] and l[1][1]==l[2][0])):
         q=x
      if(q=='X'):
         tk.Label(win,text='Player 1 wins').grid(row=5,column=0)
      elif(q=='O'):
         tk.Label(win,text='Player 2 wins').grid(row=5,column=0)
      a=[]
      for i in l:
         for j in i:
            j=str(j)
            a.append(j.isdigit())
      if(not(any(a)) and q==1):

         tk.Label(win,text='Draw').grid(row=5,column=0)

   
   # hey
   def a1(i,j): 
      global x
      a=tk.Label(win,text=(f"    {x}   "),width=10)
      a.grid(row=i,column=j)
      l[i-1][j]=x
      check(x)
      if(x=='X'):
         a.configure(background='yellow',foreground='blue')
         x='O'
         end()
      elif(x=='O'):
         a.configure(background='blue',foreground='yellow')
         x='X'
         end()

   
   win=tk.Tk()
   win.title('Tic - Tac - Toe')
   ttk.Label(win,text=f"Rules :\n 1. This is a two player game.\n 2. Player one plays with 'X' player two gets 'O'.\n ").grid(row=0,columnspan=3)
   x='X'   
   l=[[0,1,2],[3,4,5],[6,7,8]]   
   b1=tk.Button(win,text=' ',width=10,command=partial(a1,1,0))
   b1.grid(row=1,column=0)
   b2=tk.Button(win,text=' ',width=10,command=partial(a1,1,1))
   b2.grid(row=1,column=1)
   b3=tk.Button(win,text=' ',width=10,command=partial(a1,1,2))
   b3.grid(row=1,column=2)
   b4=tk.Button(win,text=' ',width=10,command=partial(a1,2,0))
   b4.grid(row=2,column=0)
   b5=tk.Button(win,text=' ',width=10,command=partial(a1,2,1))
   b5.grid(row=2,column=1)
   b6=tk.Button(win,text=' ',width=10,command=partial(a1,2,2))
   b6.grid(row=2,column=2)
   b7=tk.Button(win,text=' ',width=10,command=partial(a1,3,0))
   b7.grid(row=3,column=0)
   b8=tk.Button(win,text=' ',width=10,command=partial(a1,3,1))
   b8.grid(row=3,column=1)
   b9=tk.Button(win,text=' ',width=10,command=partial(a1,3,2))
   b9.grid(row=3,column=2)

   tk.Label(win,text=" ").grid(row=4,column=0)
   win.mainloop()

game()