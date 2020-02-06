from requests_to_vk_api.request_wrapper import RequestWrapper


class MainFriendsRequests:
    def __init__(self, person_id, access_tokens, friends_limit_ceil, friends_limit_floor):
        self.request_wrapper = RequestWrapper(person_id, access_tokens, friends_limit_ceil, friends_limit_floor)

    def get_hidden_friends(self):
        self.request_wrapper.check_more_hidden_friends()

    def to_print(self):
        self.request_wrapper.to_print()










