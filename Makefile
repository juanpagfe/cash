# A Makefile for commands I run frequently:

clean:
	rm -rf dist
	rm -rf cash.egg-info
	rm -rf cash/__pycache__

build: clean
	poetry build

install: clean build
	rm dist/cash-*-py2*
	pip3 install dist/cash-*
