import os
os['PIPELINE_ENGINE'] = 'local'

from {{cookiecutter.project_name_normalized}}_pipeline import ingest_data

def test_ingest_data(self):
    data = ingest_data()
    assert not data.empty