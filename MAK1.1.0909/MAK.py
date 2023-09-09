# -*- coding:gbk -*-
import sys,json,keyboard,time,datetime,shutil,random,hxls_resource.ui.MAK_icon
import win32api, win32gui, win32print
from threading import Thread,Event
from ctypes import windll
from hxls_thread import *
from function import *
from PyQt5 import QtCore, QtGui, QtWidgets
# pyinstaller -D -w -i D:\Kin-project\python\venv\hxls_resource\ui\folder\MAK.ico D:\Kin-project\python\venv\MAK.py
#pyrcc5 -o venv\hxls_resource\ui\folder\MAK_icon.py venv\hxls_resource\ui\folder\MAK_icon.qrc
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
        self.time_Label.setText(self._translate("main_window", "��ʱִ�нű�"))
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
        x,y = self.num_zoom([165, len(self.trans_list) * 29])
        self.topFiller.setMinimumSize(x,y)  #######���ù������ĳߴ�
        self.scroll = QtWidgets.QScrollArea(main_window)
        self.scroll.setWidget(self.topFiller)
        x,y,w,h = self.num_zoom([2, 28,165, 270])
        self.scroll.move(x,y)
        self.scroll.resize(w,h)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # �ѵ������ʼ��
        self.set_pages = QtWidgets.QStackedWidget(main_window)
        self.set_pages.setGeometry(self.ui_zoom(175, 0, 250, 210))
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
        self.help2.clicked.connect(lambda: self.sendhelp("��ս/����"))
        self.help3.clicked.connect(lambda: self.sendhelp("���²ɹ�"))
        self.help4.clicked.connect(lambda: self.sendhelp("ս���ع�"))
        self.help5.clicked.connect(lambda: self.sendhelp("������ȡ"))
        self.help6.clicked.connect(lambda: self.sendhelp("���ѷ�ļ"))
        self.help7.clicked.connect(lambda: self.sendhelp("���չ���"))
        self.help8.clicked.connect(lambda: self.sendhelp("ʹ�������"))
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
        self.config0["������"] = self.server_box.currentIndex()
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
        self.set_home("Դ������","MAK","hxls")

        # ����������Ϣ
        self.loadconfig()
        #�������ѡ��ť�����ð�ť��ʼ��
        self.choose_add_set_add_page()
        # ������Ŀ��ť��ʼ��
        self.config_set()
        #��������ҳ�水ť��ʼ��
        self.start_program()
        self.load_config0()

        # ��Ϸ��������ҳ�水ť��ʼ��
        self.fight_program()
        self.dispatch_program()
        self.review_program()
        self.recruit_program()
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
    # ��ս/��������ҳ��
    def fight_program(self):
        self.help2 = QtWidgets.QPushButton(self.fight_page)
        self.help2.setGeometry(self.ui_zoom(130, 8, 40, 20))
        self.help2.setObjectName("help2")
        self.help2.setText(self._translate("main_window", "����"))
        self.retour_Label = QtWidgets.QLabel(self.fight_page)
        self.retour_Label.setGeometry(self.ui_zoom(0, 10, 81, 16))
        self.retour_Label.setObjectName("retour_Label")
        self.retour_Label.setText(self._translate("main_window", "�ٴ�����"))
        self.fight_Label = QtWidgets.QLabel(self.fight_page)
        self.fight_Label.setGeometry(self.ui_zoom(65, 10, 81, 16))
        self.fight_Label.setObjectName("fight_Label")
        self.fight_Label.setText(self._translate("main_window", "����ѡ��"))
        self.refight = QtWidgets.QCheckBox(self.fight_page)
        self.refight.setGeometry(self.ui_zoom(15, 30, 58, 22))
        self.refight.setObjectName("refight")
        self.fight_box = QtWidgets.QComboBox(self.fight_page)
        self.fight_box.setGeometry(self.ui_zoom(60, 30, 60, 22))
        self.fight_box.setObjectName("fight_box")
        self.comboboxstyle(self.fight_box)
    # ���²ɹ�����ҳ��
    def dispatch_program(self):
        self.top_dispatch = QtWidgets.QWidget(self.dispatch_page)
        self.trans_list = self.indexdir["����"]
        x, y = self.num_zoom([250, 230])
        self.top_dispatch.setMinimumSize(x, y)  #######���ù������ĳߴ�
        self.scroll = QtWidgets.QScrollArea(self.dispatch_page)
        self.scroll.setWidget(self.top_dispatch)
        x, y, w, h = self.num_zoom([0, 10, 250, 200])
        self.scroll.move(x, y)
        self.scroll.resize(w, h)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.material_Label = QtWidgets.QLabel(self.top_dispatch)
        self.material_Label.setGeometry(self.ui_zoom(5, 30, 81, 16))
        self.material_Label.setObjectName("material")
        self.material_Label.setText(self._translate("main_window", "����ѡ��"))
        self.fund_Label = QtWidgets.QLabel(self.top_dispatch)
        self.fund_Label.setGeometry(self.ui_zoom(85, 30, 81, 16))
        self.fund_Label.setObjectName("fund")
        self.fund_Label.setText(self._translate("main_window", "�ʽ�ѡ��"))
        self.plan_Label = QtWidgets.QLabel(self.top_dispatch)
        self.plan_Label.setGeometry(self.ui_zoom(150, 30, 81, 16))
        self.plan_Label.setObjectName("plan")
        self.plan_Label.setText(self._translate("main_window", "����ѡ��"))

        self.re_dispatch= QtWidgets.QCheckBox(self.top_dispatch)
        self.re_dispatch.setGeometry(self.ui_zoom(5, 8, 81, 16))
        self.re_dispatch.setObjectName("re_dispatch")
        self.re_dispatch.setText(self._translate("main_window", "�ٴβɹ�"))
        for num in range(6):
            exec ("self.material%s = QtWidgets.QComboBox(self.top_dispatch)"%(num+1))
            exec("self.fund%s = QtWidgets.QComboBox(self.top_dispatch)" % (num + 1))
            exec("self.plan%s = QtWidgets.QComboBox(self.top_dispatch)" % (num + 1))
        # self.material1 = QtWidgets.QComboBox(self.top_dispatch)
        # self.fund1 = QtWidgets.QComboBox(self.top_dispatch)
        # self.plan1 = QtWidgets.QComboBox(self.top_dispatch)
        # self.material2 = QtWidgets.QComboBox(self.top_dispatch)
        # self.fund2 = QtWidgets.QComboBox(self.top_dispatch)
        # self.plan2 = QtWidgets.QComboBox(self.dispatch_page)
        # self.material3 = QtWidgets.QComboBox(self.dispatch_page)
        # self.fund3 = QtWidgets.QComboBox(self.dispatch_page)
        # self.plan3 = QtWidgets.QComboBox(self.dispatch_page)
        # self.material4 = QtWidgets.QComboBox(self.dispatch_page)
        # self.fund4 = QtWidgets.QComboBox(self.dispatch_page)
        # self.plan4 = QtWidgets.QComboBox(self.dispatch_page)
        # self.material5 = QtWidgets.QComboBox(self.dispatch_page)
        # self.fund5 = QtWidgets.QComboBox(self.dispatch_page)
        # self.plan5 = QtWidgets.QComboBox(self.dispatch_page)
        # self.material6 = QtWidgets.QComboBox(self.dispatch_page)
        # self.fund6 = QtWidgets.QComboBox(self.dispatch_page)
        # self.plan6 = QtWidgets.QComboBox(self.dispatch_page)

        self.help3 = QtWidgets.QPushButton(self.top_dispatch)
        self.help3.setGeometry(self.ui_zoom(90, 5, 40, 20))
        self.help3.setObjectName("help3")
        self.help3.setText(self._translate("main_window", "����"))

        for num in range(1, 7):
            strm,strd,strp = "material"+str(num),"fund"+str(num),"plan"+str(num)
            fm,fd,fp = eval("self." + strm), eval("self." + strd), eval("self." + strp)
            fm.setGeometry(self.ui_zoom(2, 20+num*30, 75, 22))
            fm.setObjectName(strm)
            self.comboboxstyle(fm)
            fd.setGeometry(self.ui_zoom(83, 20+num*30, 60, 22))
            fd.setObjectName(strd)
            self.comboboxstyle(fd)
            fp.setGeometry(self.ui_zoom(150, 20+num * 30, 75, 22))
            fp.setObjectName(strp)
            self.comboboxstyle(fp)
    # ս���ع�����ҳ��
    def review_program(self):
        self.help4 = QtWidgets.QPushButton(self.review_page)
        self.help4.setGeometry(self.ui_zoom(100, 8, 40, 20))
        self.help4.setObjectName("help4")
        self.help4.setText(self._translate("main_window", "����"))
        self.review_Label = QtWidgets.QLabel(self.review_page)
        self.review_Label.setGeometry(self.ui_zoom(10, 10, 80, 16))
        self.review_Label.setObjectName("review_Label")
        self.review_Label.setText(self._translate("main_window", "ս���ع�ѡ��"))

        self.review0 = QtWidgets.QComboBox(self.review_page)
        self.review0.setGeometry(self.ui_zoom(20, 30, 50, 22))
        self.review0.setObjectName("review0")
        self.comboboxstyle(self.review0)
    # ���ѷ�ļ����ҳ��
    def recruit_program(self):
        self.help6 = QtWidgets.QPushButton(self.recruit_page)
        self.help6.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help6.setObjectName("help6")
        self.help6.setText(self._translate("main_window", "����"))

        self.expedite_Label = QtWidgets.QLabel(self.recruit_page)
        self.expedite_Label.setGeometry(self.ui_zoom(0, 10, 81, 16))
        self.expedite_Label.setObjectName("expedite_Label")
        self.expedite_Label.setText(self._translate("main_window", "����"))
        self.recruit_Label = QtWidgets.QLabel(self.recruit_page)
        self.recruit_Label.setGeometry(self.ui_zoom(35, 10, 81, 16))
        self.recruit_Label.setObjectName("recruit_Label")
        self.recruit_Label.setText(self._translate("main_window", "��ļ�ƻ�"))

        self.expedite = QtWidgets.QCheckBox(self.recruit_page)
        self.expedite.setGeometry(self.ui_zoom(5, 30, 58, 22))
        self.expedite.setObjectName("expedite")

        self.recruit0 = QtWidgets.QComboBox(self.recruit_page)
        self.recruit0.setGeometry(self.ui_zoom(30, 30, 60, 22))
        self.recruit0.setObjectName("recruit0")
        self.comboboxstyle(self.recruit0)
    # ����δ��������ҳ��
    def othor_page(self):
        list = ["market","reward","random_gift","kill_game"]
        self.market_Label = QtWidgets.QLabel()
        self.reward_Label = QtWidgets.QLabel()
        self.random_gift_Label = QtWidgets.QLabel()
        self.kill_game_Label = QtWidgets.QLabel()
        for i in list:
            strl, strp = i+"_Label",  i+"_page"
            fl, fp = eval("self." + strl), eval("self." + strp)
            fl = QtWidgets.QLabel(fp)
            fl.setGeometry(self.ui_zoom(10, 10, 81, 16))
            fl.setObjectName(strl)
            fl.setText(self._translate("main_window", "��������ѡ��"))
        self.help5 = QtWidgets.QPushButton(self.market_page)
        self.help5.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help5.setObjectName("help5")
        self.help5.setText(self._translate("main_window", "����"))
        self.help7 = QtWidgets.QPushButton(self.reward_page)
        self.help7.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help7.setObjectName("help7")
        self.help7.setText(self._translate("main_window", "����"))
        self.help8 = QtWidgets.QPushButton(self.random_gift_page)
        self.help8.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help8.setObjectName("help8")
        self.help8.setText(self._translate("main_window", "����"))
        self.help9 = QtWidgets.QPushButton(self.kill_game_page)
        self.help9.setGeometry(self.ui_zoom(120, 8, 40, 20))
        self.help9.setObjectName("help9")
        self.help9.setText(self._translate("main_window", "����"))
    # �ű����к���
    def run(self):
        if not self.run_judge.isChecked():pass
        else:
            self.event_run.set()
            self.start.hide()
            self.stop.show()
            self.output_string.clear()
            # self.ico.setPixmap(QtGui.QPixmap(r"hxls_resource\ui\ico\0.png"))
            self.showtext("",nowtime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            nrun_list, drun_list = [], []
            if self.cg_name !="" :
                with open(self.game_name+"_resource\config\\" + self.cg_name + ".json", 'r', encoding='utf-8') as r:
                    self.rundir = json.load(r)
                self.cg_name = ""
                for name in self.indexdir["����"]: nrun_list += [self.rundir[name]]
                for num in range(1, 7):
                    drun_list += [self.rundir["���²ɹ�" + str(num)]]
                drun_list+=[self.rundir["�ٴβɹ�"]]
                rv = self.rundir["ս���ع�����"]
                fit = self.rundir["��ս����"]
                rt = self.rundir["���ѷ�ļ����"]
            else:
                for name in self.indexdir["����"]:
                    fc = eval("self.choose_" + self.indexdir[name])
                    nrun_list += [fc.isChecked()]
                for num in range(1, 7):
                    drun_list += [[eval("self.material" + str(num)).currentIndex(),
                                  eval("self.fund" + str(num)).currentIndex(),
                                  eval("self.plan" + str(num)).currentIndex()]]
                drun_list+=[self.re_dispatch.isChecked()]
                rv = self.review0.currentIndex()
                fit = [self.refight.isChecked(),self.fight_box.currentIndex()]
                rt = [self.expedite.isChecked(),self.recruit0.currentIndex()]
            login_list  = [self.game_path.text(),self.server_box.currentIndex()]
            self.tlist = [login_list, nrun_list,fit,drun_list,rv,rt]
            self.thready = Thready(self.tlist)
            self.thready.start()
            self.thready.testsignal.connect(self.showtext)
            self.thready.accomplish.connect(self.pause)
    # ������ֹ
    def pause(self,num):# 1�������� 2����ֹͣ,��ťֹͣ 3����ֹͣ
        self.event_run.clear()
        self.event_pause.set()
        self.run_judge.setChecked(False)
        if num == 1:pass
            # self.pixmap = QtGui.QPixmap(r"hxls_resource\ui\ico\1.png")
        else:
            self.thready.terminate()
            if num == 2:
                self.showtext("���ֶ�ֹͣ��")
                # self.pixmap = QtGui.QPixmap(r"hxls_resource\ui\ico\2.png")
            elif num ==3:pass
                # self.pixmap = QtGui.QPixmap(r"hxls_resource\ui\ico\3.png")
        self.stop.hide()
        self.start.show()
        self.ico.setPixmap(self.pixmap)
        main_window.activateWindow()
    # ��ʼ������
    def load_config_style(self):
        # ��ʼ����ս����
        self.fight_box.addItems(self.indexdir["��ս�ؿ�"])
        # ��ʼ����ǲ����
        mlist = self.indexdir["���²ɹ�����"]
        dlist = self.indexdir["Я���ʽ�"]
        plist = self.indexdir["�ɹ�����"]
        for num in range(1, 7):
            strm, strd, strp = "material" + str(num), "fund" + str(num), "plan" + str(num)
            fm, fd, fp = eval("self." + strm), eval("self." + strd), eval("self." + strp)
            fm.addItems(mlist)
            fd.addItems(dlist)
            fp.addItems(plist)
        # ��ʼ��ս���ع�����
        self.review0.addItems(self.indexdir["ս���ع�ѡ��"])
        # ��ʼ�����ѷ�ļ����
        numlist = ["0��", "100��", "200��", "300��", "400��", "500��", "600��", "700��"]
        self.recruit0.addItems(numlist)
    # ���ش�����
    def load_config(self,file):
        path =self.game_name+"_resource\config\\"+file+".json"
        with open(path, 'r', encoding='utf-8') as config_dir:
            self.configdir = json.load(config_dir)
        #���ع�������
        trans_list = self.indexdir["����"]
        for num in range(len(trans_list)):
            fc = eval("self.choose_" + self.indexdir[trans_list[num]])
            fc.setChecked(self.configdir[trans_list[num]])
        # ������ս����
        self.refight.setChecked(self.configdir["��ս����"][0])
        self.fight_box.setCurrentIndex(self.configdir["��ս����"][1])
        #������ǲ����
        for num in range(1, 7):
            strm, strd,strp = "material" + str(num), "fund" + str(num),"plan" + str(num)
            fm, fd,fp = eval("self." + strm), eval("self." + strd), eval("self." + strp)
            fm.setCurrentIndex(self.configdir["���²ɹ�"+ str(num)][0])
            fd.setCurrentIndex(self.configdir["���²ɹ�" + str(num)][1])
            fp.setCurrentIndex(self.configdir["���²ɹ�" + str(num)][2])
        self.re_dispatch.setChecked(self.configdir["�ٴβɹ�"])
        # ����ս���ع�����
        self.review0.setCurrentIndex(self.configdir["ս���ع�����"])
        # �������ѷ�ļ����
        self.expedite.setChecked(self.configdir["���ѷ�ļ����"][0])
        self.recruit0.setCurrentIndex(self.configdir["���ѷ�ļ����"][1])
    # ��������
    def save_config(self):
        for num in range(1, 7):
            strm, strd, strp = "material" + str(num), "fund" + str(num), "plan" + str(num)
            fm, fd, fp = eval("self." + strm), eval("self." + strd), eval("self." + strp)
            self.configdir["���²ɹ�" + str(num)] = [fm.currentIndex(),fd.currentIndex(),fp.currentIndex()]
        self.configdir["�ٴβɹ�"]  = self.re_dispatch.isChecked()
        self.configdir["ս���ع�����"] = eval("self.review0").currentIndex()
        self.configdir["��ս����"] = [self.refight.isChecked() ,self.fight_box.currentIndex()]
        self.configdir["���ѷ�ļ����"] = [self.expedite.isChecked() ,self.recruit0.currentIndex()]
        # self.pixmap = QtGui.QPixmap(r"hxls_resource\ui\ico\0.png")
        # self.ico.setPixmap(self.pixmap)
        self.save_config0()

if __name__ == '__main__':

    a=QtWidgets.QApplication(sys.argv)
    main_window=QtWidgets.QWidget()
    c = Common()
    b=Ui_main_window()
    b.setupUi(main_window)
    main_window.show()
    sys.exit(a.exec_())