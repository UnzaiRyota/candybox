from PySide2 import QtWidgets

from typing import TypeVar
from models import SettingTreeModel, IconModel, IconListModel


class BodyItemModel:
    Self = TypeVar("Self", bound="BodyItemModel")
    __widgetItems = {}

    def setBodyWidgetItems(self: Self, layout: QtWidgets.QBoxLayout) -> None:
        self.__widgetItems = {}
        for num in range(layout.count()):
            item = layout.itemAt(num)
            widget = item.widget()
            self.__widgetItems[widget.objectName()] = widget

    def showHideWidget(self: Self, widgetType: str, layout: QtWidgets.QBoxLayout) -> None:
        for num in range(layout.count()):
            item = layout.itemAt(num)
            widget = item.widget()
            objectName = widget.objectName()
            if widgetType != objectName:
                widget.hide()
            else:
                widget.show()

    @property
    def widgetItems(self) -> dict:
        return self.__widgetItems


class CandyBoxModels:
    Self = TypeVar("Self", bound="CandyBoxModels")
    bodyItemModel: BodyItemModel
    iconListModel: IconListModel
    settingTreeModel: SettingTreeModel

    def __init__(self) -> None:
        self.bodyItemModel = BodyItemModel()

    def setIconListModel(self: Self, data) -> None:
        self.iconListModel = IconListModel(data)

    def setSettingTreeModel(self: Self, data) -> None:
        self.settingTreeModel = SettingTreeModel(data)

    def createIconModel(self: Self, **kwargs) -> IconModel:
        return IconModel(**kwargs)
