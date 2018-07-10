# __author: Honorbaby
# date: 2018/7/9
from Base.read_data import read_data


def get_data():
    data_list = []
    data = read_data("data.yml").read_yaml().get('Login_data')
    for i in data:
        for j in i.keys():
            data_list.append((j, i.get(j).get("phone"), i.get(j).get("passwd"),
                              i.get(j).get("get_mess"), i.get(j).get("expect_message"),
                              i.get(j).get("tag")))
    print(data_list)

get_data()