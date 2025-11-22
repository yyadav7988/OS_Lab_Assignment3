"""
file_allocation_indexed.py

Simulates Indexed File Allocation.
"""

def main():
    total_blocks = int(input("Enter total number of blocks: "))
    block_status = [0] * total_blocks  # 0 = free, 1 = allocated

    n = int(input("Enter number of files: "))

    for i in range(n):
        print(f"\n--- File {i+1} ---")
        index = int(input(f"Enter index block for file {i+1}: "))

        if index < 0 or index >= total_blocks:
            print("Invalid index block.")
            continue

        if block_status[index] == 1:
            print("Index block already allocated.")
            continue

        count = int(input("Enter number of data blocks: "))
        data_blocks = list(map(int, input("Enter block numbers (space separated): ").split()))

        # Validate number of blocks
        if len(data_blocks) != count:
            print("Invalid input: number of data blocks does not match the count.")
            continue

        # Validate each block
        invalid = False
        for blk in data_blocks:
            if blk < 0 or blk >= total_blocks:
                print(f"Block {blk} is out of range.")
                invalid = True
                break
            if block_status[blk] == 1:
                print(f"Block {blk} is already allocated.")
                invalid = True
                break

        if invalid:
            continue

        # Allocate index and data blocks
        block_status[index] = 1
        for blk in data_blocks:
            block_status[blk] = 1

        print(f"File {i+1} allocated with index block {index} -> {data_blocks}")

    print("\nFinal Block Status (index: 0 = free, 1 = allocated):")
    print(list(enumerate(block_status)))


if __name__ == "__main__":
    main()
