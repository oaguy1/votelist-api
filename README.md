# VoteList API

Backend server for voteable list service. This has been implemented in python 3.8 with the FastAPI library. We are currently targeting PostgreSQL as the data backend, but there is no reason that any SQLAlchemy backend shouldn't work.

## Getting Started

There are a few different methods for getting started. If running locally on your own machine, the commands below should get you going (idealy running in a venv for a fresh python environment).

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0
```

Alternatively, a basic Dockerfile is provided that can be run using docker. Below is how one can build and invoke the image.

```bash
docker build -t votelist .
docker run -p 8000:8000 votelist:latest
```

## Testing

VoteList is a (somewhat) TDD shop. Therefore, running the tests is an essential part of development. We are using pytest, which can be invoked as below (note, using the `python -m` syntax is intentional as it include the project root in the `sys.path` for python)

```bash
python -m pytest
```

## Contributing

Contributins are welcome! Please fork this repo and make a pull request.