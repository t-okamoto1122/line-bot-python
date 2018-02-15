class Reply:
    # def __init__(self, reply_msg , answer):
    #     self.reply_msg = reply_msg
    #     self.answer = answer
    def __init__(self):
        pass
        print("Reply init")

    def reply(self, request_text):
        if request_text == "a":
            return "No.1"
        elif request_text == "b":
            return "No.2"
        else:
            return "No.3"


