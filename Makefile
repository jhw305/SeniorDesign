SRC=src/

buildpy: $(SRC)/setup.py
	cd $(SRC) ; ./setup.py install --user
	chmod +x $(SRC)/simlib/src/*.py
