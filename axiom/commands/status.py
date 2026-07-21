def run(context, args):
    print("\nAxiom Status")
    print("------------")
    print(f"Version : {context.version}")
    print(f"Plugins : {len(context.plugins)}")