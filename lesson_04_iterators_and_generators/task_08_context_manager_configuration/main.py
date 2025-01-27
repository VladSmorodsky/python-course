from json_config_context_manager import JsonConfigContextmanager

with JsonConfigContextmanager('config.json') as config:
    config['file_path'] = 'path_config'
    config['config_env'] = 'develop'
