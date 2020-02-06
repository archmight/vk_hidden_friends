
class AccessToken:
    """
    MUST BE SINGLETON
    """
    def __init__(self, tokens: list):
        self.__tokens_list = tokens
        self.__quantity = len(self.__tokens_list)
        self.__alternator = 0

    def get_numbers_of_tokens(self):
        return self.__quantity

    def get_token(self):
        self.__alternator = (self.__alternator + 1) % self.__quantity
        return self.__tokens_list[self.__alternator]

    def get_quantity(self):
        return self.__quantity

    def remove_token(self, token_id):
        self.__tokens_list.remove(token_id)
        self.__quantity -= 1
