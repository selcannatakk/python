import datetime

user_input = input("enter your foal \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline,"%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date



