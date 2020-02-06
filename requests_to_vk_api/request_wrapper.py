from requests_to_vk_api.request_handler import RequestHandler


class RequestWrapper:

    def __init__(self, person_id, access_tokens, friends_limit_ceil: int, friends_limit_floor: int):

        self.person_id = person_id
        self.request_handler = RequestHandler(person_id, access_tokens, friends_limit_ceil, friends_limit_floor)

        self.first_layer = self.request_handler.request_for_person(self.person_id)

        self.known_persons = self.first_layer
        self.known_persons = self.known_persons.union({person_id})

        # must be edited and sorted
        # firstly - persons with much mutual friends
        self.second_layer = self.request_handler.make_limit_requests(self.first_layer)

        self.second_layer = self.second_layer.difference(self.known_persons)
        print(self.second_layer)
        self.hidden_friends = set()
        self.tmp_hidden_friends = set()

    def check_hidden_friends(self, second_layer=None):

        print("=====================================================================")
        print("===========================START NEW ROUND===========================")
        print("=====================================================================")
        input("\n\n PUSH THE BUTTON, COSMIC JUNIOR")

        self.known_persons = self.known_persons.union(self.tmp_hidden_friends)
        self.tmp_hidden_friends = set()

        if second_layer is None:
            second_layer = self.second_layer

        size_second_layer = len(second_layer)
        count = 0

        friends_dict = dict()
        for person_of_second_layer in second_layer:
            count += 1
            print("progress: ", count, "of ", size_second_layer)
            friends_dict[person_of_second_layer] = self.request_handler.request_for_person(person_of_second_layer)

        # find hidden friends in dict
        for maybe_hidden in friends_dict:
            if self.person_id in friends_dict[maybe_hidden]:
                self.tmp_hidden_friends.add(maybe_hidden)

        self.hidden_friends = self.hidden_friends.union(self.tmp_hidden_friends)

        return bool(self.tmp_hidden_friends)

    def to_print(self):
        print("person id: ", self.person_id)
        print("persons first_layer: ", self.first_layer)
        print("persons second layer: ", self.second_layer)
        print("tmp hidden friends: ", self.tmp_hidden_friends)
        print("known persons: ", self.known_persons)
        print("REAL HIDDEN FRIENDS: ", self.hidden_friends)

    def check_more_hidden_friends(self):

        self.check_hidden_friends()
        a = True
        while a:
            hidden_second_layer = self.request_handler.make_requests(self.tmp_hidden_friends)\
                                                                .difference(self.known_persons)
            a = self.check_hidden_friends(hidden_second_layer)

