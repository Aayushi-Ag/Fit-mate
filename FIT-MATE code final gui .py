from tkinter import *

win= Tk()
win.geometry("1400x800")
win.title("FitMate")
win.config(bg="linen")

sex= StringVar()
age,meals,sleep= IntVar(),IntVar(),IntVar()
height,weight= DoubleVar(),DoubleVar()
plank,run=DoubleVar(),DoubleVar()
push,squat=IntVar(),IntVar()

def label(str):
    return Label(win,text=str,font=("Corbel Light",15,"bold"),fg="gray25",bg="linen")
def inp(var):
    return Entry(win, textvariable= var, font=('calibre',15,'italic'))

#LABELS
label1= Label(win,text="""GET STRONGER AND FITTER WITH US
in just two easy steps...
STEP 1.""",font=("Franklin Gothic Medium",25,"bold"),fg="gray25",bg="linen")

label2=label("Please enter your age: ")
label3=label("Please enter your weight (in kg): ")
label4=label("Please enter your height (in m): ")
label5=label("Please enter your Gender (M/F): ")
label6=label("Please enter an approximate amount of sleep you get in a day (in hours): ")
label7=label("Please enter the number of meals you eat in a day: ")
label8=Label(win,text="""Please follow the given instructions:
Attempt the following exercises and note the timing/count 
1. Plank
2. Push Up
3. Squats
4. Running""",font=("bell MT",20,"bold"),fg="gray25",bg="linen")
label9=label("Enter the time in minutes for plank:")
label10=label("Enter the count of pushups you did:")
label11=label("Enter the count of squats you did:")
label12=label("Enter the time in minutes for running:")


#LABEL PLACING
label1.grid(row=1,column=0)
label2.grid(row=2,column=0)
label3.grid(row=3,column=0)
label4.grid(row=4,column=0)
label5.grid(row=5,column=0)
label6.grid(row=6,column=0)
label7.grid(row=7,column=0)
label8.grid(row=12,column=0)
label9.grid(row=13,column=0)
label10.grid(row=14,column=0)
label11.grid(row=15,column=0)
label12.grid(row=16,column=0)


#INPUT
inp1= inp(age)
inp2= inp(weight)
inp3= inp(height)
inp4= inp(sex)
inp5= inp(sleep)
inp6= inp(meals)
inp7=inp(plank)
inp8=inp(push)
inp9=inp(squat)
inp10=inp(run)

#INPUT PLACING
inp1.grid(row=2,column=3)
inp2.grid(row=3,column=3)
inp3.grid(row=4,column=3)
inp4.grid(row=5,column=3)
inp5.grid(row=6,column=3)
inp6.grid(row=7,column=3)
inp7.grid(row=13,column=3)
inp8.grid(row=14,column=3)
inp9.grid(row=15,column=3)
inp10.grid(row=16,column=3)

#second page

def diet():
        new2=Tk()
        # new2=Toplevel(win)
        new2.title("FitMate")
        new2.geometry("1400x800")
        new2.config(bg="linen")
        
        # bmi is calculated here
        def calcBMI():
            w = float(inp2.get())
            h = float(inp3.get())
            bmi= w/(h*h)
            return bmi
        bmi= calcBMI()
        bmi= round(bmi,1)
        l= Label(new2,text=f"BMI: {bmi}",font=("Franklin Gothic Medium",20,"bold"),fg="gray25",bg="linen").pack()
        S= Label(new2,text="Recommended Exercises and Diet for you are:",font=("bell MT",24,"bold"),fg="gray25",bg="linen").pack()
        
        # to print the recommended exercises
        def disp(L):
            for i in range(3):
                l= Label(new2,text=L[i],font=("Corbel Light",16,"bold"),fg="gray25",bg="linen").pack()
                
        
        pup=["3 X 10 flat bench press","3 X 10 incline bench press","3 X 10 decline bench press" ]   #for chest
        pl=["3 X 10 sumo squats","4 X 10 calf rises","3 X 10 leg press"]  #for legs
        sq=["3 X 10  pushups","3 X 10  lat pull downs","3 X 10 mid rows"]  #for back
        r=["3 X 15 crunches","1km running","20 mins cycling"]   #for cardio and core
        h=["1km running","20 mins cycling","2 X 2mins plank"]   #for healthy person
        
        t=0
        if push.get() <= 20:
            disp(pup)
            t=1
        if plank.get() <= 1.5:
            disp(pl)
            t=1
        if squat.get() <= 50:
            disp(sq)
            t=1
        if run.get() <= 3:
            disp(r)
            t=1
        if t==0:
            disp(h)

    # to print nutrition for every age group 

        n18u=["Protein: egg,peanut butter,milk,hummus","Carb: whole wheat,bread,potatoes,corn,cereal","Fats: Nuts,seeds,avocados","Calories: butter,egg","Calcium: dairy product,ragi,seeds"]


        n18n=['Carb: cereal,grains','Protein: fish,meat,egg,milk,soyabean','Vitamin: sprouts,fruit,vegetables','Fibres: whole wheat,bran,fruit','Mineral: sprouts','Calcium: milk']


        n18o=['Calories less than 500','Protein: toned milk,tofu','drink a lot of water','Vitamin: fruits,vegetables','Fat: egg white','Calcium: toned milk,tofu']


        n55u=['Protein: milk,eggs','Carb: cereal,grain,paneer','Sodium: salt,chicken','Calcium: chickpea,nuts,milk','Fat: cheese,butter,meat'] 


        n55n=['Carb: milk,grains,banana,brown rice','Fat: dry fruits,butter','Calcium: milk,soyabean','Sodium: salt','Protein: fish,meat,dal','Iron: dry fruits,oats']      


        n55o=['Protein: plant oil,fish,nuts','Vitamin: citrus friut,potatoes','Iron: dry fruit,grains','Sodium: chicken,salt']    


        n55su=['Protein: cheese,yogurt,fish','Calorie: egg yolk,sugar,nuts,milkshake','Vitamin: fruits,salad','Iron: dry fruits,oats','Carb: bread,potato,tofu']     


        n55sn=['Protien: paneer,tofu,dal','Calcium: spinach,dairy product','Vitamin D: fish,egg yolk','Iron: beans,grains','Vitamin A: green leafy vegetables','Folic Acid: fruits,peas,bread']     


        n55so=['Cholestrol: use olive','Protien: egg white,paneer','Fat: vegetable soup','Potassium: cumin,sweet lime,methi','Carb: oats,cereal']        

        if age.get()<=18 and (bmi<18.5):
            a= Label(new2,text=('\n'.join(map(str,n18u))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        elif age.get()<=18 and (bmi>18.5 and bmi<24.9):
            a= Label(new2,text=('\n'.join(map(str,n18n))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        elif age.get()<=18 and (bmi>24.9):
            a= Label(new2,text=('\n'.join(map(str,n18o))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        elif (age.get()>18 and age.get()<=55) and (bmi<18.5):
            a= Label(new2,text=('\n'.join(map(str,n55u))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        elif (age.get()>18 and age.get()<=55) and (bmi>18.5 and bmi<24.5):
            a= Label(new2,text=('\n'.join(map(str,n55n))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        elif (age.get()>18 and age.get()<=55) and (bmi>24.9):
            a= Label(new2,text=('\n'.join(map(str,n55o))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        elif (age.get()>55) and (bmi<18.5):
            a= Label(new2,text=('\n'.join(map(str,n55su))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        elif (age.get()>55) and (bmi>18.5 and bmi<24.9):
            a= Label(new2,text=('\n'.join(map(str,n55sn))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()
        else:a= Label(new2,text=('\n'.join(map(str,n55so))),font=("Lucida Bright",16,"bold"),fg="gray25",bg="linen").pack()

        

#Button

b1=Button(win,text="NEXT",fg="white",bg="black",font=("sitka small semibold",14,"bold"), command=diet)
b1.grid(row=20,column=5)

win.mainloop()