# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="IBM Watson Machine Learning API",
    author_email="",
    url="",
    keywords=["Swagger", "IBM Watson Machine Learning API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    ## Authorization  Step by step instruction how to use Watson Machine Learning service can be found [here](https://console.ng.bluemix.net/docs/services/PredictiveModeling/using_pm_service_dsx.html#using_pm_service_dsx)  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an &#x60;access token&#x60; using the &#x60;username&#x60; and &#x60;password&#x60; available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  &#x60;&#x60;&#x60;json {     \&quot;url\&quot;: \&quot;https://us-south.ml.cloud.ibm.com\&quot;,     \&quot;access_key\&quot;: \&quot;ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\&quot;,     \&quot;username\&quot;: \&quot;c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\&quot;,     \&quot;password\&quot;: \&quot;030528d4-5a3e-4d4c-9258-5d553513be6f\&quot;,     \&quot;instance_id\&quot;: \&quot;a751c209-954e-dc32-b441-ad56ce7a9f40\&quot; } &#x60;&#x60;&#x60;  Example of obtaining &#x60;access token&#x60; from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  &#x60; curl --basic --user username:password https://us-south.ml.cloud.ibm.com/v4/identity/token &#x60;  The obtained &#x60;access token&#x60; needs to be prepended with &#x60;Bearer&#x60; word and it needs to be passed in the &#x60;Authorization&#x60; header for API calls.  Example of API request with &#x60;Bearer access token&#x60;:  &#x60; curl https://us-south.ml.cloud.ibm.com/v4/models -H \&quot;Authorization: Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6ImU4YmQzZGM3LWI5Y2UtNDY1OC1iZ...\&quot; &#x60; 
    """
)

