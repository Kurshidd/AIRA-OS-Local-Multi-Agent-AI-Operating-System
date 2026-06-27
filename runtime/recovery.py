class ErrorRecovery:

    @staticmethod
    def recover(error):

        text = str(error)

        if "SyntaxError" in text:

            return "Python syntax error detected."

        if "TimeoutExpired" in text:

            return "Execution timed out."

        if "FileNotFoundError" in text:

            return "Requested file does not exist."

        return text