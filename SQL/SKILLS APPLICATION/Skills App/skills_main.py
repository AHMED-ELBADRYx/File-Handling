import os
import skills_db

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_skills(user_id):
    skills = skills_db.fetch_skills(user_id)
    if skills:
        print("Your skills:")
        for skill, progress, _ in skills:
            print(f"{skill}: {progress}%")
    else:
        print("No skills found.")

def add_skill(user_id):
    skill = input("Enter skill name: ").strip().upper()
    if skills_db.skill_exists(skill, user_id):
        print("Skill already exists!")
    else:
        try:
            progress = int(input("Enter skill progress (0-100): "))
            if 0 <= progress <= 100:
                skills_db.add_skill(skill, progress, user_id)
                print("Skill added successfully.")
            else:
                print("Progress must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_skill(user_id):
    skill = input("Enter skill name to update: ").strip().upper()
    if skills_db.skill_exists(skill, user_id):
        try:
            progress = int(input("Enter new progress (0-100): "))
            if 0 <= progress <= 100:
                skills_db.update_skill(skill, progress, user_id)
                print("Skill updated successfully.")
            else:
                print("Progress must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Skill not found. Do you want to add it? (Y/N)")
        if input().strip().upper() == "Y":
            add_skill(user_id)

def delete_skill(user_id):
    skill = input("Enter skill name to delete: ").strip().upper()
    if skills_db.skill_exists(skill, user_id):
        skills_db.delete_skill(skill, user_id)
        print("Skill deleted successfully.")
    else:
        print("Skill not found. Nothing to delete.")

def main():
    skills_db.initialize_db()
    user_id = 1
    while True:
        print("\nSkills Manager")
        print("1. Show Skills")
        print("2. Add Skill")
        print("3. Update Skill")
        print("4. Delete Skill")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_skills(user_id)
        elif choice == "2":
            add_skill(user_id)
        elif choice == "3":
            update_skill(user_id)
        elif choice == "4":
            delete_skill(user_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")
        input("Press Enter to continue...")
        clear_terminal()

if __name__ == "__main__":
    main()