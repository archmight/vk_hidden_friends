from requests_to_vk_api.requests_main import MainFriendsRequests

if __name__ == "__main__":
    person_id = int(input("input person id: "))  # 432755358
    friends_limit_ceil = int(input("input friends limit ceil: "))
    friends_limit_floor = int(input("input friends limit floor: "))
    access_tokens = [
                    "dead3db23197167d3ed69adaea4c2c4b923af1d4d21c3907da15e06fa36ed2f0f240ce7b311c49ea2c2f7",
                    "dead18c23763ab6c6ee33819fdf57d4d1ef6d175371db3b3cb9e0fc57eeb9d7c4831585fd93547e8b6203",
                    "dead10d23382be118dfbe048a6b316a9f8816c60e27fed54b5160d40b93d85a8dfe2b7f3950a65092e220"
                     ]
    a = MainFriendsRequests(person_id, access_tokens, friends_limit_ceil, friends_limit_floor)
    a.get_hidden_friends()
    a.to_print()

# if __name__ == "__main__":
#     person_id = int(input("input person id: "))
#     friends_limit = int(input("input friends limit: "))
#     access_tokens = ["b9f2c6b5c320ff9871234f78f3650739f01642e9042f8c78fc7755199e8895fa483f7fc8c309cc2018891"
#                         ]
#     a = RequestHandler(person_id, access_tokens, friends_limit)
