def daily_reflection():
    day = input("How was your day? (good/average/bad): ").lower()

    if day == "good":
        productive = input("Were you productive? (yes/no): ").lower()
        if productive == "yes":
            print("Great! Maintain consistency. Plan next goals.")
        else:
            print("Relax today. Plan 3 tasks for tomorrow.")

    elif day == "average":
        issue = input("What was the issue? (distraction/low energy): ").lower()
        if issue == "distraction":
            print("Remove distractions. Try Pomodoro technique.")
        elif issue == "low energy":
            print("Take proper rest and eat healthy.")

    elif day == "bad":
        problem = input("What went wrong? (stress/overwork/personal): ").lower()
        if problem == "stress":
            print("Do breathing exercises and take a break.")
        elif problem == "overwork":
            print("Reduce workload and prioritize tasks.")
        elif problem == "personal":
            print("Take time off and talk to someone.")

    else:
        print("Invalid input. Please try again.")

daily_reflection()