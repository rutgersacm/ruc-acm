# ruc-acm.github.io
Repository for the RUC ACM Chapter website. - Webmaster chri55

### Development

Clone the 'development' branch of the repo:

```bash
$ git clone --single-branch --branch development https://github.com/rutgersacm/ruc-acm.git
$ cd ruc-acm
```

Alternatively, to clone *all* branches, remove the `--single-branch` argument from the command above. 

To install the requirements and run the development server:
```bash
$ pip install -r requirements.txt
$ export FLASK_APP='app.py'
$ flask run
```

Before submitting a pull request, remember to check the .gitignore and set it to remove all unecessary files, such as .pyc, and others.

On Windows, use `set` instead of `export` to set the environment variable.
