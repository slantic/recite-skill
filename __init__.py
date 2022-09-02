from mycroft import MycroftSkill, intent_file_handler

class Recite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('recite.intent')
    def handle_recite(self, message):
        poem = message.data.get('poem')
        with self.file_system.open('poems/' + poem.replace(" ", "_"), "r") as f:
            text = f.read()

        self.speak_dialog('recite', data={
            'poem': poem,
            'text': text
        })

    @intent_file_handler('list.intent')
    def handle_list(self):
        with self.file_system.open('poems/list.txt', "r") as f:
            poems_list = f.read()

        self.speak_dialog('list', data={
            'poems_list': poems_list
        })

def create_skill():
    return Recite()

