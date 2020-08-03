from dataclasses import dataclass


@dataclass
class MlfcoreTemplateStruct:
    """
    First section declares the variables that all template have in common
    """
    cookietemple_version: str = ''  # Version of mlf-core, which was used for creating the project
    domain: str = ''  # Domain of the template
    language: str = ''  # Primary language
    project_slug: str = ''  # Project name mlf-core uses for almost all further processing
    template_version: str = ''  # Version of the provided mlf-core template
    template_handle: str = ''  # Handle of the specific template, indicating which template is currently used
    github_username: str = ''  # Github username
    is_github_repo: bool = False  # Whether the user wants to create a GitHub repo automatically
    is_repo_private: bool = False  # Whether to create a private Github repository
    is_github_orga: bool = False  # Whether Github repository is part of an organization
    github_orga: str = ''  # Name of the GitHub organization

    """
    This section contains some attributes common to cli, lib, gui, web
    """
    full_name: str = ''  # Name of the template creator/organization
    email: str = ''  # Email of the creator
    project_name: str = ''  # Project's name the template is created for
    project_short_description: str = ''  # A short description of the project
    version: str = ''  # Version of the project; of the form: [0-9]*\.[0-9]*\.[0-9]*
    license: str = ''  # License of the project