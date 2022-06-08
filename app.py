import os, sys, shutil, aiohttp, wmi, psutil, time
from tqdm import tqdm, trange

# centers console and grabs user login
width = shutil.get_terminal_size().columns
name = os.getlogin()


# ------------------------------------------------------------
# First Menu being displayed
def menu():
    print("   Project Zero".center(width))
    print("Welcome! %s".center(width) % name)

    time.sleep(6)

menu()

# -------------------------------------------------------------
#Grabs all running tasks

if __name__ == '__main__':
    for p in psutil.process_iter():
        print('[PID: {}] ---> {}'.format(p.pid, p.name()))
        
# -------------------------------------------------------------       
def progress_bar():
        with tqdm(total=100) as pbar:
            for i in range(10):
                pbar.update(10)
progress_bar()

#--------------------------------------------------------------
# prompts for process name from list that was first displayed

def remove_task():
    ti = 0

    proc_name = input("Process name: ")

    f = wmi.WMI()

    for process in f.Win32_Process():
        if process.name == proc_name.capitalize() + ".exe":
            process.Terminate()
            ti += 1
            print("Task Succesfully Deleted")
            

    if ti == 0:
        
        print("Process not found.")

    time.sleep(3)

remove_task()

# -------------------------------------------------------------