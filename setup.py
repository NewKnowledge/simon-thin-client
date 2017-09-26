from distutils.core import setup

setup(name='SimonThinClient',
    version='1.0',
    description='A thin client for interacting with dockerized simon primitive',
    packages=['SsimonThinClient'],
#   install_requires=["numpy","pandas","pickle","requests","ast","abc","json","typing"],
#    entry_points = {
#        'd3m.primitives': [
#            'distil.simon = SimonThinClient.client:SimonThinClient'
#        ],
#    },
)
