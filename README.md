if it's not in the projectfile: python -m venv venv
On Windows: venv\Scripts\activate

pip install selenium pytest pytest-html pyyaml pylint pandas webdriver-manager
pip install -r requirements.txt

chrome driver path has to be mentioned in:
test_workflow.py
conftest.py
utils/config.py
