from pathlib import Path

def get_resource_path(file_name):
    resource_path = Path('Photo') / file_name
    if not resource_path.exists():
        raise FileNotFoundError(f"Файл не найден: {resource_path}")
    return str(resource_path.absolute())