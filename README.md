My AT Repo

# How to install
1. run this command = make -f Makefile install

# How to run one file
# web
1. pytest tests/web/test_login.py --alluredir=allure-results
# api
1. pytest tests/api/users/get_users.py --alluredir=allure-results
