import importlib
import inspect
import pkgutil

from axiom.skills.base import Skill


def discover_skills():
    """
    Discover every Skill subclass inside the axiom.skills package.
    """

    skills = []

    package_name = "axiom.skills"
    package = importlib.import_module(package_name)

    for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):

        if is_pkg:
            continue

        if module_name in ("base", "manager", "registry", "__init__"):
            continue

        module = importlib.import_module(f"{package_name}.{module_name}")

        for _, obj in inspect.getmembers(module, inspect.isclass):

            if issubclass(obj, Skill) and obj is not Skill:
                skills.append(obj())

    return skills