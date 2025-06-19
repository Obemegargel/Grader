import os
from names import NAMES


DOTNET = "\"C:\\Program Files\\dotnet\\dotnet\""
ASSIGNMENT = "prove/Develop03" #"prove/Develop02"

def main():
    # get name to grade
    selected_name = input("Enter the name of the student you would like to grade, or click enter to grade all: ").strip().lower()
    start_grading = not selected_name # if nothing is selected for a specific name, just grade as normal

    # Attempt at letting it keep going after grading specified name.
    for student_name, repository_name in NAMES:
        # keep going if not selected name
        if not start_grading:
            if selected_name == student_name.lower():
                print(f"Starting grading at {student_name.lower()}")
                input("Press enter to continue (from this starting point)...")
                print()
                start_grading = True
        # else: # once it is set to true it grades like normal
        #     continue

    # for student_name, repository_name in NAMES:
    #     # keep going if not selected name
    #     if selected_name and selected_name != student_name.lower():
    #         print(f"grading {selected_name} / {student_name}")
    #         continue
        if start_grading:
            print(f"Grading: {student_name}")
            input("Press enter to continue...")
            print()
            try:
                os.chdir(student_name)
                os.system("git pull --all")
                os.chdir(ASSIGNMENT)
                os.system(f"{DOTNET} run")
                print()
                print(f"finished Grading: {student_name}")
                input("Press enter to continue...")
            except FileNotFoundError as e:
                print(f"Error: {e}")
                print(f"Skipping {student_name} due to missing folder.")
            finally:   
                print()
                print("______________________________________________________")
                print()
                os.chdir("../../..")


if __name__ == "__main__":
    main()