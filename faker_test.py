from faker.providers import BaseProvider
import random

########### Create sourcelists
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
]

CLOUD = [
    'AWS'
    , 'Azure'
    , 'Google'
]

# Create provider class that adds fake advanced analytics data
class AATeam(BaseProvider):
    def aa_role(self):
        # Job title
        role = self.random_element(TITLES)

        output = random.choice(role)

        return output

    def aa_exp(self):
        # Years of experience
        output = random.randint(1, 10)

        return output

    def aa_cloud(self):
        # Preferred cloud platform
        platform = self.random_element(CLOUD)

        output = random.choice(platform)

        return output

    def aa_language(self):
        # Languages known
        langlist = random.sample(LANGUAGES, k = random.randint(1, 4))

        # Preferred language
        preflang = random.choice(langlist)

        return langlist, preflang


