f = open("demofile2.txt", "a")
f.write("1-Write what you have learned today?\n>>>I learned how to teach people using the python and the terminal\n \n2-What new skills you need?\n>>> How to use python and how to improve my iq \n\n3-What is your expectations?\n>>> by the end of the course i want to be professional in python and using it and learn the odoo\n\n4-How was the day for you?\n>>> amazing using monkey type")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
