import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QTableView


class Root(QStandardItem):
    def __init__(self):
        super().__init__('Root')
        for _ in range(5):
            self.appendRow([
                QStandardItem(str(randint(0, 100))),
                QStandardItem(str(randint(0, 100)))
            ])


def main(argv):
    app = QApplication(argv)
    main_window = uic.loadUi('mainwindow.ui')

    table_view = main_window.findChild(QTableView, 'tableView')

    model = QStandardItemModel()
    root_item = Root()
    model.appendRow(root_item)

    table_model = QSortFilterProxyModel()
    table_model.setSourceModel(model)

    table_view.setModel(table_model)
    table_view.setRootIndex(
        table_model.mapFromSource(
            root_item.index()))

    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
