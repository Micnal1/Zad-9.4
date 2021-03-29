import json


class Film():
    def __init__(self):
        try:
            with open("films.json", "r") as read:
                self.films_list = json.load(read)
        except FileNotFoundError:
            self.films_list = []

        try:
            with open("comments.json", "r") as read:
                self.comment_list = json.load(read)
        except FileNotFoundError:
            self.comment_list = []

    def all(self):
        return self.films_list

    def create(self, data):
        data.pop('csrf_token')
        data["comments_id"] = []
        self.films_list.append(data)
        self.save()

    def save(self):
        with open("films.json", "w") as write:
            json.dump(self.films_list,write)

        with open("comments.json", "w") as write:
            json.dump(self.comment_list,write)

    def get(self, id):
        return self.films_list[id - 1]

    def update(self, id, data, comment_id):
        data.pop('csrf_token')
        data["comments_id"] = comment_id
        self.films_list[id - 1] = data
        self.save()

    def delete(self, id):
        del self.films_list[id - 1]
        self.save()

    def create_comment(self,id,data):
        username = data.get("login")
        comment = data.get("comment")
        try:
            comment_id = max([i["comment_id"] for i in self.comment_list ]) + 1
        except:
            comment_id = 1

        comment = {"login":username,"comment":comment,"comment_id":comment_id}

        self.comment_list.append(comment)
        self.films_list[id - 1]["comments_id"].append(comment_id)

        self.save()

    def show_comments(self, id):
        comments_id = self.get(id)["comments_id"]
        comments = [i for i in self.comment_list if i["comment_id"] in comments_id]
        return comments


class Memory():
    def __init__(self):
        self.id = None

    def remember_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


memory = Memory()


films = Film()