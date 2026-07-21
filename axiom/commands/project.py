def run(context, args):

    if len(args) == 0:
        print("Usage:")
        print("  project open <name>")
        print("  project status")
        print("  project close")
        return

    action = args[0].lower()

    if action == "open":

        if len(args) < 2:
            print("Usage: project open <name>")
            return

        project_name = " ".join(args[1:])
        context.projects.open(project_name)

        print(f'Current project set to "{project_name}"')

    elif action == "status":

        if context.projects.has_project():
            print(f'Current project: {context.projects.current()}')
        else:
            print("No project is currently open.")

    elif action == "close":

        context.projects.close()
        print("Project closed.")

    else:
        print(f'Unknown project command: "{action}"')

    from axiom.core.registry import register

    register("project", run)