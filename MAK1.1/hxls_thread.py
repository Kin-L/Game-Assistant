# -*- coding:gbk -*-
from function import *
from PyQt5.QtCore import  QThread,pyqtSignal
import sys,json
# pyinstaller -D -w D:\Kin-project\python\venv\hxls\hxls.py
class Thready(QThread):
    testsignal = pyqtSignal(str)
    accomplish = pyqtSignal(int)
    def __init__(self,tlist):
        super(Thready, self).__init__()
        self.tlist =tlist
        with open(r"hxls_resource\index.json", 'r', encoding='utf-8') as d:
            self.indexdir = json.load(d)
    def run(self):
        print(self.tlist)
        self.hxls_start()
        self.testsignal.emit("(�Զ�������ʻ�����ѻ���)")
        click(769,590)
        wait(300)
        if self.tlist[1][1]:
            self.fight()
            self.testsignal.emit("�����ɣ���ս��")
        if self.tlist[1][2]:
            self.dispatch()
            self.testsignal.emit("�����ɣ����²ɹ���")
        if self.tlist[1][3]:
            self.review()
            self.testsignal.emit("�����ɣ�ս���عˡ�")
        if self.tlist[1][4]:
            self.getmarket()
            self.testsignal.emit("�����ɣ�������ȡ��")
        if self.tlist[1][5]:
            self.recruit()
            self.testsignal.emit("�����ɣ����ѷ�ļ��")
        if self.tlist[1][6]:
            self.reward()
            self.testsignal.emit("�����ɣ����չ�����")
        if self.tlist[1][7]:
            self.random_gift()
            self.testsignal.emit("�����ɣ���������")
        self.testsignal.emit("ִ����ɡ�")
        if self.tlist[1][8]:
            self.testsignal.emit("���Թر���Ϸ��")
            if killgame(self.tlist[0][0],"UnityWndClass", "��������"):
                self.testsignal.emit("��Ϸ�ѹرա�")
            else:
                self.testsignal.emit("error����Ϸ�رճ�ʱ��20s����")
                self.accomplish.emit(3)
        self.accomplish.emit(1)

    def hxls_start(self):
        imi = imitate("UnityWndClass", "��������",path = self.tlist[0][0])
        if imi.error_path_flag:
            self.testsignal.emit("error:��Ϸ����·�������ļ���")
        if imi.start_game_flag:
            self.testsignal.emit("��Ϸ��������")
        if not imi.resolution_flag:
            self.testsignal.emit("error:���������Ϸ�ֱ��ʣ�%s��%s��" % (imi.wide, imi.high))
            self.testsignal.emit("���ֶ�����Ϸ����Ϊ���ݱ�1.78��ȫ�������ޱ߿򴰿�,�����ݷֱ��ʴ��ڵ���720��")
        if not imi.start_game_flag or not imi.resolution_flag:
            self.accomplish.emit(3)
            wait(500)
        for fun in dir(imitate)[26:]:
            globals()[fun] = eval("imi." + fun)
        self.testsignal.emit("��ʼʶ����Ϸ״̬��")
        serverflag,logflag = self.tlist[0][1],True
        while 1:
            if serverflag==0:
                if findpic((871, 612, 1052, 654), r"hxls_resource\picture\startgame1.png")[1] >= 0.6:
                    wait(100)
                    click(930, 630)
                    self.testsignal.emit("��¼��Ϸ��")
                    wait(5000)
                    serverflag=2
            elif serverflag==1:
                if logflag:
                    if findpic((830, 595, 1093, 682), r"hxls_resource\picture\startgame2.png")[1] >= 0.6:
                        logflag = False
                        wait(100)
                        click(960,633)
                        self.testsignal.emit("��¼�˺š�")
                        wait(1500)
                if findcolor((910, 658, 992, 704), "blue")[0]:
                    wait(100)
                    click(958,679)
                    self.testsignal.emit("��¼��Ϸ��")
                    wait(5000)
                    serverflag = 2
            if findpic((887, 240, 1032, 280), r"hxls_resource\picture\sighin.png")[1] >= 0.6: # ǩ������
                click(970, 930)
                wait(1500)
                click(1789, 120)
                self.testsignal.emit("ǩ���ɹ���")
                wait(1000)
                for num in range(10):
                    (x, y), sim = findpic((0, 0, 1920, 1080), r"hxls_resource\picture\close\close1.png")
                    if sim >= 0.6:
                        click(x, y)
                        wait(1500)
                    else:break
                    wait(800)
            if findpic((1739, 37, 1814, 98), r"hxls_resource\picture\home.png")[1] >= 0.6:# ������
                self.testsignal.emit("���ص������档")
                break
            wait(1500)

    def fight(self):
        self.testsignal.emit("��ʼ��飺��ս��")
        val = findpic((1652, 306, 1788, 393), r"hxls_resource\picture\fight\fighting.png")[1]
        if val>=0.6:
            self.testsignal.emit("���ν����У������ٴο�����ս��")
        elif not findcolor((1784, 382, 1825, 429), "2000FF")[0]:
            self.testsignal.emit("��ս�����С�")
            if self.tlist[2][0]:self.testsignal.emit("û���ٴ�����Ŀ�ꡣ")
        else:
            click(1739, 420)
            self.testsignal.emit("������ɣ���ȡ���ν�����")
            wait(1500)
            while 1:
                if findpic((1670, 50, 1820, 110), r"hxls_resource\picture\fight\retour.png")[1] >= 0.6:
                    if self.tlist[2][0]:
                        self.testsignal.emit("�����ظ��ϴ���ս��")
                        click(1744, 80)
                        wait(1500)
                        ((x, y), sim) = findpic((1100, 335, 1900, 983), r"hxls_resource\picture\fight\add.png")
                        if sim >= 0.6:
                            click(x + 120, y)
                            wait(1000)
                            click(x, y + 280)
                            wait(1000)
                            if findpic((1085, 716,1256, 846), r"hxls_resource\picture\fight\lack.png")[1]>0.75:
                                self.testsignal.emit("��Դ���㡣")
                                click(761,781)
                                wait(1000)
                            else:
                                self.testsignal.emit("��ʼ�ظ��ϴ���ս��")
                            click(288, 78)
                            wait(1500)
                        else:
                            self.testsignal.emit("error:�ظ��ϴ���սδ֪����")
                            self.accomplish.emit(3)
                    else:
                        click(971, 930)
                        wait(800)
                    break
                if findpic((875, 182, 1048, 221), r"hxls_resource\picture\lvup.png")[1] >= 0.6:
                    self.testsignal.emit("�ȼ�������")
                    click(1282, 690)
                wait(1000)
        if (not self.tlist[2][0]) and (val==0):
            click(1446,359)
            wait(1500)
            click(964,1029)
            wait(1500)
            num = self.tlist[2][1]
            x,y = [(519,545),(885,554),(1248,534)][num]
            click(x,y)
            wait(2000)
            click(786, 555)
            wait(1500)
            click(1077,856)
            wait(1000)
            click(1525,549)
            wait(500)
            click(1458,816)
            wait(1000)
            if findpic((1085, 716, 1256, 846), r"hxls_resource\picture\fight\lack.png")[1] >= 0.75:
                self.testsignal.emit("��Դ���㡣")
                click(761, 781)
                wait(1000)
            else:
                self.testsignal.emit("��ʼ��ս����ȡ "+["��","����־","��"][num])
            click(288, 78)
            wait(1500)


    def dispatch(self):
        self.testsignal.emit("��ʼ��飺���²ɹ���")
        click(149, 795)
        wait(1000)
        click(1563, 141)
        wait(1000)
        dlist = []
        for n in range(6):
            y1, y2 = self.indexdir["���²ɹ�����"][n]
            zoom = (1068, y1, 1263, y2)
            x, y = self.indexdir["���²ɹ�����"][n]
            click(x, y)
            wait(200)
            if findpic(zoom, r"hxls_resource\picture\dispatch\condition2.png")[1] >= 0.6:  # �����ǲ
                dlist+=[n]
                x, y = self.indexdir["���²ɹ�����"][n]
                click(x, y)
                wait(500)
                click(1708, 977)
                wait(1200)
                click(1708, 977)
                wait(1200)
                self.testsignal.emit("���²ɹ�" + str(n + 1) + "����ɣ�����ȡ��")
            elif findpic((1632, 927,1796, 1013), r"hxls_resource\picture\dispatch\condition1.png")[1]>=0.6:
                self.testsignal.emit("���²ɹ�" + str(n + 1) + "�������С�")
            elif findpic(zoom, r"hxls_resource\picture\dispatch\condition0.png")[1]>=0.6:#��ǲ
                dlist += [n]
                self.testsignal.emit("���²ɹ�" + str(n + 1) + "������ǲ��")
        for n in dlist:
            self.testsignal.emit("���²ɹ�" + str(n + 1) + "�����Կ�ʼ��ǲ��")
            y1,y2 = self.indexdir["���²ɹ�����"][n]
            zoom = (1068, y1, 1263, y2)
            x,y = self.indexdir["���²ɹ�����"][n]
            click(x,y)
            wait(500)
            click(1562, 939)
            wait(800)
            mnum,fnum,pnum = self.tlist[3][n]
            tpath = "hxls_resource\picture\dispatch\zone"+str(mnum)+".png"
            (x,y), sim = findpic((666, 420, 1860, 484), tpath)
            if sim ==0:
                drag((1128,451),(-200,0))
                wait(800)
                (x,y), sim = findpic((666, 420, 1860, 484), tpath)
            click(x,y)
            wait(500)
            x, y = [(951, 667), (961, 749), (960, 838)][fnum]
            click(x, y)
            wait(500)
            click(1571, 883)
            wait(1000)
            (x, y), sim = findpic((194, 145, 454, 585), r"hxls_resource\picture\dispatch\plan"+str(pnum)+".png")
            if sim >=0.85:
                click(x, y)
                wait(500)
                self.testsignal.emit("���²ɹ���ʼ��"+self.indexdir["���²ɹ�����"][mnum]+
                                     "-"+self.indexdir["Я���ʽ�"][fnum]+
                                     "-"+self.indexdir["�ɹ�����"][pnum])
            else:
                self.testsignal.emit("�ɹ�����δ�ҵ�Ŀ�꣬���Զ�ѡ��һ��λ��")
                self.testsignal.emit("���²ɹ���ʼ��" + self.indexdir["���²ɹ�����"][mnum] +
                                     "-" + self.indexdir["Я���ʽ�"][fnum])
                click(143,151)
                wait(500)
            click(397, 1008)
            wait(1500)
        # ����
        click(296, 75)
        wait(1000)

    def review(self):
        self.testsignal.emit("��ʼ��飺ս���عˡ�")
        if findcolor((1631,876,1708,958), "red")[0]:
            self.testsignal.emit("����ս���ع�����ɡ�")
            click(1628, 946)
            wait(1000)
            click(258, 386)
            wait(1000)
            # ս��֧Ԯ
            self.testsignal.emit("��ʼս��֧Ԯ��")
            list = [(613, 795),(779, 799),(954, 803),(1132, 795),(1295, 799),(1502, 798),(1666, 798)]
            for num in range(3):
                for (x,y) in list:
                    click(x,y)
                    wait(300)
                if num < 2:
                    click(1646, 347)
                    wait(500)
                if num < 1:wait(8500)
            self.testsignal.emit("ս��֧Ԯ��ɡ�")
            # ս���ع�
            self.testsignal.emit("��ʼ���ս���عˡ�")
            click(293, 277)
            wait(500)
            list = [(575, 820, 825, 868,1),(1003, 821, 1252, 867,2),(1430, 822, 1680, 867,3)]
            for (x1,y1,x2,y2,n) in list:
                (x,y),val = findpic((x1,y1,x2,y2), r"hxls_resource\picture\review\reviewed.png")
                if val >= 0.6:#��ɻع�
                    self.testsignal.emit("ս���ع�%s������ɡ�"%(n))
                    click(x,y)
                    wait(1000)
                    click(1648, 858)
                    wait(1000)
                    click(1060, 868)
                    wait(1500)
                else:
                    (x,y),val = findpic((x1,y1,x2,y2), r"hxls_resource\picture\review\toreview.png")
                    if val >= 0.6:#��ʼ�ع�
                        self.testsignal.emit("ս���ع�%s�����С�"%(n))
                    else:
                        self.testsignal.emit("ս���ع�%s�������С�" % (n))
                if val >= 0.6:
                    self.testsignal.emit("���Դ���ս���عˡ�")
                    click(x,y)
                    wait(1000)
                    click(734, 846)
                    wait(500)
                    if self.tlist[4] !="0%":
                        while 1 :
                            rvpath = "hxls_resource\picture\\review\su"+self.indexdir["ս���ع�ѡ��"][self.tlist[4]][:-1]+".png"
                            (x,y),val = findpic((698, 131, 756, 934), rvpath)
                            if val >= 0.75:
                                click(x,y)
                                wait(500)
                                break
                            else:
                                roll(476, 833,-19)
                                wait(800)
                    click(524, 1007)
                    wait(1000)
                    click(1652, 875)
                    self.testsignal.emit("ս���ع˿�ʼ��")
                    wait(1500)
            # ����
            click(296, 75)
            wait(1000)
        else:
            self.testsignal.emit("����ս���ع���ɡ�")
            wait(500)

    def getmarket(self):
        self.testsignal.emit("��ʼ��飺������ȡ��")
        if not findcolor((304, 300, 377, 369), "red")[0]:
            self.testsignal.emit("�������޿���ȡ��")
        else:
            click(300, 383)
            wait(1000)
            if findcolor((294, 440, 334, 486),"red")[0]:
                click(217,487)
                wait(500)
                if findpic((510, 250, 684, 334), r"hxls_resource\picture\market\daily.png")[1]>=0.6:
                    click(601,247)
                    wait(1200)
                    click(1257,723)
                    wait(1200)
                    self.testsignal.emit("��ȡÿ�������ɡ�")
                    click(1054,837)
                    wait(1200)
                else:self.testsignal.emit("����ÿ���������ȡ��")
            else:
                self.testsignal.emit("����ÿ���������ȡ��")
            if findcolor((270, 538, 355, 613), "red")[0]:
                click(214, 598)
                wait(1000)
                click(1516, 50)
                wait(2000)
                self.testsignal.emit("��ȡԮ��Э����ɡ�")
                click(1010, 712)
                wait(2000)
            else:
                self.testsignal.emit("����Ԯ��Э�����ȡ��")
            click(299, 77)
            wait(1000)

    def recruit(self):
        self.testsignal.emit("��ʼ���:���ѷ�ļ��")
        click(1469,697)
        wait(2000)
        tzone = [(171, 234,379, 338),(174, 346,378, 445),(172, 455,377, 556)]
        tclick = [(129,290 ),(126,395),(131,501)]
        vflag,cflag = True,self.tlist[5][0]
        for n in range(3):
            lzone = tzone[n]
            x, y = tclick[n]
            if findpic(lzone, r"hxls_resource\picture\recruit\accomplish.png")[1] >= 0.6:
                self.testsignal.emit("��ļ%s����ɡ�������ȡ��"%(n+1))
                self.receive_recruit(x, y)
            while 1:
                if findpic(lzone, r"hxls_resource\picture\recruit\new.png")[1] >= 0.6:
                    self.testsignal.emit("��ļ%s�����С����Կ�ʼ��ļ��"%(n+1))
                    click(x, y)
                    wait(1000)
                    if findcolor((480, 253,499, 273), "2F2C30")[0]:
                        self.testsignal.emit("��ͨ��ļ��")
                        vflag = self.create_recruit()
                        if (not cflag) or (not vflag):break
                        else:
                            self.testsignal.emit("����ʹ�ø�����Ӱ����")
                            click(743, 811)
                            wait(1000)
                            if findpic((903, 70, 1021, 141), r"hxls_resource\picture\recruit\lack.png")[1]>=0.6:
                                self.testsignal.emit("ȱ�ٸ�����Ӱ����")
                                cflag = False
                            else:
                                self.testsignal.emit("������Ӱ��ʹ�óɹ���")
                                self.receive_recruit(x, y)
                    else:
                        if findcolor((480, 253,499, 273), "purple")[0]:
                            self.testsignal.emit("���ֱس�SR��ļ��")
                        elif findcolor((480, 253,499, 273), "orange+yellow")[0]:
                            self.testsignal.emit("���ֱس�SSR��ļ��")
                        break
                else:
                    self.testsignal.emit("��ļ%s�������С�"%(n+1))
                    break
            if not vflag: break
        click(296, 75)
        wait(1000)
    def create_recruit(self):
        for i in range(self.tlist[5][1]):
            click(990, 626)
            wait(100)
        click(871, 818)
        wait(800)
        if findpic((903, 70, 1021, 141), r"hxls_resource\picture\recruit\lack.png")[1]>=0.6:
            self.testsignal.emit("ȱ�ٸ�����Լ�¼��")
            return False
        else:
            self.testsignal.emit("���ѷ�ļ��ʼ��")
            return True
    def receive_recruit(self,x,y):
        click(x, y)
        wait(2000)
        if findpic((252, 444, 421, 553), r"hxls_resource\picture\recruit\N.png")[1] >= 0.75:
            self.testsignal.emit("��ļ��N����")
        else:
            R = findpic((252, 444, 421, 553), r"hxls_resource\picture\recruit\R.png")[1]
            SR = findpic((252, 444, 421, 553), r"hxls_resource\picture\recruit\SR.png")[1]
            if R >= 0.6 and SR<R:self.testsignal.emit("��ļ��R����")
            else:
                path = screenshot()
                nowtime = time.strftime("%Y-%m-%d %H��%M��%S", time.localtime())
                shutil.copyfile(path, "hxls_resource\screenshot\\" + nowtime + ".png")
                os.remove(path)
                SSR = findpic((252, 444, 421, 553), r"hxls_resource\picture\recruit\SSR.png")[1]
                if SR >= 0.6 or SSR >= 0.6:
                    if SSR < SR:
                        self.testsignal.emit("��ļ��SR��,�����ļ��С�hxls_resource\screenshot���в鿴��")
                    else:
                        self.testsignal.emit("��ļ��SSR���������ļ��С�hxls_resource\screenshot���в鿴��")
                else:
                    self.testsignal.emit("error:���ѷ�ļδ֪����("+nowtime + ".png)")
                    self.accomplish.emit(3)
        click(273, 903)
        wait(1500)
        click(273, 903)
        wait(1500)

    def reward(self):
        self.testsignal.emit("��ʼ��飺���չ�����")
        if not findcolor((181,474,236,528), "red")[0]:
            self.testsignal.emit("������������")
            wait(500)
        else:
            click(159, 490)
            wait(1500)
            if findcolor((753,146,790,189), "red")[0]:
                click(727, 183)
                wait(1000)
                click(1340, 1009)
                wait(2000)
                click(941, 827)
                wait(2000)
                self.testsignal.emit("��ȡ��������ɡ�")
            else:self.testsignal.emit("������������")
            click(296, 75)
            wait(1000)

    def random_gift(self):
        self.testsignal.emit("��ʼ��飺�������")
        click(144,686)
        wait(2000)
        click(720,301)
        wait(800)
        gdirpath = r"hxls_resource\picture\random_gift"
        dirlist =os.listdir(gdirpath)
        uglist =[]
        for g in dirlist:
            gname = self.indexdir[os.path.splitext(g)[0]]
            gpath = gdirpath+"\\"+g
            num = 0
            self.testsignal.emit("����������" + gname)
            while 1:
                (x,y),val = findpic((820,111, 1840,501), gpath)
                if val >= 0.75:
                    num += 1
                    click(x, y)
                    wait(1000)
                    click(956, 867)
                    self.testsignal.emit("��ʹ��%s����"%(num))
                    wait(1000)
                    click(956, 867)
                    wait(800)
                else:
                    self.testsignal.emit("ʹ����ϡ�")
                    break
            if num:
                uglist += ["%s:%s����"%(gname,num)]
            else:self.testsignal.emit("���޸��������")
        if uglist:
            self.testsignal.emit("ʹ�������ͳ�ƣ�")
            for i in uglist:
                self.testsignal.emit(i)
        click(296, 75)
        wait(1000)
    def getmail(self):
        self.testsignal.emit("��ʼ��飺�ʼ���")
        res,(cx,cy) = findcolor((472, 26, 521, 80),"red")
        if res:
            wait(500)
            click(472, 78)
            wait(1500)
            click(577, 809)
            wait(2000)
            click(1006, 885)
            wait(2000)
            click(1791, 122)
            self.testsignal.emit("��ȡ�ʼ���ɡ�")
            wait(2000)
        else:
            self.testsignal.emit("�������ʼ���")
            wait(500)
if __name__ == '__main__':pass






