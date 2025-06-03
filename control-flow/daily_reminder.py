enter_your_task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
is_it_time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if is_it_time_bound == "yes":
            print(f"{enter_your_task.capitalize()} is a high priority task that requires immediate attention today!")
        else:
            print("The task is not time-bound.")
    case "medium":
        if is_it_time_bound == "yes":
            print(f"{enter_your_task.capitalize()} is a high priority task that requires immediate attention today!")
        else:
            print("The task is not time-bound.")
    case "low":
        if is_it_time_bound == "no":
            print(f"{enter_your_task.capitalize()} is a low priority task. Consider completing it when you have free time.")
        else:
            print("The task is time-bound.")
