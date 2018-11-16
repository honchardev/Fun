import win32api, win32con, win32gui


class MainWindow:
    def __init__(self):
       win32gui.InitCommonControls()
       self.hinst = win32api.GetModuleHandle(None)

    def CreateWindow(self):
       className = self.RegisterClass()
       self.BuildWindow(className)

    def RegisterClass(self):
       className = "TeSt"
       message_map = {
          win32con.WM_DESTROY: self.OnDestroy,
       }
       wc = win32gui.WNDCLASS()
       wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
       wc.lpfnWndProc = message_map
       wc.cbWndExtra = 0
       wc.hCursor = win32gui.LoadCursor( 0, win32con.IDC_ARROW )
       wc.hbrBackground = win32con.COLOR_WINDOW + 1
       wc.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
       wc.lpszClassName = className
       classAtom = win32gui.RegisterClass(wc)
       return className

    def BuildWindow(self, className):
       style = win32con.WS_OVERLAPPEDWINDOW
       xstyle = win32con.WS_EX_LEFT
       self.hwnd = win32gui.CreateWindow(className,
                             "ThisIsJustATest",
                             style,
                             win32con.CW_USEDEFAULT,
                             win32con.CW_USEDEFAULT,
                             500,
                             400,
                             0,
                             0,
                             self.hinst,
                             None)
       win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)

    def OnDestroy(self, hwnd, message, wparam, lparam):
       win32gui.PostQuitMessage(0)
       return True

w = MainWindow()
w.CreateWindow()
win32gui.PumpMessages()
