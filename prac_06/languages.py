from prac_06.programming_language import Language


def run_demo():
    ruby_lang = Language("Ruby", "Dynamic", True, 1995)
    python_lang = Language("Python", "Dynamic", True, 1991)
    vb_lang = Language("Visual Basic", "Static", False, 1991)

    languages_list = [ruby_lang, python_lang, vb_lang]

    print("Programming Languages:")
    for lang in languages_list:
        print(lang)

    print("\nThe languages with dynamic typing are:")
    for lang in languages_list:
        if lang.is_dynamic_typing():
            print(lang.lang_name)


if __name__ == "__main__":
    run_demo()
