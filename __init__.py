from mycroft import MycroftSkill, intent_file_handler


class Recite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('recite.intent')
    def handle_recite(self, message):
        poem = message.data.get('poem')
        text = ''

        self.speak_dialog('recite', data={
            'poem': poem,
            'text': text
        })


def create_skill():
    return Recite()

