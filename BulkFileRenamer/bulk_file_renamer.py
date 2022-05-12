import resetter


def rename_files(text_to_replace: str, new_text: str, folder: str):
    """
    Ülesande põhiosa lahendage siin.

    Ka 1. lisaülesanne (Faililaiendi filter) tuleks sellesse funktsiooni kirjutada.

    pass statementi võite eemaldada, kui olete juba mingit koodi siia funktsiooni kirjutanud.
    """
    pass


def move_into_folders(folder: str):
    """
    2. lisaülesanne (Failide kaustadesse liigutamine) tuleks lahendada siin.

    pass statementi võite eemaldada, kui olete juba mingit koodi siia funktsiooni kirjutanud.
    """
    pass


def append_date(folder: str):
    """
    3. lisaülesanne (Loomiskuupäeva failinimele lisamine) tuleks lahendada siin.

    pass statementi võite eemaldada, kui olete juba mingit koodi siia funktsiooni kirjutanud.
    """
    pass


if __name__ == '__main__':
    resetter.reset_files()  # See rida taastab testitavad failid algseisundisse.

    # rename_files("test", "WOW NEW TEXT O.o", folder=resetter.TEST_DIR)
    # append_date(folder=resetter.TEST_DIR)
    # move_into_folders(resetter.TEST_DIR)
