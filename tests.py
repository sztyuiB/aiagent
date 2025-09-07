from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def tests():
    cases = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../")
    ]

    for case in cases:
        print(f"Result for {case[1]} directory:")
        print(get_files_info(case[0], case[1]))
        print("")

def test_content():
    cases = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py")
    ]

    for case in cases:
        print(f"Result for {case[1]} file:")
        print(get_file_content(case[0], case[1]))
        print("")

def test_write():
    cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed")
    ]

    for case in cases:
        print(f"Result for {case[1]} file:")
        print(write_file(case[0], case[1], case[2]))
        print("")

def test_run():
    cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py")
    ]

    for case in cases:
        if len(case) > 2:
            print(f"Result for {case} file:")
            print(run_python_file(case[0], case[1], case[2]))
            print("")
        else:
            print(f"Result for {case} file:")
            print(run_python_file(case[0], case[1]))
            print("")

test_run()