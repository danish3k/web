"""
Author = "Danish Khan"
Version = 1.0
Email : danish3k@gmail.com
"""
import os
import yaml

path = os.path.expanduser('~')
cwd = os.getcwd()


class read_yaml:
    """
    Class starts here
    """

    def __init__(self):
        pass

    def read_yaml_all(self):
        """
        This is for Reading Test Data and xpath
         values You can use this to load any Yaml to create keywords
        In your Python file
        :return: All the key values present in yaml
        """
        data = cwd + '\\data.yaml'
        detail = open(data, 'r')
        doc = yaml.full_load(detail)
        return doc

a= read_yaml().read_yaml_all()
print(a['url'])
