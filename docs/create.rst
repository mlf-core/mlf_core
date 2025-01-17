.. _create:

================
Create a project
================

Creating projects from templates is the heart of mlf-core.
Our templates adhere to best practices and try to be as modern as possible. Furthermore, they try to automate tasks such as automatical dependency resolvement and installation, packaging, deployment and more.
To learn more about our templates please visit :ref:`available_templates` and check out your template of interest.

Usage
-------

The creation of a new project can be invoked by

.. code-block:: console

    $ mlf-core create <<output-path>>

which will guide you through the creation process of your (customized) project via prompts and creates your project in the specified directory (if none was given,
 this will be the current working directory). If you do not have mlf-core configured yet, you will be asked to do so. For more details please visit :ref:`config`.


The prompts follow the pattern of domain (e.g. mlflow, package, ...), subdomain (if applicable, e.g. website), framework (e.g. Pytorch) followed by template specific prompts (e.g. testing frameworks, ...).
The project will be created at the current working directory, where mlf-core has been called.


After the project has been created, linting (see :ref:`lint`) is automatically performed to verify that the template creation process was successful.


Finally, you will be asked whether you want to automatically push your new project to Github. Note that for this purpose you need to have mlf-core configured with a Github personal access token.
For more details about the Github support please visit :ref:`github_support`.

Flags
------

- ``--domain`` : To directly create a template of the the corresponding domain.

  All further prompts will still be asked for. Example: ``mlflow``.
  It is also possible to directly create a specific template using its handle
