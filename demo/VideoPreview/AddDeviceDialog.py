from PyQt5 import QtWidgets


class AddDeviceDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('添加设备')

        # 创建布局和表单元素
        self.layout = QtWidgets.QVBoxLayout()

        self.form_layout = QtWidgets.QFormLayout()

        self.name_label = QtWidgets.QLabel('设备名称:')
        self.name_input = QtWidgets.QLineEdit()
        self.form_layout.addRow(self.name_label, self.name_input)

        self.address_label = QtWidgets.QLabel('设备IP地址:')
        self.address_input = QtWidgets.QLineEdit()
        self.form_layout.addRow(self.address_label, self.address_input)

        self.port_label = QtWidgets.QLabel('端口号:')
        self.port_input = QtWidgets.QSpinBox()
        self.port_input.setRange(1, 65535)
        self.form_layout.addRow(self.port_label, self.port_input)

        self.username_label = QtWidgets.QLabel('用户名:')
        self.username_input = QtWidgets.QLineEdit()
        self.form_layout.addRow(self.username_label, self.username_input)

        self.password_label = QtWidgets.QLabel('密码:')
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)  # 设置为密码输入模式
        self.form_layout.addRow(self.password_label, self.password_input)

        # 登录模式
        self.login_mode_label = QtWidgets.QLabel('登录模式:')
        self.login_mode_combo = QtWidgets.QComboBox()
        self.login_mode_combo.addItems(['私有协议', 'ISAPI协议', '自适应', 'F2F-私有协议', 'P2P-ISAPI'])  # 添加选项
        self.form_layout.addRow(self.login_mode_label, self.login_mode_combo)

        # HTTP协议版本
        self.http_version_label = QtWidgets.QLabel('HTTP协议版本:')
        self.http_version_combo = QtWidgets.QComboBox()
        self.http_version_combo.addItems(['HTTP', 'HTTPS', '自适应'])  # 添加选项
        self.form_layout.addRow(self.http_version_label, self.http_version_combo)

        # 添加 SDKTLS 下拉框
        self.sdk_tls_label = QtWidgets.QLabel('SDKTLS:')
        self.sdk_tls_combo = QtWidgets.QComboBox()
        self.sdk_tls_combo.addItems(['不认证', '双向认证', '单向认证'])  # 添加选项
        self.form_layout.addRow(self.sdk_tls_label, self.sdk_tls_combo)

        # 添加表单布局到主布局
        self.layout.addLayout(self.form_layout)

        # 创建按钮并添加到布局
        self.button_box = QtWidgets.QHBoxLayout()  # 使用水平布局来放置按钮
        self.add_button = QtWidgets.QPushButton('添加')
        self.add_button.clicked.connect(self.accept)
        self.cancel_button = QtWidgets.QPushButton('取消')
        self.cancel_button.clicked.connect(self.reject)
        self.button_box.addWidget(self.add_button)
        self.button_box.addWidget(self.cancel_button)
        self.layout.addLayout(self.button_box)

        # 设置对话框的主布局
        self.setLayout(self.layout)

    def get_device_info(self):
        # 如果用户点击了“添加”按钮，则返回设备信息
        if self.result() == QtWidgets.QDialog.Accepted:
            return {
                'name': self.name_input.text(),
                'address': self.address_input.text(),
                'port': self.port_input.value(),
                'username': self.username_input.text(),
                'password': self.password_input.text(),
                'sdk_tls': self.sdk_tls_combo.currentText(),  # 获取当前选中的SDKTLS选项
                'login_mode': self.login_mode_combo.currentText(),  # 获取当前选中的登录模式
                'http_version': self.http_version_combo.currentText()  # 获取当前选中的HTTP协议版本
            }
        return None