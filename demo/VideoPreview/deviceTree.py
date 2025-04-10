import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMenu, QAction, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt, QPoint

from demo.VideoPreview.AddDeviceDialog import AddDeviceDialog
class DeviceTree(QTreeWidget):
    def __init__(self, parent=None):
        super(DeviceTree, self).__init__(parent)
        self.setHeaderLabels(['设备'])
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
        self.root = QTreeWidgetItem(self, ['设备列表'])
        self.expandAll()  # 展开所有节点

    def add_device(self, device_name, parent=None):
        # 如果未指定父节点，则默认添加到根节点
        if parent is None:
            parent = self.root
        new_item = QTreeWidgetItem(parent, [device_name])

    def on_context_menu(self, position):
        # 获取点击位置处的项
        item = self.itemAt(position)
        menu = QMenu()

        # 添加设备选项（只能在根节点或未选择任何项时添加，这里为只能在未选择项时添加）
        if item is None or item == self.root:  # 如果未选择项或选择的是根节点
            add_device_action = QAction("添加设备", self)
            add_device_action.triggered.connect(self.on_add_device)
            menu.addAction(add_device_action)

            # 添加删除选项（仅当不是根节点时）
        if item and item != self.root:
            delete_action = QAction("删除设备", self)
            delete_action.triggered.connect(lambda: self.on_delete_device(item))
            menu.addAction(delete_action)

            # 显示菜单
        menu.exec_(self.viewport().mapToGlobal(QPoint(position)))

    # def on_add_device(self):
    #     # 提示用户输入设备名称
    #     text, ok = QInputDialog.getText(self, '添加设备', '请输入设备名称:')
    #
    #     if ok and text:
    #         # 添加新设备到设备树（默认添加到根节点）
    #         self.add_device(text)

    def on_add_device(self):
        # 创建并显示添加设备的对话框
        dialog = AddDeviceDialog(self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            # 用户点击了“添加”按钮，从对话框中获取设备信息
            device_info = dialog.get_device_info()
            if device_info:
                # 提取设备名称和其他信息
                device_name = device_info['name']

                # 添加新设备到设备树（默认添加到根节点）
                self.add_device(device_name)



    def on_delete_device(self, item):
        # 确认删除
        reply = QMessageBox.question(self, '删除设备',
                                     f"你确定要删除设备 '{item.text(0)}' 吗?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # 从树中删除项（不需要检查父节点，因为已经确保了item不是根节点）
            parent = item.parent()
            parent.takeChild(parent.indexOfChild(item))



###########################################################################

# import sys
# from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QMenu, QAction, QMessageBox, QInputDialog, QVBoxLayout, \
#     QWidget, QLineEdit, QDialog, QLabel, QFormLayout
# from PyQt5.QtCore import Qt, QPoint
#
#
# class AddDeviceDialog(QDialog):
#     def __init__(self, parent=None):
#         super(AddDeviceDialog, self).__init__(parent)
#         self.setWindowTitle('添加设备')
#         self.layout = QFormLayout()
#
#         self.name_label = QLabel('设备名称:')
#         self.name_edit = QLineEdit()
#         self.layout.addRow(self.name_label, self.name_edit)
#
#         self.address_label = QLabel('设备地址:')
#         self.address_edit = QLineEdit()
#         self.layout.addRow(self.address_label, self.address_edit)
#
#         self.port_label = QLabel('端口号:')
#         self.port_edit = QLineEdit()
#         self.layout.addRow(self.port_label, self.port_edit)
#
#         self.username_label = QLabel('用户名:')
#         self.username_edit = QLineEdit()
#         self.layout.addRow(self.username_label, self.username_edit)
#
#         self.password_label = QLabel('密码:')
#         self.password_edit = QLineEdit()
#         self.password_edit.setEchoMode(QLineEdit.Password)
#         self.layout.addRow(self.password_label, self.password_edit)
#
#         self.button_box = self.addButtons(QDialog.Ok | QDialog.Cancel)
#         self.layout.addWidget(self.button_box)
#
#         self.setLayout(self.layout)
#
#     def get_device_info(self):
#         if self.result() == QDialog.Accepted:
#             return {
#                 'name': self.name_edit.text(),
#                 'address': self.address_edit.text(),
#                 'port': self.port_edit.text(),
#                 'username': self.username_edit.text(),
#                 'password': self.password_edit.text()
#             }
#         return None
#
#
# class DeviceTree(QTreeWidget):
#     def __init__(self, parent=None):
#         super(DeviceTree, self).__init__(parent)
#         self.setHeaderLabels(['设备'])
#         self.setContextMenuPolicy(Qt.CustomContextMenu)
#         self.customContextMenuRequested.connect(self.on_context_menu)
#         self.root = QTreeWidgetItem(self, ['设备列表'])
#         self.expandAll()  # 展开所有节点
#
#     def add_device(self, device_info):
#         # 将设备信息添加到根节点
#         if device_info is None:
#             return  # 或者显示一个错误消息
#         device_name = device_info['name']
#         # 可以在这里使用其他设备信息做更多处理，或者仅仅存储到某个地方
#         new_item = QTreeWidgetItem(self.root, [device_name])
#         # 可以为每个设备项设置隐藏的数据，用于存储额外信息
#
#     def on_context_menu(self, position):
#         item = self.itemAt(position)
#         menu = QMenu()
#
#         if item is None or item == self.root:
#             add_device_action = QAction("添加设备", self)
#             add_device_action.triggered.connect(self.on_add_device)
#             menu.addAction(add_device_action)
#
#         if item and item != self.root:
#             delete_action = QAction("删除设备", self)
#             delete_action.triggered.connect(lambda: self.on_delete_device(item))
#             menu.addAction(delete_action)
#
#         menu.exec_(self.viewport().mapToGlobal(QPoint(position)))
#
#     def on_add_device(self):
#         dialog = AddDeviceDialog(self)
#         device_info = dialog.get_device_info()
#         if device_info:
#             self.add_device(device_info)
#         else:
#             # 可以选择在这里显示一个消息，告诉用户没有添加设备
#             print("没有添加设备，用户取消了操作。")
#
#     def on_delete_device(self, item):
#         reply = QMessageBox.question(self, '删除设备',
#                                      f"你确定要删除设备 '{item.text(0)}' 吗?",
#                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#
#         if reply == QMessageBox.Yes:
#             parent = item.parent()
#             parent.takeChild(parent.indexOfChild(item))


