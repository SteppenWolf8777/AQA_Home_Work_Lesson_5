from pathlib import Path


def picture_path():
    str(Path(__file__).parent.parent.joinpath('Photo', "test.jpg").resolve())
