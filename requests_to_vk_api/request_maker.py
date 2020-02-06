import requests
from access_tokens.access_token import AccessToken


class RequestMaker:
    """
    MUST BE SINGLETON
    """
    def __init__(self, access_token: AccessToken, friends_limit_ceil=999999, friends_limit_floor=0):
        self.access_token = access_token
        self.ceil_limit = friends_limit_ceil
        self.floor_limit = friends_limit_floor
        self.request_string = "https://api.vk.com/method/friends.get?user_id={}&access_token={}&v=5.52"

    def get_friends_list_from_request(self, person_id):
        token = self.access_token.get_token()
        link = self.request_string.format(person_id, token)
        request = requests.get(link).json()
        try:
            '''
            All elements type in friends_list is <class 'int'>, we optimize it
            '''
            return request['response']['items']  # must be other class
        except KeyError:
            if request['error']['error_code'] == 6:
                print("we fined for speeding light\n", request)
                return False
            if request['error']['error_code'] == 29:
                print("requests more than stars in universe")
                return False
            if request['error']['error_code'] == 5:
                print("our star has disappeared")
                self.access_token.remove_token(token)
                return False
            else:
                print("\n\nSTRANGE ERROR\n\n", request, "\n\n")
                return []

    def friends_request(self, person_id):
        friends_list = self.get_friends_list_from_request(person_id)
        if not isinstance(friends_list, list):
            while not friends_list:
                friends_list = self.get_friends_list_from_request(person_id)
        return friends_list

    def friends_request_with_limit(self, person_id):
        friends_list = self.friends_request(person_id)

        if (self.floor_limit < len(friends_list)) and (self.ceil_limit > len(friends_list)):
            return friends_list
        else:
            return []


class ParallelRequestMaker(RequestMaker):
    def __init__(self, access_tokens, friends_limit_ceil):
        RequestMaker.__init__(access_tokens, friends_limit_ceil)

    def parallel_get_friends(self):
        pass
