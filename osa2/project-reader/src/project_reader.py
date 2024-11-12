import toml
from urllib import request
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url 

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")

        project_data = toml.loads(content)

        project_name = project_data['tool']['poetry']['name']
        project_description = project_data['tool']['poetry']['description']
        project_license = project_data['tool']['poetry']['license']
        authors = project_data['tool']['poetry']['authors']
        
        dependencies = list(project_data['tool']['poetry']['dependencies'].keys())
        dev_dependencies = list(project_data['tool']['poetry']['group']['dev']['dependencies'].keys())

        return Project(project_name, project_description, authors, dependencies, dev_dependencies, project_license)
