################################################################################
# test.py - Scratchpad/space to test out hotdesk code in action
#
# AUTHOR: Pete Tunkis (tunkisp@gmail.com)
# DATE: 2022-01-19
#
# REVISION HISTORY
#
#
#
################################################################################
import pandas as pd
from faker import Faker

import faker_aateam
import pandas as pd

fake = Faker()
# Set Faker seed, uncomment for replication
# Faker.seed(8675309)

fake.add_provider(faker_aateam.AATeam)

###
# Test individual random outputs
print(fake.aa_role())
print(fake.aa_exp())
print(fake.aa_cloud())
print(fake.aa_language())
print(fake.aa_status())

###
# Create a dataframe of fake individuals with Faker's help
def make_team(n):
    fake_team = [{'Person ID': x+1000
                  , 'Name': fake.name()
                  , 'Role': fake.aa_role()
                  , 'Years Experience': fake.aa_exp()
                  , 'Preferred Cloud Platform': fake.aa_cloud()
                  , 'Languages Known': fake.aa_language()[0]
                  # , 'Preferred Language': fake.aa_language()[1]
                  # TODO: Preferred Language currently doesn't sample from
                  #  aa_language()[0], leading to preferred languages not in the
                  #  known set above.
                  , 'Employee Status': fake.aa_status()} for x in range(n)]

    return fake_team

fake_team_df = pd.DataFrame(make_team(n=100))


fake_team_df.head(10)