from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, \
    QHBoxLayout, QGroupBox, QButtonGroup, QListWidget, QTextEdit, QLineEdit, QMessageBox
import os
import json

app = QApplication([])
window = QWidget()
window.setWindowTitle('Smart Notes')
window.setFixedSize(800, 600)

notes = {
    'Добро пожаловать в заметки': {
        'text': 'Заметки - отличный способ поймать вдохновение и организовать мысли.',
        'tags': []},

    'Очерных дырах': {
        'text': 'сингулярность на горизхонте событй отсутсвует. ',
        'tags': ['Черные дыры', 'факты']},

    'Как пользоваться': {
        'text': '',
        'tags': ['помощь']
    }
}

notes_list_widget = QListWidget()
tags_list_widget = QListWidget()
note_text_widget = QTextEdit()
note_text_widget.setPlaceholderText('Note text')
notes_list_name = QLabel('Notes')
tags_list_name = QLabel('Tags')
create_note_button = QPushButton('Create note')
delete_note_button = QPushButton('Delete note')
save_note_button = QPushButton('Save note')
note_line_edit = QLineEdit()
note_line_edit.setPlaceholderText('Enter note name')
tag_create_button = QPushButton('Create tag')
tag_delete_button = QPushButton('Delete tag')
search_button = QPushButton('Search')
tag_line_edit = QLineEdit()
tag_line_edit.setPlaceholderText('Enter tags')

layout0 = QHBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6 = QHBoxLayout()
layout7 = QHBoxLayout()
layout8 = QHBoxLayout()
layout9 = QHBoxLayout()
layout10 = QHBoxLayout()
layout11 = QHBoxLayout()

sub_layout_left = QVBoxLayout()
sub_layout_right = QVBoxLayout()
main_layout = QHBoxLayout()

layout0.addWidget(notes_list_name, alignment=Qt.AlignLeft)
layout1.addWidget(notes_list_widget, alignment=Qt.AlignCenter)
layout2.addWidget(note_line_edit, alignment=Qt.AlignCenter)
layout3.addWidget(create_note_button, alignment=Qt.AlignCenter)
layout3.addWidget(delete_note_button, alignment=Qt.AlignCenter)
layout4.addWidget(save_note_button, alignment=Qt.AlignCenter)
layout5.addWidget(tags_list_name, alignment=Qt.AlignLeft)
layout6.addWidget(tags_list_widget, alignment=Qt.AlignCenter)
layout7.addWidget(tag_line_edit, alignment=Qt.AlignCenter)
layout8.addWidget(tag_create_button, alignment=Qt.AlignCenter)
layout8.addWidget(tag_delete_button, alignment=Qt.AlignCenter)
layout9.addWidget(search_button, alignment=Qt.AlignCenter)

sub_layout_left.addWidget(note_text_widget)
sub_layout_right.addLayout(layout0)
sub_layout_right.addLayout(layout1)
sub_layout_right.addLayout(layout2)
sub_layout_right.addLayout(layout3)
sub_layout_right.addLayout(layout4)
sub_layout_right.addLayout(layout5)
sub_layout_right.addLayout(layout6)
sub_layout_right.addLayout(layout7)
sub_layout_right.addLayout(layout8)
sub_layout_right.addLayout(layout9)
main_layout.addLayout(sub_layout_left)
main_layout.addLayout(sub_layout_right)

window.setLayout(main_layout)


def dump_notes():
    file = open('notes.json', 'w', encoding='utf-8')
    json.dump(notes, file)
    file.close()


def save_note():
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('No note select items')
        popup.exec_()
        return
    key = notes_list_widget.selectedItems()[0].text()
    note_text = note_text_widget.toPlainText()
    global notes
    notes[key]['text'] = note_text
    dump_notes()


def show_note():
    key = notes_list_widget.selectedItems()[0].text()
    note_text_widget.setText(notes[key]['text'])
    tags_list_widget.clear()
    tags_list_widget.addItems(notes[key]['tags'])


def create_note():
    name = note_line_edit.text()
    if name == '':
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('Note name cannot be empty')
        popup.exec_()
        return
    if name in notes:
        popup_2 = QMessageBox()
        popup_2.setWindowTitle('Error')
        popup_2.setText('Provided with name already exists')
        popup_2.exec_()
        return

    notes[name] = {
        'text': '',
        'tags': []
    }
    dump_notes()
    notes_list_widget.clear()
    notes_list_widget.addItems(notes)


def delete_note():
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('No note select items')
        popup.exec_()
        return
    name = notes_list_widget.selectedItems()[0].text()
    del notes[name]
    notes_list_widget.clear()
    notes_list_widget.addItems(notes)
    dump_notes()


def create_tag():
    tag = tag_line_edit.text()
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('No note select items')
        popup.exec_()
        return
    note_name = notes_list_widget.selectedItems()[0].text()

    if tag == '':
        popup_tag = QMessageBox()
        popup_tag.setWindowTitle('Error')
        popup_tag.setText('Tag name cannot be empty')
        popup_tag.exec_()
        return
    if tag in notes[note_name]['tags']:
        popup_tag2 = QMessageBox()
        popup_tag2.setWindowTitle('Error')
        popup_tag2.setText('Such tag already exists')
        popup_tag2.exec_()
        return

    notes[note_name]['tags'].append(tag)
    dump_notes()
    tags_list_widget.clear()
    tags_list_widget.addItems(notes[note_name]['tags'])

def delete_tag():
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('No note selected')
        popup.exec_()
        return
    if len(tags_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('No tag selected')
        popup.exec_()
        return
    note_name = notes_list_widget.selectedItems()[0].text()
    tag_name = tags_list_widget.selectedItems()[0].text()

    notes[note_name]['tags'].remove(tag_name)
    tags_list_widget.clear()
    tags_list_widget.addItems(notes[note_name]['tags'])
    dump_notes()

def search():
    query = tag_line_edit.text()

    if query == '':
        notes_list_widget.clear()
        notes_list_widget.addItems(notes)
        return

    result = {}

    for note in notes:
        if query in notes[note]['tags']:
            result[note] = notes[note]

    notes_list_widget.clear()
    notes_list_widget.addItems(result)




notes_list_widget.itemClicked.connect(show_note)
save_note_button.clicked.connect(save_note)
delete_note_button.clicked.connect(delete_note)
create_note_button.clicked.connect(create_note)
tag_create_button.clicked.connect(create_tag)
tag_delete_button.clicked.connect(delete_tag)
search_button.clicked.connect(search)

if os.path.exists('notes.json') and os.path.isfile('notes.json'):
    with open('notes.json', 'r', encoding='utf-8') as file:
        notes = json.load(file)
notes_list_widget.addItems(notes)

dump_notes()

window.show()
app.exec_()
