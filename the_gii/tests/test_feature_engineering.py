import os
os['PIPELINE_ENGINE'] = 'local'

from the_gii_pipeline import feature_engineering

def test_feature_engineering(self):
    data = feature_engineering()
    assert not data.empty