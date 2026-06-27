import os
import re


class RelevanceEngine:

    def __init__(self):
        pass

    # ----------------------------------------------------
    # Tokenize
    # ----------------------------------------------------

    def tokenize(self, text):

        return set(
            re.findall(
                r"[a-zA-Z_][a-zA-Z0-9_]*",
                text.lower()
            )
        )

    # ----------------------------------------------------
    # Score
    # ----------------------------------------------------

    def score(self, prompt, file_info):

        tokens = self.tokenize(prompt)

        score = 0

        path = file_info["path"].lower()

        content = file_info["content"].lower()

        # ----------------------------------------
        # Filename matching
        # ----------------------------------------

        filename = os.path.basename(path)

        for token in tokens:

            if token in filename:

                score += 10

        # ----------------------------------------
        # Path matching
        # ----------------------------------------

        for token in tokens:

            if token in path:

                score += 5

        # ----------------------------------------
        # Content matching
        # ----------------------------------------

        for token in tokens:

            score += content.count(token)

        return score

    # ----------------------------------------------------
    # Rank Files
    # ----------------------------------------------------

    def rank(
        self,
        prompt,
        files,
        top_k=5
    ):

        ranked = []

        for file in files:

            score = self.score(
                prompt,
                file
            )

            ranked.append({

                "score": score,

                "path": file["path"],

                "content": file["content"]

            })

        ranked.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranked[:top_k]


relevance_engine = RelevanceEngine()