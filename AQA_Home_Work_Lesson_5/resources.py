from pathlib import Path
import Photo


def path(file_name):
    return str(
        Path(Photo.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )
