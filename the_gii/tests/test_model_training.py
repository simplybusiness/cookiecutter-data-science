import os
os['PIPELINE_ENGINE'] = 'local'

from the_gii_pipeline import model_training

def test_model_training(self):
    data = model_training()
    assert not data.empty