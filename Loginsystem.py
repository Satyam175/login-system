
from tkinter import *
import os


def delete2 ():
	screen3.destroy()

def delete3 ():
	screen4.destroy()
	
def delete4 ():
	screen5.destroy()

def saved() :
	screen10 = Toplevel(screen)
	screen10.title("Info")
	screen10.geometry("800x800")
	Label(screen10 , text ="Saved successfully").pack()



def save() :
	filename = raw_filename.get()
	notes = raw_notes.get()
	data = open(filename , "w")
	data.write(notes)
	data.close()
	saved()


def create_notes() :
	global raw_filename
	raw_filename =StringVar()
	global raw_notes
	raw_notes =StringVar()
	
	global screen9
	screen9 = Toplevel(screen)
	screen9.title("Info")
	screen9.geometry("800x800")
	Label(screen9 , text ="please enter a file name").pack()
	Entry(screen9 , textvariable = raw_filename).pack()
	Label(screen9 , text ="Enter the notes : ").pack()
	Entry(screen9 , textvariable = raw_notes).pack()
	Button(screen9 , text ="save" , command =save).pack()

def view_notes1() :
	filename1 = raw_filename1.get()
	data = open(filename1 ,"r")
	data1 = data.read()
	screen12= Toplevel(screen)
	screen12.title("Info")
	screen12.geometry("1000x1000")
	Label(screen12 , text =data1).pack()
	
	
	

def view_notes() :
	screen11= Toplevel(screen)
	screen11.title("Info")
	screen11.geometry("1000x1000")
	all_files =os.listdir()
	Label(screen11 , text ="please use one of the file name below").pack()
	Label(screen11 , text = all_files).pack()
	global raw_filename1
	raw_filename1 =StringVar()
	Entry(screen11 , textvariable = raw_filename1).pack()
	Button(screen11 , command = view_notes1 , text ="ok").pack()


def delete_note1 () :
	filename3 = raw_filename2.get()
	os.remove(filename3)
	all_files =os.listdir()
	screen14 =Toplevel(screen)
	screen14.title("deleted")
	screen14.geometry("500x500")
	Label(screen14 ,text =filename3 +" deleted").pack()

def delete_note () :
	screen13 = Toplevel(screen)
	screen13.title("Info")
	screen13.geometry("1000x1000")
	all_files =os.listdir()
	Label(screen13 , text ="please use one of the file name below").pack()
	Label(screen13 , text = all_files).pack()
	global raw_filename2
	raw_filename2 = StringVar()
	Entry(screen13 , textvariable = raw_filename2).pack()
	Button(screen13 , command = delete_note1 , text="ok").pack()
	
	


def session() :
	screen8 = Toplevel(screen)
	screen8.title("dashboard")
	screen8.geometry("1000x1000")
	Label(screen8 , text ="Welcome to the dashboard ").pack()
	Button(screen8 , text ="create notes" , command = create_notes).pack()
	Button(screen8 , text ="view notes ", command = view_notes).pack()
	Button(screen8 , text ="delete note" , command = delete_note).pack()
	

def login_success() :
	session()

def incorrect_pass() :
	global screen4
	screen4 =Toplevel(screen)
	screen4.title("incorrect password")
	screen4.geometry("500x500")
	Label(screen4 , text ="incorrect password" , fg="red").pack()
	Button(screen4 , text =" ok" , command = delete3).pack()
	
def no_user() :
	global screen5
	screen5=Toplevel(screen)
	screen5.title("no user found")
	screen5.geometry("500x500")
	Label(screen5 ,  text ="user not found" , fg="red").pack()
	Label(screen5 , text ="Please Register yourself").pack()
	Button(screen5 , text =" ok" , command = delete4).pack()
	

def login_verify () :
	username1 =username_verify.get()
	password1 = password_verify.get()
	list_of_files = os.listdir()
	if username1 in list_of_files :
		file1 = open(username1 ,"r")
		verify = file1.read().splitlines()
		if password1 in verify :
			login_success()
		else :
			incorrect_pass()
	else : 
	     no_user()
	     
def register_user ():
	username_info = username.get()
	password_info = password.get()
	
	file =open(username_info,"w")
	file.write(username_info+"\n")
	file.write(password_info)
	file.close()
	
	Label(screen1 , text =" registration successfull " , fg ="green").pack()

def register() :
	global screen1
	screen1 = Toplevel(screen)
	screen1.title("REGISTER")
	screen1.geometry("1000x1000")
	
	global username
	global password
	global username_entry
	global password_entry
	
	username = StringVar()
	password = StringVar()
	
	Label(screen1 , text ="Please Enter the Details Below").pack()
	Label(screen1 , text ="").pack()
	Label(screen1 , text="Username").pack()
	username_entry =Entry(screen1 , textvariable = username).pack()
	Label(screen1 , text ="").pack()
	Label(screen1 , text="Password").pack()
	password_entry = Entry(screen1 , textvariable = password).pack()
	Label(screen1 , text="").pack()
	Button(screen1 , text="Register", width="8", height = "1" , command =register_user).pack()
	
    
def login ()    :
	global screen2
	screen2 = Toplevel(screen)
	screen2.geometry("1000x1000")
	screen2.title("LOGIN")
	global username_verify
	global password_verify
	
	
	username_verify = StringVar()
	password_verify= StringVar()

	global username_entry1
	global password_entry1
		
	Label(screen2 , text ="").pack()
	Label(screen2, text="Username").pack()
	username_entry =Entry(screen2 , textvariable = username_verify).pack()
	Label(screen2 , text ="").pack()
	Label(screen2 , text="Password").pack()
	password_entry = Entry(screen2 , textvariable = password_verify).pack()
	cbutton = Checkbutton(screen2, text ="remember password").pack()
	
	Label(screen2 , text="").pack()
	Button(screen2 , text="LOGIN", width="8", height = "1" , command = login_verify).pack()
	
	Label(screen2, text = " having trouble logging in?" , fg="red").pack(side =BOTTOM)
	
	
def main_screen ()    :
	global screen
	screen = Tk()
	screen.title("Notes")
	Label(text ="WELCOME " , bg ="white", fg="purple", width =10 ).pack(fill =X , side =TOP)
	Label(text="").pack()
	Label(text="").pack()
	Label(text="").pack()
	Label(text="").pack()
	Button(text="Login", command = login , height = "1" , width = "10" , fg="black" ).pack()
	Label(text="").pack()
	
	Label(text ="Don't have a account ? ").pack()
	Button(text ="Sign Up",width="10" , height ="1" ,command = register ).pack()
	Label(text = " login system created by Satyam Kaushik" ,fg ="green").pack(side =BOTTOM)
	screen.mainloop()
main_screen()	
