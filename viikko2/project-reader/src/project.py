class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors=authors
        self.license=license

    def _stringify_items(self, items):
        return "\n".join(f"- {item}" for item in items) if items else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:"
            f"\n{self._stringify_items(self.authors)}"
            f"\n"
            f"\nDependencies:"
            f"\n{self._stringify_items(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:"
            f"\n{self._stringify_items(self.dev_dependencies)}"
        )
