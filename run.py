import os
from cohortextractor import StudyDefinition, patients

os.environ[
    'DATABASE_URL'] = 'mssql+pyodbc://sa:SanaParveen1234@localhost:1433' \
                      '?driver=ODBC+Driver+17+for+SQL+Server'
# configured custom ms sql backend
study = StudyDefinition(
    # define default dummy data behaviour
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.2,
    },

    # define the study index date
    index_date="2020-01-01",

    # define the study population
    population=patients.all(),

    # define the study variables
    age=patients.age_as_of("index_date"),

    # id=patients.donors_choose_with_is_exciting_and_fully_funded(None)

    # more variables ...
)
print(
    study.to_sql())  # this method is lazily evaluated, it wont actually
# read the data until and unless we call some action methods. `to_sql` only generates the raw sql queries which needs to
# be executed on any given backend

print(study.to_file("/Users/sanaparveen/Desktop/JOB/GIT/cohort-extractor/temp1.csv"))
