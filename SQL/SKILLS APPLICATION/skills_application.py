"""""""""""""""""""""""""""""""""""
    ………………………………………………
.…… SKILLS APPLICATION …….
    ………………………………………………

A simple application to track and manage your skills progress.
"""""""""""""""""""""""""""""""""""

import sqlite3
import os

# Color codes for better UI (optional)
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def clear_terminal():
    """Clear the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_skills(cursor, user_id):
    """Display all skills for the given user."""
    cursor.execute("SELECT * FROM skills WHERE user_id = ?", (user_id,))
    results = cursor.fetchall()
    
    print(f"\n{Colors.OKBLUE}You have {len(results)} skills:{Colors.ENDC}")
    if len(results) > 0:
        print(f"{Colors.HEADER}Your skills and progress:{Colors.ENDC}")
        for row in results:
            print(f"- {row[0]}: {row[1]}%")
    else:
        print(f"{Colors.WARNING}No skills found. Add some skills first!{Colors.ENDC}")

def add_skill(cursor, db, user_id):
    """Add a new skill or update existing one."""
    skill = input("Enter skill name: ").strip().upper()
    
    # Check if skill already exists
    cursor.execute("SELECT skill FROM skills WHERE skill = ? AND user_id = ?", 
                  (skill, user_id))
    
    if cursor.fetchone() is None:
        # Add new skill
        progress = get_int_input("Enter skill progress (0-100): ")
        if 0 <= progress <= 100:
            cursor.execute("INSERT INTO skills(skill, progress, user_id) VALUES(?, ?, ?)", 
                          (skill, progress, user_id))
            print(f"{Colors.OKGREEN}Skill '{skill}' added successfully!{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}Progress must be between 0 and 100{Colors.ENDC}")
    else:
        # Skill exists - offer to update
        choice = input(f"Skill '{skill}' already exists. Update progress? (Y/N): ").upper()
        if choice == "Y":
            update_skill(cursor, db, user_id, skill)

def delete_skill(cursor, db, user_id):
    """Delete a skill from the database."""
    skill = input("Enter skill name to delete: ").strip().upper()
    
    # Verify skill exists
    cursor.execute("SELECT skill FROM skills WHERE skill = ? AND user_id = ?", 
                  (skill, user_id))
    
    if cursor.fetchone() is not None:
        cursor.execute("DELETE FROM skills WHERE skill = ? AND user_id = ?", 
                      (skill, user_id))
        print(f"{Colors.OKGREEN}Skill '{skill}' deleted successfully!{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Skill '{skill}' not found!{Colors.ENDC}")

def update_skill(cursor, db, user_id, skill=None):
    """Update progress of an existing skill."""
    if skill is None:
        skill = input("Enter skill name to update: ").strip().upper()
    
    progress = get_int_input("Enter new progress (0-100): ")
    if 0 <= progress <= 100:
        cursor.execute("UPDATE skills SET progress = ? WHERE skill = ? AND user_id = ?", 
                      (progress, skill, user_id))
        
        # Check if any rows were affected
        if cursor.rowcount > 0:
            print(f"{Colors.OKGREEN}Skill '{skill}' updated to {progress}%!{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}Skill '{skill}' not found!{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Progress must be between 0 and 100{Colors.ENDC}")

def get_int_input(prompt):
    """Get and validate integer input from user."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print(f"{Colors.FAIL}Invalid input. Please enter a number.{Colors.ENDC}")

def return_to_main_menu():
    """Prompt user to return to main menu or quit."""
    choice = input("\nReturn to main menu? (Y/N): ").upper()
    if choice == "Y":
        clear_terminal()
        return True
    return False

def skills_application():
    """Main application function."""
    try:
        # Database connection
        with sqlite3.connect("application.db") as db:
            cursor = db.cursor()
            
            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS skills(
                    skill TEXT, 
                    progress INTEGER, 
                    user_id INTEGER
                )
            """)
            
            user_id = 1  # Default user ID (could be made configurable)
            
            while True:
                # Main menu
                print(f"\n{Colors.HEADER}‹‹‹‹ SKILLS APPLICATION ››››{Colors.ENDC}")
                print(f"{Colors.OKBLUE}What would you like to do?{Colors.ENDC}")
                print("""
[s] Show all skills
[a] Add new skill
[d] Delete a skill
[u] Update skill progress
[q] Quit application
                """)
                
                choice = input("Your choice: ").strip().lower()
                
                if choice == "s":
                    show_skills(cursor, user_id)
                    if not return_to_main_menu():
                        break
                        
                elif choice == "a":
                    add_skill(cursor, db, user_id)
                    if not return_to_main_menu():
                        break
                        
                elif choice == "d":
                    delete_skill(cursor, db, user_id)
                    if not return_to_main_menu():
                        break
                        
                elif choice == "u":
                    update_skill(cursor, db, user_id)
                    if not return_to_main_menu():
                        break
                        
                elif choice == "q":
                    print(f"{Colors.OKBLUE}Closing application. Goodbye!{Colors.ENDC}")
                    break
                    
                else:
                    print(f"{Colors.FAIL}Invalid choice. Please try again.{Colors.ENDC}")
                    
    except sqlite3.Error as e:
        print(f"{Colors.FAIL}Database error: {e}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}An error occurred: {e}{Colors.ENDC}")

if __name__ == "__main__":
    clear_terminal()
    skills_application()