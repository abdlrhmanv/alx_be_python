task_description = input("Enter your task:")
task_priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task_description}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a medium priority task that requires attention today!")
        else:
            print(f"Reminder: '{task_description}' is a medium priority task. Consider completing it when you have time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a low priority task but it's time-bound, so complete it today!")
        else:
            print(f"Reminder: '{task_description}' is a low priority task. Consider completing it when you have free time.")





