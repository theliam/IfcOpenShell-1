from behave import step

import ifcdata_methods as idm
from utils import switch_locale


the_lang = "fr"


"""
# TODO the next line needs translation
@given("The IFC file has been provided through an argument")
def step_impl(context):
    switch_locale(context.localedir, the_lang)
    idm.provide_ifcfile_by_argument(context)
"""


@step("Les données IFC doivent utiliser le schéma {schema}")
def step_impl(context, schema):
    switch_locale(context.localedir, the_lang)
    idm.has_ifcdata_specific_schema(context, schema)
