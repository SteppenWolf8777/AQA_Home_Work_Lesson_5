from pathlib import Path

import Photo

# def picture_path(file_name):
#     return str(
#         Path(__file__).parent.parent.joinpath("Photo", "test.jpg").resolve()
#     )

def path(file_name):
    return str(
        Path(Photo.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )