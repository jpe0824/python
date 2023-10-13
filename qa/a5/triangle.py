def check_triangle(sides: list) -> str:
    a, b, c = sides
    if a <= 0 or a + b <= c:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

def main():
    with open("./a5_test_cases.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                print(line)
                continue
            sides = [int(x) for x in line.split()]
            print(check_triangle(sides))

if __name__ == "__main__":
    main()