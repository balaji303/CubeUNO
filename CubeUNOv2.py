#CubeUNO
import wx
import locale
import os

from wx.core import DefaultSize
appgui = 0
global high, low, isinofile
high = 'HIGH'
low = 'LOW'
class AppGUI(wx.Frame):
  
    def __init__(self, *args, **kwargs):
        super(AppGUI, self).__init__(*args, **kwargs)
        self.InitUI()
  
    def InitUI(self):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  
        # create parent panel for button
        self.pnl = wx.Panel(self)
        global pyfiledir
        pyfiledir = os.path.dirname(__file__)
        imagepath = os.path.join(pyfiledir,"images\BG.png")
        iconpath = os.path.join(pyfiledir,"images\icon.png")
        self.SetIcon(wx.Icon(iconpath))
        image_file = imagepath
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # image's upper left corner anchors at panel coordinates (0, 0)
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (140, 65))

        # create button at point (20, 20)
        self.gen_button = wx.Button(self, id = 1, label ="Generate Code", pos =(300, 620),
                                          size = wx.DefaultSize, name ="button")

        self.gen_button.Bind (wx.EVT_BUTTON, self.gen_cmd)

        common = ["HIGH","LOW"]
        self.textpin1 = wx.StaticText(self, -1, label = 'Pin Number', pos = (609,285), size = DefaultSize)
        self.pinValue13 = wx.ComboBox(self, -1,pos=(550,300),choices = common,style = wx.CB_READONLY)
        self.text13 = wx.StaticText(self, -1, label = '->13', pos = (609,305), size = DefaultSize)
        self.pinValue12 = wx.ComboBox(self, -1,pos=(550,320),choices = common,style = wx.CB_READONLY)
        self.text12 = wx.StaticText(self, -1, label = '->12', pos = (609,325), size = DefaultSize)
        self.pinValue11 = wx.ComboBox(self, -1,pos=(550,340),choices = common,style = wx.CB_READONLY)
        self.text11 = wx.StaticText(self, -1, label = '->11', pos = (609,345), size = DefaultSize)
        self.pinValue10 = wx.ComboBox(self, -1,pos=(550,360),choices = common,style = wx.CB_READONLY)
        self.text10 = wx.StaticText(self, -1, label = '->10', pos = (609,365), size = DefaultSize)
        self.pinValue09 = wx.ComboBox(self, -1,pos=(550,380),choices = common,style = wx.CB_READONLY)
        self.text09 = wx.StaticText(self, -1, label = '->09', pos = (609,385), size = DefaultSize)
        self.pinValue08 = wx.ComboBox(self, -1,pos=(550,400),choices = common,style = wx.CB_READONLY)
        self.text08 = wx.StaticText(self, -1, label = '->08', pos = (609,405), size = DefaultSize)
        self.pinValue07 = wx.ComboBox(self, -1,pos=(550,425),choices = common,style = wx.CB_READONLY)
        self.text07 = wx.StaticText(self, -1, label = '->07', pos = (609,430), size = DefaultSize)
        self.pinValue06 = wx.ComboBox(self, -1,pos=(550,445),choices = common,style = wx.CB_READONLY)
        self.text06 = wx.StaticText(self, -1, label = '->06', pos = (609,450), size = DefaultSize)
        self.pinValue05 = wx.ComboBox(self, -1,pos=(550,465),choices = common,style = wx.CB_READONLY)
        self.text05 = wx.StaticText(self, -1, label = '->05', pos = (609,470), size = DefaultSize)
        self.pinValue04 = wx.ComboBox(self, -1,pos=(550,485),choices = common,style = wx.CB_READONLY)
        self.text04 = wx.StaticText(self, -1, label = '->04', pos = (609,490), size = DefaultSize)
        self.pinValue03 = wx.ComboBox(self, -1,pos=(550,505),choices = common,style = wx.CB_READONLY)
        self.text03 = wx.StaticText(self, -1, label = '->03', pos = (609,510), size = DefaultSize)
        self.pinValue02 = wx.ComboBox(self, -1,pos=(550,525),choices = common,style = wx.CB_READONLY)
        self.text02 = wx.StaticText(self, -1, label = '->02', pos = (609,530), size = DefaultSize)
        self.pinValue01 = wx.ComboBox(self, -1,pos=(550,545),choices = common,style = wx.CB_READONLY)
        self.text01 = wx.StaticText(self, -1, label = '->01', pos = (609,550), size = DefaultSize)
        self.pinValue00 = wx.ComboBox(self, -1,pos=(550,565),choices = common,style = wx.CB_READONLY)
        self.text00 = wx.StaticText(self, -1, label = '->00', pos = (609,570), size = DefaultSize)
        #Analog PIN
        self.textpin2 = wx.StaticText(self, -1, label = 'Pin Number', pos = (80,445), size = DefaultSize)
        self.pinValuea0 = wx.TextCtrl ( self,
                                value = "000",
                                pos = ( 110,465 ),
                                size = ( 30,20 ))
        self.texta0 = wx.StaticText(self, -1, label = 'A0<-', pos = (80,465), size = DefaultSize)
        self.pinValuea1 = wx.TextCtrl ( self,
                                value = "000",
                                pos = ( 110,485 ),
                                size = ( 30,20 ))
        self.texta1 = wx.StaticText(self, -1, label = 'A1<-', pos = (80,485), size = DefaultSize)
        self.pinValuea2 = wx.TextCtrl ( self,
                                value = "000",
                                pos = ( 110,505 ),
                                size = ( 30,20 ))
        self.texta2 = wx.StaticText(self, -1, label = 'A2<-', pos = (80,505), size = DefaultSize)
        self.pinValuea3 = wx.TextCtrl ( self,
                                value = "000",
                                pos = ( 110,525 ),
                                size = ( 30,20 ))
        self.texta3 = wx.StaticText(self, -1, label = 'A3<-', pos = (80,525), size = DefaultSize)
        self.pinValuea4 = wx.TextCtrl ( self,
                                value = "000",
                                pos = ( 110,545 ),
                                size = ( 30,20 ))
        self.texta4 = wx.StaticText(self, -1, label = 'A4<-', pos = (80,545), size = DefaultSize)
        self.pinValuea5 = wx.TextCtrl ( self,
                                value = "000",
                                pos = ( 110,565 ),
                                size = ( 30,20 ))
        self.texta5 = wx.StaticText(self, -1, label = 'A5<-', pos = (80,565), size = DefaultSize)
        #Credit
        self.credit = wx.StaticText(self, -1, label = 'Credit: bit.ly/balajiv', pos = (0,640), size = DefaultSize)
        #self.pinValue13.Bind(wx.EVT_COMBOBOX, self.onpinValue)
        #Button for future use#
        #self.button1 = wx.Button(self.bitmap1, id=-1, label='Button1', pos=(8, 8))
        # change size of button
        #self.st.SetSize((100, 50))
        self.SetSize((700, 700))
        self.SetTitle('CubeUNO v2')
        self.SetForegroundColour( 
                            wx.SystemSettings.GetColour(
                            wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( 
                            wx.Colour( 0, 179, 186 ) )
        self.Centre()

    def gen_cmd(self,e):
        logic.mainfun(None)
        appgui.success()
        return

    def success(self): 
      wx.MessageBox("Code Generated Successfully!\nCheck Output Folder", "Message" ,wx.OK | wx.ICON_INFORMATION)


class logic:
    def mainfun(self):
        os.chdir(pyfiledir)
        codedirpath = os.path.join(pyfiledir,"output")
        isoutputFile = os.path.isdir(codedirpath)
        if isoutputFile:
            pass
        else:
            os.mkdir("output")
        os.chdir(codedirpath)
        #logic.pinvalueprint(None)
        finalcode = "void setup() {\n//The code in this function runs only once\nSerial.begin(9600);\n"+ logic.void_setup(None) +"}\nvoid loop() {\n//The code in this sectiono runs forever\n" + logic.void_loop(None) +"}"
        with open("output.ino","w") as outputfile:
            outputfile.write(finalcode)
        outputfile.close()
        return

    def pin_init(self):
        global pin13, pin12, pin11, pin10, pin09, pin08, pin07, pin06, pin05, pin04, pin03, pin02, pin01, pin00, pina0, pina1, pina2, pina3, pina4, pina5
        pin13 = appgui.pinValue13.GetStringSelection()
        pin12 = appgui.pinValue12.GetStringSelection()
        pin11 = appgui.pinValue11.GetStringSelection()
        pin10 = appgui.pinValue10.GetStringSelection()
        pin09 = appgui.pinValue09.GetStringSelection()
        pin08 = appgui.pinValue08.GetStringSelection()
        pin07 = appgui.pinValue07.GetStringSelection()
        pin06 = appgui.pinValue06.GetStringSelection()
        pin05 = appgui.pinValue05.GetStringSelection()
        pin04 = appgui.pinValue04.GetStringSelection()
        pin03 = appgui.pinValue03.GetStringSelection()
        pin02 = appgui.pinValue02.GetStringSelection()
        pin01 = appgui.pinValue01.GetStringSelection()
        pin00 = appgui.pinValue00.GetStringSelection()
        pina0 = appgui.pinValuea0.GetValue()
        pina1 = appgui.pinValuea1.GetValue()
        pina2 = appgui.pinValuea2.GetValue()
        pina3 = appgui.pinValuea3.GetValue()
        pina4 = appgui.pinValuea4.GetValue()
        pina5 = appgui.pinValuea5.GetValue()
        return

    def void_setup(self):
        logic.pin_init(None)
        setupstr = pinsetup.pin_setup00(None) + pinsetup.pin_setup01(None) + pinsetup.pin_setup02(None) + pinsetup.pin_setup03(None) + pinsetup.pin_setup04(None) + pinsetup.pin_setup05(None) + pinsetup.pin_setup06(None) + pinsetup.pin_setup07(None) + pinsetup.pin_setup08(None) + pinsetup.pin_setup09(None) + pinsetup.pin_setup10(None) + pinsetup.pin_setup11(None) + pinsetup.pin_setup12(None) + pinsetup.pin_setup13(None) + pinsetup.pin_setupa0(None) + pinsetup.pin_setupa1(None) + pinsetup.pin_setupa2(None) + pinsetup.pin_setupa3(None) + pinsetup.pin_setupa4(None) + pinsetup.pin_setupa5(None)
        return setupstr

    def void_loop(self):
        loopstr = pinloop.pin_loop00(None) + pinloop.pin_loop01(None) + pinloop.pin_loop02(None) + pinloop.pin_loop03(None) + pinloop.pin_loop04(None) + pinloop.pin_loop05(None) + pinloop.pin_loop06(None) + pinloop.pin_loop07(None) + pinloop.pin_loop08(None) + pinloop.pin_loop09(None) + pinloop.pin_loop10(None) + pinloop.pin_loop11(None) + pinloop.pin_loop12(None) + pinloop.pin_loop13(None) + pinloop.pin_loopa0(None) + pinloop.pin_loopa1(None) + pinloop.pin_loopa2(None) + pinloop.pin_loopa3(None) + pinloop.pin_loopa4(None) + pinloop.pin_loopa5(None)
        return loopstr

class pinsetup:
    def pin_setup13(self):
        if pin13 == high or pin13 == low:
            pin13setup = "pinMode(13,OUTPUT);\n"
        else:
            pin13setup = ""
        return pin13setup

    def pin_setup12(self):
        if pin12 == high or pin12 == low:
            pin12setup = "pinMode(12,OUTPUT);\n"
        else:
            pin12setup = ""
        return pin12setup

    def pin_setup11(self):
        if pin11 == high or pin11 == low:
            pin11setup = "pinMode(11,OUTPUT);\n"
        else:
            pin11setup = ""
        return pin11setup

    def pin_setup10(self):
        if pin10 == high or pin10 == low:
            pin10setup = "pinMode(10,OUTPUT);\n"
        else:
            pin10setup = ""
        return pin10setup

    def pin_setup09(self):
        if pin09 == high or pin09 == low:
            pin09setup = "pinMode(9,OUTPUT);\n"
        else:
            pin09setup = ""
        return pin09setup

    def pin_setup08(self):
        if pin08 == high or pin08 == low:
            pin08setup = "pinMode(8,OUTPUT);\n"
        else:
            pin08setup = ""
        return pin08setup

    def pin_setup07(self):
        if pin07 == high or pin07 == low:
            pin07setup = "pinMode(7,OUTPUT);\n"
        else:
            pin07setup = ""
        return pin07setup

    def pin_setup06(self):
        if pin06 == high or pin06 == low:
            pin06setup = "pinMode(6,OUTPUT);\n"
        else:
            pin06setup = ""
        return pin06setup

    def pin_setup05(self):
        if pin05 == high or pin05 == low:
            pin05setup = "pinMode(5,OUTPUT);\n"
        else:
            pin05setup = ""
        return pin05setup

    def pin_setup04(self):
        if pin04 == high or pin04 == low:
            pin04setup = "pinMode(4,OUTPUT);\n"
        else:
            pin04setup = ""
        return pin04setup

    def pin_setup03(self):
        if pin03 == high or pin03 == low:
            pin03setup = "pinMode(3,OUTPUT);\n"
        else:
            pin03setup = ""
        return pin03setup

    def pin_setup02(self):
        if pin02 == high or pin02 == low:
            pin02setup = "pinMode(2,OUTPUT);\n"
        else:
            pin02setup = ""
        return pin02setup

    def pin_setup01(self):
        if pin01 == high or pin01 == low:
            pin01setup = "pinMode(1,OUTPUT);\n"
        else:
            pin01setup = ""
        return pin01setup

    def pin_setup00(self):
        if pin00 == high or pin00 == low:
            pin00setup = "pinMode(0,OUTPUT);\n"
        else:
            pin00setup = ""
        return pin00setup

    def pin_setupa0(self):
        if int(pina0) > 0 and int(pina0) < 256:
            pina0setup = "pinMode(A0,OUTPUT);\n"
        else:
            pina0setup = ""
        return pina0setup

    def pin_setupa1(self):
        if int(pina1) > 0 and int(pina1) < 256:
            pina1setup = "pinMode(A1,OUTPUT);\n"
        else:
            pina1setup = ""
        return pina1setup

    def pin_setupa2(self):
        if int(pina2) > 0 and int(pina2) < 256:
            pina2setup = "pinMode(A2,OUTPUT);\n"
        else:
            pina2setup = ""
        return pina2setup

    def pin_setupa3(self):
        if int(pina3) > 0 and int(pina3) < 256:
            pina3setup = "pinMode(A3,OUTPUT);\n"
        else:
            pina3setup = ""
        return pina3setup

    def pin_setupa4(self):
        if int(pina4) > 0 and int(pina4) < 256:
            pina4setup = "pinMode(A4,OUTPUT);\n"
        else:
            pina4setup = ""
        return pina4setup

    def pin_setupa5(self):
        if int(pina5) > 0 and int(pina5) < 256:
            pina5setup = "pinMode(A5,OUTPUT);\n"
        else:
            pina5setup = ""
        return pina5setup


class pinloop:
    
    def pin_loop13(self):
        if pin13 == high or pin13 == low:
            if pin13 == high:
                pin13loop = "digitalWrite(13,HIGH);\ndelay(1000);\n"
            elif pin13 == low:
                pin13loop = "digitalWrite(13,LOW);\ndelay(1000);\n"
            else:
                pin13loop = ''
        else:
                pin13loop = ''
        return pin13loop

    def pin_loop12(self):
        if pin12 == high or pin12 == low:
            if pin12 == high:
                pin12loop = "digitalWrite(12,HIGH);\ndelay(1000);\n"
            elif pin12 == low:
                pin12loop = "digitalWrite(12,LOW);\ndelay(1000);\n"
            else:
                pin12loop = ''
        else:
                pin12loop = ''
        return pin12loop

    def pin_loop11(self):
        if pin11 == high or pin11 == low:
            if pin11 == high:
                pin11loop = "digitalWrite(11,HIGH);\ndelay(1000);\n"
            elif pin11 == low:
                pin11loop = "digitalWrite(11,LOW);\ndelay(1000);\n"
            else:
                pin11loop = ''
        else:
                pin11loop = ''
        return pin11loop

    def pin_loop10(self):
        if pin10 == high or pin10 == low:
            if pin10 == high:
                pin10loop = "digitalWrite(10,HIGH);\ndelay(1000);\n"
            elif pin10 == low:
                pin10loop = "digitalWrite(10,LOW);\ndelay(1000);\n"
            else:
                pin10loop = ''
        else:
                pin10loop = ''
        return pin10loop

    def pin_loop09(self):
        if pin09 == high or pin09 == low:
            if pin09 == high:
                pin09loop = "digitalWrite(9,HIGH);\ndelay(1000);\n"
            elif pin09 == low:
                pin09loop = "digitalWrite(9,LOW);\ndelay(1000);\n"
            else:
                pin09loop = ''
        else:
                pin09loop = ''
        return pin09loop

    def pin_loop08(self):
        if pin08 == high or pin08 == low:
            if pin08 == high:
                pin08loop = "digitalWrite(8,HIGH);\ndelay(1000);\n"
            elif pin08 == low:
                pin08loop = "digitalWrite(8,LOW);\ndelay(1000);\n"
            else:
                pin08loop = ''
        else:
                pin08loop = ''
        return pin08loop


    def pin_loop07(self):
        if pin07 == high or pin07 == low:
            if pin07 == high:
                pin07loop = "digitalWrite(7,HIGH);\ndelay(1000);\n"
            elif pin07 == low:
                pin07loop = "digitalWrite(7,LOW);\ndelay(1000);\n"
            else:
                pin07loop = ''
        else:
                pin07loop = ''
        return pin07loop


    def pin_loop06(self):
        if pin06 == high or pin06 == low:
            if pin06 == high:
                pin06loop = "digitalWrite(6,HIGH);\ndelay(1000);\n"
            elif pin06 == low:
                pin06loop = "digitalWrite(6,LOW);\ndelay(1000);\n"
            else:
                pin06loop = ''
        else:
                pin06loop = ''
        return pin06loop


    def pin_loop05(self):
        if pin05 == high or pin05 == low:
            if pin05 == high:
                pin05loop = "digitalWrite(5,HIGH);\ndelay(1000);\n"
            elif pin05 == low:
                pin05loop = "digitalWrite(5,LOW);\ndelay(1000);\n"
            else:
                pin05loop = ''
        else:
                pin05loop = ''
        return pin05loop


    def pin_loop04(self):
        if pin04 == high or pin04 == low:
            if pin04 == high:
                pin04loop = "digitalWrite(4,HIGH);\ndelay(1000);\n"
            elif pin04 == low:
                pin04loop = "digitalWrite(4,LOW);\ndelay(1000);\n"
            else:
                pin04loop = ''
        else:
                pin04loop = ''
        return pin04loop


    def pin_loop03(self):
        if pin03 == high or pin03 == low:
            if pin03 == high:
                pin03loop = "digitalWrite(3,HIGH);\ndelay(1000);\n"
            elif pin03 == low:
                pin03loop = "digitalWrite(3,LOW);\ndelay(1000);\n"
            else:
                pin03loop = ''
        else:
                pin03loop = ''
        return pin03loop


    def pin_loop02(self):
        if pin02 == high or pin02 == low:
            if pin02 == high:
                pin02loop = "digitalWrite(2,HIGH);\ndelay(1000);\n"
            elif pin02 == low:
                pin02loop = "digitalWrite(2,LOW);\ndelay(1000);\n"
            else:
                pin02loop = ''
        else:
                pin02loop = ''
        return pin02loop


    def pin_loop01(self):
        if pin01 == high or pin01 == low:
            if pin01 == high:
                pin01loop = "digitalWrite(1,HIGH);\ndelay(1000);\n"
            elif pin01 == low:
                pin01loop = "digitalWrite(1,LOW);\ndelay(1000);\n"
            else:
                pin01loop = ''
        else:
                pin01loop = ''
        return pin01loop

    def pin_loop00(self):
        if pin00 == high or pin00 == low:
            if pin00 == high:
                pin00loop = "digitalWrite(0,HIGH);\ndelay(1000);\n"
            elif pin00 == low:
                pin00loop = "digitalWrite(0,LOW);\ndelay(1000);\n"
            else:
                pin00loop = ''
        else:
                pin00loop = ''
        return pin00loop

    def pin_loopa0(self):
        if int(pina0) > 0 and int(pina0) < 256:
            pina0loop = "analogWrite(A0,"+ pina0 +");\ndelay(1000);\n"
        else:
            pina0loop = ''
        return pina0loop

    def pin_loopa1(self):
        if int(pina1) > 0 and int(pina1) < 256:
            pina1loop = "analogWrite(A1,"+ pina1 +");\ndelay(1000);\n"
        else:
            pina1loop = ''
        return pina1loop

    def pin_loopa2(self):
        if int(pina2) > 0 and int(pina2) < 256:
            pina2loop = "analogWrite(A2,"+ pina2 +");\ndelay(1000);\n"
        else:
            pina2loop = ''
        return pina2loop

    def pin_loopa3(self):
        if int(pina3) > 0 and int(pina3) < 256:
            pina3loop = "analogWrite(A3,"+ pina3 +");\ndelay(1000);\n"
        else:
            pina3loop = ''
        return pina3loop

    def pin_loopa4(self):
        if int(pina4) > 0 and int(pina4) < 256:
            pina4loop = "analogWrite(A4,"+ pina4 +");\ndelay(1000);\n"
        else:
            pina4loop = ''
        return pina4loop

    def pin_loopa5(self):
        if int(pina5) > 0 and int(pina5) < 256:
            pina5loop = "analogWrite(A5,"+ pina5 +");\ndelay(1000);\n"
        else:
            pina5loop = ''
        return pina5loop
  

if __name__ == '__main__':
    app = wx.App()
    appgui = AppGUI(None)
    appgui.Show()
    app.MainLoop()

#value = appgui.pinValue13.GetStringSelection()