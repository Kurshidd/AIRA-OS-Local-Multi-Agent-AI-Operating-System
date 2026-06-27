import ast


def extract_symbols(code):

    symbols = []

    try:

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                symbols.append(
                    f"Function: {node.name}"
                )

            elif isinstance(node, ast.ClassDef):

                symbols.append(
                    f"Class: {node.name}"
                )

    except Exception:

        pass

    return symbols