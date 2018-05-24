import tkinter as tk
import final_UI_fcts as f1
from pandastable import Table, TableModel
import pandas as pd
LARGE_FONT = ("Verdana", 13)
class NFL_Cap(tk.Tk):
        def __init__(self, *args, **kwargs):

                tk.Tk.__init__(self,*args,**kwargs)
                container = tk.Frame(self)
                self.shared_data = pd.DataFrame()
                container.pack(side="top",fill ="both",expand = True)
                
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)
                
                self.frames = { }

                for F in ( StartPage, ChooseYourTeam,Coaching_Preference,Coaching_Preference_Offense,Coaching_Preference_Defense,Coaching_Preference_Offense_Statistical,Coaching_Preference_Defense_Statistical,Coaching_Preference_Offense_Sim_Coach,Coaching_Preference_Defense_Sim_Coach,Result_Page):
                        
                        frame = F(container, self)
                        
                        self.frames[F] = frame
                        
                        frame.grid(row=0,column =0, sticky="nsew")

                self.show_frame(StartPage)

        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()

        def get_page(self, page_class):
            return self.frames[page_class]
def qf():
        print("y......................................................................")
class StartPage(tk.Frame):# button1,label1
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label1 = tk.Label(self,text="Lets PLay a Game !",font=LARGE_FONT)
                label1.pack(pady=10,padx=10)
                button1 = tk.Button(self, text = "Start",
                                     command=lambda :controller.show_frame(ChooseYourTeam))
                button1.pack()

class ChooseYourTeam(tk.Frame):#label2,variable1,om1,button2,3
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="Choose your Team !",font=LARGE_FONT)
                label2.pack(pady=10,padx=10)
                OPTIONS = [
                
                    "Arizone Cardinals",
                    "Atlanta Falcons",
                    "Baltimore Ravens","Buffalo Bills",
                    "Carolina Panthers",
                    "Chicago Bears",
                    "Cincinnatti Bengals",
                    "Cleveland Browns",
                    "dallas Cowboys",
                    "Denver broncos",
                    "detroi Liions",
                    "Green bay packers",
                    "Houston Texans",
                    "indianapolis Colts",
                    "Jaclsonville jaguars",
                    "kansas city chiefs","loss angeles rams",
                    "miami dolphins","minnesotta vikings",
                    "new england patriots",
                    "new orleans saints",
                    "new york giants",
                    "new york jets",
                    "oakland raiders",
                    "philadelphia eagles",
                    "pittsburgh steelers",
                    "san doego chargers",
                    "san francisco 49ers",
                    "Seattle Sea hawks",
                    "saint louis rams","tampa bay buccanneers", "tennessee titans", "washington Redsons"
                ] #etc

                

                variable1 = tk.StringVar(self)
                variable1.set(OPTIONS[0]) # default value

                optionmenu1 = tk.OptionMenu(self, variable1, *OPTIONS)
                optionmenu1.pack()

                def ok():
                    chosen_team = variable1.get()
                    print ("IM right ", chosen_team)
                    controller.show_frame(Coaching_Preference)


                button2 = tk.Button(self, text="OK", command=ok)
                button2.pack()
                


                label2.pack(pady=10,padx=10)
                button3 = tk.Button(self, text = "Back",
                                     command=lambda :controller.show_frame(StartPage))
                button3.pack()
              
class Coaching_Preference(tk.Frame):#
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="Choose your Coaching Preference !",font=LARGE_FONT)
                label2.pack(pady=10,padx=10)
                def okq():
                        controller.show_frame(Coaching_Preference_Offense)
                button4 = tk.Button(self, text = "Offense",
                                     command=okq)
                button4.pack()
                def okw():
                        controller.show_frame(Coaching_Preference_Defense)
                        Improvement = "Statistical"
                button5 = tk.Button(self, text = "Defense",
                                     command=okw)
                button5.pack()
                def back():
                        controller.show_frame(ChooseYourTeam)
                backbutton = tk.Button(self,text="back",command=back)
                backbutton.pack()

class Coaching_Preference_Offense(tk.Frame):#
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="In which way would you like to improve ??",font=LARGE_FONT)
                label2.pack(pady=10,padx=10)
                def okq():
                        controller.show_frame(Coaching_Preference_Offense_Statistical)
                        Improvement = "Statistical"
                button6 = tk.Button(self, text = "Statistical Improvement",command=okq)
                button6.pack()
                def okw():
                        controller.show_frame(Coaching_Preference_Offense_Sim_Coach)
                        Improvement = "Statistical"
                button7 = tk.Button(self, text = "Similar Coach",command=okw)                  
                button7.pack()
                def back():
                        controller.show_frame(Coaching_Preference)
                backbutton = tk.Button(self,text="back",command=back)
                backbutton.pack()
class Coaching_Preference_Defense(tk.Frame):#
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="In which way would you like to improve ??",font=LARGE_FONT)
                label2.pack(pady=10,padx=10)  
                def okq():
                        controller.show_frame(Coaching_Preference_Defense_Statistical)
                        Improvement = "Statistical"
                button8 = tk.Button(self, text = "Statistical Improvement",command=okq)
                button8.pack()
                def okw():
                        controller.show_frame(Coaching_Preference_Defense_Sim_Coach)
                        Improvement = "Statistical"
                button9 = tk.Button(self, text = "Similar Coach",command=okw)
                button9.pack()  
                def back():
                        controller.show_frame(Coaching_Preference)
                backbutton = tk.Button(self,text="back",command=back)
                backbutton.pack()
class Coaching_Preference_Offense_Statistical(tk.Frame):
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="Coaching Preference : Offense",font=LARGE_FONT).grid(row=2,column=3)
                #label2.pack(pady=10,padx=10)
                label3 = tk.Label(self,text="Improvement Strategy : Statical Improvement",font=LARGE_FONT).grid(row=5,column=3)
                #label3.pack(pady=10,padx=10)
                message = tk.Message(self,text="Please rate and score the following 10 statistical categories by assigning the number 1 to the stat you care the least about and assigning the number 10 to the stat you care the most about, and so forth.",font=LARGE_FONT).grid(row=8,column=3)
                #message.pack()
                label5 = tk.Label(self,text="Pass Yards Per Game",font=LARGE_FONT).grid(row=10,column=3)
                #label5.pack()
                entry1 = tk.Entry(self,width=10).grid(row=10,column=8)
                #entry1.pack()
                #entry1.focus_set()
                
                label6 = tk.Label(self,text="Point Per Game",font=LARGE_FONT).grid(row=11,column=3)
                #label6.pack()
                entry2 = tk.Entry(self,width=10).grid(row=11,column=8)
                #entry2.pack()
                #entry2.focus_set()

                label7 = tk.Label(self,text="Run Yards Per Game",font=LARGE_FONT).grid(row=12,column=3)
                #label7.pack()
                entry3 = tk.Entry(self,width=10).grid(row=12,column=8)
                #entry3.pack()
                #entry3.focus_set()

                label8 = tk.Label(self,text="Sacks Allowed Per Game",font=LARGE_FONT).grid(row=13,column=3)
                #label8.pack()                
                entry4 = tk.Entry(self,width=10).grid(row=13,column=8)
                #entry4.pack()
                #entry4.focus_set()
                label9 = tk.Label(self,text="Turnovers Per Game",font=LARGE_FONT).grid(row=14,column=3)
                #label9.pack()                
                entry5 = tk.Entry(self,width=10).grid(row=14,column=8)
                #entry5.pack()
                #entry5.focus_set()
                def compute():
                    off_stat1 = float(entry1.get())
                    print (off_stat1)
                    off_stat2 = float(entry2.get())   
                    print (off_stat2)
                    off_stat3 = float(entry3.get())
                    print(off_stat3)
                    off_stat4 = float(entry4.get())
                    print (off_stat4)
                    off_stat5 = float(entry5.get())
                    controller.show_frame(Result_Page)
                    self.controller.shared_data = f1.filter_succMet_byCluster('PHI',"offense",[off_stat1,off_stat2,off_stat3,off_stat4,off_stat5])
                    print(self.controller.shared_data.iloc[0:1,0:1])
                    print(self.controller.shared_data.iloc[1:5,0:1])
                    self.table = pt = Table(self, dataframe=self.controller.shared_data,
                                       showtoolbar=True, showstatusbar=True)
                    pt.show()
                    

                result1 = tk.Button(self,text="Compute",command=compute).grid(row=16,column=5)
                #result1.pack()
                def back():
                        controller.show_frame(Coaching_Preference_Offense)
                backbutton = tk.Button(self,text="back",command=back).grid(row=18,column=5)
                #backbutton.pack()
class Coaching_Preference_Defense_Statistical(tk.Frame):
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="Coaching Preference : Defense",font=LARGE_FONT)
                label2.pack(pady=10,padx=10)
                label3 = tk.Label(self,text="Improvement Strategy : Statical Improvement",font=LARGE_FONT)
                label3.pack(pady=10,padx=10)
                message = tk.Message(self,text="Please rate and score the following 10 statistical catgeroies by assigning the number 1 to the stat you care the least about and assigning the number 10 to the stat you care the most about, and so forth.",font=LARGE_FONT)
                message.pack()
                label5 = tk.Label(self,text="Points Per Game Allowed",font=LARGE_FONT)
                label5.pack()
                entry1 = tk.Entry(self,width=10)
                entry1.pack()
                entry1.focus_set()
                
                label6 = tk.Label(self,text="Run Yards Per Game Allowed",font=LARGE_FONT)
                label6.pack()
                entry2 = tk.Entry(self,width=10)
                entry2.pack()
                entry2.focus_set()

                label7 = tk.Label(self,text="Pass Yards Per game allowed",font=LARGE_FONT)
                label7.pack()
                entry3 = tk.Entry(self,width=10)
                entry3.pack()
                entry3.focus_set()

                label8 = tk.Label(self,text="Sacks per Game",font=LARGE_FONT)
                label8.pack()                
                entry4 = tk.Entry(self,width=10)
                entry4.pack()
                entry4.focus_set()

                label9 = tk.Label(self,text="Turnovers Forced Per Game",font=LARGE_FONT)
                label9.pack()                
                entry5 = tk.Entry(self,width=10)
                entry5.pack()
                entry5.focus_set()
                def compute():
                    def_stat1 = float(entry1.get())
                    print (def_stat1)
                    def_stat2 = float(entry2.get())   
                    print (def_stat2)
                    def_stat3 = float(entry3.get())
                    print(def_stat3)
                    def_stat4 = float(entry4.get())
                    print (def_stat4)
                    def_stat5 = float(entry5.get())
                    result = f1.filter_succMet_byCluster('PHI',"defense",[def_stat1,def_stat2,def_stat3,def_stat4,def_stat5])

                    print(result)
                    controller.show_frame(Result_Page)
                result1 = tk.Button(self,text="Compute",command=compute)
                result1.pack()
                def back():
                        controller.show_frame(Coaching_Preference_Defense)
                backbutton = tk.Button(self,text="back",command=back)
                backbutton.pack()
class Coaching_Preference_Offense_Sim_Coach(tk.Frame):
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="Coaching Preference : Offense",font=LARGE_FONT)
                label2.pack(pady=10,padx=10)
                label3 = tk.Label(self,text="Improvement Strategy : Similar Coach",font=LARGE_FONT)
                label3.pack(pady=10,padx=10)


                label4 = tk.Label(self,text="Coach Name",font=LARGE_FONT)
                label4.pack()
                
                entry1 = tk.Entry(self,width=10)
                entry1.pack()
                entry1.focus_set()
                label5 = tk.Label(self,text="Coach Year",font=LARGE_FONT)
                label5.pack()
                
                
                entry2 = tk.Entry(self,width=10)
                entry2.pack()
                entry2.focus_set()
                def compute():
                    Coach_Name = entry1.get() 
                    print (Coach_Name)
                    Year = entry2.get()   
                    print (Year)
                    controller.show_frame(Result_Page)
                result1 = tk.Button(self,text="Compute",command=compute)
                result1.pack()
                def back():
                        controller.show_frame(Coaching_Preference_Offense)
                
                backbutton = tk.Button(self,text="back",command=back)
                backbutton.pack()
                

                
class Coaching_Preference_Defense_Sim_Coach(tk.Frame):
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label2 = tk.Label(self,text="Coaching Preference : Defense",font=LARGE_FONT)
                label2.pack(pady=10,padx=10)
                label3 = tk.Label(self,text="Improvement Strategy : Similar Coach",font=LARGE_FONT)
                label3.pack(pady=10,padx=10)
                
                label4 = tk.Label(self,text="Coach Name",font=LARGE_FONT)
                label4.pack()
                entry1 = tk.Entry(self,width=10)
                entry1.pack()
                entry1.focus_set()
                
                label5 = tk.Label(self,text="Coach Year",font=LARGE_FONT)
                label5.pack()
                entry2 = tk.Entry(self,width=10)
                entry2.pack()
                entry2.focus_set()
             
                def compute():
                    Coach_Name = entry1.get() 
                    print (Coach_Name)
                    Year = entry2.get()   
                    print (Year)
                    controller.show_frame(Result_Page)
                result1 = tk.Button(self,text="Compute",command=compute)
                result1.pack()
                def back():
                        controller.show_frame(Coaching_Preference_Defense)
                backbutton = tk.Button(self,text="back",command=back)
                backbutton.pack()
class Result_Page(tk.Frame):
        def __init__(self, parent, controller):
                self.controller=controller
                tk.Frame.__init__(self,parent)
                label1 = tk.Label(self,text = "Final Page",font=LARGE_FONT).grid(row=1)
                #page1 = self.controller.get_page(Coaching_Preference_Offense_Statistical)
                #df = page1.shared_data
                #print(self.controller.shared_data)
                #label2=tk.Label(self, text=df.iloc[0:1,0:1]).grid(row=2,column=1)
                #label3=tk.Label(self, text=df.iloc[0:1,2:2]).grid(row=3,column=1)
                def back():
                        controller.show_frame(Coaching_Preference_Defense)
                backbutton = tk.Button(self,text="back",command=back).grid(row=10,column=2)
print()                
app = NFL_Cap()
app.mainloop()



