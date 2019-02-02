dist:
	python setup.py sdist bdist_wheel

update_pypi_test:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

update_pypi:
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -Rf build dist

lint:
	pylint icelander_generator --rcfile=setup.cfg
