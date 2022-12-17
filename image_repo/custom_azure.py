from storages.backends.azure_storage import AzureStorage


class AzureMediaStorage(AzureStorage):
    account_name = 'iert'
    account_key = 'lxgbjBQg3QNnG9WyT7w5XdOpE6yY5xkM8/9brKohx/3sNs07QE1GBk9u7QIG8hcBXcx1eGd/coFE+AStBiI0HA=='
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = 'iert'
    account_key = 'lxgbjBQg3QNnG9WyT7w5XdOpE6yY5xkM8/9brKohx/3sNs07QE1GBk9u7QIG8hcBXcx1eGd/coFE+AStBiI0HA=='
    azure_container = 'static'
    expiration_secs = None
