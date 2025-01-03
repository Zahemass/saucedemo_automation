if it's not in the projectfile: python -m venv venv
On Windows: venv\Scripts\activate(optional)

pip install selenium pytest pytest-html pyyaml pylint pandas webdriver-manager
(or)
pip install -r requirements.txt

chrome driver path has to be mentioned in:
conftest.py
utils/config.py
