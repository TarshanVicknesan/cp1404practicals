import datetime
from prac_07.project import Project

MENU = "Menu:\nL - Load projects\nS - Save projects\nD - Display projects\nF - Filter projects by date\nA - Add new project\nU - Update project\nQ - Quit"


def main():
    """
    Main function to manage the project management software.
    """
    print("Custom-built project management software - Created by Your Name")
    projects = load_projects()  # Load existing projects
    print(f"Loaded {len(projects)} projects")
    print(MENU)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            load_projects_menu(projects)
        elif choice == "S":
            save_projects_menu(projects)
        elif choice == "D":
            display_projects_menu(projects)
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

    save_projects(projects)  # Save updated projects back to a file
    print(f"{len(projects)} projects saved\nThank you for using custom-built project management software :)")


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                parts = line.strip().split('\t')
                name, start_date_str, priority, cost_estimate, completion_percentage = parts
                start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
                projects.append(
                    Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return projects


def save_projects(filename, projects):
    try:
        with open(filename, 'w') as file:
            # Write the header
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")

            # Write each project
            for project in projects:
                file.write(
                    f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate:.1f}\t{project.completion_percentage}\n")
        print(f"Projects saved to '{filename}'")
    except Exception as e:
        print(f"An error occurred while saving the projects: {e}")


def display_projects(projects):
    incomplete_projects = [p for p in projects if p.completion_percentage < 100]
    completed_projects = [p for p in projects if p.completion_percentage == 100]

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered_projects = [p for p in projects if p.start_date > date]
    filtered_projects.sort(key=lambda x: x.start_date)

    print("Filtered projects:")
    for project in filtered_projects:
        print(f"  {project}")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print("New project added.")


def update_project(projects):
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        project_choice = int(input("Project choice: "))
        if 0 <= project_choice < len(projects):
            project = projects[project_choice]
            new_completion_percentage = input("New Percentage: ")
            if new_completion_percentage:
                project.completion_percentage = int(new_completion_percentage)
            new_priority = input("New Priority: ")
            if new_priority:
                project.priority = int(new_priority)
            print("Project updated.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a valid project choice.")


main()
