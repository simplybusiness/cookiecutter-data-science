import os
os['PIPELINE_ENGINE'] = 'local'

from the_gii_pipeline import validate_data

def test_data_validation(self):
    assert validate_data()