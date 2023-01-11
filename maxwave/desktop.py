import os
import shutil

from .default import Directory, ProjectDirectory
from .modelers import Modeler


class Desktop:
    def __init__(
        self,
        simulation_type: str = "FDTD",
        project_name: str = "PMaxwave",
        project_path: str = None
    ):
        self.project_name = project_name
        self.simulation_type = simulation_type

        if project_path is not None:
            self.project_path = project_path 
        else:
            self.project_path = Directory().default_path

    
        self.modeler = Modeler()
        self.temp_directory = self.modeler.temp_directory
    

    
    def Validation(self):
        self.project_path = ProjectDirectory(
            project_path=self.project_path, 
            project_name=self.project_name        
        ).default_path

        
    def Simulation(self):
        pass

    

