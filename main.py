from tkinter import *
root=Tk()
root.geometry("450x600")
root.title("Jala Academy")
Jala_label1=Label(root,text="JALA Academy",font=("times new roman",30,"bold"))
Jala_label1.grid(row=0,column=0,padx=80,pady=15)


Jala_label2=Label(root,text="Login Credentials",font=("times new roman",20,"bold"))
Jala_label2.grid(row=1,column=0,pady=5)

Jala_label3=Label(root,text="Email:training@jalaacademy.com",font=("times new roman",10,"bold"))
Jala_label3.grid(row=2,column=0,pady=5)

Jala_label4=Label(root,text="Password:jobprogram",font=("times new roman",10,"bold"))
Jala_label4.grid(row=3,column=0,pady=5)

Jala_label5=Label(root,text="Learn  Everything  On  Real-Time  Senerios",font=("times new roman",10,"bold"),fg="black",bg="yellow")
Jala_label5.grid(row=4,column=0,pady=5)


Jala_label6=Label(root,text="Sign In",font=("Times New Roman",15,"bold"))
Jala_label6.grid(row=5,column=0,pady=6)


Email_entry=Entry(root,text="Email or Mobile No",font=("times new roman",10,"bold"))
Email_entry.grid(row=6,column=0,pady=10)
Email_entry.config(width=30)
Email_entry.insert(0,"Email or Mobile No")

Password_entry1=Entry(root,text="Password",font=("times new roman",10,"bold"))
Password_entry1.grid(row=7,column=0,pady=7)
Password_entry1.config(width=30)
Password_entry1.insert(0,"Password")

check_box=Checkbutton(root,text="Remember Me",font=("Times New Roman",8,"bold"))
check_box.grid(row=8,column=0)

sign_button=Button(root,text="SignIn",font=("Times New Roman",8,"bold"),fg="black",bg="deep sky blue")
sign_button.grid(row=9,column=0,pady=4)
sign_button.config(width=15)

forgot_button=Button(root,text="Forgot Password",font=("Times New Roman",8,"bold"),fg="black",bg="deep sky blue")
forgot_button.grid(row=10,column=0,pady=4)
forgot_button.config(width=15)

admin_button=Button(root,text="Admin Login",font=("Times New Roman",8,"bold"),fg="black",bg="deep sky blue")
admin_button.grid(row=11,column=0,pady=4)
admin_button.config(width=15)

admin_label=Label(root,text="Jala academy offers job guaranteed program \n for freshers and 12 years experienced candidates\n on fullstack development/automation testing/\n devops/QA/SDET/Cyber Security/RPA/Cloud Technologies.\n Training would be completely on live project scenerios\n Read Our Website JALA academy for more details:\n https://jalaacademy.com/",font=("Times New Roman",13,"bold"),fg="white",bg="deep sky blue")
admin_label.grid(row=13,column=0,padx=2,pady=2)      


root.mainloop()

