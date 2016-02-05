#! coding:utf-8
"""
Plotter

Created by 0160929 on 2016/02/05 16:21
"""
__version__ = '1.0'

import sys
import math

from PySide.QtGui import *
from PySide.QtCore import *

colorForIds = [Qt.red, Qt.green, Qt.blue, Qt.cyan, Qt.magenta, Qt.yellow]


class Plotter(QWidget):
    def __init__(self, parent=None):
        super(Plotter, self).__init__(parent)

        # ============================================
        # プロパティ
        # ============================================
        self.Margin = 50  # [pix]
        self.curveMap = {}
        self.pixmap = QPixmap()
        # ============================================
        # QWidget初期設定
        # ============================================
        self.setBackgroundRole(QPalette.Shadow)
        self.setAutoFillBackground(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setFocusPolicy(Qt.StrongFocus)
        # ============================================
        # Setup UI
        # ============================================
        iniSetting = PlotSettings()
        self.setPlotSettings(iniSetting)

    def setPlotSettings(self, settings):
        self.setting = settings
        self.refreshPixmap()
        pass

    def plot(self):
        self.refreshPixmap()

    def set_xlabel(self, xlabel):
        self.setting.xlabel = xlabel
        # self.refreshPixmap()
        pass

    def set_ylabel(self, ylabel):
        self.setting.ylabel = ylabel
        # self.refreshPixmap()
        pass

    def set_title(self, title):
        # self.refreshPixmap()
        pass

    def set_xlim(self, xlim):
        self.setting.minX, self.setting.maxX = xlim
        self.setting.adjust()
        # self.refreshPixmap()
        pass

    def set_ylim(self, ylim):
        self.setting.minY, self.setting.maxY = ylim
        self.setting.adjust()
        # self.refreshPixmap()
        pass

    def setCurveData(self, id, x, y):
        """
        曲線データを格納
        :param id: 曲線データのインデックス
        :param data: 曲線データ(CurveDataクラス)
        :return:
        """
        data = CurveData(x, y)
        self.curveMap[id] = data
        # self.refreshPixmap()
        # # print self.curveMap
        pass

    def clearCurve(self, id):
        """
        曲線データを削除
        :param id: 曲線データのインデックス
        :return:
        """
        if self.curveMap.has_key(id):
            self.curveMap.pop(id)
        self.refreshPixmap()

        pass

    def minimumSizeHint(self, *args, **kwargs):
        '''ウィジェットの理想的な最小サイズ
        '''
        return QSize(6 * self.Margin, 4 * self.Margin)
        pass

    def sizeHint(self, *args, **kwargs):
        '''ウィジェットの理想的なサイズ
        '''
        return QSize(12 * self.Margin, 8 * self.Margin)
        pass

    # =================================================
    # SLOTの接続
    # =================================================

    # 無し

    # =================================================
    # Qtイベント
    # =================================================

    def paintEvent(self, *args, **kwargs):
        # 1. イメージグラフの描画
        painter = QStylePainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

        # 2. ウィジェットがフォーカスされているときの色処理
        if self.hasFocus():
            # # print '> self.hasFocus now!'
            option = QStyleOptionFocusRect()
            option.initFrom(self)
            option.backgroundColor = self.palette().dark().color()
            painter.drawPrimitive(QStyle.PE_FrameFocusRect, option)

    def resizeEvent(self, *args, **kwargs):
        self.refreshPixmap()
        pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # print '> Push "Left Button Click"'
            pass
        pass

    def mouseMoveEvent(self, event):
        """ドラッグ処理"""
        # # print event.pos()
        pass

    def keyPressEvent(self, event):
        e = event.key()
        if e == Qt.Key_Q:
            self.close()
        pass

    # =================================================
    # 描画処理
    # =================================================
    def refreshPixmap(self):
        # print '> refreshPixmap()'
        """バッファに曲線描画. あわせてプロット指示も出す"""
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(self, 0, 0)

        # painterの初期化
        painter = QPainter(self.pixmap)
        painter.initFrom(self)
        # バッファーへ描画
        self.drawGrid(painter)
        self.drawCurves(painter)
        # 画面の描画更新命令
        self.update()

    def drawGrid(self, painter):
        rect = QRect(self.Margin,
                     self.Margin,
                     self.width() - 2 * self.Margin,
                     self.height() - 2 * self.Margin)
        if not rect.isValid():
            return


        # グラフプロットの設定
        settings = self.setting
        # ペンの色の指定
        quiteDark = self.palette().dark().color()
        light = self.palette().light().color()

        # 横軸の目盛線の描画
        for i in range(settings.numXTicks + 1):
            x = rect.left() + (i * (rect.width() - 1) / settings.numXTicks)
            label = settings.minX + (i * settings.spanX() / settings.numXTicks)
            # 補助目盛り線の描画
            painter.setPen(quiteDark)
            painter.drawLine(x, rect.top(), x, rect.bottom())
            # 目盛りの描画
            painter.setPen(light)
            # 内目盛り線
            painter.drawLine(x, rect.bottom(), x, rect.bottom() - 5)
            painter.drawText(x - 50, rect.bottom() + 5, 100, 15,
                             Qt.AlignCenter | Qt.AlignTop,
                             unicode('%0.2f' % label))

        # 縦軸の目盛線の描画
        for j in range(settings.numYTicks + 1):
            y = rect.bottom() - (j * (rect.height() - 1) / settings.numYTicks)
            label = settings.minY + (j * settings.spanY() / settings.numYTicks)
            painter.setPen(quiteDark)
            painter.drawLine(rect.left(), y, rect.right(), y)
            painter.setPen(light)
            painter.drawLine(rect.left() + 5, y, rect.left(), y)
            painter.drawText(rect.left() - self.Margin, y - 10, self.Margin - 5, 20,
                             Qt.AlignRight | Qt.AlignVCenter,
                             unicode('%0.2f' % label))
        painter.drawRect(rect.adjusted(0, 0, -1, -1))

        # X軸ラベルの表示
        painter.drawText(rect.left(), rect.bottom(), rect.width(), self.Margin, Qt.AlignCenter | Qt.AlignVCenter,
                         unicode(u'%s' % self.setting.xlabel))
        # Y軸ラベルの表示
        painter.rotate(-90)
        painter.translate(-rect.height(), 0)
        # painter.drawText(0, 0, unicode(u'%s' % self.setting.xlabel))
        painter.drawText(self.Margin, 0, rect.height(), self.Margin / 2., Qt.AlignLeft | Qt.AlignVCenter,
                         unicode(u'%s' % self.setting.ylabel))
        painter.translate(rect.height(), 0)
        painter.rotate(90)


        # painter.rotate(-90)

        pass

    def drawCurves(self, painter):

        settings = self.setting

        rect = QRect(self.Margin,
                     self.Margin,
                     self.width() - 2. * self.Margin,
                     self.height() - 2. * self.Margin)

        # 再描画する範囲を、曲線が含まれる矩形内のみに指定
        painter.setClipRect(rect.adjusted(+1, +1, -1, -1))

        for id, data in self.curveMap.iteritems():
            # TODO:data配列がlist型->numpyにも対応させる
            polyline = QPolygonF()
            for j in range(data.length()):
                dx = data.x[j] - settings.minX
                dy = data.y[j] - settings.minY
                x = rect.left() + (dx * (rect.width() - 1) / settings.spanX())
                y = rect.bottom() - (dy * (rect.height() - 1) / settings.spanY())
                # print x, y
                polyline.append(QPointF(x, y))

            painter.setPen(colorForIds[id % 6])
            painter.drawPolyline(polyline)

        pass


class PlotSettings():
    '''PlotSettingsクラス
    X軸とY軸の範囲と量軸の目盛の数を保持している
    ※ 慣習的にnumXTicksとnumYTicksは実際の数とは1つ違う.
    '''
    minX = -100.0
    maxX = 100.0
    numXTicks = 10
    minY = -10.0
    maxY = 10.0
    numYTicks = 10
    xlabel = ''
    ylabel = ''

    def __init__(self):
        pass

    def scroll(self, dx, dy):
        """１目盛りずつスクロール"""
        stepX = self.spanX() / self.numXTicks
        self.minX += dx * stepX
        self.maxX += dx * stepX

        stepY = self.spanY() / self.numYTicks
        self.minY += dy * stepY
        self.maxY += dy * stepY
        pass

    def adjust(self):
        self.minX, self.maxX, self.numXTicks = self.adjustAxis(self.minX, self.maxX, self.numXTicks)
        self.minY, self.maxY, self.numYTicks = self.adjustAxis(self.minY, self.maxY, self.numYTicks)
        pass

    def spanX(self):
        return self.maxX - self.minX

    def spanY(self):
        return self.maxY - self.minY

    def adjustAxis(self, min, max, numTicks):
        '''引数値min,maxから、表示用に最適な値を算出し
        指定された値域[min,max]に適した目盛の数を計算する
        '''
        MinTicks = 4
        grossStep = (max - min) / MinTicks
        step = math.pow(10.0, math.floor(math.log10(grossStep)))

        if 5 * step < grossStep:
            step *= 5
        elif 2 * step < grossStep:
            step *= 2

        numTicks = int(math.ceil(max / step) - math.floor(min / step))
        if numTicks < MinTicks:
            numTicks = MinTicks
            min = math.floor(min / step) * step
            max = math.ceil(max / step) * step
        return min, max, numTicks


class CurveData():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return len(self.x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('plastique')
    pl = Plotter()

    # データ生成
    Fs = 4800.
    x = range(int(Fs))
    y = [math.sin(2. * 3. * 100 * xn / Fs) for xn in x]
    y2 = [math.cos(2. * 3. * 100 * xn / Fs) for xn in x]

    # グラフの表示
    pl.setCurveData(id=1, x=x, y=y)
    pl.setCurveData(id=2, x=x, y=y2)
    pl.set_xlim([0, 100.])
    pl.set_ylim([-2, 2])
    pl.set_xlabel('Frequency [Hz]')
    pl.set_ylabel('Amplitude [db]')

    pl.show()
    sys.exit(app.exec_())
