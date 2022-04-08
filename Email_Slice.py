import tkinter as tk
window = tk.Tk()
window.geometry("480x440")
window.config(bg="#777777")
window.resizable(width=False,height=False)
window.title('Simple Email Slicer')
 
def result():
    try:
        email=entry.get()
        inp_email = email.strip()
        username = inp_email[0:inp_email.index('@')]
        domain = inp_email[inp_email.index('@') + 1:]
        text_box.delete('1.0', tk.END)
        msg = 'Email Entered: {}\nYour email username: {}\nAnd your email domain server is {}'
        msg_formatted = msg.format(email,username,domain)
        text_box.insert(tk.END,msg_formatted)
        entry.delete(0, 'end')
    except:
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END,"ERROR!\nPlease Enter Valid Email\nFormat 'example@domain.com'")
 
def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')
 
# Labels
greeting = tk.Label(text="We'll Slice Email for You",font=(12),foreground="black",background="#777777")
entry_label = tk.Label(foreground= "black",background="#777777",font=(10),text="Enter the Email: ")
result_label = tk.Label(font=(10),foreground= "black",background="#777777",text="The results are as follows:")
empty_label0=tk.Label(background="#BE361A")
empty_label1=tk.Label(background="#BE361A") 
empty_label2=tk.Label(background="#BE361A")
empty_label3=tk.Label(background="#BE361A")
empty_label4=tk.Label(background="#BE361A")
empty_label5=tk.Label(background="#BE361A")
 
#Entry
e1=tk.StringVar()
entry = tk.Entry(font=(11),width=40,justify='center',textvariable=e1)
 
#Buttons
button = tk.Button(text="Done!",command=result,font=(11))
reset=tk.Button(text="Reset!",command=reset_all,font=(11))
 
#Result
text_box = tk.Text(height=5,width=50)
 
#Packing Everything Together
empty_label0.pack()
greeting.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()
text_box.pack()
 
window.mainloop()