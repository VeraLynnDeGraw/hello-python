Yay—**all 3 tests passed!** Let’s make the README explain setup, running the app, and testing it.

Open it:

```bash
nano README.md
```

Replace the contents with this:

```markdown
# Hello Python

A small Python project that makes an HTTP request to a URL and reports whether it succeeded. It uses `requests`, includes timeout and error handling, and has automated tests written with `pytest`.

## Requirements

- Python 3
- Git
- An internet connection to make real HTTP requests

These commands use a Linux/macOS-style terminal. The project was developed on Arch Linux.

## Set up

Clone the repository and enter the project directory:

```bash
git clone https://github.com/VeraLynnDeGraw/hello-python.git
cd hello-python
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the app’s dependencies and the development dependency used for testing:

```bash
python -m pip install -r requirements-dev.txt
```

## Run

Run the app using its default URL, `https://example.com`:

```bash
python app.py
```

Expected output when the request succeeds:

```text
Request succeeded: 200
```

You can also provide a different URL:

```bash
python app.py https://example.com
```

The request uses a 10-second timeout. If the request fails or times out, the app prints an error message and exits with a nonzero status code.

## Run the tests

```bash
python -m pytest -q
```

The tests cover a successful response, a timeout, and an HTTP error. They use mocked responses, so those tests do not need to contact the internet.

## Project files

- `app.py` — command-line app
- `requirements.txt` — app dependencies
- `requirements-dev.txt` — app and test dependencies
- `tests/test_app.py` — automated tests
- `.gitignore` — files Git should ignore, including `.venv`

## License

See (LICENSE).
```

Save with **Ctrl+O**, press **Enter**, and exit with **Ctrl+X**. Then review what changed:

```bash
git diff -- README.md
```

If it looks good, commit and push it:

```bash
git add README.md
git commit -m "Expand project README"
git push
```
