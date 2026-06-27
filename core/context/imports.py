import ast


def extract_imports(code):

    imports = []

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for name in node.names:

                    imports.append(name.name)

            elif isinstance(node, ast.ImportFrom):

                imports.append(node.module)

    except Exception:

        pass

    return imports