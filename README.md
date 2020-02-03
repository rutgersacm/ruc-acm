# ruc-acm
Repository for the RUC ACM Chapter website. - Webmaster chri55

### Development

#### Setting up the git environment

To submit pull requests, fork this version of the repo, and clone your copy to your machine. After doing this, you need to add the upstream remote tracker to your git environment on your machine to be able to fetch changes back from this version.

```bash 
# Add the remote, call it "upstream" (note that github desktop makes this for you when you clone your fork):

git remote add upstream https://github.com/rutgersacm/ruc-acm.git

# Fetch all the branches of that remote into remote-tracking branches,
# such as upstream/master:

git fetch upstream

# Make sure that you're on your development branch:

git checkout development

# Rewrite your development branch so that any commits of yours that
# aren't already in upstream/development are replayed on top of that
# other branch:

git rebase upstream/development

git push
```

When working, after you've added the remote you only need to run the last 4 commands to ensure your development branch is even with origin.

#### Running the Flask app

To install the requirements and run the development server:
```bash
#only need to do this once.
pip install -r requirements.txt

export FLASK_APP=app.py
flask run
```

Before submitting a pull request, remember to check the .gitignore and set it to remove all unecessary files, such as .pyc, and others.

On ***Windows***, use `set` instead of `export` to set the environment variable.
