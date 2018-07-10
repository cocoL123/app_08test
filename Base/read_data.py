# __author: Honorbaby
# date: 2018/7/9
import yaml,os



class read_data():
    def __init__(self, file_name):
        self.file_path = os.getcwd()+os.sep+"Data"+os.sep+file_name

    def read_yaml(self):
        with open(self.file_path, "r", encoding='utf-8') as f:
            return yaml.load(f)

    def write_yaml(self, data):
        with open(self.file_path, "w", encoding='utf-8') as f:
            yaml.dump(data, f, encoding='utf-8', allow_unicode=True)