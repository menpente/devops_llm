.PHONY: setup run clean load-data retrain

load-data:
	python src/prep/load_data.py

setup:
	python src/setup_vanna.py

run:
	python src/run_vanna.py

retrain:
	python src/train/train_corrections.py

clean:
	rm -rf vanna_chroma_db
