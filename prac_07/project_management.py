import datetime
from prac_07.project import Project

MENU = "Menu:\nL - Load projects\nS - Save projects\nD - Display projects\nF - Filter projects by date\nA - Add new project\nU - Update project\nQ - Quit"

FILE_NAME = 'projects.txt'
NAME_INDEX = 0
DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
PERCENT_COMPLETE_INDEX = 4


def main():
    """
    Main function to manage the project management software.
    """
    print("Custom-built project management software - Created by Your Name")
    projects = load_projects(FILE_NAME)  # Load existing projects from a file called 'projects.txt'
    print(f"Loaded {len(projects)} projects")
    print(MENU)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            projects = load_projects(FILE_NAME)  # Load projects from file
        elif choice == "S":
            save_projects(FILE_NAME, projects)  # Save projects to file
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_menu(projects)
        elif choice == "A":
            add_new_project_menu(projects)
        elif choice == "U":
            update_project_menu(projects)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    save_projects(FILE_NAME, projects)  # Save updated projects back to the 'projects.txt' file
    print(f"{len(projects)} projects saved\nThank you for using custom-built project management software :)")


def load_projects(filename):
    """
    Load projects from a specified file.
    :param filename: Name of the file to load projects from.
    :return: List of projects.
    """
    projects = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                parts = line.strip().split('\t')
                name = parts[NAME_INDEX]
                start_date = datetime.datetime.strptime(parts[DATE_INDEX].strip(), "%d/%m/%Y").date()
                priority = int(parts[PRIORITY_INDEX])
                cost_estimate = float(parts[COST_INDEX])
                percent_complete = int(parts[PERCENT_COMPLETE_INDEX])
                project = Project(name, start_date, priority, cost_estimate, percent_complete)
                projects.append(project)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while loading projects: {e}")
    return projects


def save_projects(filename, projects):
    """
    Save projects to a specified file.
    :param filename: Name of the file to save projects to.
    :param projects: List of projects to save.
    """
    try:
        with open(filename, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                           f"\t{project.cost_estimate:.1f}\t{project.completion_percentage}\n")
        print(f"Projects saved to '{filename}'")
    except Exception as e:
        print(f"An error occurred while saving the projects: {e}")


def display_projects(projects):
    """
    Display all projects.
    :param projects: List of projects to display.
    """
    print("Projects:")
    for project in projects:
        print(f"  {project}")


def filter_projects_menu(projects):
    """
    Display a menu to filter projects by date.
    :param projects: List of projects to filter.
    """
    try:
        date_str = input("Enter a filter date (dd/mm/yyyy): ")
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date >= filter_date]
        if filtered_projects:
            print("Filtered projects:")
            for project in filtered_projects:
                print(f"  {project}")
        else:
            print("No projects found for the specified date.")
    except ValueError:
        print("Invalid date format. Please use the format dd/mm/yyyy.")


def add_new_project_menu(projects):
    """
    Display a menu to add a new project.
    :param projects: List of projects to add to.
    """
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
        priority = int(priority)
        cost_estimate = float(cost_estimate)
        completion_percentage = int(completion_percentage)
        new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(new_project)
        print("New project added.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please ensure all inputs are valid.")


def update_project_menu(projects):
    """
    Display a menu to update an existing project.
    :param projects: List of projects to update.
    """
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        project_choice = int(input("Project choice: "))
        if 0 <= project_choice < len(projects):
            project = projects[project_choice]
            new_completion_percentage = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_completion_percentage:
                project.completion_percentage = int(new_completion_percentage)
            if new_priority:
                project.priority = int(new_priority)
            print("Project updated.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a valid project choice.")


main()
