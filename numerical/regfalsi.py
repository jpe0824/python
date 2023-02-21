test_pass = 0

def assertEquals(a, b):
    global test_pass
    if a == b:
        print("Pass: ", a)
        test_pass += 1
        return
    print(f"Fail:  expected {b}, but got {a}")

def testRegFalsi():
    pass

def regFalsi():
    pass


def main():
    testRegFalsi()
    print(f"\n{test_pass}/9 tests passed")

if __name__ == '__main__':
    main()