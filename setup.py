from setuptools import setup

setup(
    name="rehket",
    version="0.0.1",
    description="A small repo to provide functions to authenticate against SalesForce.",
    url="https://github.com/Rehket/SalesForceJWT-Server-Auth",
    author="Adam A",
    author_email="aalbright425@gmail.com",
    license="MIT",
    packages=["SFJWT"],
    zip_safe=True,
    install_requires=["requests", "PyJWT", "responses"],
)
