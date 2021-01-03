from distutils.core import setup
import py2exe 
import argparse
import os
import subprocess

setup(console=['GeneratePDFs.py']) # Calls setup function to indicate that we're dealing with a single console application
