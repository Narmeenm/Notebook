import datetime
import  itertools
class Note:
    last_id = itertools.count()
    def __init__(self,memo,tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        self.id =next(self.last_id)
    def match(self,filter):
        list_words = self.memo.split()
        if filter in list_words:
            return True
        else:return False

class Notebook:
    def __init__(self):
        self.notes = []
    def new_note(self,memo,tags=''):
        self.notes.append(Note(memo,tags))

    def modify_memo(self,note_id,memo):
        if self._find_note(note_id) !=None:
            self._find_note(note_id).memo = memo
        else:
            print("no note like that")

    def modify_tags(self,note_id,tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
    def search(self,filter):
        return[note for note in self.notes if note.match(filter)]

    def _find_note(self,note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

main_tasks = Notebook()
main_tasks.new_note("hello flori")
print(main_tasks._find_note(0))
main_tasks.modify_memo(0,"flori is great")
print(main_tasks.notes[0].memo)
main_tasks.modify_memo(1,"no way")
