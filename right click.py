import tkinter as tk

def cut_text() :
    print('Text cut ')
root = tk.Tk()
root.title('Right Click Menu')
root.geometry('400(x)300')

popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="Cut", command=cut_text)
popup_menu.add_command(label="Copy")
popup_menu.add_command(label="Paste")

def show_popup(event):
      popup_menu.tk_popup(event.x_root, event.y_root)
                    
   finally:
    popup_menu.grab_release()
root.bind("<Button-3>", show_popup)
root.mainloop()