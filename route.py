class RouteCipher:

    # Generate hash using weighted ASCII sum
    @staticmethod
    def get_hash(key):
        return sum(ord(ch) * (i + 1) for i, ch in enumerate(key))

    # Create grid (COLUMN-WISE filling)
    @staticmethod
    def create_grid(text, rows, cols):
        text = text.replace(" ", "").upper()  # remove spaces, convert to uppercase
        
        # initialize empty grid
        grid = [['' for _ in range(cols)] for _ in range(rows)]

        index = 0
        # fill column-wise
        for j in range(cols):
            for i in range(rows):
                if index < len(text):
                    grid[i][j] = text[index]
                    index += 1
                else:
                    grid[i][j] = 'X'  # padding

        return grid

    # Print grid for visualization
    @staticmethod
    def print_grid(grid):
        print("\nGrid:")
        for row in grid:
            print(" ".join(row))

    # Spiral traversal based on start position and direction
    @staticmethod
    def spiral(grid, start_pos, clockwise):
        res = ""
        top, bottom = 0, len(grid) - 1
        left, right = 0, len(grid[0]) - 1

        # continue until all layers are traversed
        while top <= bottom and left <= right:

            # Top-Left
            if start_pos == 0:
                if clockwise:
                    # → across top row
                    for i in range(left, right + 1): res += grid[top][i]
                    top += 1
                    # ↓ down right column
                    for i in range(top, bottom + 1): res += grid[i][right]
                    right -= 1
                    # ← across bottom row
                    if top <= bottom:
                        for i in range(right, left - 1, -1): res += grid[bottom][i]
                        bottom -= 1
                    # ↑ up left column
                    if left <= right:
                        for i in range(bottom, top - 1, -1): res += grid[i][left]
                        left += 1
                else:
                    # ↓ down left column
                    for i in range(top, bottom + 1): res += grid[i][left]
                    left += 1
                    # → across bottom row
                    for i in range(left, right + 1): res += grid[bottom][i]
                    bottom -= 1
                    # ↑ up right column
                    if left <= right:
                        for i in range(bottom, top - 1, -1): res += grid[i][right]
                        right -= 1
                    # ← across top row
                    if top <= bottom:
                        for i in range(right, left - 1, -1): res += grid[top][i]
                        top += 1

            # Top-Right
            elif start_pos == 1:
                if clockwise:
                    for i in range(top, bottom + 1): res += grid[i][right]
                    right -= 1
                    for i in range(right, left - 1, -1): res += grid[top][i]
                    top += 1
                    if top <= bottom:
                        for i in range(top, bottom + 1): res += grid[i][left]
                        left += 1
                    if left <= right:
                        for i in range(left, right + 1): res += grid[bottom][i]
                        bottom -= 1
                else:
                    for i in range(right, left - 1, -1): res += grid[top][i]
                    top += 1
                    for i in range(top, bottom + 1): res += grid[i][left]
                    left += 1
                    if left <= right:
                        for i in range(left, right + 1): res += grid[bottom][i]
                        bottom -= 1
                    if top <= bottom:
                        for i in range(bottom, top - 1, -1): res += grid[i][right]
                        right -= 1

            # Bottom-Right
            elif start_pos == 2:
                if clockwise:
                    for i in range(right, left - 1, -1): res += grid[bottom][i]
                    bottom -= 1
                    for i in range(bottom, top - 1, -1): res += grid[i][left]
                    left += 1
                    if left <= right:
                        for i in range(left, right + 1): res += grid[top][i]
                        top += 1
                    if top <= bottom:
                        for i in range(top, bottom + 1): res += grid[i][right]
                        right -= 1
                else:
                    for i in range(bottom, top - 1, -1): res += grid[i][right]
                    right -= 1
                    for i in range(left, right + 1): res += grid[top][i]
                    top += 1
                    if top <= bottom:
                        for i in range(top, bottom + 1): res += grid[i][left]
                        left += 1
                    if left <= right:
                        for i in range(right, left - 1, -1): res += grid[bottom][i]
                        bottom -= 1

            # Bottom-Left
            else:
                if clockwise:
                    for i in range(bottom, top - 1, -1): res += grid[i][left]
                    left += 1
                    for i in range(left, right + 1): res += grid[bottom][i]
                    bottom -= 1
                    if left <= right:
                        for i in range(bottom, top - 1, -1): res += grid[i][right]
                        right -= 1
                    if top <= bottom:
                        for i in range(right, left - 1, -1): res += grid[top][i]
                        top += 1
                else:
                    for i in range(left, right + 1): res += grid[bottom][i]
                    bottom -= 1
                    for i in range(bottom, top - 1, -1): res += grid[i][right]
                    right -= 1
                    if top <= bottom:
                        for i in range(right, left - 1, -1): res += grid[top][i]
                        top += 1
                    if left <= right:
                        for i in range(top, bottom + 1): res += grid[i][left]
                        left += 1

        return res

    # X+1 cipher (shift each letter by 1)
    @staticmethod
    def shift_plus_one(text):
        return "".join('A' if ch == 'Z' else chr(ord(ch) + 1) for ch in text)

    # Main encryption function
    @staticmethod
    def encrypt(text, key, rows, cols):
        grid = RouteCipher.create_grid(text, rows, cols)

        print("\nProcessed Text:", text.replace(" ", "").upper())

        RouteCipher.print_grid(grid)

        # generate rules using hash
        hash_value = RouteCipher.get_hash(key)
        start_pos = hash_value % 4
        clockwise = (hash_value % 2 == 0)

        positions = ["Top-Left", "Top-Right", "Bottom-Right", "Bottom-Left"]

        print("\nHash Value:", hash_value)
        print("Starting Position:", positions[start_pos])
        print("Direction:", "Clockwise" if clockwise else "Anti-Clockwise")

        # perform spiral traversal
        cipher = RouteCipher.spiral(grid, start_pos, clockwise)

        print("\nAfter Route Cipher:", cipher)

        return cipher


# Main execution
if __name__ == "__main__":
    text = input("Enter text: ")
    key = input("Enter key: ")
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))

    result = RouteCipher.encrypt(text, key, rows, cols)

    # ask user for optional X+1 cipher
    choice = input("\nApply X+1 cipher? (yes/no): ").lower()

    if choice in ["yes", "y"]:
        result = RouteCipher.shift_plus_one(result)
        print("\nFinal Encrypted Text (after X+1):", result)
    else:
        print("\nFinal Encrypted Text:", result)