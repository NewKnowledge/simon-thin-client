from distutils.core import setup

setup(name='SimonThinClient',
    version='1.0.0',
    description='A thin client for interacting with dockerized simon primitive',
    packages=['SimonThinClient'],
    install_requires=["numpy","pandas","requests","typing"],
    entry_points = {
        'd3m.primitives': [
            'distil.simon = SimonThinClient:simon'
        ],
    },
)
