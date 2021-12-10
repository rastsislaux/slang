import re

class Utils:

    """Contains utilities to format the source code"""

    @staticmethod
    def remove_comments(source: str) -> str:
        """Removes C-like comments using regexp"""

        return re.sub(
            r"/[*]([^*]|([*][^/]))*[*]+/", "", source
        )

    @staticmethod
    def remove_newlines(source: str) -> str:

        """Removes all newlines"""

        return source.replace('\n', '')

    @staticmethod
    def strip_lines(source: list) -> list:

        """Strips all the lines"""

        lines = []
        for s_line in source:
            lines.append(s_line.replace('\n', ''))
        return lines
