from pathlib import Path
from services.workspace_indexer import WorkspaceIndexer

indexer = WorkspaceIndexer()
indexer.build_index(Path("."))

print(f"Indexed {len(indexer.files)} files.\n")

results = indexer.find_file("engine")

for file in results:
    print("=" * 60)
    print(file.path)
    print()

    print("Classes:")
    for cls in file.classes:
        print(f"  - {cls}")

    print()

    print("Functions:")
    for func in file.functions:
        print(f"  - {func}")

    print()

    print("Imports:")
    for imp in file.imports:
        print(f"  - {imp}")

    print("=" * 60)

print()
print("=== Symbol Index ===")

for symbol in indexer.symbol_index.symbols:
    print(
        f"{symbol.kind:<10} "
        f"{symbol.name:<30} "
        f"{symbol.file.name}:{symbol.line}"
    )