from setuptools import setup

setup(
    name="sfjwt",
    version="1.0.0",
    description="A small repo to provide functions to authenticate against SalesForce.",
    url="https://github.com/Rehket/SalesForceJWT-Server-Auth",
    author="Adam A",
    author_email="aalbright425@gmail.com",
    license="MIT",
    packages=["sfjwt"],
    zip_safe=True,
    install_requires=["requests", "PyJWT", "responses"],
)
