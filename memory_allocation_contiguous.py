"""
memory_allocation_contiguous.py

Simulates First-fit, Best-fit, and Worst-fit contiguous memory allocation.
"""

def allocate_memory(strategy):
    """
    strategy: "first", "best", or "worst"
    """
    print(f"\n=== {strategy.capitalize()} Fit Allocation ===")
    partitions = list(map(int, input("Enter partition sizes (space separated): ").split()))
    processes = list(map(int, input("Enter process sizes (space separated): ").split()))

    allocation = [-1] * len(processes)  # which partition each process gets (-1 = not allocated)

    for i, psize in enumerate(processes):
        idx = -1

        if strategy == "first":
            for j, part in enumerate(partitions):
                if part >= psize:
                    idx = j
                    break

        elif strategy == "best":
            best_fit = float("inf")
            for j, part in enumerate(partitions):
                if part >= psize and part < best_fit:
                    best_fit = part
                    idx = j

        elif strategy == "worst":
            worst_fit = -1
            for j, part in enumerate(partitions):
                if part >= psize and part > worst_fit:
                    worst_fit = part
                    idx = j

        if idx != -1:
            allocation[i] = idx
            partitions[idx] -= psize

    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} of size {processes[i]} allocated in Partition {a+1}")
        else:
            print(f"Process {i+1} of size {processes[i]} cannot be allocated")

    print("Remaining partition sizes:", partitions)


def main():
    while True:
        print("\n==== Contiguous Memory Allocation ====")
        print("1. First Fit")
        print("2. Best Fit")
        print("3. Worst Fit")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            allocate_memory("first")
        elif choice == "2":
            allocate_memory("best")
        elif choice == "3":
            allocate_memory("worst")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
