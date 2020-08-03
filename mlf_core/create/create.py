from collections import OrderedDict

from mlf_core.create.domains.mlflow_creator import MlflowCreator
from mlf_core.custom_cli.questionary import mlf_core_questionary_or_dot_mlf_core


def choose_domain(domain: str or None, dot_mlf_core: OrderedDict = None):
    """
    Prompts the user for the template domain.
    Creates the .mlf_core file.
    Prompts the user whether or not to create a Github repository

    :param domain: Template domain
    :param dot_mlf_core: Dictionary created from the .mlf_core.yml file. None if no .mlf_core.yml file was used.
    """
    if not domain:
        domain = mlf_core_questionary_or_dot_mlf_core(function='select',
                                                      question='Choose the project\'s domain',
                                                      choices=['mlflow'],
                                                      default='mlflow',
                                                      dot_mlf_core=dot_mlf_core,
                                                      to_get_property='domain')

    switcher = {
        'mlflow': MlflowCreator
    }

    creator_obj = switcher.get(domain.lower())()
    creator_obj.create_template(dot_mlf_core)