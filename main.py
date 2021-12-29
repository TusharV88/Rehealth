# Main File

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import Clock
import Face_Recognitiontv as fre
import datetime
import time


win = Tk()    
win.title('Rehealth')
win.geometry('600x400')
win.maxsize(600,400)
win.minsize(600,400)


# Cirles and Labels Images
blue_circle  = PhotoImage(file="Images/blue_circle_image.png")
red_circle  = PhotoImage(file="Images/red_circle_image.png")
curve_login  = PhotoImage(file="Images/curve_login_image.png")
curve_register  = PhotoImage(file="Images/curve_reg_image.png")

# Face and Password Protection images
Face_recognition_img  = PhotoImage(file="Images/face_image.png")

# Buttons Images
face_reco_start_img = PhotoImage(file="Images/start_button.png")

# Red Cross 
red_cross_img = PhotoImage(file="Images/red_cross.png")

# Face Recognition Login
face_reco_login_img = PhotoImage(file="Images/face_reco_log.png")

# Lifestyle Button 
lfy_bt_img = PhotoImage(file="Images/button_image2.png")
lfy_bt_img2 = PhotoImage(file="Images/button_image4.png")
lfy_bt_img3 = PhotoImage(file="Images/button_image.png")
lfy_bt_img4 = PhotoImage(file="Images/button_image3.png")

# Challenge Button Image
challenge_bt_img = PhotoImage(file="Images/challenge_image4.png")


def main_fun():

    # Welcome Frame
    welcome_fr = Frame(win, bg='#182733')
    welcome_fr.pack(fill=BOTH, expand=True)


    # Face Recognition Frame
    face_reco_fr = Frame(win, bg='#182733')

    # Login Frame
    login_fr = Frame(win, bg='#182733')
    login_fr_main = Frame(win, bg='#182733')

    # User Account Frame
    account_fr = Frame(win, bg='#182733')


    # Logo Image
    render = PhotoImage(file="Images/frt_logo_img1.png")
    img = Label(welcome_fr, image=render, bg='#182733')
    img.image = render
    img.place(x=140, y=10)
    
    # Back Button Image
    back_button_img  = PhotoImage(file="Images/Back_1.png")


    # Challenge Function
    def chall_main():
        with open('user_info/challenge_checker.txt', 'r') as f:
            checker = f.read()

        with open('user_info/challenge_days.txt', 'r') as f:
            day_num = f.read()

        # day_num = 30
        if int(day_num) < 6:
            with open('Challenges/Days_1to5.txt', 'r') as f:
                user_challenges = f.readlines()

        elif int(day_num) < 12:
            with open('Challenges/Days_6to11.txt', 'r') as f:
                user_challenges = f.readlines()

        elif int(day_num) < 21:
            with open('Challenges/Days_12to20.txt', 'r') as f:
                user_challenges = f.readlines()

        else:
            with open('Challenges/Days_21to30.txt', 'r') as f:
                user_challenges = f.readlines()

        with open('user_info/user_time.txt', 'r') as f:
                check = f.read()

        # Challenge Countdown
        def challenge_countdown():
            count_win = Tk()    
            count_win.title('Rehealth')
            count_win.config(bg='#182733')
            count_win.geometry('600x400')
            count_win.maxsize(600,400)
            count_win.minsize(600,400)

            
            with open('user_info/user_time.txt', 'r') as f:
                check = f.read()
            with open('user_info/challenge_checker.txt', 'w') as f:
                f.write('done')

            if check == 'not done':
            
                hour = int(time.strftime('%H'))
                minute = int(time.strftime('%M'))
                second = int(time.strftime('%S'))
                month = int(time.strftime('%m'))
                year = int(time.strftime('%Y'))
                date = int(time.strftime('%d'))
                date += 1
                with open('user_info/user_time.txt', 'w') as f:
                    f.write('done')
                with open('user_info/user_hour.txt', 'w') as f:
                    f.write(str(hour))
                with open('user_info/user_minute.txt', 'w') as f:
                    f.write(str(minute))
                with open('user_info/user_second.txt', 'w') as f:
                    f.write(str(second))
                with open('user_info/user_month.txt', 'w') as f:
                    f.write(str(month))
                with open('user_info/user_year.txt', 'w') as f:
                    f.write(str(year))
                with open('user_info/user_date.txt', 'w') as f:
                    f.write(str(date))
            else:
                with open('user_info/user_hour.txt', 'r') as f:
                    hour = f.read()
                    hour = int(hour)
                with open('user_info/user_minute.txt', 'r') as f:
                    minute = f.read()
                    minute = int(minute)
                with open('user_info/user_second.txt', 'r') as f:
                    second = f.read()
                    second = int(second)
                with open('user_info/user_month.txt', 'r') as f:
                    month = f.read()
                    month = int(month)
                with open('user_info/user_year.txt', 'r') as f:
                    year = f.read()
                    year = int(year)
                with open('user_info/user_date.txt', 'r') as f:
                    date = f.read()
                    date = int(date)


            # labels
            lb_challenge = Label(count_win, text='Time Left', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#76FF03')
            lb_challenge.place(x=210, y=5)

            lb_day = Label(count_win, text=f'Day {day_num}', font=("Times new roman", 40, 'normal'), bg='#182733', fg='#F4511E')
            lb_day.place(x=410, y=170)

            lb_challenge = Label(count_win, text='Challenges :', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#1E88E5')
            lb_challenge.place(x=10, y=180)

            y_num = 240
            for line in user_challenges:
                lb_user_challenge = Label(count_win, text=line, font=("Times new roman", 18, 'normal'), bg='#182733', fg='#FDD835')
                
                lb_user_challenge.place(x=10, y=y_num)
                y_num += 30


            lb_Timer = Label(count_win, text='Time', font=("Times new roman", 60, 'normal'), bg='#182733', fg='#D50000')
            lb_Timer.place(x=150, y=60)


            def timer_chal():
                delta = datetime.datetime(year, month, date, hour, minute, second) - datetime.datetime.now()
                count_down = str(delta)
                
                if count_down[0] in "-":
                    # print('Timer is over!!')
                    with open('user_info/user_time.txt', 'w') as f:
                        f.write('not done')
                    with open('user_info/challenge_checker.txt', 'w') as f:
                        f.write('done')
                    with open('user_info/challenge_days.txt', 'r') as f:
                        day_num = f.read()
                    day_num = 1 + int(day_num)
                    with open('user_info/challenge_days.txt', 'w') as f:
                        f.write(day_num)
                    count_win.destroy()
                    chall_main()
                else:
                    len_num = len(count_down)
                    if len_num == 15:
                        lb_Timer.config(text=count_down[:8])
                    else:
                        lb_Timer.config(text=count_down[:7])

                lb_Timer.after(200, timer_chal)


            timer_chal()
            count_win.mainloop()


        # Challenge intro
        def intro_challenge():
            chall_win = Tk()    
            chall_win.title('Rehealth')
            chall_win.config(bg='#182733')
            chall_win.geometry('600x400')
            chall_win.maxsize(600,400)
            chall_win.minsize(600,400)


            # labels
            lb_day = Label(chall_win, text=f'Day {day_num}', font=("Times new roman", 50, 'normal'), bg='#182733', fg='#F4511E')
            lb_day.place(x=220, y=5)

            lb_challenge = Label(chall_win, text='Challenges :', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#1E88E5')
            lb_challenge.place(x=10, y=90)

            y_num = 160
            for line in user_challenges:
                lb_user_challenge = Label(chall_win, text=line, font=("Times new roman", 18, 'normal'), bg='#182733', fg='#FDD835')
                
                lb_user_challenge.place(x=10, y=y_num)
                y_num += 30

            def switcher():
                chall_win.destroy()
                with open('user_info/challenge_checker.txt', 'w') as f:
                    f.write('not done')
                challenge_countdown()

            # Start button
            start_bt = Button(chall_win, text='Start', font=("Times new roman", 20, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher)
            start_bt.place(x=250, y=330, width=80, height=65)


            chall_win.mainloop()

        # check if challenge is started or not
        if checker == "done":
            intro_challenge()
        else:
            challenge_countdown()



    # Modern Technology Function
    def tech_main():
        tech_win = Tk()    
        tech_win.title('Rehealth')
        tech_win.geometry('600x400')
        tech_win.maxsize(600,400)
        tech_win.minsize(600,400)

        # Tech Frames
        tech_fr1 = Frame(tech_win, bg='#182733')
        tech_fr2 = Frame(tech_win, bg='#182733')

        # Tech 2nd Frame
        def tech_frame2():
            tech_fr2.pack(fill=BOTH, expand='True')

            lb_tech1 = Label(tech_fr2, text='How to spend less time \nwith technology ?', font=("Times new roman", 25, 'normal'), bg='#182733', fg='#FFD600')
            lb_tech1.place(x=150, y=5)

            lb_tech_ans1 =  Text(tech_fr2, width=57, height=13, bd=0, bg='#182733', fg='#18FFFF', font=("Times new roman", 15, 'normal'))
            lb_tech_ans1.place(x=10, y=100)
            answer1 = "1. Keep track of your screen time\n\n2. Don't check your phone immediately after waking up\n\n3. Do computer related work as soon as possible\n\n4. Make concrete plans with family/friends\n\n5. Read More Books\n\n6. Learn a New Language or Develop a Skill"
            lb_tech_ans1.insert(tk.END, answer1)
            lb_tech_ans1.config(state=DISABLED) 

            # Back button
            bck_bt = Button(tech_fr2, text='Back', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher2)
            bck_bt.place(x=500, y=13, width=50, height=40)


        # Tech 1st Frame
        def tech_frame1():
            tech_fr1.pack(fill=BOTH, expand='True')

            lb_tech1 = Label(tech_fr1, text='Technology', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#FFD600')
            lb_tech1.place(x=180, y=5)

            lb_tech_ans1 =  Text(tech_fr1, width=57, height=13, bd=0, bg='#182733', fg='#FF5722', font=("Times new roman", 15, 'normal'))
            lb_tech_ans1.place(x=10, y=70)
            answer1 = "Technology is the sum of any techniques, skills, methods, and processes used in the production of goods or services or in the accomplishment of objectives, such as scientific investigation. Technology can be the knowledge of techniques, processes, and the like, or it can be embedded in machines to allow for operation without detailed knowledge of their workings. Systems (e.g. machines) applying technology by taking an input, changing it according to the system's use, and then producing an outcome are referred to as technology systems or technological systems. \n\nThe simplest form of technology is the development and use of basic tools. The prehistoric invention of shaped stone tools followed by the discovery of how to control fire increased sources of food."
            lb_tech_ans1.insert(tk.END, answer1)
            lb_tech_ans1.config(state=DISABLED) 

            # Next button
            nxt_bt = Button(tech_fr1, text='Next', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher)
            nxt_bt.place(x=500, y=13, width=50, height=40)

        # Switch Frames
        def switcher():
            tech_fr1.destroy()
            tech_frame2()

        def switcher2():
            tech_fr2.destroy()
            tech_win.destroy()
            tech_main()

        tech_frame1()
        tech_win.mainloop()


    # Medical Abuse Function
    def medical_main():
        medical_win = Tk()    
        medical_win.title('Rehealth')
        medical_win.geometry('600x400')
        medical_win.maxsize(600,400)
        medical_win.minsize(600,400)

        # Medical Frames
        medical_fr1 = Frame(medical_win, bg='#182733')

        # Medical 1st Frame
        def medical_frame1():
            medical_fr1.pack(fill=BOTH, expand='True')

            lb_medical1 = Label(medical_fr1, text='Medcial Abuse', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#F4511E')
            lb_medical1.place(x=180, y=5)

            lb_medical1 = Label(medical_fr1, text='Medcial Child Abuse', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#FFD600')
            lb_medical1.place(x=10, y=70)

            lb_medical_ans1 =  Text(medical_fr1, width=57, height=11, bd=0, bg='#182733', fg='#18FFFF', font=("Times new roman", 15, 'normal'))
            lb_medical_ans1.place(x=10, y=115)
            answer1 = "Medical child abuse is a term that has come into use in recent years. It refers to a child receiving unnecessary and or even harmful care as a result of a parent exaggerating symptoms, fabricating physical findings or intentionally inducing illness in the child. \n\nWhile nearly everyone agrees that this type of parental behavior may take place on rare occasions, accusations of medical child abuse have risen sharply in recent years, and there have been numerous situations in which families feel they have been wrongly and unfairly accused. Families affected by rare diseases that are complex, little known and difficult to diagnose are particularly vulnerable to this accusation."
            lb_medical_ans1.insert(tk.END, answer1)
            lb_medical_ans1.config(state=DISABLED)          

        medical_frame1()
        medical_win.mainloop()


    # Substance Abuse Function
    def substance_main():
        substance_win = Tk()    
        substance_win.title('Rehealth')
        substance_win.geometry('600x400')
        substance_win.maxsize(600,400)
        substance_win.minsize(600,400)

        # Substance Frames
        substance_fr1 = Frame(substance_win, bg='#182733')
        substance_fr2 = Frame(substance_win, bg='#182733')

        # substance 2nd Frame
        def substance_frame2():
            substance_fr2.pack(fill=BOTH, expand='True')

            lb_substance1 = Label(substance_fr2, text='Classification', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#F4511E')
            lb_substance1.place(x=180, y=5)

            # Fintness Label and Text
            lb_substacne2 = Label(substance_fr2, text='Public health', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_substacne2.place(x=10, y=70)

            lb_substance_ans1 =  Text(substance_fr2, width=20, height=18, bd=0, bg='#182733', fg='#18FFFF')
            lb_substance_ans1.place(x=10, y=110)
            answer1 = "Public health practitioners have attempted to look at substance use from a broader perspective than the individual, emphasizing the role of society, culture, and availability. Some health professionals choose to avoid the terms alcohol or drug abuse in favor of language considered more objective, such as substance and alcohol."
            lb_substance_ans1.insert(tk.END, answer1)
            lb_substance_ans1.config(state=DISABLED)

            # Cardiovascular System Label and Text
            lb_substance_ques2 = Label(substance_fr2, text='Medical', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_substance_ques2.place(x=240, y=70)

            lb_substance_ans2 =  Text(substance_fr2, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_substance_ans2.place(x=215, y=110)
            answer2 = "'Drug abuse' is no longer a current medical diagnosis in either of the most used diagnostic tools in the world, the American Psychiatric Association's Diagnostic and Statistical Manual of Mental Disorders (DSM), and the World Health Organization's International Classification of Diseases (ICD)."
            lb_substance_ans2.insert(tk.END, answer2)
            lb_substance_ans2.config(state=DISABLED)

            # Brain Waves Label and Text
            lb_substance_ques3 = Label(substance_fr2, text='Drug misuse', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_substance_ques3.place(x=427, y=70)

            lb_substance_ans3 =  Text(substance_fr2, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_substance_ans3.place(x=428, y=110)
            answer3 = "Drug misuse is a term used commonly when prescription medication with sedative, anxiolytic, analgesic, or stimulant properties are used for mood alteration or intoxication ignoring the fact that overdose of such medicines can sometimes have serious adverse effects. It sometimes involves drug diversion from the individual for whom it was prescribed."
            lb_substance_ans3.insert(tk.END, answer3)
            lb_substance_ans3.config(state=DISABLED)


            # Bar Labels
            lb_bar1 = Label(substance_fr2, bg='#FFD600')
            lb_bar1.place(x=190, y=80, width=5, height=298)
            
            lb_bar2 = Label(substance_fr2, bg='#FFD600')
            lb_bar2.place(x=400, y=80, width=5, height=298)

            # Back button
            bck_bt = Button(substance_fr2, text='Back', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher2)
            bck_bt.place(x=500, y=13, width=50, height=40)


        # substance 1st Frame
        def substance_frame1():
            substance_fr1.pack(fill=BOTH, expand='True')
            
            lb_substance_ques1 = Label(substance_fr1, text='Substance Abuse', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#F4511E')
            lb_substance_ques1.place(x=160, y=5)

            lb_substance_ans1 =  Text(substance_fr1, width=58, height=13, bd=0, bg='#182733', fg='#7C4DFF', font=("Times new roman", 15, 'normal'))
            lb_substance_ans1.place(x=10, y=65)
            answer1 = "Substance abuse, also known as drug abuse, is the use of a drug in amounts or by methods which are harmful to the individual or others. It is a form of substance-related disorder. Differing definitions of drug abuse are used in public health, medical and criminal justice contexts. In some cases, criminal or anti-social behaviour occurs when the person is under the influence of a drug, and long-term personality changes in individuals may also occur.In addition to possible physical, social, and psychological harm, the use of some drugs may also lead to criminal penalties, although these vary widely depending on the local jurisdiction. \n\nDrugs most often associated with this term include: alcohol, amphetamines, barbiturates, benzodiazepines, cannabis, cocaine, hallucinogens, methaqualone, and opioids."
            lb_substance_ans1.insert(tk.END, answer1)
            lb_substance_ans1.config(state=DISABLED)

            # Next button
            nxt_bt = Button(substance_fr1, text='Next', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher)
            nxt_bt.place(x=500, y=13, width=50, height=40)

        # Switch Frames
        def switcher():
            substance_fr1.destroy()
            substance_frame2()

        def switcher2():
            substance_fr2.destroy()
            substance_win.destroy()
            substance_main()

        substance_frame1()
        substance_win.mainloop()



    # Exercise Main Function
    def exercise_main():
        exercise_win = Tk()    
        exercise_win.title('Rehealth')
        exercise_win.geometry('600x400')
        exercise_win.maxsize(600,400)
        exercise_win.minsize(600,400)

        # Exercise Frames
        exercise_fr1 = Frame(exercise_win, bg='#182733')
        exercise_fr2 = Frame(exercise_win, bg='#182733')

        # Exercise 2nd Frame
        def exercise_frame2():
            exercise_fr2.pack(fill=BOTH, expand='True')

            # Fintness Label and Text
            lb_exercise_ques1 = Label(exercise_fr2, text='Fitness', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_exercise_ques1.place(x=10, y=70)

            lb_exercise_ans1 =  Text(exercise_fr2, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_exercise_ans1.place(x=10, y=110)
            answer1 = "Individuals can increase fitness by increasing physical activity levels. Increases in muscle size from resistance training are primarily determined by diet and testosterone.This genetic variation in improvement from training is one of the key physiological differences between athletes and population."
            lb_exercise_ans1.insert(tk.END, answer1)
            lb_exercise_ans1.config(state=DISABLED)

            # Cardiovascular System Label and Text
            lb_exercise_ques2 = Label(exercise_fr2, text='Cardiovascular\nsystem', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_exercise_ques2.place(x=220, y=40)

            lb_exercise_ans2 =  Text(exercise_fr2, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_exercise_ans2.place(x=215, y=110)
            answer2 = "The beneficial effect of exercise on the cardiovascular system is well documented. There is a direct correlation between physical inactivity and cardiovascular disease, and physical inactivity is an independent risk factor for the development of coronary artery disease."
            lb_exercise_ans2.insert(tk.END, answer2)
            lb_exercise_ans2.config(state=DISABLED)

            # Immune System Label and Text
            lb_exercise_ques3 = Label(exercise_fr2, text='Immune system', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_exercise_ques3.place(x=420, y=70)

            lb_exercise_ans3 =  Text(exercise_fr2, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_exercise_ans3.place(x=425, y=110)
            answer3 = "Although there have been hundreds of studies on physical exercise and the immune system, there is little direct evidence on its connection to illness. Epidemiological evidence suggests that moderate exercise has a beneficial effect on the human immune system; an effect which is modeled in a J curve."
            lb_exercise_ans3.insert(tk.END, answer3)
            lb_exercise_ans3.config(state=DISABLED)


            # Bar Labels
            lb_bar1 = Label(exercise_fr2, bg='#FFD600')
            lb_bar1.place(x=190, y=50, width=5, height=298)
            
            lb_bar2 = Label(exercise_fr2, bg='#FFD600')
            lb_bar2.place(x=400, y=50, width=5, height=298)

            # Back button
            bck_bt = Button(exercise_fr2,text='Back', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher2)
            bck_bt.place(x=500, y=13, width=50, height=40)



        # Exercise 1st Frame
        def exercise_frame1():
            exercise_fr1.pack(fill=BOTH, expand='True')

            lb_exercise = Label(exercise_fr1, text='Exercise', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#FF9800')
            lb_exercise.place(x=230, y=5)

            lb_exercise_ans1 =  Text(exercise_fr1, width=57, height=7, bd=0, bg='#182733', fg='#2979FF', font=("Times new roman", 15, 'normal'))
            lb_exercise_ans1.place(x=10, y=70)
            answer1 = "Exercise is any bodily activity that enhances or maintains physical fitness and overall health and wellness. It is performed for various reasons, to aid growth and improve strength, prevent aging, develop muscles and the cardiovascular system, hone athletic skills, weight loss or maintenance, improve health, or simply for enjoyment. Many individuals choose to exercise outdoors where they can congregate in groups, socialize, and improve well-being as well as mental health."
            lb_exercise_ans1.insert(tk.END, answer1)
            lb_exercise_ans1.config(state=DISABLED)

            lb_exercise = Label(exercise_fr1, text='Health Effects', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#FF9800')
            lb_exercise.place(x=200, y=230)

            lb_exercise_ans1 =  Text(exercise_fr1, width=57, height=5, bd=0, bg='#182733', fg='#64DD17', font=("Times new roman", 15, 'normal'))
            lb_exercise_ans1.place(x=10, y=270)
            answer1 = "Physical exercise is important for maintaining physical fitness and can contribute to maintaining a healthy weight, regulating the digestive system, building and maintaining healthy bone density, muscle strength, and joint mobility, promoting physiological well-being, reducing surgical risks, and strengthening the immune system."
            lb_exercise_ans1.insert(tk.END, answer1)
            lb_exercise_ans1.config(state=DISABLED)

            # Next button
            nxt_bt = Button(exercise_fr1,text='Next', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher)
            nxt_bt.place(x=500, y=13, width=50, height=40)


        # Swicth Frames
        def switcher():
            exercise_fr1.destroy()
            exercise_frame2()
        
        def switcher2():
            exercise_fr2.destroy()
            exercise_win.destroy()
            exercise_main()
     

        exercise_frame1()
        exercise_win.mainloop()


    # Diet Main Function
    def diet_main():
        diet_win = Tk()    
        diet_win.title('Rehealth')
        diet_win.geometry('600x400')
        diet_win.maxsize(600,400)
        diet_win.minsize(600,400)

        # Diet Frames
        diet_fr1 = Frame(diet_win, bg='#182733')
        diet_fr2 = Frame(diet_win, bg='#182733')

        # Diet 2nd Frame
        def diet_frame2():  
            diet_fr2.pack(fill=BOTH, expand='True')

            lb_diet = Label(diet_fr2, text='Weight management', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#FF9800')
            lb_diet.place(x=150, y=5)

            lb_diet_ans1 =  Text(diet_fr2, width=57, height=5, bd=0, bg='#182733', fg='#2979FF', font=("Times new roman", 15, 'normal'))
            lb_diet_ans1.place(x=10, y=70)
            answer1 = "A particular diet may be chosen to promote weight loss or weight gain. Changing a subject's dietary intake, or 'going on a diet', can change the energy balance and increase or decrease the amount of fat stored by the body. The terms 'healthy diet' and 'diet for weight management'(dieting) are often related, as the two promote healthy weight management."
            lb_diet_ans1.insert(tk.END, answer1)
            lb_diet_ans1.config(state=DISABLED)

            lb_diet = Label(diet_fr2, text='Eating Disorders', font=("Times new roman", 25, 'normal'), bg='#182733', fg='#FF9800')
            lb_diet.place(x=190, y=200)

            lb_diet_ans2 =  Text(diet_fr2, width=57, height=5, bd=0, bg='#182733', fg='#76FF03', font=("Times new roman", 15, 'normal'))
            lb_diet_ans2.place(x=10, y=250)
            answer2 = "An eating disorder is a mental disorder that interferes with normal food consumption. It is defined by abnormal eating habits and thoughts about food that may involve eating much more or much less than needed. Common eating disorders include anorexia nervosa, bulimia nervosa, and binge-eating disorder."
            lb_diet_ans2.insert(tk.END, answer2)
            lb_diet_ans2.config(state=DISABLED)

            # Back button
            bck_bt = Button(diet_fr2,text='Back', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher2)
            bck_bt.place(x=280, y=350, width=50, height=40)


        # Diet 1st Frame 
        def diet_frame1():
            diet_fr1.pack(fill=BOTH, expand='True')
            
            lb_diet = Label(diet_fr1, text='Diet', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#FF9800')
            lb_diet.place(x=250, y=5)

            lb_diet_ans1 =  Text(diet_fr1, width=57, height=7, bd=0, bg='#182733', fg='#AB47BC', font=("Times new roman", 15, 'normal'))
            lb_diet_ans1.place(x=10, y=70)
            answer1 = "In nutrition, diet is the sum of food consumed by a person or other organism. The word diet often implies the use of specific intake of nutrition for health or weight-management reasons (with the two often being related). Although humans are omnivores, each culture and each person holds some food preferences or some food taboos. This may be due to personal tastes or ethical reasons. Individual dietary choices may be more or less healthy."
            lb_diet_ans1.insert(tk.END, answer1)
            lb_diet_ans1.config(state=DISABLED)

            lb_diet_ans2 =  Text(diet_fr1, width=57, height=3, bd=0, bg='#182733', fg='#AB47BC', font=("Times new roman", 15, 'normal'))
            lb_diet_ans2.place(x=10, y=270)
            answer2 = "A healthy diet can improve and maintain optimal health. People on a balanced vegan diet can get all necessary nutrients, but may need to specifically focus on consumption of nutrients like protein, iron, calcium, zinc."
            lb_diet_ans2.insert(tk.END, answer2)
            lb_diet_ans2.config(state=DISABLED)

            # Bar Label 
            lb_bar1 = Label(diet_fr1, bg='#FF9800')
            lb_bar1.place(x=110, y=243, width=400, height=3)

            # Next button
            nxt_bt = Button(diet_fr1,text='Next', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher)
            nxt_bt.place(x=280, y=350, width=50, height=40)


        # switch frames
        def switcher():
            diet_fr1.destroy()
            diet_frame2()

        def switcher2():
            diet_fr2.destroy()
            diet_win.destroy()
            diet_main()


        diet_frame1()
        diet_win.mainloop()



    # Sleep Main Function 
    def sleep_main():
        sleep_win = Tk()    
        sleep_win.title('Rehealth')
        sleep_win.geometry('600x400')
        sleep_win.maxsize(600,400)
        sleep_win.minsize(600,400)

        # Sleep Frames
        sleep_fr1 = Frame(sleep_win, bg='#182733')
        sleep_fr2 = Frame(sleep_win, bg='#182733')
        sleep_fr3 = Frame(sleep_win, bg='#182733')

        # Sleep 3rd Frame
        def sleep_frame3():
            sleep_fr3.pack(fill=BOTH, expand='True')

            lb_sleep = Label(sleep_fr3, text='How to improve sleep ?', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#FFD600')
            lb_sleep.place(x=110, y=5)

            lb_sleep = Label(sleep_fr3, text='1. Avoid Caffeine, Alcohol, Nicotine, and Other Chemicals that Interfere'+'\nwith Sleep', font=("Times new roman", 15, 'normal'), bg='#182733', fg='#64DD17')
            lb_sleep.place(x=10, y=80)

            lb_sleep = Label(sleep_fr3, text='2. Turn Your Bedroom into a Sleep-Inducing Environment', font=("Times new roman", 15, 'normal'), bg='#182733', fg='#64DD17')
            lb_sleep.place(x=10, y=140)

            lb_sleep = Label(sleep_fr3, text='3. Establish a Soothing Pre-Sleep Routine', font=("Times new roman", 15, 'normal'), bg='#182733', fg='#64DD17')
            lb_sleep.place(x=10, y=180)

            lb_sleep = Label(sleep_fr3, text='4. Increase bright light exposure during the day', font=("Times new roman", 15, 'normal'), bg='#182733', fg='#64DD17')
            lb_sleep.place(x=10, y=220)

            lb_sleep = Label(sleep_fr3, text='5. Exercise regularly — but not before bed', font=("Times new roman", 15, 'normal'), bg='#182733', fg='#64DD17')
            lb_sleep.place(x=10, y=260)

            lb_sleep = Label(sleep_fr3, text="6. Don't Be a Nighttime Clock-Watcher", font=("Times new roman", 15, 'normal'), bg='#182733', fg='#64DD17')
            lb_sleep.place(x=10, y=300)

            # Back Button
            bck_bt = Button(sleep_fr3,text='Back', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher3)
            bck_bt.place(x=250, y=350, width=50, height=40)

        # Sleep 2nd Frame
        def sleep_frame2():
            sleep_fr2.pack(fill=BOTH, expand='True')

            lb_sleep = Label(sleep_fr2, text='Sleep Disorder', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#FFD600')
            lb_sleep.place(x=190, y=5)

            lb_sleep_ans1 =  Text(sleep_fr2, width=57, height=12, bd=0, bg='#182733', fg='#18FFFF', font=("Times new roman", 15, 'normal'))
            lb_sleep_ans1.place(x=10, y=70)
            answer1 = "Sleep disorders are conditions that result in changes in the way that you sleep.A sleep disorder can affect your overall health, safety and quality of life. Sleep deprivation can affect your ability to drive safely and increase your risk of other health problems." + '\n\nSome common types of sleep disorders include:' + "\n1. Insomnia, in which you have difficulty falling asleep or staying asleep throughout the night." + "\n2. Sleep apnea, in which you experience abnormal patterns in breathing while you are asleep. There are several types of sleep apnea." + "\n3. Narcolepsy, a condition characterized by extreme sleepiness during the day and falling asleep suddenly during the day."
            lb_sleep_ans1.insert(tk.END, answer1)
            lb_sleep_ans1.config(state=DISABLED)

            # Next button
            nxt_bt = Button(sleep_fr2,text='Next', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher2)
            nxt_bt.place(x=280, y=350, width=50, height=40)


        # Sleep 1st Frame
        def sleep_frame1():
            sleep_fr1.pack(fill=BOTH, expand='True')

            lb_sleep = Label(sleep_fr1, text='Sleep', font=("Times new roman", 30, 'normal'), bg='#182733', fg='#FFD600')
            lb_sleep.place(x=250, y=5)

            # What is sleep Label and Text
            lb_sleep_ques1 = Label(sleep_fr1, text='what is sleep ?', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_sleep_ques1.place(x=10, y=70)

            lb_sleep_ans1 =  Text(sleep_fr1, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_sleep_ans1.place(x=10, y=110)
            answer1 = 'Sleep is a naturallyrecurring state of mind and body, characterized by altered consciousness, relatively inhibited sensory activity, reduced muscle activity and inhibition of nearly all voluntary muscles during rapid eye movement (REM) sleep, and reduced interactions with surroundings.'
            lb_sleep_ans1.insert(tk.END, answer1)
            lb_sleep_ans1.config(state=DISABLED)

            # Quality Label and Text
            lb_sleep_ques2 = Label(sleep_fr1, text='Quality', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_sleep_ques2.place(x=250, y=70)

            lb_sleep_ans2 =  Text(sleep_fr1, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_sleep_ans2.place(x=215, y=110)
            answer2 = 'The quality of sleep may be evaluated from an objective and a subjective point of view. Objective sleep quality refers to how difficult it is for a person to fall asleep and remain in a sleeping state, and how many times they wake up during a single night.'
            lb_sleep_ans2.insert(tk.END, answer2)
            lb_sleep_ans2.config(state=DISABLED)

            # Brain Waves Label and Text
            lb_sleep_ques3 = Label(sleep_fr1, text='Brain Waves', font=("Times new roman", 20, 'normal'), bg='#182733', fg='#F4511E')
            lb_sleep_ques3.place(x=430, y=70)

            lb_sleep_ans3 =  Text(sleep_fr1, width=20, height=15, bd=0, bg='#182733', fg='#18FFFF')
            lb_sleep_ans3.place(x=425, y=110)
            answer3 = "The electrical activity seen on an EEG are called brain waves. It has been revealed that the intensity of EEG waves on a frequency are related to one's sleep-wake cycle. Meaning that the body is linked to certain waves at certain points during a person's day such as falling asleep,being awake."
            lb_sleep_ans3.insert(tk.END, answer3)
            lb_sleep_ans3.config(state=DISABLED)


            # Bar Labels
            lb_bar1 = Label(sleep_fr1, bg='#FFD600')
            lb_bar1.place(x=190, y=70, width=5, height=277)
            
            lb_bar2 = Label(sleep_fr1, bg='#FFD600')
            lb_bar2.place(x=400, y=70, width=5, height=277)

            # Next and Back button
            nxt_bt = Button(sleep_fr1,text='Next', font=("Times new roman", 15, 'normal'), bd=3, fg='#651FFF', activeforeground='#651FFF', command=switcher)
            nxt_bt.place(x=280, y=350, width=50, height=40)

        # Switch frames
        def switcher():
            sleep_fr1.destroy()
            sleep_frame2()

        def switcher2():
            sleep_fr2.destroy()
            sleep_frame3()

        def switcher3():
            sleep_fr3.destroy()
            sleep_win.destroy()
            sleep_main()


        sleep_frame1()
        sleep_win.mainloop()




    # User Account
    def user_acc():
        account_fr.pack(fill=BOTH, expand=True)

        lb_hr3 = Label(account_fr, text='12', font=("Lucida Handwriting", 40, 'normal'), bg='#182733', fg='#DF002A')
        lb_hr3.place(x=100, y=5)

        lb_min3 = Label(account_fr, text='12', font=("Lucida Handwriting", 40, 'normal'), bg='#182733', fg='#DF002A')
        lb_min3.place(x=190, y=5)
        
        lb_sec3 = Label(account_fr, text='12', font=("Lucida Handwriting", 40, 'normal'), bg='#182733', fg='#0875B7')
        lb_sec3.place(x=310, y=5)
        
        lb_noon3 = Label(account_fr, text='12', font=("Lucida Handwriting", 40, 'normal'), bg='#182733', fg='#0875B7')
        lb_noon3.place(x=400, y=5)

        lb_full_date = Label(account_fr, text='12', font=("Lucida Handwriting", 18, 'normal'), bg='#182733', fg='#00E5FF')
        lb_full_date.place(x=450, y=120)


        lb_divider = Label(account_fr, text=':', font=("times new roman", 50, 'bold'), bg='#182733')
        lb_divider.place(x=278, y=-7)

        lb_bar1 = Label(account_fr, bg='#FFEA00')
        lb_bar1.place(x=0, y=100, width=150, height=8)

        lb_bar2 = Label(account_fr, bg='#FFEA00')
        lb_bar2.place(x=448, y=100, width=150, height=8)

        lb_day = Label(account_fr, text='12', font=("Lucida Handwriting", 25, 'normal'), bg='#182733', fg='#8E24AA')
        lb_day.place(x=190, y=80)

        # Lifestyle Problem Labels
        lb_sleep = Label(account_fr, text='sleep', font=("Comic Sans MS", 20, 'normal'), bg='#182733', fg='#FB8C00')
        lb_sleep.place(x=1, y=200)

        lb_diet = Label(account_fr, text='Diet', font=("Comic Sans MS", 20, 'normal'), bg='#182733', fg='#FB8C00')
        lb_diet.place(x=1, y=280)

        lb_exercise = Label(account_fr, text='Exercise', font=("Comic Sans MS", 20, 'normal'), bg='#182733', fg='#FB8C00')
        lb_exercise.place(x=1, y=360)
        
        lb_substance = Label(account_fr, text='Substance Abuse', font=("Comic Sans MS", 20, 'normal'), bg='#182733', fg='#FB8C00')
        lb_substance.place(x=365, y=205)

        lb_Medical = Label(account_fr, text='Medical Abuse', font=("Comic Sans MS", 20, 'normal'), bg='#182733', fg='#FB8C00')
        lb_Medical.place(x=400, y=280)

        lb_tech = Label(account_fr, text='Modern Technology', font=("Comic Sans MS", 20, 'normal'), bg='#182733', fg='#FB8C00')
        lb_tech.place(x=340, y=360)


        # Buttons
        sleep_bt = Button(account_fr, image=lfy_bt_img, bg='#182733', activebackground='#182733', bd=0, command=sleep_main)
        sleep_bt.place(x=140, y=200)

        diet_bt = Button(account_fr, image=lfy_bt_img2, bg='#182733', activebackground='#182733', bd=0, command=diet_main)
        diet_bt.place(x=140, y=280)

        exercise_bt = Button(account_fr, image=lfy_bt_img, bg='#182733', activebackground='#182733', bd=0, command=exercise_main)
        exercise_bt.place(x=140, y=350)

        substance_bt = Button(account_fr, image=lfy_bt_img3, bg='#182733', activebackground='#182733', bd=0, command=substance_main)
        substance_bt.place(x=280, y=200)

        tech_bt = Button(account_fr, image=lfy_bt_img3, bg='#182733', activebackground='#182733', bd=0,command=tech_main)
        tech_bt.place(x=280, y=350)

        medical_bt = Button(account_fr, image=lfy_bt_img4, bg='#182733', activebackground='#182733', bd=0, command=medical_main)
        medical_bt.place(x=280, y=280)

        challenge_bt = Button(account_fr, image=challenge_bt_img, bg='#182733', activebackground='#182733', bd=0, command=chall_main)
        challenge_bt.place(x=10, y=130)


        # Divider Color
        def div_col():
            with open('user_info/color_binary.txt', 'r') as f:  
                binary_col = f.read()

            if binary_col == '0':
                lb_divider.config(foreground='#FFEA00')
                with open('user_info/color_binary.txt', 'w') as f:  
                    f.write('1')
            else:
                lb_divider.config(foreground='#182733')
                with open('user_info/color_binary.txt', 'w') as f: 
                    f.write('0')

            # print(binary_col)
            lb_hr3.after(1000, div_col)

        # Clock
        def clock_fun2():
            hour, minute, second, noon, day, year, date, month = Clock.current_time()
                
            # Config Labels
            lb_hr3.config(text=hour)
            lb_min3.config(text=minute)
            lb_sec3.config(text=second)
            lb_noon3.config(text=noon)
            lb_full_date.config(text=f'{date}-{month}-{year}')

            if day in ['Monday', 'Tuesday', 'Sunday', 'Friday']:
                lb_day.place(x=215, y=80)
                lb_day.config(text=day)

            elif day in ['Thursday', 'Saturday']:
                lb_day.place(x=205, y=80)
                lb_day.config(text=day)

            else:
                lb_day.config(text=day)


            # print(f'Seconds: {day}')

            lb_hr3.after(200, clock_fun2)


        clock_fun2()
        div_col()




    # Login to User Account
    def login_process():
        fre.face_check()  # Recognize user face 
        
        with open('user_info/user_recognition.txt', 'r') as f:  # Write if face is recognitize
            log_check = f.read()

        if log_check == 'known':
            login_fr_main.destroy()
            user_acc()
        else:  
            messagebox.showerror('Error', 'Face did not matched!!')


    # Login Page
    def login_page():
        with open('user_info/security.txt', 'r') as f:
            log_check = f.read()

        # Not Register Frame
        def not_register():
            login_fr.pack(fill=BOTH, expand=True)

            # Back Button
            back_button = Button(login_fr, image=back_button_img, bd=0, bg='#182733', activebackground='#182733', command=login_welcome)
            back_button.image = back_button_img
            back_button.place(x=20, y=20)
          
            # Labels
            lb_not_reg = Label(login_fr, text='Not Registered', bg='#182733', font=("Times new roman", 50, 'normal'), fg='#F44336') 
            lb_not_reg.place(x=130, y=20)

            
            lb_red_cross = Label(login_fr, image=red_cross_img, bg='#182733') 
            lb_red_cross.place(x=220, y=120)

            lb_not_reg = Label(login_fr, text='First register and then login!!', bg='#182733', font=("Times new roman", 30, 'normal'), fg='#03A9F4') 
            lb_not_reg.place(x=86, y=300)


            # Register Frame
        def registered():
            login_fr_main.pack(fill=BOTH, expand=True)

            # Back Button
            back_button = Button(login_fr_main, image=back_button_img, bd=0, bg='#182733', activebackground='#182733', command=login_welcome2)
            back_button.image = back_button_img
            back_button.place(x=20, y=20)

            # Labels
            lb_not_reg = Label(login_fr_main, text='Face Recognition Login', bg='#182733', font=("Times new roman", 30, 'normal'), fg='#AA00FF') 
            lb_not_reg.place(x=130, y=20)

            lb_not_reg = Label(login_fr_main, image=face_reco_login_img, bg='#182733') 
            lb_not_reg.place(x=220, y=80)

            lb_not_reg_warn = Label(login_fr_main, text='warnings:', bg='#182733', fg='red', font=("Times new roman", 14, 'bold')) 
            lb_not_reg_warn.place(x=14, y=300)

            lb_not_reg_warn = Label(login_fr_main, text='1.Make sure that your face is visible.', bg='#182733', fg='red', font=("Times new roman", 12, 'bold')) 
            lb_not_reg_warn.place(x=14, y=335)

            lb_not_reg_warn = Label(login_fr_main, text='2.You must have a camera that is connected to your device.', bg='#182733', fg='red', font=("Times new roman", 12, 'bold')) 
            lb_not_reg_warn.place(x=14, y=367)


            # Button
            lb_not_reg_bt = Button(login_fr_main, image=face_reco_start_img, bg='#182733', activebackground='#182733', bd=0, command=login_process) 
            lb_not_reg_bt.place(x=280, y=290)
            


        if log_check != 'done':
            not_register()
        else:
            registered()

    # Face to user account
    def face_process():
        fre.face_capture()
        face_reco_fr.destroy()
        user_acc()


    # Face Recognition Frame
    def face_reco_page():
        face_reco_fr.pack(fill=BOTH, expand=True)

        # Back Button
        back_button = Button(face_reco_fr, image=back_button_img, bd=0, bg='#182733', activebackground='#182733', command=face_welcome)
        back_button.image = back_button_img
        back_button.place(x=20, y=20)

        # Labels
        lb_face_main = Label(face_reco_fr, text='Face Lock Protection', font=("Times new roman", 30, 'bold'), bg='#182733', fg='#03A9F4') 
        lb_face_main.place(x=150, y=20)

        lb_face_image = Label(face_reco_fr, bg='#182733', image=Face_recognition_img) 
        lb_face_image.place(x=250, y=90)

        lb_face_info1 = Label(face_reco_fr, bg='#182733', text='It takes 20 seconds to recognizing your face', font=("Times new roman", 20, 'bold'), fg='#FFEB3B') 
        lb_face_info1.place(x=55, y=228)

        lb_face_info2 = Label(face_reco_fr, bg='#182733', text='Warning: You must have a camera that is connected to your device.', font=("Times new roman", 15, 'bold'), fg='red') 
        lb_face_info2.place(x=16, y=370)

        # Button
        start_bt = Button(face_reco_fr, image=face_reco_start_img, bg='#182733', activebackground='#182733',bd=0, command=face_process)
        start_bt.place(x=280, y=280)




    # Switch between Frames
    def welcome_reg():
        welcome_fr.destroy()
        face_reco_page()


    # Face Page to Welcome
    def face_welcome():
        face_reco_fr.destroy()
        main_fun()

    # Welcome to login
    def welcome_login():
        welcome_fr.destroy()
        login_page()

    # login to welcome
    def login_welcome():
        login_fr.destroy()
        main_fun()

    # login to welcome
    def login_welcome2():
        login_fr_main.destroy()
        main_fun()



    # Login and Register Labels and Buttoms
    lb_blue_circle = Button(welcome_fr, image=blue_circle, bg='#182733', activebackground='#182733' ,bd=0, command=welcome_login)
    lb_blue_circle.place(x=280, y=160)
    lb_red_circle = Button(welcome_fr, image=red_circle, bg='#182733', activebackground='#182733' ,bd=0, command=welcome_reg)
    lb_red_circle.place(x=280, y=240)
    lb_curve_login = Label(welcome_fr, image=curve_login, bg='#182733')
    lb_curve_login.place(x=230, y=100)
    lb_curve_register = Label(welcome_fr, image=curve_register, bg='#182733')
    lb_curve_register.place(x=220, y=285)



    # Clock 
    lb_hr = Label(welcome_fr, text='12', font=("times new roman", 35, 'bold'), bg='#182733', fg='#DF002A')
    lb_hr.place(x=35, y=160)
    lb_hr2 = Label(welcome_fr, text='HOUR', font=("times new roman", 15, 'bold'), bg='#0875B7', fg='white')
    lb_hr2.place(x=30, y=240)

    lb_min = Label(welcome_fr, text='12', font=("times new roman", 35, 'bold'), bg='#182733', fg='#DF002A')
    lb_min.place(x=158, y=160)
    lb_min2 = Label(welcome_fr, text='MINUTE', font=("times new roman", 15, 'bold'), bg='#0875B7', fg='white')
    lb_min2.place(x=140, y=240)
    
    lb_sec = Label(welcome_fr, text='12', font=("times new roman", 35, 'bold'), bg='#182733', fg='#0875B7')
    lb_sec.place(x=387, y=160)
    lb_sec2 = Label(welcome_fr, text='SECOND', font=("times new roman", 15, 'bold'), bg='#DF002A', fg='white')
    lb_sec2.place(x=370, y=240)
    
    lb_noon = Label(welcome_fr, text='12', font=("times new roman", 35, 'bold'), bg='#182733', fg='#0875B7')
    lb_noon.place(x=500, y=160)
    lb_noon2 = Label(welcome_fr, text='NOON', font=("times new roman", 15, 'bold'), bg='#DF002A', fg='white')
    lb_noon2.place(x=504, y=240)

    def clock_fun():
        hr, min, sec, noon, day, year, date, month = Clock.current_time()

        # Config Labels
        lb_hr.config(text=hr)
        lb_min.config(text=min)
        lb_sec.config(text=sec)
        lb_noon.config(text=noon)

        # print(f'Seconds: {sec}')

        lb_hr.after(200, clock_fun)





    clock_fun()
    # chall_main()


main_fun()
win.mainloop()



