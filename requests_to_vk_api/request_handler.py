from access_tokens.access_token import AccessToken
from requests_to_vk_api.request_maker import RequestMaker


class RequestHandler:
    def __init__(self, person_id: int, tokens_list: [], friends_limit_ceil: int, friends_limit_floor: int):
        self.person_id = person_id
        self.access_token = AccessToken(tokens_list)
        self.request_maker = RequestMaker(self.access_token, friends_limit_ceil, friends_limit_floor)

    def request_for_person(self, person_id):
        return set(self.request_maker.friends_request(person_id))

    def limit_request_for_person(self, person_id):
        return set(self.request_maker.friends_request_with_limit(person_id))

    def make_requests(self, persons_id):
        full_set = set()
        for person_id in persons_id:
            full_set = full_set.union(self.request_for_person(person_id))  # bloody union
        return full_set  # https://stackoverflow.com/questions/31486802/python-set-wont-perform-union

    def make_limit_requests(self, persons_id):
        full_set = set()
        for person_id in persons_id:
            full_set = full_set.union(set(self.limit_request_for_person(person_id)))  # bloody union
        return full_set  # https://stackoverflow.com/questions/31486802/python-set-wont-perform-union