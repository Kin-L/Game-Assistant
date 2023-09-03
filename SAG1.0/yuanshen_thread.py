# -*- coding:gbk -*-
from function import *
from PyQt5.QtCore import  QThread,pyqtSignal
import sys,json
# pyinstaller -D -w D:\Kin-project\python\venv\yuanshen\yuanshen.py
class Thready(QThread):
    testsignal = pyqtSignal(str)
    accomplish = pyqtSignal(int)
    def __init__(self,tlist):
        super(Thready, self).__init__()
        self.tlist =tlist
        with open(r"genshin_resource\index.json", 'r', encoding='utf-8') as d:
            self.indexdir = json.load(d)
    def run(self):
        print(self.tlist)
        self.yuanshen_start()
        self.testsignal.emit("��Ϸ��������")
        if self.tlist[1][1]:
            self.team()
            self.testsignal.emit("�����л���ɡ�")
        if self.tlist[1][2]:
            self.tpkatheryne()
            self.dispatch()
            self.testsignal.emit("̽����ǲ�����ɡ�")
        if self.tlist[1][3]:
            self.use_transformer()
            self.testsignal.emit("�����ʱ��Ǽ����ɡ�")
        if self.tlist[1][4]:
            self.catch_crystalfly()
            self.testsignal.emit("��׽������ɡ�")
        if self.tlist[1][5]:
            self.tpfontaine1()
            self.make_condensed()
            self.testsignal.emit("�ϳ�Ũ����֬��ɡ�")
        if self.tlist[1][6]:
            self.tpfontaine1()
            self.enter_rambler()
            self.tubby()
            self.testsignal.emit("��ȡ�������ɡ�")
        if self.tlist[1][7]:
            self.cut_tree()
            self.testsignal.emit("��ľ��ɡ�")
        self.testsignal.emit("ִ����ɡ�\n")
        if self.tlist[1][8]:
            self.testsignal.emit("���Թر���Ϸ��")
            if killgame(self.tlist[0][0], "UnityWndClass", "ԭ��"):
                self.testsignal.emit("��Ϸ�ѹرա�")
            else:
                self.testsignal.emit("error����Ϸ�رճ�ʱ��20s����")
                self.accomplish.emit(3)
        self.accomplish.emit(1)
    def yuanshen_start(self):
        imi = imitate("UnityWndClass", "ԭ��",8000,self.tlist[0][0])
        print(self.tlist[0])
        if imi.error_path_flag:
            self.testsignal.emit("error:��Ϸ����·�������ļ���")
        if imi.start_game_flag:
            self.testsignal.emit("��Ϸ��������")
        if not imi.resolution_flag:
            self.testsignal.emit("error:���������Ϸ�ֱ��ʣ�%s��%s��"%(imi.wide, imi.high))
            self.testsignal.emit("���ֶ�����Ϸ����Ϊ���ݱ�1.78��ȫ�������ޱ߿򴰿�,�����ݷֱ��ʴ��ڵ���720��")
        if not imi.start_game_flag or not imi.resolution_flag:
            self.accomplish.emit(3)
            wait(500)
        for fun in dir(imitate)[26:]:
            globals()[fun] = eval("imi." + fun)
        self.testsignal.emit("��ʼʶ����Ϸ״̬��")
        serverflag,logflag,sighinflag = self.tlist[0][1],True,True
        while 1:
            if serverflag ==0:
                if findpic((900, 995, 1030, 1043), r"genshin_resource\picture\login1.png")[1] >= 0.6:
                    serverflag =2
                    click(930, 630)
                    self.testsignal.emit("���š�")
                    wait(4000)
            elif serverflag==1:
                if logflag:
                    if findpic((863, 370, 1059, 467), r"genshin_resource\picture\login2.png")[1] >= 0.6:
                        logflag = False
                        click(953,659)
                        self.testsignal.emit("��¼B���˺š�")
                        wait(4000)
                if findpic((900, 995, 1030, 1043), r"genshin_resource\picture\login1.png")[1] >= 0.6:
                    serverflag = 2
                    click(930, 630)
                    self.testsignal.emit("���š�")
                    wait(4000)
            if sighinflag:
                if findpic((865, 240, 1060, 470), r"genshin_resource\picture\sighin.png")[1] >= 0.6:
                    sighinflag = False
                    click(930, 850)
                    wait(800)
                    click(930, 850)
                    wait(100)
                    click(930, 850)
                    wait(1000)
                    click(930, 850)
                    wait(800)
                    self.testsignal.emit("�����¿���ȡ�ɹ���")
            if findpic((57, 998, 179, 1075), r"genshin_resource\picture\world.png")[1] >= 0.6:
                self.testsignal.emit("���ص����硣")
                break
            if findpic((0, 0, 97, 88), r"genshin_resource\picture\home\home.png")[1] >= 0.6:
                self.testsignal.emit("���ص������档")
                break
            wait(2000)

    def team(self):
        self.home()
        self.testsignal.emit("��ʼȷ�϶���")
        self.opensub("��������")
        wait(1000)
        for i in range(15):
            wait(1000)
            res = findpic((37,980, 115,1058), r"genshin_resource\picture\team.png")
            if res[1] >= 0.6:
                self.testsignal.emit("���뵽�������ý��档")
                break
            elif i == 14:
                self.testsignal.emit("error:���ض������ý��泬ʱ��\n")
                self.accomplish.emit(3)
        click(77,1016)
        wait(800)
        roll(580,224,55)
        wait(500)
        click(580,224)
        wait(500)
        click(328,1016)
        wait(800)
        click(1685,1018)
        wait(500)
        click(1843,47)
        self.world()
        press("1")
        wait(300)
        press("1")
        wait(300)

    def world(self):
        i=1
        while i >0 :
            i+=1
            wait(1000)
            pos,val = findpic((57, 998, 179, 1075), r"genshin_resource\picture\world.png")
            if val >=0.6:
                i=0
                self.testsignal.emit("���ص����硣")
            elif i == 15:
                self.testsignal.emit("error:�������糬ʱ��\n")
                self.accomplish.emit(3)
    # ǰ������
    def tpxm(self):
        self.home()
        self.testsignal.emit("ǰ�����֣����ֳ�ê��1")
        self.opensub("��ͼ")
        self.map_region("����")
        click(1008,599)
        wait(800)
        self.tp_point()
        self.testsignal.emit("�������֣����ֳ�ê��1")

    # ǰ�����ֿ�ɪ��
    def tpkatheryne(self):
        self.home()
        self.testsignal.emit("ǰ���㵤���㵤͢ê��1")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�������")
        click(1107,786)
        wait(800)
        self.tp_point()
        self.testsignal.emit("ǰ���㵤��ɪ��")
        keydown("W")
        wait(2700)
        keyup("W")
        wait(500)
        keydown("A")
        wait(1500)
        keyup("A")
        wait(500)
        self.testsignal.emit("ǰ�����ֿ�ɪ�����")
    #ÿ����ǲ
    def dispatch(self):
        self.testsignal.emit("��ʼ�����ǲ")
        press("F")
        wait(1000)
        click(960, 900)
        wait(1500)
        (x,y), val = findpic((1247,311, 1337,909 ), r"genshin_resource\picture\dispatch\dispatch.png")
        if (x,y) ==(0,0):
            self.testsignal.emit("error:��ǲδ֪����")
            return False
        res,(cx,cy) = findcolor((x+30,y-15,x+110,y+15),"32CCFF")
        click(x+30,y)
        wait(2000)
        if res:
            self.testsignal.emit("���ڿ���ȡ��ǲ")
            glist = self.indexdir["��ǲ��������"]
            for g in range(len(glist)):#��ȡ
                num = -1
                while num ==-1:
                    click(glist[g][0], glist[g][1])
                    wait(800)
                    pos, val = findpic((1490, 979, 1823, 1045), r"genshin_resource\picture\dispatch\get.png")
                    if val>=0.6:
                        click(1692, 1024)
                        wait(1500)
                        click(1692, 1024)
                        wait(1500)
                    else:break
                    click(glist[g-1][0], glist[g-1][1])
                    wait(800)
            self.testsignal.emit("��ȡ��ǲ���")
        valt, num = 0, 0
        scpath = shotzone((1695, 12, 1755, 76))
        for i in range(6):
            val = findpic(scpath, r'genshin_resource\picture\number\%s.png' % (i))[1]
            if val > valt: valt, num = val, i
        os.remove(scpath)
        if num != 5:
            self.testsignal.emit("��ǰ����ǲ")
            ylist = [123, 228, 332 ,440,545]
            for num in range(5):#��ǲ
                r = self.indexdir["��ǲ����"][self.tlist[2][num]]
                self.testsignal.emit("�����ǲ��"+r)
                [x,y] = self.indexdir["��ǲ��������"][self.tlist[2][num]]
                click(x,y)
                wait(800)
                [x,y] = self.indexdir[r + "��ǲ��������"][self.tlist[3][num]]
                click(x, y)
                wait(800)
                cname = r+"-"+self.indexdir[r + "��ǲ����"][self.tlist[3][num]]
                scpath = shotzone((1490,979, 1823,1050))
                if findpic(scpath,r"genshin_resource\picture\dispatch\recall.png")[1] >=0.6:
                    self.testsignal.emit("ִ���У�"+cname)
                    os.remove(scpath)
                elif findpic(scpath, r"genshin_resource\picture\dispatch\max.png")[1] >=0.6:
                    self.testsignal.emit("�Ѵ���ǲ����")
                    os.remove(scpath)
                    break
                else:
                    res1 = findpic(scpath, r"genshin_resource\picture\dispatch\choose.png")[1]
                    res2 = findpic(scpath, r"genshin_resource\picture\dispatch\get.png",rm=True)[1]
                    if res2>=0.7:
                        click(1692, 1024)
                        wait(1500)
                        click(1692, 1024)
                        wait(1500)
                    if res1>=0.7 or res2>=0.7:
                        self.testsignal.emit("���Կ�ʼ��ǲ��"+cname)
                        click(1793, 683)
                        wait(500)
                        click(1692, 1024)
                        wait(1000)
                        alist,blist,clist = [],[],[]
                        for y in ylist:
                            scpath = shotzone((154,y,430,y+82))
                            if findpic(scpath,r"genshin_resource\picture\dispatch\exploring.png")[1]>=0.75:
                                os.remove(scpath)
                                pass
                            else:
                                res1 = findpic(scpath,r"genshin_resource\picture\dispatch\20h.png")[1]
                                res2 = findpic(scpath,r"genshin_resource\picture\dispatch\25percent.png")[1]
                                res3 = findpic(scpath,r"genshin_resource\picture\dispatch\no_promote.png",rm=True)[1]
                                if res1 or res2 or res3:
                                    if res1>res2 and res1>res3:alist += [y]
                                    elif res2>res3:blist += [y]
                                    else:clist += [y]
                                else:self.testsignal.emit("��ǲѡ��ʶ�����")
                        if alist :cy = alist[0]
                        else:
                            if blist: cy = blist[0]
                            else:cy = clist[0]
                        click(269, cy+40)
                        self.testsignal.emit("��ʼ��ǲ��"+cname)
                        wait(800)
                    else:
                        self.testsignal.emit("error:��ǲִ��δ֪����")
                        return False
        # �ر���ǲ
        click(1853, 51)
        self.testsignal.emit("��ǲ����")
        wait(3500)
        self.home()

    #��������
    def home(self):
        m = 0
        while m >= 0:
            m += 1
            wait(1500)
            (x, y), val = findpic((0, 0, 97, 88), r"genshin_resource\picture\home\home.png")
            if val >= 0.6:m = -1
            else:press("esc")
            if m == 15:
                self.testsignal.emit("error:�������泬ʱ��\n")
                self.accomplish.emit(3)
    #����������ӽ���
    def opensub(self,cho):
        dir = {"��ͼ":(358,697),"����":(663,556),"ð��֤֮":(659,698),"��������":(352,416)}
        x,y=dir[cho]
        click(x,y)
        self.testsignal.emit("��"+cho)
        wait(2000)
    #�ڵ�ͼ����ѡ��������
    def map_region(self,str):
        tdir = {"�ɵ�":"mondstadt" ,"����":"liyue" ,"����":"inazuma" ,"����":"sumeru" ,"���¿���":"underground" }
        click(1835, 1024)
        wait(800)
        roll(1657, 747, 5)
        wait(800)
        (x1, y1), val1 = findpic((1445, 83, 1608, 1012), "genshin_resource\picture\maps\\"+tdir[str]+".png")
        (x2, y2), val2 = findpic((1445, 83, 1608, 1012), r"genshin_resource\picture\maps\now.png")
        if (val1 >= 0.6) and (val2 >= 0.6) and 0<= (y2 - y1) <= 60:
            click(x1, y1 + 120)
            wait(800)
            click(1835, 1024)
            wait(800)
        click(x1, y1)
        wait(500)
        for i in range(5):
            click(46, 651)
            wait(300)
        for i in range(2):
            click(44, 426)
            wait(300)

    #ѡ��ȷ�ϴ���ê��ͼ�겢��ʼ���ͣ�����жϴ��ͳɹ�
    def tp_point(self,num=0):
        (x, y), val = findpic((1245, 621, 1528, 1023), "genshin_resource\picture\maps\\tp_point%s.png"%(num))
        if val >= 0.75:
            click(x, y)
            wait(800)
        click(1634, 1003)
        wait(3000)
        self.world()
    # ǰ������
    def tply(self):
        self.home()
        self.testsignal.emit("ǰ�����£����¸�ê��1")
        self.opensub("map")
        self.map_region("����")
        click(958,537 )
        wait(800)
        self.tp_point()
        self.testsignal.emit("�������£����¸�ê��1")
    def tpfontaine1(self):
        self.home()
        self.testsignal.emit("ǰ���㵤���㵤͢ê��1")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�������")
        click(1107, 786)
        wait(800)
        self.tp_point()
        self.testsignal.emit("����㵤���㵤͢ê��1")

    # ���볾���
    def enter_rambler(self):
        self.home()
        self.testsignal.emit("ǰ���������Ĭ�ϳ����-������")
        self.opensub("����")
        click(1053, 48)
        wait(800)
        (x,y),val=findpic((109,113,1275,459),r"genshin_resource\picture\lit_tools\rambler.png")
        click(x,y)
        wait(800)
        click(1694, 1022)
        wait(800)
        press("esc")
        wait(1000)
        press("F")
        wait(3000)
        self.world()
        self.testsignal.emit("���ﳾ�����Ĭ�ϳ����-������")
    # ��Բ��ȡ
    def tubby(self):
        self.testsignal.emit("��ʼ��ȡ�����")
        keydown("S")
        wait(200)
        keyup("S")
        wait(500)
        keydown("D")
        wait(400)
        keyup("D")
        press("F")
        wait(2000)
        click(1300,431)
        wait(2000)
        click(1300,431)
        wait(2000)
        click(1076, 950)
        wait(800)
        click(1815,899)
        wait(800)
        click(1805, 704)
        wait(800)
        click(1815, 899)
        wait(800)
        click(1874, 48)
        wait(4000)
        click(1362,800)
        wait(1000)
        click(1362,800)
        self.home()

    #�ϳ���֬
    def make_condensed(self):
        self.testsignal.emit("ǰ���ϳ�Ũ����֬")
        keydown("W")
        wait(5300)
        keyup("W")
        wait(500)
        keydown("D")
        wait(600)
        keyup("D")
        wait(500)
        press("F")
        wait(1000)
        click(960, 950)
        wait(1500)
        (x,y),val = findpic((57,110,627,800),r"genshin_resource\picture\valu_tools\nssz.png")
        if val >= 0.6:
            click(x,y)
            wait(800)
            click(1298,400)
            wait(800)
            valt,num=0,0
            scpath = shotzone((976, 866,1043, 943))
            for i in range(6):
                val = findpic(scpath,r"genshin_resource\picture\number\%s.png"%(i))[1]
                if val>valt:valt,num =val,i
            os.remove(scpath)
            click(1618,497)
            wait(800)
            if num != None:
                for i in range(5-num):
                    click(1562,674)
                    wait(400)
                click(1727,1019)
                wait(800)
                click(1173,786)
                wait(200)
                self.testsignal.emit("�ϳ�Ũ����֬�ɹ�")
            else:
                self.testsignal.emit("error:num is" + str(type[strn])+"\n")
                self.accomplish.emit(3)
        else:self.testsignal.emit("�޷��ϳ�Ũ����֬��ȱ����֬�򾧺�")
        click(1836,48)
        wait(2200)

    # ׽����ִ���ж�
    def catch_crystalfly(self):
        self.testsignal.emit("��ʼ��׽������")
        for num in range(len(self.tlist[5])):
            if self.tlist[5][num]:
                self.testsignal.emit("��ʼ��λ"+str(num+1))
                eval("self.fly"+str(num+1))()
                self.testsignal.emit("������λ"+str(num+1))

    # ׽����-����֮���·�
    def fly3(self):
        self.home()
        self.testsignal.emit("׽����-����֮���·�")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("���ķ���")
        click(1872, 34)
        wait(800)
        drag((960, 967), (0, -800))
        wait(500)
        click(1152,739 )
        wait(800)
        self.tp_point(0)
        keydown("A")
        wait(2800)
        keyup("A")
        wait(500)
        keydown("S")
        wait(5400)
        keyup("S")
        wait(500)
        keydown("A")
        wait(2100)
        keyup("A")
        wait(500)
        keydown("W")
        for i in range(5):
            wait(300)
            press("F")
        wait(200)
        keyup("W")
        wait(500)

    # ׽����-�����ݿ��·�
    def fly2(self):
        self.home()
        self.testsignal.emit("׽����-�����ݿ��·�")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("���ķ���")
        click(1872, 34)
        wait(800)
        drag((960, 967), (0, -800))
        wait(500)
        click(832,732)
        wait(800)
        self.tp_point(0)
        keydown("W")
        wait(1300)
        keyup("W")
        wait(500)
        keydown("A")
        for i in range(7):
            wait(300)
            press("F")
        keyup("A")

    # ׽����-���ǹ���
    def fly4(self):
        self.home()
        self.testsignal.emit("׽����-���ǹ���")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("Ե����")
        click(577,692)
        wait(800)
        self.tp_point(0)
        keydown("S")
        for i in range(4):
            wait(300)
            press("F")
        keyup("S")
        wait(500)
        keydown("D")
        for i in range(4):
            wait(300)
            press("F")
        keyup("D")
        wait(500)
        keydown("S")
        wait(5000)
        keyup("S")
        wait(500)
        keydown("A")
        wait(1600)
        press("SPACE")
        wait(1600)
        keyup("A")
        wait(500)
        keydown("W")
        wait(500)
        keyup("W")
        wait(500)
        press("2")
        wait(800)
        press("E")
        wait(200)
        keydown("W")
        for i in range(8):
            wait(300)
            press("F")
        keyup("W")
        wait(500)
        press("1")
    # ׽����-����ƽ����
    def fly6(self):
        self.home()
        self.testsignal.emit("׽����-����ƽ����")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("����֮ͥ")
        click(1139,528)
        wait(800)
        self.tp_point(0)
        keydown("S")
        for i in range(12):
            wait(300)
            press("F")
        keyup("S")
        wait(500)
        keydown("D")
        for i in range(2):
            wait(300)
            press("F")
        keyup("D")
        wait(500)
        keydown("S")
        for i in range(5):
            wait(300)
            press("F")
        keyup("S")
        wait(500)
        keydown("A")
        for i in range(4):
            wait(300)
            press("F")
        keyup("A")
        wait(500)
        keydown("W")
        for i in range(5):
            wait(300)
            press("F")
        keyup("W")
        wait(500)
    # ׽����-���Ҿ�Ԩ������������
    def fly5(self):
        self.home()
        self.testsignal.emit("׽����-���Ҿ�Ԩ������������")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�����Ĺ�")
        click(878,698)
        wait(800)
        self.tp_point(2)
        keydown("A")
        for i in range(8):
            wait(300)
            press("F")
        wait(200)
        keyup("A")
        wait(500)
        keydown("W")
        for i in range(7):
            wait(300)
            press("F")
        wait(100)
        keyup("W")
        wait(500)
        keydown("A")
        for i in range(10):
            wait(300)
            press("F")
        keyup("A")
        wait(500)
        keydown("W")
        for i in range(7):
            wait(300)
            press("F")
        keyup("W")
    # ׽����-������Ϸ�
    def fly1(self):
        self.home()
        self.testsignal.emit("׽����-������Ϸ�")
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("���ķ���")
        click(962,738)
        wait(800)
        self.tp_point(0)
        keydown("D")
        wait(4700)
        keyup("D")
        wait(500)
        keydown("W")
        wait(6000)
        keyup("W")
        wait(500)
        keydown("D")
        wait(150)
        keyup("D")
        wait(500)
        keydown("W")
        wait(3900)
        press("SPACE")
        wait(400)
        press("F")
        wait(700)
        keyup("W")

    def tp_domain(self,str):
        tdir = {"������������":"cecilia_garden","���ķ���":"city_of_gold","����֮ͥ":"slumbering_court",
                "�����Ĺ�":"the_lost_valley","��ɫ֮ͥ":"violet_court","�������":"deep_tides","�������ĩ":"denouement",
                "�԰׵�����":"pale_glory","Ե����":"enlightenment","ɰ��֮ͥ":"flow_sand"}
        self.testsignal.emit("���Դ��͵��ؾ���"+str)
        for num in range(15):
            wait(200)
            (x, y), val = findpic((752, 270, 977, 886), r"genshin_resource\picture\domain\\"+tdir[str]+".png")
            if val >=0.8:
                click(1555, y)
                wait(2000)
                break
            elif num <= 13:
                roll(1116, 296, -32)
            else:
                self.testsignal.emit("error:δʶ���ؾ�-"+str+"\n")
                self.accomplish.emit(3)
    #ʹ�ò����ʱ���
    def use_transformer(self):
        self.home()
        self.testsignal.emit("�������ʱ���")
        self.opensub("����")
        click(1053, 48)
        wait(800)
        (x, y), val = findpic((109, 113, 1275, 459), r"genshin_resource\picture\lit_tools\para_trans.png")
        if val >= 0.75:
            self.testsignal.emit("�����ʱ��ǿ���")
            click(x, y)
            wait(800)
            (x, y), val = findpic((1645, 971, 1769, 1058), r"genshin_resource\picture\lit_tools\para_retrieve.png")
            if val>=0.6:
                click(x, y)
                wait(1500)
            else:
                click(1840, 47)
                wait(1500)
            self.opensub("ð��֤֮")
            click(300,440 )
            wait(800)
            click(537,296)
            wait(800)
            self.tp_domain("��ɫ֮ͥ")
            click(1669, 1009)
            self.world()
            keydown("A")
            wait(2100)
            keyup("A")
            wait(500)
            keydown("W")
            wait(2100)
            keyup("W")
            wait(500)
            self.home()
            self.opensub("����")
            click(1053, 48)
            wait(800)
            (x, y), val = findpic((109, 113, 1275, 459), r"genshin_resource\picture\lit_tools\para_trans.png")
            click(x, y)
            wait(800)
            click(1694, 1022)
            wait(1500)
            click(1633,549 )
            wait(1000)
            press("F")
            wait(2000)
            for str in self.tlist[4]:
                if str=="":
                    self.testsignal.emit("δ���ÿ��ò��ϡ�")
                    break
                else:
                    c = os.path.splitext(str)[0]
                    c,b = os.path.split(c)
                    a= os.path.split(c)[1]
                    self.testsignal.emit("������Ӳ��ϣ�"+b)
                (x, y), val = findpic((456,0,1450,94), "genshin_resource\picture\\"+a+"\\"+a+".png")
                click(x, y)
                wait(800)
                (x, y), val = findpic((104,107,1282,955), str)
                click(x, y)
                wait(800)
                click(497,1021)
                wait(800)
                res,(cx,cy) = findcolor((1406,1001,1446,1033),"D8E5EC")
                if res:
                    click(1703,1020)
                    wait(800)
                    click(1178, 757)
                    wait(1000)
                    self.testsignal.emit("�����ʱ�����װ����")
                    break
                else:self.testsignal.emit("�����ʱ��ǻ�δװ����")
            self.testsignal.emit("�����ʱ��ǳ����С�")
            i=0
            while i>=0:
                i+=1
                wait(2000)
                pos, val = findpic((871,242, 1050,339), r"genshin_resource\picture\acquire.png")
                if val>=0.6:
                    i=-1
                    click(961,804)
                    self.testsignal.emit("�����ʱ���ʹ�óɹ���")
                    self.home()
                elif i == 15:
                    self.testsignal.emit("�ȴ������ʱ���ʹ�ó�ʱ��\n")
                    self.accomplish.emit(3)
        else:
            self.testsignal.emit("�����ʱ��ǣ�δ�ҵ�/��ȴ�У�")
            click(1840,47 )
            wait(1500)
    def cut_tree(self):
        runlist = []
        for u in range(1,4):
            woodlist = self.indexdir["tree_kind%s"%(u)]
            for num in range(len(woodlist)):
                if self.tlist[6][u][num]:runlist+=[woodlist[num]]
        if self.tlist[6][0] =="":cirnum = 0
        else:cirnum = int(self.tlist[6][0])
        for i in range(cirnum):
            for wood in runlist:
                eval("self."+wood)()

    #����ľ
    def mallow(self):
        self.testsignal.emit("�ɼ�������ľ��9���ľ��3")
        self.home()
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�������ĩ")
        wait(800)
        click(1682,1008)
        self.world()
        keydown("S")
        wait(10000)
        keyup("S")
        wait(300)
        keydown("D")
        wait(300)
        keyup("D")
        wait(300)
        keydown("S")
        wait(2000)
        keyup("S")
        wait(300)
        keydown("A")
        wait(1000)
        keyup("A")
        wait(500)
        press("Z")
        wait(500)
    #��ľ
    def torch(self):
        self.testsignal.emit("�ɼ�����ľ��15")
        self.home()
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�԰׵�����")
        click(545,1000)
        wait(800)
        self.tp_point(1)
        keydown("A")
        wait(3300)
        keyup("A")
        wait(500)
        keydown("W")
        wait(3000)
        keyup("W")
        wait(500)
        keydown("A")
        wait(1200)
        keyup("A")
        wait(500)
        press("Z")
        wait(500)
    #�חqľ
    def ash(self):
        self.testsignal.emit("�ɼ����חqľ��12")
        self.home()
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�԰׵�����")
        click(522,808)
        wait(800)
        self.tp_point(2)
        keydown("S")
        wait(8000)
        keyup("S")
        wait(500)
        keydown("A")
        wait(7000)
        keyup("A")
        wait(500)
        keydown("W")
        wait(3400)
        keyup("W")
        wait(500)
        keydown("A")
        wait(4700)
        keyup("A")
        wait(500)
        press("Z")
        wait(500)
    #�ľ
    def linden(self):
        self.testsignal.emit("�ɼ����ľ��9")
        self.home()
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�������ĩ")
        wait(800)
        click(1682, 1008)
        self.world()
        keydown("S")
        wait(2500)
        keyup("S")
        wait(500)
        keydown("A")
        wait(2500)
        keyup("A")
        wait(300)
        keydown("W")
        wait(11800)
        keyup("W")
        wait(300)
        keydown("A")
        wait(100)
        keyup("A")
        wait(300)
        press("Z")
        wait(500)
    #���ľ
    def cypress(self):
        self.testsignal.emit("�ɼ������ľ��15")
        self.home()
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("�������ĩ")
        click(1213,201)
        wait(800)
        self.tp_point(0)
        keydown("S")
        wait(4000)
        keyup("S")
        wait(500)
        keydown("D")
        wait(6000)
        keyup("D")
        wait(500)
        keydown("W")
        wait(3000)
        keyup("W")
        wait(500)
        keydown("D")
        wait(3600)
        keyup("D")
        wait(500)
        keydown("W")
        wait(2100)
        keyup("W")
        wait(500)
        press("Z")
        wait(500)
    #��ľ
    def athel(self):
        self.testsignal.emit("�ɼ�����ľ��12")
        self.home()
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("���ķ���")
        click(371,837)
        wait(800)
        self.tp_point(0)
        keydown("A")
        wait(1300)
        keyup("A")
        wait(500)
        keydown("W")
        wait(6300)
        keyup("W")
        wait(500)
        press("Z")
        wait(500)
    #�μ�ľ
    def yumemiru(self):
        self.testsignal.emit("�ɼ����μ�ľ��12")
        self.home()
        self.opensub("ð��֤֮")
        click(300, 440)
        wait(800)
        click(537, 296)
        wait(800)
        self.tp_domain("ɰ��֮ͥ")
        click(937,617)
        wait(800)
        self.tp_point(0)
        keydown("S")
        wait(1300)
        keyup("S")
        wait(500)
        keydown("A")
        wait(400)
        keyup("A")
        wait(300)
        press("Z")
        wait(300)
        keydown("W")
        wait(500)
        keyup("W")
        wait(500)
        keydown("D")
        wait(2200)
        keyup("D")
        wait(500)
        keydown("W")
        wait(1000)
        keyup("W")
        wait(300)
        keydown("D")
        wait(800)
        keyup("D")
        wait(300)
        keydown("W")
        wait(500)
        keyup("W")
        wait(9000)
        press("Z")
        wait(500)
if __name__ == '__main__':pass