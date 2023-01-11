import pathlib

from datetime import datetime

class Directory:
    def __init__(self):
        home = pathlib.Path.home()
        self.default_path = home / "Documents" / "MaxWave"
        create_directory(self.default_path)
        

class ProjectDirectory(Directory):
    def __init__(self, project_path=None, project_name=None):
        super().__init__()

        if project_path is not None:
            self.project_path = pathlib.Path(project_path)
            create_directory(self.project_path)
            create_directory(self.project_path / project_name)

        else:
            create_directory(self.default_path / project_name)


class TempsDirectory(Directory):
    def __init__(self):
        super().__init__()
        now = datetime.now()
        self.temp_path = self.default_path/ "Temp" / f"temp_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}"
        create_directory(self.temp_path)


def create_directory(path: pathlib.Path):
    path.mkdir(parents=True, exist_ok=True)

