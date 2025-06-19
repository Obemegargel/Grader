import os
from names import NAMES


def main():
    for student_name, repository_name in NAMES:
        command = f"git clone https://github.com/{repository_name} {student_name}"
        os.system(command)


if __name__ == "__main__":
    main()
