class StringUtils:
    def reverse_string(self, s: str) -> str:
        if not isinstance(s, str):
            raise TypeError("Должна быть пережана строка")
        return s[::-1]

    def get_initials(self, fullname: str) -> str:
        if not isinstance(fullname, str):
            raise TypeError("Должна быть пережана строка")
        if not fullname:
            raise ValueError("Должно быть передано хотя бы имя")
        return "".join(word[0].upper() for word in fullname.strip().split())
