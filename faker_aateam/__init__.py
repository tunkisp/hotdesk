################################################################################
# faker_aateam\__init__.py - Provider script for Faker that adds fake advanced
#                            analytics characteristics. This file should be
#                            contained in an appropriately named directory if
#                            used manually, or should be kept as-is if pulled
#                            remotely.
#
# AUTHOR: Pete Tunkis (tunkisp@gmail.com)
# DATE: 2022-01-19
#
# REVISION HISTORY
#
# tunkisp    2022-01-19    Added meta/description, reorganized directories;
#                          added language, employment status, fixed issue where
#                          fake role and platforms not outputting correctly.
#
################################################################################

from faker.providers import BaseProvider
import random

# Create sourcelists
TITLES = [
    'Data Scientist'
    , 'Data Engineer'
    , 'ML Ops/Implementation'
    , 'Software Developer'
    , 'Cloud Architect'
    , 'Database Architect'
    , 'Data Analyst'
    , 'Business Analyst'
    , 'Business Intelligence Developer'
    , 'Web Developer'
    , 'UX/UI Researcher'
    , 'UX/UI Designer'
    , 'Project Manager'
]

LANGUAGES = [
    'R'
    , 'Python'
    , 'MatLab'
    , 'Julia'
    , 'C/C++'
    , 'Java'
    , 'html'
    , 'GraphQL'
    , 'SQL'
    , 'angular'
]

CLOUD = [
    'AWS'
    , 'Azure'
    , 'Google'
]

STATUS = [
    'Salaried'
    , 'Contractor - FT'
    , 'Contractor - PT'
]

# Create provider class that adds fake advanced analytics data
class AATeam(BaseProvider):
    def aa_role(self):
        # Job title
        role = random.choice(TITLES)

        return role

    def aa_exp(self):
        # Years of experience
        exp = random.randint(1, 10)

        return exp

    def aa_cloud(self):
        # Preferred cloud platform
        platform = random.choice(CLOUD)

        return platform

    def aa_language(self):
        # Languages known
        langlist = random.sample(LANGUAGES, k = random.randint(1, 5))

        # Preferred language
        preflang = random.choice(langlist)

        return langlist, preflang

    def aa_status(selfself):
        # Status whether contractor or salaried
        status = random.choice(STATUS)

        return status



