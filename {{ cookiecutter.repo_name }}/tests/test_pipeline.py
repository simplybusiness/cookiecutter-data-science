import os
os['PIPELINE_ENGINE'] = 'local'

from {{cookiecutter.project_name_normalized}}_pipeline import pipeline

def test_pipeline(self):
    result = pipeline.run()