import sys
import os
from tkinter import *
from tkinter import messagebox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

current_device = None
device_data = {
    "Электронный замок": {
        "image": "images/zamok2.png",
        "characteristics": "устройство, которое работает под управлением электроники",
        "functions": "поддерживают дистанционное управление, интеграцию с умным домом, журнал посещений и возможность временного доступа.",
        "instruction": "Войти в меню настройки, нажав «*», а затем «#». Ввести заводской пароль администратора (например, «123456») и нажать «#». Установить новый пароль администратора, который станет главным код-паролем (заводской пароль после этого автоматически удалится). Добавить или удалить пользователей. Настроить внутренние настройки. Подключить замок к приложению"
    },
    "Умная лампочка": {
        "image": "images/lampa2.png",
        "characteristics": "это светодиодный источник света с модулем беспроводной связи (Wi-Fi или Bluetooth), который можно подключить к смартфону или системе «умного дома»",
        "functions": "Дистанционное управление, синхронизация с музыкой, создание сценариев освещения",
        "instruction": "Выбрать параметры и режимы в приложении производителя лампочки — установить на мобильный телефон или планшет. Дать команды по освещению голосовому ассистенту — колонке с Алисой от Яндекса, Марусе от ВКонтакте или Салюту от «Сбера». Настроить режим работы лампочки, например, указать, что по будням в 8:30 свет выключается. Создать свои сценарии или использовать встроенные — например, лампа может включаться в определённое время или по датчику движения/освещения."
    },
    "Система отопления": {
        "image": "images/otoplenie2.png",
        "characteristics": "система управления отоплением с учётом заданных пользователем параметров, чаще всего температуры и времени.",
        "functions": "Автоматизация и управление отоплением через центральный контроллер, интеграция с другими системами умного дома, энергоэффективность и снижение затрат на топление",
        "instruction": "Настройка режимов работы. Можно настроить значения целевых температур для заданных режимов или алгоритм работы контроллера в каждом режиме. Настройка управления по расписанию. Например, можно составить таблицу для работы по расписанию: выделить временные участки для управления по целевой температуре или по заданным режимам работы. Настройка оповещений. Например, можно указать номера телефонов для информирования о тревожных событиях. Обслуживание беспроводных датчиков. Контроллеры отслеживают уровень заряда и заблаговременно предупреждают о необходимости замены батарей."
    },
    "Автоматический полив растений": {
        "image": "images/rastenie2.png",
        "characteristics": "система орошения, которая подаёт влагу растениям без участия человека.",
        "functions": "Полив без участия пользователя, экономичное потребление воды, контроль уровня влаги в почве",
        "instruction": "Частота полива. Продолжительность полива. Напор воды. Порядок орошения разных секторов. Длина перерывов между обработками зон"
    }
}

def show_text(text):
    info_label.config(text=text)

def show_image(file_path):
    global current_img
    try:
        full_path = resource_path(file_path)
        current_img = PhotoImage(file=full_path)
        image_label.config(image=current_img)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить изображение\n{str(e)}")

def set_current_device(device_name):
    global current_device
    current_device = device_name
    show_device_image()
    show_device_characteristics()
    update_nav_buttons_state()

def show_device_image():
    if current_device and current_device in device_data:
        show_image(device_data[current_device]["image"])

def show_device_characteristics():
    if current_device and current_device in device_data:
        show_text(device_data[current_device]["characteristics"])

def show_device_functions():
    if current_device and current_device in device_data:
        show_text(device_data[current_device]["functions"])

def show_device_instruction():
    if current_device and current_device in device_data:
        show_text(device_data[current_device]["instruction"])

def update_nav_buttons_state():
    if current_device:
        btn_image.config(state=NORMAL)
        btn_characteristics.config(state=NORMAL)
        btn_functions.config(state=NORMAL)
    else:
        btn_image.config(state=DISABLED)
        btn_characteristics.config(state=DISABLED)
        btn_functions.config(state=DISABLED)

class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self):
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def create_tooltip(widget, text):
    tool_tip = ToolTip(widget, text)
    def enter(event):
        tool_tip.showtip()
    def leave(event):
        tool_tip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

root = Tk()
root.geometry("800x700")
root.title("Умные устройства")

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть")
filemenu.add_command(label="Сохранить")
filemenu.add_command(label="Выход", command=root.quit)

charkimenu = Menu(mainmenu, tearoff=0)
charkimenu.add_command(label="Эл. замок", command=lambda: set_current_device("Электронный замок"))
charkimenu.add_command(label="Умная лампочка", command=lambda: set_current_device("Умная лампочка"))
charkimenu.add_command(label="Система отопления", command=lambda: set_current_device("Система отопления"))
charkimenu.add_command(label="Автоматический полив растений", command=lambda: set_current_device("Автоматический полив растений"))

functionmenu = Menu(mainmenu, tearoff=0)

functionmenu2 = Menu(functionmenu, tearoff=0)
functionmenu2.add_command(label="Изображение", command=lambda: set_current_device("Электронный замок"))
functionmenu2.add_command(label="Характеристики", command=lambda: set_current_device("Электронный замок"))
functionmenu2.add_command(label="Функции", command=lambda: set_current_device("Электронный замок"))
functionmenu.add_cascade(label="Эл. замок", menu=functionmenu2)

functionmenu3 = Menu(functionmenu, tearoff=0)
functionmenu3.add_command(label="Изображение", command=lambda: set_current_device("Умная лампочка"))
functionmenu3.add_command(label="Характеристики", command=lambda: set_current_device("Умная лампочка"))
functionmenu3.add_command(label="Функции", command=lambda: set_current_device("Умная лампочка"))
functionmenu.add_cascade(label="Умная лампочка", menu=functionmenu3)

functionmenu4 = Menu(functionmenu, tearoff=0)
functionmenu4.add_command(label="Изображение", command=lambda: set_current_device("Система отопления"))
functionmenu4.add_command(label="Характеристики", command=lambda: set_current_device("Система отопления"))
functionmenu4.add_command(label="Функции", command=lambda: set_current_device("Система отопления"))
functionmenu.add_cascade(label="Система отопления", menu=functionmenu4)

functionmenu5 = Menu(functionmenu, tearoff=0)
functionmenu5.add_command(label="Изображение", command=lambda: set_current_device("Автоматический полив растений"))
functionmenu5.add_command(label="Характеристики", command=lambda: set_current_device("Автоматический полив растений"))
functionmenu5.add_command(label="Функции", command=lambda: set_current_device("Автоматический полив растений"))
functionmenu.add_cascade(label="Автоматический полив растений", menu=functionmenu5)

helpmenu = Menu(mainmenu, tearoff=0)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Устройства", menu=functionmenu)
mainmenu.add_cascade(label="Инструкция для пользователя", menu=charkimenu)
mainmenu.add_cascade(label="Помощь", menu=helpmenu)
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
left_frame = Frame(main_frame)
left_frame.pack(side=LEFT, fill=BOTH, expand=True)
image_label = Label(left_frame, bg="white")
image_label.pack(side=TOP, fill=BOTH, expand=True, pady=(0, 10))
nav_frame = Frame(left_frame)
nav_frame.pack(side=BOTTOM, fill=X, pady=10)

btn_image = Button(nav_frame, text="Изображение", width=15, command=show_device_image, state=DISABLED)
btn_image.pack(side=LEFT, padx=5)

btn_characteristics = Button(nav_frame, text="Характеристики", width=15, command=show_device_characteristics, state=DISABLED)
btn_characteristics.pack(side=LEFT, padx=5)

btn_functions = Button(nav_frame, text="Функции", width=15, command=show_device_functions, state=DISABLED)
btn_functions.pack(side=LEFT, padx=5)

btn_instruction = Button(nav_frame, text="Инструкция", width=15, command=show_device_instruction, state=DISABLED)
btn_instruction.pack(side=LEFT, padx=5)
info_label = Label(left_frame, wraplength=400, justify='left', anchor=NW,
                   bg="white", relief=SUNKEN, borderwidth=2, height=8)
info_label.pack(side=BOTTOM, fill=BOTH, expand=True, pady=(10, 0))
right_frame = Frame(main_frame)
right_frame.pack(side=RIGHT, fill=Y, padx=(10, 0))

right_label = Label(right_frame, text="Выбор устройства", font=("Arial", 10, "bold"))
right_label.pack(pady=(0, 10))

icons_and_actions = [
    ("images/zamok.png", "Электронный замок", lambda: set_current_device("Электронный замок")),
    ("images/lampa.png", "Умная лампочка", lambda: set_current_device("Умная лампочка")),
    ("images/otoplenie.png", "Система отопления", lambda: set_current_device("Система отопления")),
    ("images/rastenie.png", "Автоматический полив", lambda: set_current_device("Автоматический полив растений"))
]

for icon_file, tooltip_text, action in icons_and_actions:
    try:
        button_icon = PhotoImage(file=resource_path(icon_file))
        button = Button(right_frame, image=button_icon, command=action, relief=RAISED, bd=2)
        button.image = button_icon
        button.pack(pady=10)
        create_tooltip(button, tooltip_text)
    except Exception as e:
        print(f"Не удалось загрузить иконку {icon_file}: {e}")
        button = Button(right_frame, text=tooltip_text, command=action, width=15, height=2)
        button.pack(pady=10)
root.mainloop()