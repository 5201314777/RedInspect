from datetime import datetime

import qtpy
from qtpy import QtWidgets


class Logger(QtWidgets.QDialog):
    """
    日志记录器类，用于显示日志信息。
    """

    def __init__(self, parent=None):
        super(Logger, self).__init__(parent)
        self.table_widget = QtWidgets.QTableWidget(self)
        self.table_widget.setRowCount(0)  # 初始化行数为0
        self.table_widget.setColumnCount(5)  # 设置列数为3
        self.table_widget.setHorizontalHeaderLabels(["时间", "状态", "操作", "设备信息", "错误信息"])

        # 设置表格可编辑
        self.table_widget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table_widget.setAlternatingRowColors(True)  # 设置交替行颜色

        # 允许调整列宽
        #self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_widget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_widget.setColumnWidth(0, 160)
        self.table_widget.setColumnWidth(1, 40)
        self.table_widget.setColumnWidth(2, 270)
        self.table_widget.setColumnWidth(3, 270)
        self.table_widget.setColumnWidth(4, 260)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)
        self.add_log(True, "登录", "无", "无")
        self.add_log(True, "登录", "无", "无")
        self.add_log(True, "登录", "无", "无")
        self.add_log(True, "登录", "error", "无")

    def add_log(self, success, operation_type,deviceMes,errorMes):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)  # 插入新行

        # 创建单元格并设置数据
        curTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_item = QtWidgets.QTableWidgetItem(curTime)

        status_item = QtWidgets.QTableWidgetItem("成功" if success else "失败")

        operation_item = QtWidgets.QTableWidgetItem(operation_type)

        deviceMes_item = QtWidgets.QTableWidgetItem(deviceMes)

        errorMes_item = QtWidgets.QTableWidgetItem(errorMes)
        # 将单元格添加到表格中

        self.table_widget.setItem(row_position, 0, time_item)
        self.table_widget.setItem(row_position, 1, status_item)
        self.table_widget.setItem(row_position, 2, operation_item)
        self.table_widget.setItem(row_position, 3, deviceMes_item)
        self.table_widget.setItem(row_position, 4, errorMes_item)
        self.table_widget.scrollTo(
            self.table_widget.model().index(row_position, 0),
            QtWidgets.QAbstractItemView.PositionAtBottom
        )
