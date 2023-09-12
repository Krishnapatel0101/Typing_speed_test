from tkinter import *
import random
# import ttkthemes
from time import sleep
import threading
from email_validator import validate_email, EmailNotValidError
from tkinter import messagebox

totaltime=20
time=0
wrongwords=0
elapsedtimeinminutes=0
a,b=0,0

# function for start timer
def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1,21):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)

# function for calculate wpm,accuracy,time
def count():
    global wrongwords
    while time!=totaltime:
        entered_paragraph=textarea.get(1.0,END).split()
        totalwords=len(entered_paragraph)

    totalwords_count_label.config(text=totalwords)

    para_word_list=label_paragraph['text'].split()

    for pair in list(zip(para_word_list,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1

    wrongwords_count_label.config(text=wrongwords)
    elapsedtimeinminutes=time/60
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes
    accuracy=wpm/gross_wpm*100
    accuracy=round(accuracy)
    with open("accuracy.txt","a") as f:
        f.write(str(accuracy)+"\n")
    with open("wpm.txt","a") as f:
        f.write(str(wpm)+"\n")
    accuracy_percent_label.config(text=str(accuracy)+'%')
    global a,b
    a,b=wpm,accuracy
   

# starting function
def start():
    t1=threading.Thread(target=start_timer)
    t1.start()
    t2 = threading.Thread(target=count)
    t2.start()


# function for reset 
def reset():
    global time,elapsedtimeinminutes,wrongwords
    time=0
    elapsedtimeinminutes=0
    wrongwords=0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    
    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')

# function for display bar graph 
def graph():
    import matplotlib.pyplot as plt
    dict1={}

    with open("accuracy.txt","r") as f1,open("wpm.txt","r") as f2:
        a1=f1.readlines()
        a2=f2.readlines()
    for i,j in zip(a1,a2):
        dict1[int(i[:-1])]=float(j[:-1])
    sorted_mydict = dict(sorted(dict1.items(), key=lambda item: item[0]))

    accuracy=list(dict1.keys())
    wpm=list(dict1.values())
    plt.xlabel("wpm")
    plt.ylabel("accuracy")
    plt.bar(wpm,accuracy)
    plt.show()

# function for check email and send mail
def email():
    email= Tk()
    email.geometry("500x200")
    email.config(bg="")
    label=Label(email, text="Enter your email id", font=("Courier 22 bold"))
    label.pack()
    entry= Entry(email, width= 40)
    entry.focus_set()
    entry.pack()

# function for check email
    def check():
        email = entry.get()
        try:
            v = validate_email(email)
            email = v["email"] 
            work_done()
        except EmailNotValidError as e:
            messagebox.showerror("Invalid",e)

# function for sending mail for valid mail
    def work_done():
        import smtplib
        from email.mime.text import MIMEText
        def SendEmail(Email, subject, msgstr):
            print("Emailing")
            msg = MIMEText(msgstr)
            msg['Subject'] = subject
            msg['From'] = "pythonemailtestservice@gmail.com"
            msg['To'] = Email
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("pythonemailtestservice@gmail.com", "tzleaaknhfstkngz")
            s.sendmail("pythonemailtestservice@gmail.com", Email, msg.as_string())
            s.quit()
            print("Done Email")
            return
        SendEmail(entry.get(),"Your Score for the Typing speed test","words per minutes:"+str(a)+"\n"+"accuracy:"+str(b))
        email.destroy()
    Button(email, text= "Okay",width= 20,command=check).pack(pady=20)
    email.mainloop()




# GUI part
root=Tk()
root.geometry('980x450')
root.resizable(0,0)

mainframe=Frame(root,bd=4)
mainframe.grid()

titleframe=Frame(mainframe,bg='orange')
titleframe.grid()

titleLabel=Label(titleframe,text='Typing Speed Test',font=('algerian',28,'bold'),bg='goldenrod3',fg='white',width=38,bd=10)
titleLabel.grid(pady=5)

paragraph_frame=Frame(mainframe)
paragraph_frame.grid(row=1,column=0)

paragraph_list=["The wind howled through the empty streets, carrying with it the scent of rain and the promise of a storm. Leaves rustled and danced in the gusts, swirling around like frenzied dancers. Somewhere in the distance, a dog barked, its voice echoing through the night.","She ran her fingers over the rough texture of the bark, feeling the bumps and grooves of the tree's skin. The leaves above rustled softly, whispering secrets to each other in the gentle breeze. She closed her eyes and breathed in the scent of nature, feeling at peace.","The coffee shop was bustling with activity, the air thick with the aroma of freshly brewed coffee. People chatted and laughed, their voices blending together into a comforting hum. The baristas worked tirelessly behind the counter, expertly crafting drinks and taking orders with ease.","The waves crashed against the shore, their relentless force sending spray flying into the air. The sand beneath her feet shifted and swirled, moving with the rhythm of the sea. She stood there, feeling small and insignificant in the face of such power.","The city was alive with energy, the streets filled with people rushing to and fro. Cars honked and screeched, their drivers jostling for position on the crowded roads. Amidst the chaos, a lone street musician played his guitar, his music a peaceful oasis in the midst of the storm."]

random.shuffle(paragraph_list)

label_paragraph=Label(paragraph_frame,text=paragraph_list[0],wraplength=912,justify=LEFT,font=('arial',14,'bold'))
label_paragraph.grid(row=0,column=0)

textarea_frame=Frame(mainframe)
textarea_frame.grid(row=2,column=0)

textarea=Text(textarea_frame,font=('arial',12,'bold'),width=100,height=7,bd=4,wrap='word'
              ,state=DISABLED)
textarea.grid()

frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text='20',font=('Tahoma',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)

wpm_label=Label(frame_output,text='WPM',font=('Tahoma',12,'bold'),fg='red')
wpm_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wpm_count_label.grid(row=0,column=5,padx=5)

totalwords_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='red')
totalwords_label.grid(row=0,column=6,padx=5)

totalwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
totalwords_count_label.grid(row=0,column=7,padx=5)

wrongwords_label=Label(frame_output,text='Wrong Words',font=('Tahoma',12,'bold'),fg='red')
wrongwords_label.grid(row=0,column=8,padx=5)

wrongwords_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
wrongwords_count_label.grid(row=0,column=9,padx=5)

accuracy_label=Label(frame_output,text='Accuracy',font=('Tahoma',12,'bold'),fg='red')
accuracy_label.grid(row=0,column=10,padx=5)

accuracy_percent_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'))
accuracy_percent_label.grid(row=0,column=11,padx=5)

buttons_Frame=Frame(mainframe)
buttons_Frame.grid(row=4,column=0)

startButton=Button(buttons_Frame,text='Start',command=start)
startButton.grid(row=0,column=0,padx=10)

resetButton=Button(buttons_Frame,text='Reset',state=DISABLED,command=reset)
resetButton.grid(row=0,column=1,padx=10)

exitButton=Button(buttons_Frame,text='Exit',command=root.destroy)
exitButton.grid(row=0,column=2,padx=10)

graph=Button(buttons_Frame,text='Analysis',command=graph)
graph.grid(row=0,column=3,padx=10)

email=Button(buttons_Frame,text='Email your score',command=email)
email.grid(row=0,column=4,padx=10)
root.mainloop()