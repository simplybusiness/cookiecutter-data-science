import os
os['PIPELINE_ENGINE'] = 'local'

from the_gii_pipeline import model_testing

def test_model_testing(self):
    data = model_testing()
    assert not data.empty