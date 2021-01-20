import requests
import credentials
import datetime as dt

graph_id = "graph1"

user_param = {
    "token": credentials.token,
    "username": credentials.username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id": graph_id,
    "name": "days of coding",
    "unit": "days",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": credentials.token
}

update_data_config = {
    "date": str(dt.datetime.today().strftime('%Y%m%d')),
    "quantity": "1"
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{credentials.username}/graphs"
update_endpoint = f"{graph_endpoint}/{graph_id}"


def create_user_account():
    response = requests.post(
        url=pixela_endpoint, json=user_param)
    print(response.text)


def create_graph():
    response = requests.post(
        url=graph_endpoint, json=graph_config, headers=headers)


def post_info_to_graph():
    response = requests.post(
        url=update_endpoint, json=update_data_config, headers=headers)
    print(response)


def main():
    # create_user_account()
    # create_graph()
    post_info_to_graph()


main()
