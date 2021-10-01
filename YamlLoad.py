import yaml


def get_yaml_data_all(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    data = yaml.load(file_data)
    # 返回一个字典，对应yaml文件中的数据
    return data
# current_path = os.path.abspath(".")
# yaml_path = os.path.join(current_path, "config.yaml")
# get_yaml_data_all(yaml_path)
# 使用get_yaml_data_all函数的示例。