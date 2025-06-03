task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task.capitalize()} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task.capitalize()} is high priority, but not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task.capitalize()} is a medium priority task that should be completed soon.")
        else:
            print(f"Reminder: {task.capitalize()} is a medium priority, not urgent.")
    case "low":
        if time_bound == "no":
            print(f"Reminder: {task.capitalize()} is a low priority task. Do it when you have free time.")
        else:
            print(f"Reminder: {task.capitalize()} is low priority but time-sensitive.")
