from tkinter import *
import pygame
from random import *
import os
from tkinter import messagebox
import pyttsx3

def signup():
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Text, messagebox, Button, PhotoImage, StringVar
    import mysql.connector as mysql
    s=os.getcwd()+r'\\frame1\\'
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(s)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()

    window.geometry("890x650")
    window.configure(bg="#F4D6CC")


    mydb = mysql.connect(host="localhost", user="root", password="mysql123", database="codefusion")
    mycursor = mydb.cursor()
    name_var = StringVar()
    email_var = StringVar()
    passw_var = StringVar()
    def submit():
        name = name_var.get()
        passw = passw_var.get()
        email = email_var.get()
        mycursor = mydb.cursor()

        class user:
            def __init__(self, username, email, password):
                self.username = username
                self.password = password
                self.email = email

            def store(self):
                a = (self.username, self.email, self.password)
                query = "insert into learnquest values(%s,%s,%s)"
                mycursor.execute(query, a)
                mydb.commit()

            def check(self):
                exists = False
                mycursor.execute("select * from learnquest")
                a = mycursor.fetchall()
                for x in a:
                    if self.username.lower() in x[0] or self.username == '' or self.email.lower() in x[0]:
                        exists = True
                return exists

        tba_user = user(name.lower(), email, passw)
        if tba_user.check():
            messagebox.showwarning("SIGN UP ERROR", "user already exists / fill out the form")
        else:
            tba_user.store()
            messagebox.showinfo("SIGN IN", "SIGN UP SUCCESSFUL. Please sign in again.")
            window.destroy()
            signin()

    def existing():
        window.destroy()
        signin()


    canvas = Canvas(window,bg="#F4D6CC",height=650,width=890,bd=0,highlightthickness=0,relief="ridge")

    canvas.place(x=0, y=0)
    canvas.create_text(260,94,anchor="nw",text="Create an account",fill="black",font=("Poppins Regular", 40 * -1))

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(449, 274, image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,textvariable=name_var,font=("Poppind Regular", 12, "bold"))
    entry_1.place(x=216, y=244, width=466, height=58)
    canvas.create_text(216,224,anchor="nw",text="Name",fill="black",font=("Poppins Regular", 16 * -1))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(449.0, 386.0, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, textvariable=email_var, font=("Poppind Regular", 12, "bold"))
    entry_2.place(x=216, y=356, width=466, height=58)

    canvas.create_text(216.0,336.0,anchor="nw",text="Email",fill="black",font=("Poppins Regular", 16 * -1))

    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(449.0, 504.0, image=entry_image_3)
    entry_3 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,textvariable=passw_var,show="*",font=("Poppind Regular", 12, "bold"))
    entry_3.place(x=216, y=474, width=466, height=58)

    canvas.create_text(216.0,454.0,anchor="nw",text="Password",fill="black",font=("Poppins Regular", 16 * -1))

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=submit,relief="flat")
    button_1.place(x=510.0, y=578.0, width=172.18182373046875, height=43.085723876953125)



    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=existing,relief="flat")
    button_3.place(x=216, y=544, width=168, height=24)
    canvas.create_rectangle(221, 250, 675, 298, fill="#F4D6CC", outline="")
    canvas.create_rectangle(221, 362, 675, 410, fill="#F4D6CC", outline="")
    canvas.create_rectangle(221, 480, 675, 528, fill="#F4D6CC", outline="")
    window.resizable(False, False)
    window.mainloop()

def signin():
    from pathlib import Path
    import os
    from tkinter import Tk, Canvas, Entry, Text, messagebox, StringVar, Button, PhotoImage

    s=os.getcwd()+'/frame0/'
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(s)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()
    window.geometry("890x650")
    window.configure(bg = "#F4D6CC")
    import mysql.connector as mysql
    mydb = mysql.connect(
        host="localhost", user="root", password="mysql123", database="codefusion")
    mycursor = mydb.cursor()
    email_var = StringVar()
    passw_var = StringVar()
    def submit():
        email = email_var.get()
        passw = passw_var.get()
        mycursor = mydb.cursor()
        query = "SELECT * FROM learnquest WHERE email = %s"
        mycursor.execute(query, (email.lower(),))
        rows = mycursor.fetchall()
        if len(rows) == 0:
            messagebox.showerror("Error!", "Incorrect Email")
        for row in rows:
            if passw == row[2]:
                messagebox.showinfo("Success!", "Logged in successfully!")
                os.environ["USERNAME"] = row[0]
                try:
                    window.destroy()
                except:
                    pass
                programrunner()
            else:
                messagebox.showerror("Error!", "Incorrect Password!")
    def create():
        try:
            window.destroy()
            signup()
        except:
            pass
    canvas = Canvas(window,bg = "#F4D6CC",height = 650,width = 890,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_text(218.0,150.0,anchor="nw",text="Sign In to your account",fill="black",font=("Poppins Regular", 40 * -1))
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(457.0,308.0,image=entry_image_1)
    entry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=("Poppins Regular", 12, "bold"),textvariable=email_var)
    entry_1.place(x=224.0,y=278.0,width=466.0,height=58.0)
    canvas.create_text(224.0,255.0,anchor="nw",text="Email",fill="black",font=("Poppins Regular", 16 * -1))
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(457.0,417.0,image=entry_image_2)
    entry_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0,font=("Poppins Regular", 12, "bold"),textvariable=passw_var,show='*')
    entry_2.place(x=224.0,y=388.0,width=466.0,height=56.0)
    canvas.create_text(224.0,366.0,anchor="nw",text="Password",fill="black",font=("Poppins Regular", 16 * -1))
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=create,relief="flat")
    button_1.place(x=224,y=473,width=168,height=24)
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=submit,relief="flat")
    button_2.place(x=316,y=524,width=268,height=43)
    canvas.create_rectangle(229,284,683,332,fill="#F4D6CC",outline="")
    canvas.create_rectangle(229,393,683,441,fill="#F4D6CC",outline="")
    window.resizable(False, False)
    window.mainloop()

secs = 0
runn = False

def programrunner():
    root=Tk()
    def analysistt():
        try:
            pygame.mixer.music.stop()
        except:
            pass
        import matplotlib.pyplot as plt
        import tkinter as tk
        from tkinter import scrolledtext,ttk,messagebox
        import numpy as np
        from pathlib import Path
        analysertt=tk.Toplevel(root)
        analysertt.wm_attributes("-topmost",True)
        analysertt.title("Graph Your Grades")
        analysertt.geometry("500x500")
        analysertt.config(bg='#ffffb7')
        l=[]
        n=[]
        m=[]
        q=[]
        e=[]
        r=[]

        def on_enter(event):
                nextexambut.config(bg='#BFBFFF')

        def on_leave(event):
                nextexambut.config(bg='white')

        def on_enter2(event):
                genbut.config(bg='#BFBFFF')

        def on_leave2(event):
                genbut.config(bg='white')

        def next():
            if combo.get().isalnum() and len(combo.get())!=0:
                l.append(combo.get())
                combo.delete(0, tk.END)
                n.append(quant_ent.get())
                m.append(quant_ent2.get())
                q.append(quant_ent3.get())
                e.append(quant_ent4.get())
                r.append(quant_ent5.get())
            else:
                z=messagebox.showerror("Invalid!","Enter a valid exam name or\nchoose from the Dropdown.")
                z.wm_attributes("-topmost",True)
        def on_select(event):
            selected_value.set(combo.get())
        def kk() :
            from prettytable import PrettyTable
            from tkinter import filedialog
            var7 = PrettyTable()
            from pathlib import Path
            import tkinter
            from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
            import random
            kkkk = tkinter.Toplevel()
            kkkk.wm_attributes("-topmost",True)
            def max1(x):
                l = ""
                c = x.count(x[0])
                l = x[0]
                for i in x:
                    k = 0
                    for j in x:
                        if i == j:
                            k += 1
                    if k >= c:
                        c = k
                        l = i
                return l

            def se(x1, x3, y1=1):
                x2 = x1.copy()
                y2 = 0
                while y2 < y1:
                    try:
                        x4 = x2.index(x3)
                        x2.pop(x4)
                    except:
                        x2 = max(x1)
                        global c
                        c = x2
                    y2 += 1
                return x4

            k = "phy"
            k = "chem"
            m = "math"
            y = "phy"
            x = "Eng"
            u = "elective"
            class11 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
            for j in range(1, 7):
                for i in range(6):
                    class11[j].append(None)
            o = [k, y, u, x, m]
            for p in range(1, 7):
                j = 0
                while j < 6:
                    r = random.randint(0, 4)
                    class11[p][j] = o[r]
                    j += 1
                if k not in class11[p] or y not in class11[p] or m not in class11[p] or u not in class11[p] or x not in class11[
                    p]:
                    q = 1
                    while k not in class11[p]:
                        q = 1
                        go = 0
                        a = 0
                        while go < 6:
                            if class11[p][go] == None:
                                class11[p][go] = k
                                a += 1
                                break
                            go += 1
                        if a > 0:
                            break
                        c = max1(class11[p])
                        g = se(class11[p], c, q)
                        class11[p][g] = k
                    while y not in class11[p]:
                        q = 1
                        go = 0
                        a = 0
                        while go < 6:
                            if class11[p][go] == None:
                                class11[p][go] = y
                                a += 1
                                break
                            go += 1
                        if a > 0:
                            break
                        c = max1(class11[p])
                        g = se(class11[p], c, q)
                        class11[p][g] = y
                    while u not in class11[p]:
                        q = 1
                        go = 0
                        a = 0
                        while go < 6:
                            if class11[p][go] == None:
                                class11[p][go] = u
                                a += 1
                                break
                            go += 1
                        if a > 0:
                            break
                        c = max1(class11[p])
                        g = se(class11[p], c, q)
                        class11[p][g] = u
                    while m not in class11[p]:
                        q = 1
                        go = 0
                        a = 0
                        while go < 6:
                            if class11[p][go] == None:
                                class11[p][go] = k
                                a += 1
                                break
                            go += 1
                        if a > 0:
                            break
                        c = max1(class11[p])
                        g = se(class11[p], c, q)
                        class11[p][g] = m
                    while x not in class11[p]:
                        q = 1
                        go = 0
                        a = 0
                        while go < 6:
                            if class11[p][go] == None:
                                class11[p][go] = x
                                a += 1
                                break
                            go += 1
                        if a > 0:
                            break
                        c = max1(class11[p])
                        g = se(class11[p], c, q)
                        class11[p][g] = x
            var7.field_names = ['day', "5 to 7", "7 to 8", "4 to 5", "5 to 6", 'break', '6:30 to 7', '8 to 9']
            var7.add_row(
                ["mon", class11[1][0], class11[1][1], class11[1][2], class11[1][3], 'break', class11[1][4], class11[1][5]])
            var7.add_row(
                ["tue", class11[2][0], class11[2][1], class11[2][2], class11[2][3], 'break', class11[2][4], class11[2][5]])
            var7.add_row(
                ["wed", class11[3][0], class11[3][1], class11[3][2], class11[3][3], 'break', class11[3][4], class11[3][5]])
            var7.add_row(
                ["thurs", class11[4][0], class11[4][1], class11[4][2], class11[4][3], 'break', class11[4][4], class11[4][5]])
            var7.add_row(
                ["fri", class11[5][0], class11[5][1], class11[5][2], class11[5][3], 'break', class11[5][4], class11[5][5]])
            var7.add_row(
                ["sat", class11[6][0], class11[6][1], class11[6][2], class11[6][3], 'break', class11[6][5], class11[6][5]])
            l1 = tkinter.Label(kkkk,text=var7,font=("Calibri",30))
            l1.pack()
            global var8
            var8=str(var7)
            def mhsave(x1=var8):
                file=filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("Text file",".txt")])
                if file is not None:
                    file.write(x1)
                    file.close()
            b1=Button(kkkk,text='save table',command=mhsave)
            b1.pack()
            kkkk.mainloop()

        def gen():
            global tt
            font1 = {'family': 'Serif', 'color': 'blue', 'size': 20}
            font2 = {'family': 'Serif', 'color': 'darkred', 'size': 15}
            plt.title("Mark Analysis", fontdict=font1)
            xpoints = np.array(n)
            ypoints = np.array(l)
            plt.xlabel("Exams", fontdict=font2)
            plt.plot(ypoints, xpoints, 'o-r')
            plt.title("Detailed Analysis")
            plt.ylabel('Marks', fontdict=font2)

            x2points = np.array(m)
            plt.plot(ypoints, x2points, 'o-b')

            x3points = np.array(q)
            plt.plot(ypoints, x3points, 'o-g')
            x4=np.array(e)
            x5=np.array(r)
            plt.plot(ypoints,x4,'o-y')
            plt.plot(ypoints,x5,'o-c')
            plt.legend(['maths', 'physics', 'chemistry','english','maths'])
            plt.show()
            total=tk.Label(analysertt,text='AVERAGE',bg='#ffffb7',bd=2,font=('times',13,'bold'))
            total.place(x=50,y=290)
            a1=tk.Label(analysertt,text=f"Average in maths : {round(sum(n)/len(n),2)}",font=('times',13),bg='#ffffb7')
            a1.place(x=15,y=320)
            a2=tk.Label(analysertt,text=f"Average in physics : {round(sum(m)/len(m),2)}",font=('times',13),bg='#ffffb7')
            a2.place(x=15,y=350)
            a3=tk.Label(analysertt,text=f"Average in chem : {round(sum(q)/len(q),2)}",font=('times',13),bg='#ffffb7')
            a3.place(x=15,y=380)
            a4=tk.Label(analysertt,text=f"Average in english : {round(sum(e)/len(e),2)}",font=('times',13),bg='#ffffb7')
            a4.place(x=15,y=410)
            a5=tk.Label(analysertt,text=f"Average in elective : {round(sum(r)/len(r),2)}",font=('times',13),bg='#ffffb7')
            a5.place(x=15,y=440)
            a6=scrolledtext.ScrolledText(analysertt,bg='#ffffb7',font=('times',13),bd=0,borderwidth=0)
            a6.place(y=315,x=280)
            total=tk.Label(analysertt,text='TOTAL',bg='#ffffb7',bd=2,font=('times',13,'bold'))
            total.place(x=300,y=290)
            for i in range(len(n)) :
                var1=n[i]+m[i]+q[i]+e[i]+r[i]
                a6.insert(tk.INSERT,f'Total in {l[i]}={var1}/500\n')
            tt=tk.Button(analysertt,text="TIME TABLE",relief='ridge',bd=2,font=('times'),command=kk)
            tt.place(x=365,y=450)
        exam=tk.Label(analysertt,text="EXAM NAME",font=('times',13),bg='#ffffb7',borderwidth=1)
        exam.place(x=15,y=15)
        maths=tk.Label(analysertt,text='MATHS',font=('times',13),bg='#ffffb7')
        maths.place(x=50,y=60)
        phy=tk.Label(analysertt,text='PHYSICS',font=('times',13),bg='#ffffb7')
        phy.place(x=208,y=60)
        che=tk.Label(analysertt,text='CHEMISTRY',font=('times',13),bg='#ffffb7')
        che.place(x=352,y=60)
        en=tk.Label(analysertt,text='ENGLISH',font=('times',13),bg='#ffffb7')
        en.place(x=105,y=135)
        ele=tk.Label(analysertt,text='ELECTIVE',font=('times',13),bg='#ffffb7')
        ele.place(x=272,y=135)
        var=10
        var2=11
        var3=12
        var4=13
        var5=14
        entry = ttk.Entry(analysertt,width= 7,textvariable=var)
        entry.place(x=20,y=120)
        entry2 = ttk.Entry(analysertt,width= 7,textvariable=var2)
        entry2.place(x=180,y=120)
        entry3 = ttk.Entry(analysertt,width= 7,textvariable=var3)
        entry3.place(x=340,y=120)
        entry4 = ttk.Entry(analysertt,width= 7,textvariable=var4)
        entry4.place(x=80,y=196)
        entry5 = ttk.Entry(analysertt,width= 7,textvariable=var5)
        entry5.place(x=249,y=196)
        quant_ent=tk.Scale(analysertt,from_=1,to=100,variable=var,orient='horizontal',bg='#BFBFFF',width=10,length=123,troughcolor='#FFD9AB')
        quant_ent.place(x=18,y=85)

        quant_ent2=tk.Scale(analysertt,from_=1,to=100,variable=var2,orient='horizontal',bg='#BFBFFF',width=10,length=123,troughcolor='#FFD9AB')
        quant_ent2.place(x=178,y=85)

        quant_ent3=tk.Scale(analysertt,from_=1,to=100,variable=var3,orient='horizontal',bg='#BFBFFF',width=10,length=123,troughcolor='#FFD9AB')
        quant_ent3.place(x=338,y=85)

        quant_ent4=tk.Scale(analysertt,from_=1,to=100,variable=var4,orient='horizontal',bg='#BFBFFF',width=10,length=123,troughcolor='#FFD9AB')
        quant_ent4.place(x=78,y=160)

        quant_ent5=tk.Scale(analysertt,from_=1,to=100,orient='horizontal',variable=var5,bg='#BFBFFF',width=10,length=123,troughcolor='#FFD9AB')
        quant_ent5.place(x=248,y=160)

        nextexambut=tk.Button(analysertt,text="SAVE EXAM",relief='ridge',bd=2,font=('times'),command=next)
        nextexambut.place(x=10,y=250)
        genbut=tk.Button(analysertt,text="ANALYSIS",relief='ridge',bd=2,font=('times'),command=gen)
        genbut.place(x=340,y=250)
        nextexambut.bind('<Enter>', on_enter)
        nextexambut.bind('<Leave>', on_leave)
        genbut.bind('<Enter>', on_enter2)
        genbut.bind('<Leave>', on_leave2)
        selected_value = tk.StringVar()

        combo = ttk.Combobox(analysertt, textvariable=selected_value)
        combo['values'] = ("Quarterly", "HalfYearly", "Midterm","Annual","RevisionTest")
        combo.place(x=125,y=17)
        combo.bind("<<ComboboxSelected>>", on_select)
        combo.set("Select/Enter an exam")
        analysertt.resizable(False,False)
        analysertt.mainloop()

    def focusmode():
        global l
        global secs
        global runn
        global uptime
        import pygame
        focus=Toplevel(root)
        uptime='00:00:00'
        s=os.getcwd()+"\AnimeKeyboard.png"
        img=PhotoImage(file=s)
        f=Canvas(focus,width=800,height=390)
        f.pack()
        f.create_image(400,195,image=img)
        l=f.create_text(400,198,text=uptime, font=("Helvetica", 50,"bold"),fill='white')
        pygame.mixer.init()
        z=os.getcwd()+"\Forest sound.mp3"
        pygame.mixer.music.load(z)
        def start():
            global secs, runn
            pygame.mixer.music.play()
            if not runn:
                runn = True
                update()
            
        def stop():
            try:
                pygame.mixer.music.stop()
            except:
                pass
            global runn
            runn = False
        def reset():
            global secs, runn, uptime
            uptime="00:00:00"
            runn = False
            secs = 0
            updatedis()
            try:
                pygame.mixer.music.stop()
            except:
                pass
        def update():
            global secs, runn
            if runn:
                secs += 1
                uptime='00:00:00'
                updatedis()
                focus.after(1000, update)
        def updatedis():
            global text
            global secs
            global l
            mins,secs = divmod(secs, 60)
            uptime = '{:02d}:{:02d}:{:02d}'.format(mins // 60, mins % 60, secs)
            text=uptime
            f.delete(l)
            l=f.create_text(400, 198, text=uptime, font=("Helvetica", 50,"bold"),fill='white')
        
        startbut = Button(focus, text="Start", command=start,font=("calibri",25),bg='#39ff14',fg='white',relief="groove",bd=2)
        startbut.place(x=100,y=320,anchor=CENTER)
        stopbut = Button(focus, text="Stop", command=stop,font=("calibri",25),bg='Red',fg='white',relief="groove",bd=2)
        stopbut.place(x=400,y=320,anchor=CENTER)
        resetbut = Button(focus, text="Reset", command=reset,font=("calibri",25),bg='yellow',relief="groove",bd=2)
        resetbut.place(x=700,y=320,anchor=CENTER)
        f.create_text(400,50,text='Welcome to Focus Mode!',font=("Poppins Regular",45,"bold"),fill='#ffd700')
        focus.title("Focus Mode")
        uptime="00:00:00"
        runn = False
        secs = 0
        updatedis()
        def endwindow():
            try:
                pygame.mixer.music.stop()
            except:
                pass
            focus.destroy()
        focus.protocol('WM_DELETE_WINDOW', endwindow)
        focus.resizable(False,False)
        focus.mainloop()
    def jokesystem():
        from tkinter import messagebox
        jokes = [
            "Why did the math book look sad? Because it had too many problems.",
            "What do you call\nfake spaghetti? An impasta.",
            "Why did the scarecrow win an award?\nBecause he was outstanding in his field.",
            "How do you organize a\nspace party? You planet.",
            "Why did the student bring a ladder to class?\nBecause he wanted to go to high school.",
            "What did one wall say to the other wall?\n'I'll meet you at the corner.'",
            "Why was the math book sad? Because it had too many problems.",
            "What's orange and sounds like a parrot? A carrot.",
            "What did one plate say to another plate? 'Lunch is on me!'",
            "Why did the tomato turn red? Because it saw the salad dressing.",
            "How do you organize a fantastic space party? You planet!",
            "What do you call a fish wearing a crown? A kingfish.",
            "Why did the banana go to the doctor? Because it wasn't peeling well.",
            "How do you make a tissue dance? You put a little boogie in it.",
            "What's a vampire's favorite fruit? A blood orange.",
            "Why did the computer go to therapy? Because it had too many bytes of emotional baggage.",
            "What do you call a snowman with a six-pack? An abdominal snowman.",
            "Why don't scientists trust atoms? Because they make up everything.",
            "What did one ocean say to the other ocean? Nothing, they just waved.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "What do you call a bear with no teeth? A gummy bear.",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What did one hat say to the other? 'Stay here, I'm going on ahead.'",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "How does a penguin build its house? Igloos it together!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What did one plate say to the other plate? 'Lunch is on me!'",
            "Why did the student do multiplication problems on the floor? The teacher told him not to use tables.",
            "How does a snowman get around? By riding an 'icicle.",
            "What do you call a shoe made of a banana? A slipper.",
            "Why did the chicken join a band? Because it had the drumsticks.",
            "What do you call a bear with no teeth? A gummy bear.",
            "Why was the belt arrested? Because it was holding up a pair of pants!",
            "How does a penguin build its house? Igloos it together.",
            "Why did the cookie go to the hospital? Because it felt crumbly.",
            "What do you call a fish wearing a crown? A kingfish.",
            "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
            "What did the janitor say when he jumped out of the closet? Supplies!",
            "Why don't scientists trust atoms? Because they make up everything.",
            "What did one hat say to the other? 'Stay here, I'm going on ahead.'",
            "Why did the chicken go to the seance? To talk to the other side.",
            "How does a snowman get around? By riding an 'icicle.",
            "What's brown and sticky? A stick.",
            "Why did the cookie go to the doctor? Because it was feeling crumbly.",
            "What's a vampire's favorite fruit? A blood orange.",
            "Why did the teacher wear sunglasses to school? Because her students were so bright.",
            "What's a pirate's favorite letter? Arrr!"
            "Why are fish so smart? Because they live in schools.",]
        joke=Toplevel(root)
        joke.wm_transient(root)
        joke.geometry("500x500")
        y=''
        def a() :
            if len(jokes)==0:
                b1['state']=DISABLED
                messagebox.showerror("Limit Reached!","You have exhausted the\nnumber of jokes available!\nCome back after another session of studying.").wm_attributes("-topmost",True)
            else :
                global y
                y=choice(jokes)
                jokes.remove(y)
                engine = pyttsx3.init()
                engine.setProperty('rate',150)
                engine.setProperty('volume',1.0)
                engine.say(y)
                engine.runAndWait()
                p=messagebox.showinfo("Your Joke is Served!",y)
                joke.resizable(False,False)
        b1=Button(joke,text='Generate Joke',font=('Calibri',35,'bold'),command=a,bg='#ffd700',fg='black',activebackground='white',activeforeground='#ffd700')
        b1.pack(pady=190)
        joke.title("Stress-Busters!")
        joke.config(bg='grey')
        joke.mainloop()
            
    def mentalhealthjournal():
        from pathlib import Path
        from tkinter import filedialog 
        from tkinter import messagebox
        from datetime import date
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd())

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        def mhsave():
            file=filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("Text file",".txt")])
            s=str(date.today().strftime("%B %d, %Y"))+"\n\nA word to describe my day - "+str(entry_1.get())+"\nWhat made me happy- "+str(entry_2.get())+"\nWhat made me unhappy - "+str(entry_3.get())
            if file is not None:
                file.write(s)
                file.close()
                messagebox.showinfo("Success!","Your mental health log for "+str(date.today().strftime("%B %d, %Y"))+"\n was saved succesfully!")
        mhj = Toplevel(root)
        mhj.geometry("1155x650")
        canvas = Canvas(mhj,bg = "#FFFFFF",height = 650,width = 1155,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)
        image= PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(577.0,325.0,image=image)
        canvas.create_text(600,100,anchor="center",text="Mental Health Journal\n",fill="#000000",font=("Georgia", 65 * -1,"underline"))
        canvas.create_text(90,225,anchor="nw",text="Describe how you feel today in a word",fill="#000000",font=("Calibri", 34 * -1))
        canvas.create_text(83,350,anchor="nw",text="What made you happy 😁?",fill="#000000",font=("Calibri", 34 * -1))
        canvas.create_text(83,485,anchor="nw",text="What made you unhappy 😞?",fill="#000000",font=("Calibri", 34 * -1))
        entry_1 = Entry(mhj,font=('Calibri',25),fg="#000716",highlightthickness=0)
        entry_1.place(x=669,y=213,width=379,height=60)
        entry_2 = Entry(mhj,font=('Calibri',25),fg="#000716",highlightthickness=0)
        entry_2.place(x=669,y=350,width=379,height=60)
        entry_3 = Entry(mhj,font=('Calibri',25),fg="#000716",highlightthickness=0)
        entry_3.place(x=669,y=477,width=379,height=60)
        button = Button(mhj,text='Submit',bg='#ffd700',borderwidth=0,highlightthickness=0,activebackground='green',activeforeground='white',command=mhsave,font=("Arial",25),relief='raised',bd=2)
        button.place(x=939,y=562,width=132,height=45)
        canvas.create_text(600,120,text=str(date.today().strftime("%B %d, %Y")),anchor=CENTER,font=("Georgia",20,"bold italic"))
        mhj.resizable(False, False)
        mhj.title('Mental Health Journal')
        mhj.bind("<Return>",lambda event: mhsave())
        mhj.wm_transient(root)
        mhj.mainloop()

    def tdlist():
        from tkinter import messagebox

        class TodoListApp:
            def __init__(self, todolist):
                self.todolist = todolist
                self.todolist.title("To-Do List")

                self.tasks = []
                self.points = 0

                self.custom_font = ("Arial", 12)

                self.task_entry = Entry(todolist, width=50, font=self.custom_font)
                self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

                self.add_button = Button(todolist, text="Add Task", command=self.add_task, font=self.custom_font, bg="#4CAF50", fg="white")
                self.add_button.grid(row=0, column=2, padx=10, pady=10)

                self.task_listbox = Listbox(todolist, selectmode=SINGLE, width=50, height=10, font=self.custom_font, bg="#FFFFE0")
                self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

                self.complete_button = Button(todolist, text="Mark Completed", command=self.mark_complete, font=self.custom_font, bg="#008CBA", fg="white")
                self.complete_button.grid(row=1, column=2, padx=10, pady=10)

                self.delete_button = Button(todolist, text="Delete Task", command=self.delete_task, font=self.custom_font, bg="#FF6347", fg="white")
                self.delete_button.grid(row=2, column=2, padx=10, pady=10)

                self.points_label = Label(todolist, text=f"Points: {self.points}", font=(self.custom_font, 20, "bold"),bg="light blue")
                self.points_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

                self.load_tasks()

            def add_task(self):
                task = self.task_entry.get()
                if task:
                    self.tasks.append(task)
                    self.task_listbox.insert(END, task)
                    self.task_entry.delete(0, END)
                    self.save_tasks()

            def mark_complete(self):
                selected_task_index = self.task_listbox.curselection()
                if selected_task_index:
                    task = self.tasks[selected_task_index[0]]
                    messagebox.showinfo("Task Completed!", f"Task '{task}' completed.")
                    self.task_listbox.delete(selected_task_index)
                    self.tasks.remove(task)
                    self.points += 10
                    self.update_points_label()
                    self.save_tasks()

            def delete_task(self):
                selected_task_index = self.task_listbox.curselection()
                if selected_task_index:
                    task = self.tasks[selected_task_index[0]]
                    response = messagebox.askyesno("Delete Task", f"Are you sure you want to delete task\n '{task}'?")
                    if response:
                        self.task_listbox.delete(selected_task_index)
                        self.tasks.remove(task)
                        self.save_tasks()

            def update_points_label(self):
                self.points_label.config(text=f"Points: {self.points}")

            def save_tasks(self):
                with open("tasks.txt", "w") as file:
                    file.write(f"{self.points}\n")
                    for task in self.tasks:
                        file.write(task + "\n")

            def load_tasks(self):
                try:
                    with open("tasks.txt", "r") as file:
                        lines = file.readlines()
                        if lines:
                            self.points = int(lines[0].strip())
                            self.update_points_label()
                            self.tasks = [task.strip() for task in lines[1:]]
                            for task in self.tasks:
                                self.task_listbox.insert(END, task)
                except FileNotFoundError:
                    pass


        todolist = Toplevel(root)
        todolist.wm_transient(root)
        todolist.config(bg='light blue')
        app = TodoListApp(todolist)
        todolist.resizable(False,False)
        todolist.mainloop()

    def quitbutt():
        k=messagebox.askyesno("Warning!","Are you sure you want\nto quit the app?")
        if k:
            root.destroy()
    def helpbutt():
        help=Toplevel(root)
        help.geometry("1000x600")
        help.config(bg="white")
        help.resizable(False,False)
        helpl=Label(help,text='''\nTo-Do List - An app for keeping track of your tasks.

Focus Mode- Procrastinating? Take a tour of the forests\nand see how long you can remain focussed.

Result Analysis+Timetable-\nDo a thorough analysis of your past examinations\nand work on your performances with a code-generated Time-Table.

Stress-Busters- Unwind and relax with a set of handpicked jokes after a study session.

Mental health journal-\nUse this method to self-introspect and find out your mental state.''',bg='white',font=('Poppins',15))
        helpl.pack()
    root.attributes('-fullscreen',True)
    c=Canvas(root,bg="#ffd700",width=1920,height=1080)
    bgimg=PhotoImage(file=("Chalkboard.png"))
    c.create_image(910,490,image=bgimg)
    bhelp=Button(root,text='Help',font=("Georgia",15,"bold"),command=helpbutt)
    bhelp.place(x=50,y=830,anchor=CENTER)
    bsb=Button(root,text='Stress-Busters!',font=("Times New Roman",25,"bold"),width=24,relief="groove",bd=4,activebackground="#933930",activeforeground="#ffd700",command=jokesystem,bg="#e7d7c1",fg="black")
    bsb.place(x=800,y=530)
    btt=Button(root,text='Result Analysis + \nTimetable',font=("Times New Roman",25,"bold"),width=24,relief="groove",bd=4,activebackground="#933930",activeforeground="#ffd700",command=analysistt,bg="#e7d7c1",fg="black")
    btt.place(x=800,y=400)
    bfm=Button(root,text='Focus Mode',font=("Times New Roman",35,"bold"),width=17,relief="groove",bd=4,activebackground="#933930",activeforeground="#ffd700",command=focusmode,bg="#e7d7c1",fg="black")
    bfm.place(x=800,y=280)
    btd=Button(root,text='To-Do List',font=("Times New Roman",30,"bold"),width=20,relief="groove",bd=4,activebackground="#933930",activeforeground="#ffd700",command=tdlist,bg="#e7d7c1",fg="black")
    btd.place(x=800,y=180)
    bmh=Button(root,text='Mental health\nJournal',font=("Times New Roman",30,"bold"),width=20,relief="groove",bd=4,activebackground="#933930",activeforeground="#ffd700",command=mentalhealthjournal,bg="#e7d7c1",fg="black")
    bmh.place(x=800,y=618)
    bq=Button(root,text="Exit",font=("Georgia",15,"bold"),activebackground="red",activeforeground="white",command=quitbutt)
    bq.place(x=1490,y=830,anchor=CENTER)
    img=PhotoImage(file=("KIPd Logo.png"))
    c.create_image(525,425,image=img)
    c.create_text(1400,25,text=('Hi, '+str(os.environ['username']).title()+'!'),font=("Poppins 18"),fill='white')
    c.create_text(525,650,text='KIPdashboard',fill="#ffd700",font=("Valorant 45 bold"))
    c.create_text(525,690,text="©2023, DAV BGPM",font=("Poppins 18"),fill='white')
    c.place(x=960,y=540,anchor=CENTER)
    root.title("KIPdashboard")
    root.resizable(False,False)
    root.mainloop()
signin()

'''This code was made by students representing DAV Gopalapuram in the PS Codessey Codefusion event in the month of Novemeber, 2023.'''
'''© 2023, DAV BGPM'''
