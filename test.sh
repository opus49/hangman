#!/bin/bash

coverage run -m unittest discover -s tests
coverage report -m
