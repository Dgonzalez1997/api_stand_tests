import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={'count': 20})
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)
#response = post_new_user(data.user_body)

def post_kit_by_product(products_id):
    return requests.post(configuration.URL_SERVICE + configuration.KIT_BY_USER_PATH,
                         json=products_id, headers=data.headers)
response = post_kit_by_product(data.products_id);
print(response.status_code)
print(response.json())
