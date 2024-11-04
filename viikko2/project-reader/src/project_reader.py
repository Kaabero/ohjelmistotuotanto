from urllib import request
from project import Project
import tomli # type: ignore


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_dict = tomli.loads(content)

        license=toml_dict['tool']['poetry']['license']

        name=toml_dict['tool']['poetry']['name']
        
        description=toml_dict['tool']['poetry']['description']
        dependencies=[]

        for dependency in toml_dict['tool']['poetry']['dependencies']:
            dependencies.append(dependency)
   
        dev_dependencies=[]

        for dev_dependency in toml_dict['tool']['poetry']['group']['dev']['dependencies']:
            dev_dependencies.append(dev_dependency)

        authors=[]

        for author in toml_dict['tool']['poetry']['authors']:
            authors.append(author)


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, authors,  license)
