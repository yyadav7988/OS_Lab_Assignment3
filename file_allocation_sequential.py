"""
file_allocation_sequential.py

Simulates Sequential File Allocation.
"""

def main():
    total_blocks = int(input("Enter total number of blocks: "))
    block_status = [0] * total_blocks  # 0 = free, 1 = allocated

    n = int(input("Enter number of files: "))

    for i in range(n):
        print(f"\n--- File {i+1} ---")
        start = int(input(f"Enter starting block for file {i+1}: "))
        length = int(input(f"Enter length of file {i+1}: "))

        allocated = True
        # Check if all required blocks are free and within range
        for j in range(start, start + length):
            if j >= total_blocks or block_status[j] == 1:
                allocated = False
                break

        if allocated:
            for j in range(start, start + length):
                block_status[j] = 1
            print(f"File {i+1} allocated from block {start} to {start + length - 1}")
        else:
            print(f"File {i+1} cannot be allocated.")

    print("\nFinal Block Status (index: 0 = free, 1 = allocated):")
    print(list(enumerate(block_status)))


if __name__ == "__main__":
    main()
