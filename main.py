from tkinter import *

expression = ""

def press(num):
  global expression
  expression = expression + str(num)
  equation.set(expression)
  
  def equalpress():
   try:
      global expression
      total = str(eval(expression))
      equation.set(total)
      expression = ""
    except:
      equation.set(" error ")
      expression = ""
      
      def clear():
        global expression
        expression = ""
        equation.set("")
        
if __name__ == "__main__":
  gui = Tk()
  gui.configure(background = "light green")
  gui.title("Simple calculator")
  gui.geometry("270x150")
  equation = StringVar()
  expression_field = Entry(gui, textvariable=equation)
  expression_field.grid(columnspan=4, ipadx=70)
  
  button1 = Button(gui, text='1', fg)
  
      
      
      
      
      
    gui.mainloop()
      
