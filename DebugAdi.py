import time
def LogAdi(text):
    #Append-adds at last
    file1 = open("C:/testing/Loguri.txt", "a")  # append mode
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # Get the current time as a string
    file1.write(current_time + text + "\n" )
    file1.close()
#This is something added with first branch
