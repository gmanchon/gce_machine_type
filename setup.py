
from setuptools import setup

setup(
    name="gce_machine_type",
    version="0.1",
    description="List GCE machine types",
    install_requires=["click"],
    packages=["gce_machine_type"],
    scripts=["scripts/gce"],
    )
