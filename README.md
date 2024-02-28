## Quick Prepare

```bash
sudo apt update
```

* Ubuntu (23.04~)

```bash
# with pyqt5
sudo apt show python3-pyqt5* | grep -P "^Package: "
sudo apt install -y python3-pyqt5*

# with pyside
sudo apt show python3-pyside* | grep -P "^Package: "
sudo apt install -y python3-pyside2.qtsvg # Depends: python3-pyside2.qtwidgets/qtgui/qtcore
```

* Ubuntu (~22.10)

```bash
# Note: Create a virtual python env via conda or virtualenv 1st.

# with pyqt5
python3 -m pip install pyqt5 pyqt5-tools -i https://pypi.tuna.tsinghua.edu.cn/simple/
#python -m pip show pyqt5
# Note: One can see that PyQt5 is required by pyqt5-plugins, pyqt5-tools

# with pyside
python3 -m pip install pyside6 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## Quick Start

```bash
python3 main.py
```

## Quick Note

1. `PySide2.QtWidgets.QApplication` object has no attribute 'exec', try 'exec_' plz.

## Quick TODO

1. fix app with pyqt5