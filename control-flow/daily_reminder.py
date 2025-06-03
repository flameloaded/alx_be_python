enter_your_task = input("Enter your task: ").lower()
priority = input("high/medium/low: ").lower()
is_it_time_bound = input("yes/no: ").lower()

match priority:
    case "high" | "medium":
        if is_it_time_bound == "yes":
            print("Finish project report is a high priority task that requires immediate attention today!")
        else:
            print("The project is not of high priority")
    case "low":
        if is_it_time_bound == "no":
            print("Read a book is a low priority task. Consider completing it when you have free time.")
        else:
            print("The task is time-bound ")

