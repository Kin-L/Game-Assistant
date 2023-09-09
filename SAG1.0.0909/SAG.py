# -*- coding:gbk -*-
import sys,json,keyboard,time,datetime,shutil,random,genshin_resource.ui.SAG_icon
import win32api, win32gui, win32print
from threading import Thread,Event
from ctypes import windll
from yuanshen_thread import *
from function import *
from PyQt5 import QtCore, QtGui, QtWidgets
# pyinstaller -D -w -i D:\Kin-project\python\venv\genshin_resource\ui\folder\SAG.ico D:\Kin-project\python\venv\SAG.py
#pyrcc5 -o venv\genshin_resource\ui\folder\SAG_icon.py venv\genshin_resource\ui\folder\SAG_icon.qrc
user32 = windll.user32
now_width = user32.GetSystemMetrics(0)
user32.SetProcessDPIAware()
origin_width = user32.GetSystemMetrics(0)#round(origin_width / 1920, 2)
origin_high = user32.GetSystemMetrics(1)#round(origin_high / 1080, 2)
uizoom = round(origin_width / now_width, 2)
class Common(object):
    def __init__(self):
        self.event_run = Event()
        self.event_pause = Event()
        self.event_pause.set()
        self.cg_name = ""
        self.uizoom = uizoom
    def ui_zoom(self,x,y,w,h):
        x,y,w,h =int(self.uizoom*x),int(self.uizoom*y),int(self.uizoom*w),int(self.uizoom*h)
        return QtCore.QRect(x,y,w,h)
    def num_zoom(self,numlist):
        for num in range(len(numlist)):numlist[num] = int(self.uizoom*numlist[num])
        return numlist
    # ������Ŀ��ť��ʼ��
    def config_set(self):
        self.helpconfig = QtWidgets.QPushButton(main_window)
        self.helpconfig.setGeometry(self.ui_zoom(240, 215, 40, 23))
        self.helpconfig.setObjectName("helpconfig")
        self.helpconfig.setText(self._translate("main_window", "����"))
        # ֹͣ��ť
        self.stop = QtWidgets.QPushButton(main_window)
        self.stop.setGeometry(self.ui_zoom(20, 305, 65, 23))
        self.stop.setObjectName("stop")
        self.stop.setText(self._translate("main_window", "ֹͣ"))
        # ��ʼ��ť
        self.start = QtWidgets.QPushButton(main_window)
        self.start.setGeometry(self.ui_zoom(20, 305, 90, 23))
        self.start.setObjectName("start")
        self.start.setText(self._translate("main_window", "����"))
        # ������Ŀ��ǩ
        self.change_config_Label = QtWidgets.QLabel(main_window)
        self.change_config_Label.setGeometry(self.ui_zoom(170, 215, 60, 23))
        self.change_config_Label.setObjectName("change_config_Label")
        self.change_config_Label.setText(self._translate("main_window", "�л�����"))
        # �����л�
        self.change_config = QtWidgets.QComboBox(main_window)
        self.change_config.setGeometry(self.ui_zoom(170, 245, 110, 23))
        self.change_config.setObjectName("change_config")
        self.comboboxstyle(self.change_config)
        # �������ð�ť
        self.save = QtWidgets.QPushButton(main_window)
        self.save.setGeometry(self.ui_zoom(170, 305, 40, 23))
        self.save.setObjectName("save")
        self.save.setText(self._translate("main_window", "����"))
        # �½�����
        self.new_config = QtWidgets.QPushButton(main_window)
        self.new_config.setGeometry(self.ui_zoom(170, 275, 58, 23))
        self.new_config.setObjectName("new_config")
        self.new_config.setText(self._translate("main_window", "�½�����"))
        # ���������
        self.config_rename_bfinish = QtWidgets.QPushButton(main_window)
        self.config_rename_bfinish.setGeometry(self.ui_zoom(233, 275, 48, 23))
        self.config_rename_bfinish.setObjectName("config_rename_bfinish")
        self.config_rename_bfinish.setText(self._translate("main_window", "ȷ��"))
        # ������
        self.config_rename = QtWidgets.QPushButton(main_window)
        self.config_rename.setGeometry(self.ui_zoom(233, 275, 48, 23))
        self.config_rename.setObjectName("config_rename")
        self.config_rename.setText(self._translate("main_window", "������"))
        # ʹ����֪
        self.help0 = QtWidgets.QPushButton(main_window)
        self.help0.setGeometry(self.ui_zoom(220, 305, 60, 23))
        self.help0.setObjectName("help0")
        self.help0.setText(self._translate("main_window", "ʹ����֪"))

    # ��ҳ������
    # ��Ϸ��������ҳ��
    def start_program(self):
        self.game_path_Label = QtWidgets.QLabel(self.create_page)
        self.game_path_Label.setGeometry(self.ui_zoom(10, 10, 81, 16))
        self.game_path_Label.setObjectName("game_path_Label")
        self.game_path_Label.setText(self._translate("main_window", "��Ϸ����·��"))
        self.game_path = QtWidgets.QLineEdit(self.create_page)
        self.game_path.setGeometry(self.ui_zoom(0, 40, 240, 20))
        self.game_path.setObjectName("game_path")
        self.game_path.home(False)
        self.server_box = QtWidgets.QComboBox(self.create_page)
        self.server_box.setGeometry(self.ui_zoom(90, 8, 50, 22))
        self.server_box.setObjectName("server_box")
        self.comboboxstyle(self.server_box)
        self.help1 = QtWidgets.QPushButton(self.create_page)
        self.help1.setGeometry(self.ui_zoom(160, 8, 40, 20))
        self.help1.setObjectName("help1")
        self.help1.setText(self._translate("main_window", "����"))

        self.week_Label = QtWidgets.QLabel(self.create_page)
        self.week_Label.setGeometry(self.ui_zoom(0, 70, 81, 16))
        self.week_Label.setObjectName("week_Label")
        self.week_Label.setText(self._translate("main_window", "ÿ��"))
        self.time_Label = QtWidgets.QLabel(self.create_page)
        self.time_Label.setGeometry(self.ui_zoom(40, 70, 81, 16))
        self.time_Label.setObjectName("time_Label")
        self.time_Label.setText(self._translate("main_window", "��ʱִ��"))
        self.cho_config_Label = QtWidgets.QLabel(self.create_page)
        self.cho_config_Label.setGeometry(self.ui_zoom(150, 70, 81, 16))
        self.cho_config_Label.setObjectName("cho_config_Label")
        self.cho_config_Label.setText(self._translate("main_window", "�����ļ�"))
        self.enable_Label = QtWidgets.QLabel(self.create_page)
        self.enable_Label.setGeometry(self.ui_zoom(220, 70, 81, 16))
        self.enable_Label.setObjectName("enable_Label")
        self.enable_Label.setText(self._translate("main_window", "����"))
        for num in range(1, 4):
            exec("self.daily%s = QtWidgets.QCheckBox(self.create_page)"%(num))
            exec("self.time%s = QtWidgets.QDateTimeEdit(self.create_page)" % (num))
            exec("self.cho_config%s = QtWidgets.QComboBox(self.create_page)" % (num))
            exec("self.enable%s = QtWidgets.QCheckBox(self.create_page)" % (num))
            strw, strt, strc, stre = "daily" + str(num), "time" + str(num), "cho_config" + str(num), "enable" + str(
                num)
            fw, ft, fc, fe = eval("self." + strw), eval("self." + strt), eval("self." + strc), eval("self." + stre)
            fw.setGeometry(self.ui_zoom(5, 60 + num * 30, 58, 22))
            fw.setObjectName(strw)
            ft.setGeometry(self.ui_zoom(30, 60 + num * 30, 95, 22))
            ft.setObjectName(strt)
            ft.setDisplayFormat("dddd hh:mm")
            fc.setGeometry(self.ui_zoom(135, 60 + num * 30, 80, 22))
            fc.setObjectName(strt)
            self.comboboxstyle(fc)
            fe.setGeometry(self.ui_zoom(225, 60 + num * 30, 58, 22))
            fe.setObjectName(stre)

    # �������ѡ��ť�����ð�ť����ҳ���ʼ��
    def choose_add_set_add_page(self):
        # ��ǩLabel
        self.choose = QtWidgets.QLabel(main_window)
        self.choose.setGeometry(self.ui_zoom(10, 10, 54, 16))
        self.choose.setObjectName("choose")
        self.choose.setText(self._translate("main_window", "����ѡ��"))
        self.set = QtWidgets.QLabel(main_window)
        self.set.setGeometry(self.ui_zoom(125, 10, 31, 16))
        self.set.setObjectName("set")
        self.set.setText(self._translate("main_window", "����"))
        # ����ҳ��
        self.topFiller = QtWidgets.QWidget(main_window)
        self.trans_list = self.indexdir["����"]
        self.topFiller.setMinimumSize(165, len(self.trans_list) * 29)  #######���ù������ĳߴ�
        self.scroll = QtWidgets.QScrollArea(main_window)
        self.scroll.setWidget(self.topFiller)
        x,y,w,h = self.num_zoom([2, 28,165, 270])
        self.scroll.move(x,y)
        self.scroll.resize(w,h)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # �ѵ������ʼ��
        self.set_pages = QtWidgets.QStackedWidget(main_window)
        self.set_pages.setGeometry(self.ui_zoom(175, 0, 250, 180))
        self.set_pages.setObjectName("set_pages")
        for num in range(len(self.trans_list)):
            tname = self.trans_list[num]
            fnamep = self.indexdir[tname]
            strc, strs, strp = "self.choose_%s" % (fnamep), "self.set_%s" % (fnamep), "self.%s_page" % (fnamep)
            exec(strc + "= QtWidgets.QCheckBox(self.topFiller)")
            exec(strs + "= QtWidgets.QPushButton(self.topFiller)")
            exec(strp + "= QtWidgets.QWidget()")
            fc, fs, fp = eval(strc), eval(strs), eval(strp)
            fc.setGeometry(self.ui_zoom(5, 5 + 30 * num, 110, 16))
            fc.setObjectName(strc)
            fc.setText(self._translate("main_window", tname))
            fs.setGeometry(self.ui_zoom(125, 5 + (30 * num), 15, 15))
            fs.setObjectName(strs)
            fp.setObjectName(strp)
            self.set_pages.addWidget(fp)
        self.choose_create.setEnabled(False)

    # ��ʼ����ҳ
    def set_home(self,cname,ename,game_name):
        self.game_name = game_name
        # ���ڳ�ʼ��
        main_window.setObjectName("main_window")
        main_window.resize(int(self.uizoom * 700), int(self.uizoom * 340))
        self._translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(self._translate("main_window", cname))
        main_window.setWindowIcon(QtGui.QIcon(":/%s.ico"%(ename)))
        main_window.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                                   QtCore.Qt.WindowCloseButtonHint)
        main_window.setFixedSize(main_window.width(), main_window.height())
        # ��ʾͼ��
        self.ico = QtWidgets.QLabel(main_window)
        self.ico.setGeometry(self.ui_zoom(290, 215, 120, 120))
        self.pixmap = QtGui.QPixmap(game_name+"_resource\\ui\%s.png"%(ename))
        self.ico.setPixmap(self.pixmap)
        self.ico.setScaledContents(True)
        # �����ж�
        self.run_judge = QtWidgets.QCheckBox(main_window)
        self.run_judge.setGeometry(self.ui_zoom(0, 0, 110, 16))
        self.run_judge.setObjectName("run_judge")
        self.run_judge.setChecked(False)
        self.run_judge.stateChanged.connect(self.run)
        self.run_judge.hide()
        # �ı������
        self.output_string = QtWidgets.QTextBrowser(main_window)
        self.output_string.setGeometry(self.ui_zoom(430, 10, 256, 320))
        self.output_string.setObjectName("output_string")
        self.sendhelp("ʹ����֪")
        self.output_string.moveCursor(self.output_string.textCursor().Start)
        # self.output_string.clear()

    # ���ð�ť��������ҳ��
    def set_button_connect(self):
        # ���ð�ť��������ҳ��
        self.set_pages.setCurrentIndex(0)
        for i in self.indexdir["����"]:
            for u in self.indexdir["����"]:
                f1, f2 = eval("self.set_" + self.indexdir[i]), eval("self." + self.indexdir[u] + "_page")
                if i == u:
                    f1.clicked.connect(f2.show)
                else:
                    f1.clicked.connect(f2.hide)
        # ������ť���Ͱ����ı�
        self.helpconfig.clicked.connect(lambda: self.sendhelp("�����л�"))
        self.help0.clicked.connect(lambda: self.sendhelp("ʹ����֪"))
        self.help1.clicked.connect(lambda: self.sendhelp("������Ϸ"))
        self.help2.clicked.connect(lambda: self.sendhelp("�л���׼����"))
        self.help3.clicked.connect(lambda: self.sendhelp("̽����ǲ"))
        self.help4.clicked.connect(lambda: self.sendhelp("ʹ�ò����ʱ���"))
        self.help5.clicked.connect(lambda: self.sendhelp("��׽����"))
        self.help6.clicked.connect(lambda: self.sendhelp("�ϳ�Ũ����֬"))
        self.help7.clicked.connect(lambda: self.sendhelp("��ȡ�����"))
        self.help8.clicked.connect(lambda: self.sendhelp("�ɼ�ľ��"))
        self.help9.clicked.connect(lambda: self.sendhelp("��ɺ�ر���Ϸ"))
        # ���ӿ�ʼֹͣ
        self.start.clicked.connect(lambda: self.run_judge.setChecked(True))  # ��ʼ��ť���ӿ�ʼ����
        self.stop.clicked.connect(lambda: self.pause(2))  # ֹͣ��ť���ӹ�����ֹ
        # ����������Ŀ���ð�ť
        self.save.clicked.connect(self.save_config)  # ���水ť���ӱ������ú���
        self.change_config.currentIndexChanged.connect(
            lambda: self.load_config(self.change_config.currentText()))  # �л���ǩʱ�Զ��л�����
        self.new_config.clicked.connect(self.create_new_config)  # �½�����ѡ��
        self.config_rename.clicked.connect(self.config_rename_fun)  # ������������Ŀ
        self.config_rename_bfinish.clicked.connect(self.config_rename_finish)  # ȷ��������������Ŀ
        QtCore.QMetaObject.connectSlotsByName(main_window)

    # ������ʽ
    def comboboxstyle(self, f):
        f.setStyleSheet("QAbstractItemView::item {height: 22px;}")
        f.setView(QtWidgets.QListView())
        # font = QtGui.QFont()
        # font.setPointSize(10)  # �����С
        # f.setFont(font)

    def wait_to_time(self):
        while 1:
            time.sleep(10)
            self.event_pause.wait()
            nowtime = time.localtime()
            for num in range(1, 4):
                fw, fdt, fe = eval("self.daily" + str(num)), eval("self.time" + str(num)), eval(
                    "self.enable" + str(num))
                timetuple = fdt.dateTime().toPyDateTime().timetuple()
                if fe.isChecked():
                    if (nowtime[3:5] == timetuple[3:5]):
                        if (fw.isChecked() or nowtime[6] == timetuple[6]):
                            self.cg_name = eval("self.cho_config" + str(num)).currentText()
                            self.event_pause.clear()
                            self.run_judge.setChecked(True)
                            break
            time.sleep(10)

    # ָʾ��Ϣ���
    # ���ָʾ�ı�������¼�ı���ʷ
    def showtext(self, msg, nowtime=None):
        txt = open(self.game_name + "_resource\logging.txt", 'a+', encoding='utf-8')
        if nowtime == None:
            nowtime = time.strftime("%H:%M:%S ", time.localtime())
        else:
            txt.write("\n")
        self.output_string.append(nowtime + msg)
        self.output_string.ensureCursorVisible()
        txt.write(nowtime + msg + "\n")

    # ���������Ϣ
    def sendhelp(self, helpstr):
        with open(self.game_name + "_resource\help.json", 'r', encoding='utf-8') as d:
            self.help_dir = json.load(d)
        help_list = self.help_dir[helpstr]
        self.output_string.moveCursor(self.output_string.textCursor().End)
        self.output_string.append("")
        for i in help_list:
            self.output_string.append(i)
            self.output_string.ensureCursorVisible()

    # ����������Ϣ
    def loadconfig(self):
        with open(self.game_name + "_resource\config0.json", 'r', encoding='utf-8') as m:
            self.config0 = json.load(m)
        with open(self.game_name + "_resource\config\\" + self.config0["�����ļ�"] + ".json", 'r',
                  encoding='utf-8') as s:
            self.configdir = json.load(s)
        with open(self.game_name + "_resource\index.json", 'r', encoding='utf-8') as d:
            self.indexdir = json.load(d)

    # ����������ֹ
    def wait_to_kill(self):
        while 1:
            self.event_run.wait()
            keyboard.wait("ctrl+/")
            if self.event_run.isSet(): self.pause(2)

    # ���ù��ܺ���
    # ����������
    def config_rename_fun(self):
        self.config_rename.hide()
        self.config_rename_bfinish.show()
        self.old = self.change_config.currentText()
        self.change_config.setEditable(True)

    # �������������
    def config_rename_finish(self):
        newname = self.change_config.currentText()
        os.rename(self.game_name + "_resource\config\\" + self.old + ".json",
                  self.game_name + "_resource\config\\" + newname + ".json")
        self.change_config.setEditable(False)
        index = self.change_config.currentIndex()
        self.change_config.setItemText(index, newname)
        self.config0["�����ļ�"] = newname
        with open(self.game_name + "_resource\config0.json", 'w', encoding='utf-8') as f:
            json.dump(self.config0, f, ensure_ascii=False, indent=1)
        self.config_rename_bfinish.hide()
        self.config_rename.show()
        for num in range(1, 4):
            fc = eval("self.cho_config" + str(num))
            fc.setItemText(index, newname)

    # �½�����
    def create_new_config(self):
        random_num = str(random.randint(999, 10000))
        shutil.copyfile(self.game_name + "_resource\Ĭ������.json",
                        self.game_name + "_resource\config\Ĭ������" + random_num + ".json")
        self.change_config.addItems(["Ĭ������" + random_num])
        self.change_config.setCurrentText("Ĭ������" + random_num)
        for num in range(1, 4):
            fc = eval("self.cho_config" + str(num))
            fc.addItems(["Ĭ������" + random_num])

    # ����������
    def load_config0(self):
        # ����������
        filedir = self.game_name + "_resource\config"
        self.filelist = []
        for file in os.listdir(filedir):
            name, suffix = os.path.splitext(file)
            if suffix == ".json": self.filelist += [name]
        self.change_config.addItems(self.filelist)
        for num in range(1, 4):
            strw, strt, strc, stre = "daily" + str(num), "time" + str(num), "cho_config" + str(num), "enable" + str(
                num)
            fw, ft, fc, fe = eval("self." + strw), eval("self." + strt), eval("self." + strc), eval("self." + stre)
            che, time, config_file, ena = self.config0["ʱ��" + str(num)]
            ft.setDateTime(datetime.datetime.fromtimestamp(time))
            fw.setChecked(che)
            fc.addItems(self.filelist)
            fc.setCurrentText(config_file)
            fe.setChecked(ena)
        self.game_path.setText(self.config0["��Ϸ����·��"])
        self.game_path.home(False)
        self.change_config.setCurrentText(self.config0["�����ļ�"])
        self.server_box.addItems(self.indexdir["������"])
        self.server_box.setCurrentIndex(self.config0["������"])
    # ����������
    def save_config0(self):
        self.config0["��Ϸ����·��"] = self.game_path.text().strip("\"")
        self.config0["�����ļ�"] = self.change_config.currentText()
        for num in range(1, 4):
            strw, strt, strc, stre = "daily" + str(num), "time" + str(num), "cho_config" + str(num), "enable" + str(
                num)
            fw, ft, fc, fe = eval("self." + strw), eval("self." + strt), eval("self." + strc), eval("self." + stre)
            timenum = time.mktime(ft.dateTime().toPyDateTime().timetuple())
            self.config0["ʱ��" + str(num)] = [fw.isChecked(), timenum, fc.currentText(), fe.isChecked()]
        plist = self.indexdir["����"]
        for num in range(len(plist)):
            strc = "choose_" + self.indexdir[plist[num]]
            fc = eval("self." + strc)
            self.configdir[plist[num]] = fc.isChecked()
        with open(self.game_name + "_resource\config0.json", 'w', encoding='utf-8') as f:
            json.dump(self.config0, f, ensure_ascii=False, indent=1)
        with open(self.game_name + "_resource\config\\" + self.config0["�����ļ�"] + ".json", 'w',
                  encoding='utf-8') as d:
            json.dump(self.configdir, d, ensure_ascii=False, indent=1)
class Ui_main_window(Common):
    def setupUi(self, main_window):
        # ��ʼ��ҳ��
        self.set_home("ɰ������", "SAG", "genshin")

        # ����������Ϣ
        self.loadconfig()
        # �������ѡ��ť�����ð�ť��ʼ��
        self.choose_add_set_add_page()
        # ������Ŀ��ť��ʼ��
        self.config_set()
        # ��������ҳ�水ť��ʼ��
        self.start_program()
        self.load_config0()

        # ��Ϸ��������ҳ�水ť��ʼ��
        self.dispatch_program()
        self.para_trans_program()
        self.crystalfly_program()
        self.cut_tree_program()
        self.othor_page()

        # ���ð�ť
        self.load_config_style()
        self.load_config(self.config0["�����ļ�"])
        #���Ӻ���
        self.set_button_connect()
        #��ʱ����
        self.wait_key = Thread(target=self.wait_to_kill, daemon=True)
        self.wait_key.start()
        self.wait_time = Thread(target=self.wait_to_time, daemon=True)
        self.wait_time.start()

    # ��ǲ����ҳ��
    def dispatch_program(self):
        self.region_Label = QtWidgets.QLabel(self.dispatch_page)
        self.region_Label.setGeometry(self.ui_zoom(0, 10, 81, 16))
        self.region_Label.setObjectName("region")
        self.region_Label.setText(self._translate("main_window", "����ѡ��"))
        self.material_Label = QtWidgets.QLabel(self.dispatch_page)
        self.material_Label.setGeometry(self.ui_zoom(80, 10, 81, 16))
        self.material_Label.setObjectName("material")
        self.material_Label.setText(self._translate("main_window", "����ѡ��"))

        self.help2 = QtWidgets.QPushButton(self.dispatch_page)
        self.help2.setGeometry(self.ui_zoom(140, 8, 40, 20))
        self.help2.setObjectName("help2")
        self.help2.setText(self._translate("main_window", "����"))

        rlist = self.indexdir["��ǲ����"]
        for num in range(1, 6):
            strr,strm = "region"+str(num),"material"+str(num)
            exec ("self.region%s = QtWidgets.QComboBox(self.dispatch_page)"%(num))
            exec ("self.material%s = QtWidgets.QComboBox(self.dispatch_page)"%(num))
            fr,fm = eval("self." + strr), eval("self." + strm)
            fr.setGeometry(self.ui_zoom(0, num*30, 62, 22))
            fr.setObjectName(strr)
            self.comboboxstyle(fr)

            fm.setGeometry(self.ui_zoom(80, num*30, 128, 22))
            fm.setObjectName(strm)
            self.comboboxstyle(fm)
    # �����ʱ�������ҳ��
    def para_trans_program(self):
        self.para_trans_Label = QtWidgets.QLabel(self.para_trans_page)
        self.para_trans_Label.setGeometry(self.ui_zoom(10, 10, 81, 16))
        self.para_trans_Label.setObjectName("para_trans_Label")
        self.para_trans_Label.setText(self._translate("main_window", "���Ĳ���Ԥ��"))
        self.para_trans_material1 = QtWidgets.QLineEdit(self.para_trans_page)
        self.para_trans_material2 = QtWidgets.QLineEdit(self.para_trans_page)
        self.para_trans_material3 = QtWidgets.QLineEdit(self.para_trans_page)
        self.para_trans_material4 = QtWidgets.QLineEdit(self.para_trans_page)
        self.para_trans_material5 = QtWidgets.QLineEdit(self.para_trans_page)
        self.help3 = QtWidgets.QPushButton(self.para_trans_page)
        self.help3.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help3.setObjectName("help3")
        self.help3.setText(self._translate("main_window", "����"))
        for num in range(1,6):
            strt = "para_trans_material" + str(num)
            ft= eval("self." + strt)
            ft.setGeometry(self.ui_zoom(0, 0+num*30, 230, 20))
            ft.setObjectName("para_trans_material"+str(num))
    # ׽��������ҳ��
    def crystalfly_program(self):
        # ��ѡ��ť��ʼ��
        self.crystalfly1 = QtWidgets.QCheckBox(self.crystalfly_page)
        self.crystalfly2 = QtWidgets.QCheckBox(self.crystalfly_page)
        self.crystalfly3 = QtWidgets.QCheckBox(self.crystalfly_page)
        self.crystalfly4 = QtWidgets.QCheckBox(self.crystalfly_page)
        self.crystalfly5 = QtWidgets.QCheckBox(self.crystalfly_page)
        self.crystalfly6 = QtWidgets.QCheckBox(self.crystalfly_page)
        self.help4 = QtWidgets.QPushButton(self.crystalfly_page)
        self.help4.setGeometry(self.ui_zoom(120, 13, 40, 20))
        self.help4.setObjectName("help4")
        self.help4.setText(self._translate("main_window", "����"))
        strlist = self.indexdir["����"]
        for num in range(len(strlist)):
            strc = "crystalfly" + str(num+1)
            fc= eval("self." + strc)
            fc.setGeometry(self.ui_zoom(0, 10+num*30, 140, 22))
            fc.setObjectName(strc)
            fc.setText(self._translate("main_window", strlist[num]))
            # fc.setChecked(blist[num])
    # ��������ҳ��
    def cut_tree_program(self):#
        woodlist1a, woodlist2a, woodlist3a = self.indexdir["ľ������1"], self.indexdir["ľ������2"], self.indexdir[
            "ľ������3"]
        woodlist1b, woodlist2b, woodlist3b = self.indexdir["tree_kind1"], self.indexdir["tree_kind2"], self.indexdir[
            "tree_kind3"]
        self.filler_tree = QtWidgets.QWidget(self.cut_tree_page)
        w,h =self.num_zoom([250, len(woodlist1a) * 30+25])
        self.filler_tree.setMinimumSize(w,h)  #######���ù������ĳߴ�
        self.scroll_tree = QtWidgets.QScrollArea(self.cut_tree_page)
        self.scroll_tree.setWidget(self.filler_tree)
        [w,h] =self.num_zoom([250, 160])
        self.scroll_tree.move(0,10)
        self.scroll_tree.resize(w,h)
        self.scroll_tree.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.cut_circulate_Label = QtWidgets.QLabel(self.filler_tree)
        self.cut_circulate_Label.setGeometry(self.ui_zoom(5, 5, 81, 16))
        self.cut_circulate_Label.setObjectName("cut_circulate_Label")
        self.cut_circulate_Label.setText(self._translate("main_window", "ѭ������"))
        self.cut_circulate = QtWidgets.QLineEdit(self.filler_tree)
        self.cut_circulate.setGeometry(self.ui_zoom(60, 3, 50, 20))
        self.cut_circulate.setObjectName("cut_circulate")
        self.help8 = QtWidgets.QPushButton(self.filler_tree)
        self.help8.setGeometry(self.ui_zoom(120, 3, 40, 20))
        self.help8.setObjectName("help8")
        self.help8.setText(self._translate("main_window", "����"))
        intValidator = QtGui.QIntValidator()
        intValidator.setRange(1, 99)
        self.cut_circulate.setValidator(intValidator)
        for i in range(1,4):
            la,lb = self.indexdir["ľ������%s"%(i)],self.indexdir["tree_kind%s"%(i)]
            for num in range(len(lb)):
                strw = "self.choose_%s" % (lb[num])
                exec(strw + "= QtWidgets.QCheckBox(self.filler_tree)")
                fw = eval(strw)
                fw.setGeometry(self.ui_zoom(-67+i*75, 25 + num * 30, 140, 22))
                fw.setObjectName(strw)
                fw.setText(self._translate("main_window", la[num]))
    # ����δ��������ҳ��
    def othor_page(self):
        list = ["team","comp","serenitea_pot","kill_game"]
        self.team_Label = QtWidgets.QLabel()
        self.crystalfly_Label = QtWidgets.QLabel()
        self.comp_Label = QtWidgets.QLabel()
        self.serenitea_pot_Label = QtWidgets.QLabel()
        self.kill_game_Label = QtWidgets.QLabel()
        for i in list:
            strl, strp = i+"_Label",  i+"_page"
            fl, fp = eval("self." + strl), eval("self." + strp)
            fl = QtWidgets.QLabel(fp)
            fl.setGeometry(self.ui_zoom(10, 10, 81, 16))
            fl.setObjectName(strl)
            fl.setText(self._translate("main_window", "��������ѡ��"))
        self.help5 = QtWidgets.QPushButton(self.team_page)
        self.help5.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help5.setObjectName("help5")
        self.help5.setText(self._translate("main_window", "����"))
        self.help6 = QtWidgets.QPushButton(self.comp_page)
        self.help6.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help6.setObjectName("help6")
        self.help6.setText(self._translate("main_window", "����"))
        self.help7 = QtWidgets.QPushButton(self.serenitea_pot_page)
        self.help7.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help7.setObjectName("help7")
        self.help7.setText(self._translate("main_window", "����"))
        self.help9 = QtWidgets.QPushButton(self.kill_game_page)
        self.help9.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help9.setObjectName("help9")
        self.help9.setText(self._translate("main_window", "����"))

    # �ű����к���
    def run(self):
        if not self.run_judge.isChecked():pass
        else:
            self.event_run.set()
            self.event_pause.clear()
            self.start.hide()
            self.stop.show()
            self.output_string.clear()
            self.ico.setPixmap(QtGui.QPixmap(r"genshin_resource\ui\ico\0.png"))
            self.showtext("",nowtime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            ctlist1,ctlist2,ctlist3=[],[],[]
            nrun_list, rrun_list, mrun_list, trun_list, frun_list,ctrun_list = [], [], [], [], [],[]
            if self.cg_name !="" :
                with open("genshin_resource\config\\" + self.cg_name + ".json", 'r', encoding='utf-8') as r:
                    self.rundir = json.load(r)
                self.cg_name = ""
                for name in self.indexdir["����"]: nrun_list += [self.rundir[name]]
                for num in range(1, 6):
                    rrun_list += [self.rundir["��ǲ����" + str(num)]]
                    mrun_list += [self.rundir["��ǲ����" + str(num)]]
                    trun_list += [self.rundir["ʹ�ò���" + str(num)]]
                for num in range(1, 7): frun_list = self.rundir["����"]
            else:
                for name in self.indexdir["����"]:
                    fc = eval("self.choose_" + self.indexdir[name])
                    nrun_list += [fc.isChecked()]
                for num in range(1, 6):
                    rrun_list += [eval("self.region" + str(num)).currentIndex()]
                    mrun_list += [eval("self.material" + str(num)).currentIndex()]
                    trun_list += [eval("self.para_trans_material" + str(num)).text()]
                for num in range(1, 7): frun_list += [eval("self.crystalfly" + str(num)).isChecked()]
                for wood in self.indexdir["tree_kind1"]: ctlist1 += [eval("self.choose_"+wood).isChecked()]
                for wood in self.indexdir["tree_kind2"]: ctlist2 += [eval("self.choose_" + wood).isChecked()]
                for wood in self.indexdir["tree_kind3"]: ctlist3 += [eval("self.choose_" + wood).isChecked()]
                ctrun_list = [self.cut_circulate.text(),ctlist1,ctlist2,ctlist3]
            login_list = [self.game_path.text(), self.server_box.currentIndex()]
            self.tlist = [login_list, nrun_list, rrun_list, mrun_list, trun_list, frun_list,ctrun_list]
            self.thready = Thready(self.tlist)
            self.thready.start()
            self.thready.testsignal.connect(self.showtext)
            self.thready.accomplish.connect(self.pause)

    # ������ֹ
    def pause(self,num):# 1�������� 2����ֹͣ,��ťֹͣ 3����ֹͣ
        self.event_run.clear()
        self.event_pause.set()
        self.run_judge.setChecked(False)
        if num == 1:
            self.pixmap = QtGui.QPixmap(r"genshin_resource\ui\ico\1.png")
        else:
            self.thready.terminate()
            if num == 2:
                self.showtext("���ֶ�ֹͣ��\n")
                self.pixmap = QtGui.QPixmap(r"genshin_resource\ui\ico\2.png")
            elif num ==3:
                self.pixmap = QtGui.QPixmap(r"genshin_resource\ui\ico\3.png")
        self.stop.hide()
        self.start.show()
        self.ico.setPixmap(self.pixmap)
        main_window.activateWindow()

    # ��ʼ������
    def load_config_style(self):
        # ������ǲ����
        rlist = self.indexdir["��ǲ����"]
        for num in range(1, 6):
            strr, strm = "region" + str(num), "material" + str(num)
            fr, fm = eval("self." + strr), eval("self." + strm)
            fr.addItems(rlist)
            rnum = self.configdir["��ǲ����" + str(num)]
            mlist = self.indexdir[rlist[rnum] + "��ǲ����"]
            fm.clear()
            fm.addItems(mlist)
        self.region1.currentIndexChanged.connect(lambda:self.change_list(self.region1,self.material1))
        self.region2.currentIndexChanged.connect(lambda: self.change_list(self.region2, self.material2))
        self.region3.currentIndexChanged.connect(lambda: self.change_list(self.region3, self.material3))
        self.region4.currentIndexChanged.connect(lambda: self.change_list(self.region4, self.material4))
        self.region5.currentIndexChanged.connect(lambda: self.change_list(self.region5, self.material5))

    # ���ش�����
    def load_config(self,file):
        path ="genshin_resource\config\\"+file+".json"
        with open(path, 'r', encoding='utf-8') as config_dir:
            self.configdir = json.load(config_dir)
        #���ع�������
        trans_list = self.indexdir["����"]
        for num in range(len(trans_list)):
            fc = eval("self.choose_" + self.indexdir[trans_list[num]])
            tname = trans_list[num]
            che = self.configdir[tname]
            fc.setChecked(che)
        #������ǲ����
        rlist = self.indexdir["��ǲ����"]
        for num in range(1, 6):
            strr, strm = "region" + str(num), "material" + str(num)
            fr, fm = eval("self." + strr), eval("self." + strm)
            rnum = self.configdir["��ǲ����" + str(num)]
            fr.setCurrentIndex(rnum)
            fm.setCurrentIndex(self.configdir["��ǲ����" + str(num)])
        #���ز����ʱ���ʹ�ò�������
        for num in range(1,6):
            strt = "para_trans_material" + str(num)
            ft= eval("self." + strt)
            ft.setText(self.configdir["ʹ�ò���"+str(num)])
            ft.home(False)
        #���ؾ�������
        blist = self.configdir["����"]
        # print(33)
        for num in range(len(blist)):
            strc = "crystalfly" + str(num + 1)
            fc = eval("self." + strc)
            fc.setChecked(blist[num])
        for i in range(1,4):
            for num in range(len(self.indexdir["tree_kind%s"%(i)])):
                eval("self.choose_" + self.indexdir["tree_kind%s"%(i)][num]).setChecked(self.configdir["����%s"%(i)][num])
        self.cut_circulate.setText(self.configdir["����ѭ��"])
    # ��������
    def save_config(self):
        self.config0["��Ϸ����·��"] = self.game_path.text().strip("\"")
        self.config0["������"]=self.server_box.currentIndex()
        self.config0["�����ļ�"] = self.change_config.currentText()
        for num in range(1,4):
            strw, strt, strc,stre = "daily" + str(num), "time" + str(num), "cho_config" + str(num), "enable" + str(num)
            fw, ft, fc ,fe= eval("self." + strw), eval("self." + strt), eval("self." + strc), eval("self." + stre)
            timenum = time.mktime(ft.dateTime().toPyDateTime().timetuple())
            self.config0["ʱ��"+str(num)]=[fw.isChecked(),timenum,fc.currentText(),fe.isChecked()]
        plist = self.indexdir["����"]
        for num in range(len(plist)):
            strc = "choose_" + self.indexdir[plist[num]]
            fc = eval("self."+strc)
            self.configdir[plist[num]] = fc.isChecked()
        for num in range(1, 6):
            strr,strm,strt= "region" + str(num),"material" + str(num),"para_trans_material" + str(num)
            fr,fm,ft= eval("self." + strr),eval("self." + strm),eval("self." + strt)
            t_region = fr.currentText()
            self.configdir["��ǲ����" + str(num)] = self.indexdir["��ǲ����"].index(t_region)
            self.configdir["��ǲ����" + str(num)] = self.indexdir[t_region+"��ǲ����"].index(fm.currentText())
            self.configdir["ʹ�ò���" + str(num)] = ft.text()
        for num in range(1, 7): self.configdir["����"][num-1] = eval("self.crystalfly" + str(num)).isChecked()
        for i in range(1, 4):
            for num in range(len(self.indexdir["tree_kind%s"%(i)])):
                self.configdir["����%s"%(i)][num] = eval("self.choose_" + self.indexdir["tree_kind%s"%(i)][num]).isChecked()
        self.configdir["����ѭ��"] = self.cut_circulate.text()
        with open(r"genshin_resource\config0.json", 'w', encoding='utf-8') as f:
            json.dump(self.config0, f, ensure_ascii=False,indent=1)
        with open("genshin_resource\config\\"+self.config0["�����ļ�"]+".json", 'w', encoding='utf-8') as d:
            json.dump(self.configdir, d, ensure_ascii=False,indent=1)
        self.pixmap = QtGui.QPixmap(r"genshin_resource\ui\ico\0.png")
        self.ico.setPixmap(self.pixmap)

# ��ǲ����ҳ��-�л��б�
    def change_list(self,fr,fm):
        # print(fr.currentText())
        mlist = self.indexdir[fr.currentText() + "��ǲ����"]
        fm.clear()
        fm.addItems(mlist)

if __name__ == '__main__':

    a=QtWidgets.QApplication(sys.argv)
    main_window=QtWidgets.QWidget()
    b=Ui_main_window()
    b.setupUi(main_window)
    main_window.show()
    sys.exit(a.exec_())