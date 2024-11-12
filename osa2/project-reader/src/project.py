class Project:
    def __init__(self, name, description, authors, dependencies, dev_dependencies, license):
        self.name = name
        self.description = description
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies) if dependencies else "-"

    def _stringify_authors(self, authors):
        return "\n- ".join(authors) if authors else "-"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"Authors:\n- {self._stringify_authors(self.authors)}\n"
            f"License: {self.license or '-'}\n"
            f"Dependencies:\n- {self._stringify_dependencies(self.dependencies)}\n" 
            f"Development dependencies:\n- {self._stringify_dependencies(self.dev_dependencies)}" 
        )