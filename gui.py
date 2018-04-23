import pkg_resources
from random import randint
import sys

from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5 import uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QTreeView, QTableView


class TaggedItem(QStandardItem):
    def __init__(self, value):
        super().__init__()
        self._value = value

    def data(self, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._value
        return super().data(role)


class Grandchild(TaggedItem):
    def __init__(self):
        super().__init__('Grandchild')
        for i in range(5):
            self.appendRow([
                TaggedItem(str(randint(0, 100))),
                TaggedItem(str(randint(0, 100))),
                TaggedItem(str(randint(0, 100)))
            ])

class Child(TaggedItem):
    def __init__(self):
        super().__init__('Child')
        self.appendRow(Grandchild())


class Root(QStandardItem):
    def __init__(self):
        super().__init__('Root')
        self.appendRow(Child())


class TableModel(QSortFilterProxyModel):
    pass


def main(argv):
    app = QApplication(argv)
    main_window = uic.loadUi('mainwindow.ui')

    tree_view = main_window.findChild(QTreeView, 'treeView')
    table_view = main_window.findChild(QTableView, 'tableView')

    model = QStandardItemModel()
    root_item = Root()
    model.appendRow(root_item)

    tree_view.setModel(model)

    table_model = TableModel()
    table_model.setSourceModel(model)
    table_view.setModel(table_model)
    table_view.setRootIndex(
        table_model.mapFromSource(
            root_item.child(0, 0).child(0, 0).index()))

    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
