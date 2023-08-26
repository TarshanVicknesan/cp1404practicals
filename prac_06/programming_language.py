class Language:
    """Class for storing programming language information."""

    def __init__(self, lang_name, typing_style, supports_reflection, year_introduced):
        """Initialize a Language instance."""
        self.lang_name = lang_name
        self.typing_style = typing_style
        self.supports_reflection = supports_reflection
        self.year_introduced = year_introduced

    def __str__(self):
        """Return a formatted string representation of a Language instance."""
        reflection_str = "Reflection supported" if self.supports_reflection else "No reflection support"
        return f"{self.lang_name}, Typing: {self.typing_style}, {reflection_str}, Introduced: {self.year_introduced}"

    def is_dynamic_typing(self):
        """Check if the language has dynamic typing."""
        return self.typing_style == "Dynamic"


def demonstrate_languages():
    """Demonstrate the use of the Language class."""
    ruby_lang = Language("Ruby", "Dynamic", True, 1995)
    python_lang = Language("Python", "Dynamic", True, 1991)
    vb_lang = Language("Visual Basic", "Static", False, 1991)

    lang_list = [ruby_lang, python_lang, vb_lang]
    print(python_lang)

    print("Languages with dynamic typing:")
    for lang in lang_list:
        if lang.is_dynamic_typing():
            print(lang.lang_name)


if __name__ == "__main__":
    demonstrate_languages()
