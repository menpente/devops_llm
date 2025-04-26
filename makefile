.PHONY: setup run clean

setup:
	python setup_vanna.py

run:
	python run_vanna.py

clean:
	rm -rf vanna_chroma_db
