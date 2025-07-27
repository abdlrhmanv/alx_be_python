task_description = input("Enter your task:")
task_priority = input("Priority (high/medium/low):")
time_bound = int(input("Is it time-bound? (yes/no):"))

if time_bound == "yes":
    print(f"Reminder: '{task_description}  ' is a high priority task that requires immediate attention today!")
else:
    print(f"Reminder: '{task_description}'  is a low priority task. Consider completing it when you have free time.")