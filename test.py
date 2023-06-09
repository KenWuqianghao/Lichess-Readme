import lichess.api
user = lichess.api.user('kenwuu')
print(user['perfs']['blitz']['rating'])