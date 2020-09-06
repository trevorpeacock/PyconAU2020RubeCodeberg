default: run

venv:
	virtualenv venv
	bash -c ". venv/bin/activate && pip install -r requirements.txt"

run: venv
	bash -c ". venv/bin/activate && python first_program.py"

test: venv
	bash -c ". venv/bin/activate && python tests.py"

generate: venv
	bash -c ". venv/bin/activate && python generate.py"

clean:
	rm -dfr venv
