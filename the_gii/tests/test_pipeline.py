import os
os['PIPELINE_ENGINE'] = 'local'

from the_gii_pipeline import pipeline

def test_pipeline(self):
    result = pipeline.run()