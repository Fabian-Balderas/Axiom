from axiom.config.settings import APP_NAME, VERSION, WELCOME_MESSAGE


def show_banner():
    print("=" * 45)
    print(APP_NAME)
    print(WELCOME_MESSAGE)
    print(f"Version: {VERSION}")
    print("=" * 45)