from PyQt5 import QtWidgets, QtGui, QtCore
import os.path as osp

here = osp.dirname(osp.abspath(__file__))

class OperationBar(QtWidgets.QWidget):
    def __init__(self):
        super(OperationBar, self).__init__()
        self.initUI()

    def initUI(self):
        toolbarLayout = QtWidgets.QVBoxLayout()
        # 创建镜头调整GroupBox并添加到布局
        self.toolbarMoveGroupBox = self.create_toolbar_move_groupbox()
        self.toolbarPathSetGroupBox =self.create_toolbar_PathSet_groupbox()
        self.toolbarParamGroupBox =self.create_toolbar_param_groupbox()
        toolbarLayout.addWidget(self.toolbarMoveGroupBox)
        toolbarLayout.addWidget(self.toolbarPathSetGroupBox)
        toolbarLayout.addWidget(self.toolbarParamGroupBox)
        self.setLayout(toolbarLayout)

    def create_toolbar_param_groupbox(self):
        groupbox = QtWidgets.QGroupBox("参数栏")
        layout = QtWidgets.QVBoxLayout()
        groupbox.setLayout(layout)

        # 参数名称和初始值
        params = {
            "亮度": 50,
            "对比度": 50,
            "饱和度": 50,
            "色度": 50,
            "锐度": 50,
            "去噪": 50,
            "音量": 50
        }

        # 创建参数控制组件
        for param, value in params.items():
            paramLayout = QtWidgets.QHBoxLayout()
            paramLabel = QtWidgets.QLabel(param)
            paramLabel.setAlignment(QtCore.Qt.AlignRight)
            paramLabel.setFixedSize(50, 20)
            paramSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            paramSlider.setMinimum(0)
            paramSlider.setMaximum(100)
            paramSlider.setValue(value)
            paramLayout.addWidget(paramLabel)
            paramLayout.addWidget(paramSlider)
            layout.addLayout(paramLayout)
            # 连接信号（如果需要）
            paramSlider.valueChanged.connect(lambda value, param= param: self.on_param_changed(param, value))

        return groupbox
    def create_toolbar_PathSet_groupbox(self):
        groupbox =QtWidgets.QGroupBox("路径预设")
        layout = QtWidgets.QVBoxLayout()
        groupbox.setFixedHeight(200)
        groupbox.setLayout(layout)

        self.PathIDBtn = QtWidgets.QLabel("ID")
        self.PathIDBtn.setFixedSize(30, 30)

        self.PathIDSelectBtn = QtWidgets.QComboBox()

        self.PathSetBeginBtn = self.addBtn(
            "开始",
            "开始运行所选预设路径",
            None,
            self.on_PathSetBeginBtn_clicked
        )
        self.PathSetEndBtn = self.addBtn(
            "结束",
            "结束运行所选预设路径",
            None,
            self.on_PathSetEndBtn_clicked
        )
        self.PathPreSetBeginBtn = self.addBtn(
            "预设路径",
            "预设巡航路径",
            None,
            self.on_PathPreSetBeginBtn_clicked
        )
        self.PathPreSetEndBtn = self.addBtn(
            "结束路径",
            "结束预设巡航路径",
            None,
            self.on_PathPreSetEndBtn_clicked
        )
        self.DelOnePathBtn = self.addBtn(
            "删除单条",
            "删除当前预设路径",
            None,
            self.on_DelOnePathBtn_clicked
        )
        self.DelAllPathtn = self.addBtn(
            "删除所有",
            "删除所有预设路径",
            None,
            self.on_DelAllPathtn_clicked
        )
        toolBarBtnLayout = QtWidgets.QHBoxLayout()
        toolBarBtnLayout.addWidget(self.PathIDBtn)
        toolBarBtnLayout.addWidget(self.PathIDSelectBtn)
        toolBarBtnLayout.addWidget(self.PathSetBeginBtn)
        toolBarBtnLayout.addWidget(self.PathSetEndBtn)
        layout.addLayout(toolBarBtnLayout)
        toolBarBtnLayout = QtWidgets.QHBoxLayout()
        toolBarBtnLayout.addWidget(self.PathPreSetBeginBtn)
        toolBarBtnLayout.addWidget(self.PathPreSetEndBtn)
        layout.addLayout(toolBarBtnLayout)
        toolBarBtnLayout = QtWidgets.QHBoxLayout()
        toolBarBtnLayout.addWidget(self.DelOnePathBtn)
        toolBarBtnLayout.addWidget(self.DelAllPathtn)
        layout.addLayout(toolBarBtnLayout)

        return groupbox
    def create_toolbar_move_groupbox(self):
        groupbox = QtWidgets.QGroupBox("镜头调整")
        groupbox.setFixedHeight(300)
        layout = QtWidgets.QVBoxLayout()
        groupbox.setLayout(layout)

        # 创建移动按钮
        self.toolBarUpBtn = self.addBtn(
            "上",
            "向上移动镜头",
            "Up",
            self.on_toolBarUpBtn_clicked
        )
        self.toolBarLeftBtn = self.addBtn(
            "左",
            "向左移动镜头",
            "left",
            self.on_toolBarLeftBtn_clicked)
        self.toolBarRightBtn = self.addBtn(
            "右",
            "向右移动镜头",
            "right",
            self.on_toolBarRightBtn_clicked
        )
        self.toolBarDownBtn = self.addBtn(
            "下",
            "向下移动镜头",
            "down",
            self.on_toolBarDownBtn_clicked
        )

        # 添加移动按钮到布局
        toolBarBtnLayout = QtWidgets.QHBoxLayout()
        toolBarBtnLayout.addWidget(self.toolBarUpBtn)
        layout.addLayout(toolBarBtnLayout)
        toolBarBtnLayout = QtWidgets.QHBoxLayout()
        toolBarBtnLayout.addWidget(self.toolBarLeftBtn)
        toolBarBtnLayout.addWidget(self.toolBarRightBtn)
        layout.addLayout(toolBarBtnLayout)
        toolBarBtnLayout = QtWidgets.QHBoxLayout()
        toolBarBtnLayout.addWidget(self.toolBarDownBtn)

        layout.addLayout(toolBarBtnLayout)

        # 创建焦距调整组件
        self.toolBarSubFocusBtn = self.addBtn(
            "减少",
            "缩小焦距",
            "sub",
            self.on_toolBarSubFocusBtn)
        self.toolBarFocusText = QtWidgets.QLabel("焦距")
        self.toolBarFocusText.setFixedSize(30, 30)
        self.toolBarAddFocusBtn = self.addBtn(
            "增加",
            "增加焦距",
            "add",
            self.on_toolBarAddFocusBtn)

        # 添加焦距调整组件到布局
        toolBarFocusLayout = QtWidgets.QHBoxLayout()
        toolBarFocusLayout.addWidget(self.toolBarSubFocusBtn)
        toolBarFocusLayout.addWidget(self.toolBarFocusText)
        toolBarFocusLayout.addWidget(self.toolBarAddFocusBtn)
        layout.addLayout(toolBarFocusLayout)

        # 创建聚焦长度调整组件
        self.toolBarSubFocusLenBtn = self.addBtn(
            "减少",
            "缩焦距",
            "sub",
            self.on_toolBarSubFocusLenBtn
        )
        self.toolBarFocusLenText = QtWidgets.QLabel("聚焦")
        self.toolBarFocusLenText.setFixedSize(30, 30)
        self.toolBarAddFocusLenBtn = self.addBtn(
            "增加",
            "伸聚焦",
            "add",
            self.on_toolBarAddFocusLenBtn
        )

        # 添加聚焦长度调整组件到布局
        toolBarFocusLenLayout = QtWidgets.QHBoxLayout()
        toolBarFocusLenLayout.addWidget(self.toolBarSubFocusLenBtn)
        toolBarFocusLenLayout.addWidget(self.toolBarFocusLenText)
        toolBarFocusLenLayout.addWidget(self.toolBarAddFocusLenBtn)
        layout.addLayout(toolBarFocusLenLayout)

        # 创建光圈调整组件
        self.toolBarSubApertureBtn = self.addBtn(
            "缩小",
            "缩小光圈",
            "sub",
            self.on_toolBarSubApertureBtn
        )
        self.toolBarApertureText = QtWidgets.QLabel("光圈")
        self.toolBarApertureText.setFixedSize(30, 30)
        self.toolBarAddApertureBtn = self.addBtn(
            "增大",
            "增大光圈",
            "add",
            self.on_toolBarAddApertureBtn
        )

        # 添加光圈调整组件到布局
        toolBarApertureLayout = QtWidgets.QHBoxLayout()
        toolBarApertureLayout.addWidget(self.toolBarSubApertureBtn)
        toolBarApertureLayout.addWidget(self.toolBarApertureText)
        toolBarApertureLayout.addWidget(self.toolBarAddApertureBtn)
        layout.addLayout(toolBarApertureLayout)

        return groupbox

    def addBtn(self, title=None, tip=None, icon=None, slot=None):
        btn = QtWidgets.QToolButton()
        if icon is not None:
            btn.setIcon(self.newIcon(icon))
        if title is not None:
            btn.setText(title)
        if tip is not None:
            btn.setToolTip(tip)
        if slot is not None:
            btn.clicked.connect(slot)
        return btn

    def newIcon(self, icon):
        icons_dir = osp.join(here, "../icons")
        return QtGui.QIcon(osp.join(":/", icons_dir, "%s.png" % icon))

    # 槽函数定义
    def on_toolBarUpBtn_clicked(self):
        print("向上移动镜头")

    def on_toolBarDownBtn_clicked(self):
        print("向下移动镜头")

    def on_toolBarLeftBtn_clicked(self):
        print("向左移动镜头")

    def on_toolBarRightBtn_clicked(self):
        print("向右移动镜头")

    def on_toolBarSubFocusBtn(self):
        print("缩小焦距")

    def on_toolBarAddFocusBtn(self):
        print("增加焦距")

    def on_toolBarSubFocusLenBtn(self):
        print("缩焦距")

    def on_toolBarAddFocusLenBtn(self):
        print("伸聚焦")

    def on_toolBarSubApertureBtn(self):
        print("缩小光圈")

    def on_toolBarAddApertureBtn(self):
        print("增大光圈")
    def on_PathSetBeginBtn_clicked(self):
        print("开始")
    def on_PathSetEndBtn_clicked(self):
        print("结束")
    def on_PathPreSetBeginBtn_clicked(self):
        pass
    def on_PathPreSetEndBtn_clicked(self):
        pass
    def on_DelOnePathBtn_clicked(self):
        pass

    def on_DelAllPathtn_clicked(self):
        pass

    def on_param_changed(self, param, value):
        # 处理参数改变的槽函数
        print(f"{param} changed to {value}")
