import yaml

def getYAMLDataAll(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    data = yaml.load(file_data)
    # 返回一个字典，对应yaml文件中的数据
    return data