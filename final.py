import datetime
import matplotlib.pyplot as plt
import subprocess
from plyer import notification  # For desktop notifications

# Class Task
class Task:
    def __init__(self, task_id, name, task_type, start_time, end_time, priority, deadline):
        self.task_id = task_id
        self.name = name
        self.task_type = task_type  # "personal" or "academic"
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority
        self.deadline = deadline

# Sorting implementation with priority (Higher priority first)
def merge_sort(tasks, key):
    if len(tasks) > 1:
        mid = len(tasks) // 2
        left_half = tasks[:mid]
        right_half = tasks[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if getattr(left_half[i], key) >= getattr(right_half[j], key):  # Higher priority first
                tasks[k] = left_half[i]
                i += 1
            else:
                tasks[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            tasks[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            tasks[k] = right_half[j]
            j += 1
            k += 1

# Binary Search for Upcoming Tasks
def find_upcoming_tasks(tasks, current_time):
    left, right = 0, len(tasks) - 1
    result_index = -1

    while left <= right:
        mid = (left + right) // 2
        if tasks[mid].start_time > current_time:
            result_index = mid
            right = mid - 1  # Look for earlier possible tasks
        else:
            left = mid + 1

    # Collect all tasks starting from the found index
    if result_index != -1:
        return tasks[result_index:]
    else:
        return []

# Analyze Task Density with Priorities
def analyze_task_density_with_priorities(tasks, interval=1):
    time_slots = {hour: 0 for hour in range(24)}

    for task in tasks:
        for hour in range(task.start_time, task.end_time):
            if hour in time_slots:
                time_slots[hour] += task.priority  # Weight by priority

    return time_slots

# Plot Task Density with Priorities
def plot_task_density(density):
    times = list(density.keys())
    counts = list(density.values())

    plt.figure(figsize=(10, 6))
    plt.bar(times, counts, color='tab:orange', alpha=0.8)
    plt.xlabel("Time (Hours)")
    plt.ylabel("Priority-Weighted Task Count")
    plt.title("Task Density Analysis (Weighted by Priority)")
    plt.xticks(range(0, 24, 1))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Visualization of tasks as a Gantt chart
def plot_gantt_chart(tasks):
    fig, ax = plt.subplots()
    for i, task in enumerate(tasks):
        color = 'tab:blue' if task.task_type == "academic" else 'tab:green'
        ax.broken_barh([(task.start_time, task.end_time - task.start_time)], (i - 0.4, 0.8), facecolors=color)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task.name for task in tasks])
    ax.set_xlabel('Time (Hours)')
    ax.set_title('Task Schedule')
    plt.show()

# Notifications (For desktop)
def notify(title, message):
    try:
        subprocess.run([
            "osascript", "-e",
            f'display notification "{message}"  with title "{title}"'
        ])
    except Exception as e:
        print(f"Notification Error: {e}")

# Reminder system with priority notifications
def check_notifications(tasks):
    current_time = datetime.datetime.now().time().hour  # Current hour
    
    # Find upcoming tasks using binary search
    upcoming_tasks = find_upcoming_tasks(tasks, current_time)
    if upcoming_tasks:
        for task in upcoming_tasks:
            print(f"Reminder: Upcoming task '{task.name}' with priority {task.priority}, starting at {task.start_time}:00.")
            notify("Upcoming Task", f"Task '{task.name}' (Priority {task.priority}) starts at {task.start_time}:00.")
    else:
        print("No upcoming tasks.")

    # Check for missed tasks
    for task in tasks:
        if task.end_time < current_time:
            print(f"Missed Task: You missed '{task.name}' with priority {task.priority}, which ended at {task.end_time}:00.")
            notify("Missed Task", f"Task '{task.name}' (Priority {task.priority}) ended at {task.end_time}:00.")

# Main function to add tasks and run the scheduler
def main():
    print("Welcome to the Task Scheduler!")
    print("Enter tasks to create a Gantt chart, receive reminders, and analyze busy time slots.")
    
    tasks = []
    task_id = 1

    while True:
        print(f"\nEnter details for Task {task_id}:")
        name = input("Task Name: ")
        task_type = input("Task Type (personal/academic): ").lower()
        start_time = int(input("Start Time (e.g., 1 for 1:00): "))
        end_time = int(input("End Time (e.g., 5 for 5:00): "))
        priority = int(input("Priority (e.g., 10 for highest): "))
        deadline = int(input("Deadline (e.g., 5 for day 5): "))

        # Add task to the list
        tasks.append(Task(task_id, name, task_type, start_time, end_time, priority, deadline))
        task_id += 1

        another = input("Do you want to add another task? (yes/no): ").lower()
        if another != "yes":
            break

    # Sorting tasks by priority first (higher priority first), then by start time
    merge_sort(tasks, "priority")

    print("\nChecking for reminders and missed tasks...")
    check_notifications(tasks)

    print("\nAnalyzing Busy Time Slots...")
    task_density = analyze_task_density_with_priorities(tasks)
    plot_task_density(task_density)

    print("\nGenerating Gantt Chart...")
    plot_gantt_chart(tasks)

# Run the program
if __name__ == "__main__":
    main()