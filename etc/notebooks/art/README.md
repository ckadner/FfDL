# Jupyter Notebook Using ART to Test the Robustness of Deep Learning Models

This [notebook](ART_model_robustness_check.ipynb) shows how [ART](https://github.com/IBM/adversarial-robustness-toolbox)
can be used to test the robustness of Deep Learning models against adversarial attacks.

## Setup

Before running this notebook for the first time we recommend creating a Python virtual environment.

```bash
# assuming present working directory to be the project root
pip3 install virtualenv
virtualenv .venv/art
.venv/art/bin/pip install -r etc/notebooks/art/requirements.txt
```

Now any time you want to run the notebook make sure to activate the Python virtual environment
and deactivate it when done.

```bash
source .venv/art/bin/activate
jupyter-notebook --notebook-dir etc/notebooks/art
# ... use Control-C to stop the notebook server
deactivate
```

To delete the Python virtual environment run the following command:

```bash
rm -rf .venv/art
```
