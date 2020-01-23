from win10toast import ToastNotifier 

def Error(Message):
    try:
        ToastNotifier().show_toast("SB_ERROR", Message, duration = 10)
    except:
        pass

def Notify(Message):
    try:
        ToastNotifier().show_toast("SB_NOTIFICATION", Message, duration = 10)
    except:
        pass