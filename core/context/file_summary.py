import os


def summarize(path, content):

    lines = content.count("\n") + 1

    return {

        "path": path,

        "extension": os.path.splitext(path)[1],

        "lines": lines,

        "characters": len(content),

        "preview": content[:500]

    }