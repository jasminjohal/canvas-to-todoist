# Canvas to Todoist

This application utilizes the Canvas API and Todoist API to automatically transfer the tasks of a course hosted on Canvas into a new Todoist project.

## Getting Started

Follow the instructions below to get the project up and running locally.

## Installation

First, clone this repository:

```sh
$ git clone https://github.com/ORG/PROJECT.git
$ cd PROJECT
```

_Before proceeding, I recommend setting up a [virtual environment](https://docs.python.org/3/library/venv.html)._

Install the dependencies:

```sh
$ pip install -r requirements.txt
```

## Usage

### Creating a .env file

Create a new file in the same folder as the `main.py` script and name it `.env`.
Add the following two lines to the file and replace both `{your_canvas_key}` and `{your_todoist_key}` with your API keys for Canvas and Todoist, respectively.

```
CANVAS_KEY={your_canvas_key}
TODOIST_KEY={your_todoist_key}
```

### Running the app

```sh
$ python main.py
```
