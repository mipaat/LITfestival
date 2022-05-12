import os
import shutil

TEST_FILENAMES = (
    "test_file_name1.txt",
    "file",
    "random_video.mp4",
    "this should not get affected by your functions.py",
    "hohoho test hehehe.json",
)

TEST_DIR = "test stuff in here"


def reset_files():
    original_dir = os.getcwd()
    for filename in os.listdir():
        if not (filename.endswith(".py") or filename == "venv" or filename == ".idea" or filename == "__pycache__"):
            if os.path.isfile(filename):
                os.remove(filename)
            elif os.path.isdir(filename):
                shutil.rmtree(filename)
    os.mkdir(TEST_DIR)
    os.chdir(TEST_DIR)
    __create_files(TEST_FILENAMES)
    os.chdir(original_dir)


def __create_files(filenames):
    try:
        for filename in filenames:
            with open(filename, "w") as f:
                pass
    except Exception as e:
        print(e)
        print(e.__traceback__)


if __name__ == '__main__':
    reset_files()
