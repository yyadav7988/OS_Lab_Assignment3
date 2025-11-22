"""
cpu_scheduling.py

Simulate:
1. Non-preemptive Priority Scheduling
2. Round Robin Scheduling

Outputs:
- Gantt chart for each algorithm
- Waiting time & Turnaround time for each process
- Average waiting time and turnaround time
"""

def priority_scheduling():
    """
    Non-preemptive priority scheduling.
    Lower priority number => higher priority.
    All processes are assumed to arrive at time 0.
    """
    n = int(input("Enter number of processes: "))

    processes = []
    for i in range(n):
        pid = i + 1
        bt = int(input(f"Enter Burst Time for P{pid}: "))
        pr = int(input(f"Enter Priority (lower number = higher priority) for P{pid}: "))
        processes.append({"pid": pid, "bt": bt, "priority": pr})

    # Sort by priority (ascending: lower number = higher priority)
    processes.sort(key=lambda x: x["priority"])

    time = 0
    gantt = []        # list of tuples: (pid, start_time, end_time)
    wt = [0] * n      # waiting times indexed by pid-1
    tat = [0] * n     # turnaround times indexed by pid-1

    for p in processes:
        start = time
        time += p["bt"]
        end = time

        gantt.append((p["pid"], start, end))

        pid_index = p["pid"] - 1
        tat[pid_index] = end                  # since arrival time = 0
        wt[pid_index] = tat[pid_index] - p["bt"]

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n

    print("\n=== Priority Scheduling (Non-preemptive) ===")
    print("\nGantt Chart:")
    print_gantt_chart(gantt)

    print("\nPID\tBT\tPriority\tWT\tTAT")
    for p in processes:
        pid = p["pid"]
        pid_index = pid - 1
        print(f"P{pid}\t{p['bt']}\t{p['priority']}\t\t{wt[pid_index]}\t{tat[pid_index]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def round_robin():
    """
    Round Robin scheduling.
    All processes arrive at time 0.
    Time Quantum will be entered by the user.
    """
    n = int(input("Enter number of processes: "))
    burst_times = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        burst_times.append(bt)

    tq = int(input("Enter Time Quantum: "))

    remaining_bt = burst_times[:]
    time = 0
    completed = 0
    gantt = []  # (pid, start_time, end_time)

    # For calculating waiting and turnaround times
    finish_time = [0] * n

    # Simple Round Robin with all processes initially in queue
    from collections import deque
    q = deque()
    for i in range(n):
        q.append(i)  # store index 0..n-1

    while q:
        i = q.popleft()

        if remaining_bt[i] == 0:
            continue

        start = time
        exec_time = min(tq, remaining_bt[i])
        time += exec_time
        remaining_bt[i] -= exec_time
        end = time
        gantt.append((i + 1, start, end))

        if remaining_bt[i] == 0:
            completed += 1
            finish_time[i] = time
        else:
            # Still remaining burst time, push back to queue
            q.append(i)

        if completed == n:
            break

    wt = [0] * n
    tat = [0] * n
    for i in range(n):
        tat[i] = finish_time[i]          # since arrival = 0
        wt[i] = tat[i] - burst_times[i]

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n

    print("\n=== Round Robin Scheduling ===")
    print(f"Time Quantum = {tq}")
    print("\nGantt Chart:")
    print_gantt_chart(gantt)

    print("\nPID\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1}\t{burst_times[i]}\t{wt[i]}\t{tat[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def print_gantt_chart(gantt):
    """
    Pretty print a Gantt chart from a list of (pid, start, end).
    Example: | P1 (0-3) | P2 (3-7) | ...
    """
    chart = ""
    timeline = ""
    for pid, start, end in gantt:
        chart += f"| P{pid} "
    chart += "|"

    # timeline below the chart
    times = [gantt[0][1]] + [end for (_, _, end) in gantt]
    timeline = " ".join(str(t) for t in times)

    print(chart)
    print(timeline)


def main():
    while True:
        print("\n==== CPU Scheduling Simulator ====")
        print("1. Priority Scheduling (Non-preemptive)")
        print("2. Round Robin Scheduling")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            priority_scheduling()
        elif choice == "2":
            round_robin()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
