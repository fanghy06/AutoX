# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(name="automl-x",
        version="0.1.2",
        description="automl tools",
#         author="caihengxing",
#         author_email="caihengxing@4paradigm.com",
        url='https://github.com/fanghy06/autox1',
        install_requires=[
            'lightgbm',
            'xgboost',
            # 'pytorch-tabnet',
            'torch',
            'numpy',
            'pandas',
            'sklearn',
            'tqdm',
            'optuna',
            'img2vec_pytorch'
        ],
        python_requires='>=3.6',
        packages=find_packages(exclude=['data', 'demo', 'img', 'sub', 'test',
                                        'run.py', 'run_oneclick.py', 'submit.py']),
        include_package_data=True,
        zip_safe=False
        )
# python setup.py sdist build
# twine upload dist/*
