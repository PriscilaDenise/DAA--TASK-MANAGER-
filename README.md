COURSE UNIT: DESIGN AND ANALYSIS OF ALGORITHMS
TASK MANAGER PROJECT
GROUP MEMBERS
1. Muwanguzi Priscila Denise M23B23/010
2. Mawejje JohnPaul M23B23/049
3. Nicole Johnson S23B23/020
Task Scheduler Documentation with Pseudocode
This Task Scheduler application allows users to manage and prioritize tasks, visualize task
schedules, analyze task density based on priority, and receive notifications for upcoming or
missed tasks. The main components of the system include a Task class, sorting algorithms for
task prioritization, a binary search for upcoming tasks, task density analysis, and desktop
notifications.
Task Class
The Task class is the fundamental structure used to represent each task in the system. It
contains the following attributes:
● task_id: Unique identifier for the task.
● name: Name of the task.
● task_type: Type of task (either "personal" or "academic").
● start_time: The starting time of the task (in hours).
● end_time: The ending time of the task (in hours).
● priority: The priority of the task (higher numbers denote higher priority).
● deadline: The day or time by which the task must be completed.
Pseudocode for Task Class:
Class Task:
Function __init__(task_id, name, task_type, start_time, end_time, priority, deadline):
Set self.task_id = task_id
Set self.name = name
Set self.task_type = task_type
Set self.start_time = start_time
Set self.end_time = end_time
Set self.priority = priority
Set self.deadline = deadline
Merge Sort for Task Prioritization
The merge_sort function is used to sort tasks based on priority (higher priority first). If two
tasks have the same priority, they are sorted by their start time.
Pseudocode for Merge Sort:
Function merge_sort(tasks, key):
If len(tasks) > 1:
mid = len(tasks) // 2
left_half = tasks[:mid]
right_half = tasks[mid:]
merge_sort(left_half, key)
merge_sort(right_half, key)
i = j = k = 0
While i < len(left_half) and j < len(right_half):
If getattr(left_half[i], key) >= getattr(right_half[j], key):
tasks[k] = left_half[i]
Increment i
Else:
tasks[k] = right_half[j]
Increment j
Increment k
While i < len(left_half):
tasks[k] = left_half[i]
Increment i
Increment k
While j < len(right_half):
tasks[k] = right_half[j]
Increment j
Increment k
Binary Search for Upcoming Tasks
The find_upcoming_tasks function uses binary search to find tasks whose start time is later
than the current time. It returns all tasks starting from the identified task.
Pseudocode for Binary Search:
Function find_upcoming_tasks(tasks, current_time):
left = 0
right = len(tasks) - 1
result_index = -1
While left <= right:
mid = (left + right) // 2
If tasks[mid].start_time > current_time:
result_index = mid
right = mid - 1 # Continue searching for earlier tasks
Else:
left = mid + 1
If result_index != -1:
Return tasks[result_index:]
Else:
Return []
Task Density Analysis with Priorities
The analyze_task_density_with_priorities function calculates the task density for
each hour of the day, considering the priority of each task. This helps to understand the
distribution of tasks based on their priority.
Pseudocode for Task Density Analysis:
Function analyze_task_density_with_priorities(tasks, interval=1):
Initialize time_slots as a dictionary with keys 0 to 23 (representing hours) and values set to 0
For each task in tasks:
For each hour from task.start_time to task.end_time:
If hour in time_slots:
Increment time_slots[hour] by task.priority
Return time_slots
Plotting Task Density
The plot_task_density function visualizes the task density on a bar chart, where the x-axis
represents the hours of the day and the y-axis represents the priority-weighted task count.
Pseudocode for Plotting Task Density:
Function plot_task_density(density):
Create a list of times from the density dictionary
Create a list of counts from the density dictionary
Plot the bar chart using times as x-values and counts as y-values
Label the axes and title the chart
Display the chart
Plotting Gantt Chart
The plot_gantt_chart function visualizes the tasks as a Gantt chart, where each task is
represented by a horizontal bar spanning from its start time to end time. Tasks are colored
based on their type (e.g., academic tasks in blue, personal tasks in green).
Pseudocode for Plotting Gantt Chart:
Function plot_gantt_chart(tasks):
Create a new figure for the plot
For each task in tasks:
If task.task_type is "academic":
Set color to blue
Else:
Set color to green
Plot a broken bar for the task using its start_time and end_time
Label the y-axis with task names
Label the x-axis with hours
Title the chart
Display the chart
Desktop Notifications
The notify function sends a desktop notification to alert the user about upcoming or missed
tasks.
Pseudocode for Sending Notifications:
Function notify(title, message):
Try:
Run "osascript" to display a notification with title and message
Except Exception as e:
Print error message
Reminder System
The check_notifications function checks for upcoming tasks based on the current time
and sends notifications for upcoming tasks and missed tasks. It utilizes the binary search to find
the next tasks and checks if any tasks have passed their end time.
Pseudocode for Reminder System:
Function check_notifications(tasks):
Get the current hour from the system clock
Find upcoming tasks using find_upcoming_tasks function
If upcoming tasks are found:
For each upcoming task:
Print a reminder message and send a notification
Else:
Print "No upcoming tasks."
For each task in tasks:
If task.end_time < current time:
Print a missed task message and send a notification
Main Function
The main function is the entry point for the program. It prompts the user to enter details for
multiple tasks, adds them to the task list, sorts them by priority, and then runs the scheduler to
check reminders, analyze task density, and plot the task schedule.
Pseudocode for Main Function:
Function main():
Print a welcome message
Initialize an empty list for tasks
Set task_id = 1
While True:
Prompt the user to enter task details
Add the new task to the tasks list
Ask if the user wants to add another task
If no more tasks, break out of loop
Sort tasks by priority using merge_sort function
Run check_notifications to display task reminders and missed tasks
Run analyze_task_density_with_priorities to calculate task density
Plot the task density and Gantt chart
If __name__ == "__main__":
Run main()
Usage Instructions
1. Enter Tasks: The user is prompted to input task details, including name, type, start time,
end time, priority, and deadline.
2. Sort and Prioritize: The tasks are sorted by priority and start time.
3. Task Reminders: Notifications will be sent for upcoming or missed tasks.
4. Task Density Analysis: Task density is analyzed and visualized to show the distribution
of tasks over a 24-hour period.
5. Gantt Chart: A Gantt chart is generated to visualize the task schedule.
This system helps in managing and visualizing tasks effectively based on priority and time
constraints.
