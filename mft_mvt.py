"""
mft_mvt.py

Simulates:
- MFT (Multiprogramming with Fixed Tasks / Fixed partitions)
- MVT (Multiprogramming with Variable Tasks / Variable partitions)
"""

def MFT():
    """
    Fixed-size partitions.
    Checks whether each process can fit into a fixed partition.
    """
    print("\n=== MFT (Fixed Partition) Simulation ===")
    mem_size = int(input("Enter total memory size: "))
    part_size = int(input("Enter partition size: "))
    n = int(input("Enter number of processes: "))

    partitions = mem_size // part_size
    internal_frag = 0

    print(f"Memory divided into {partitions} partitions of size {part_size}.")

    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))

        if psize <= part_size:
            internal_frag += (part_size - psize)
            print(f"Process {i+1} of size {psize} allocated.")
        else:
            print(f"Process {i+1} of size {psize} too large for fixed partition.")

    print(f"Total internal fragmentation: {internal_frag}")


def MVT():
    """
    Variable-size partitions.
    Memory is allocated as needed until exhausted.
    """
    print("\n=== MVT (Variable Partition) Simulation ===")
    mem_size = int(input("Enter total memory size: "))
    n = int(input("Enter number of processes: "))

    for i in range(n):
        psize = int(input(f"Enter size of Process {i+1}: "))

        if psize <= mem_size:
            print(f"Process {i+1} of size {psize} allocated.")
            mem_size -= psize
            print(f"Remaining memory: {mem_size}")
        else:
            print(f"Process {i+1} of size {psize} cannot be allocated. Not enough memory.")

    print(f"Final remaining memory (external fragmentation): {mem_size}")


def main():
    while True:
        print("\n==== MFT & MVT Memory Management ====")
        print("1. MFT")
        print("2. MVT")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            MFT()
        elif choice == "2":
            MVT()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
