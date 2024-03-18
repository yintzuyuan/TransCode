import tkinter as tk
from tkinter import scrolledtext
import pyperclip

def chars_to_unicode(chars):
    unicode_values = [ord(char) for char in chars]
    unicode_str = '\n'.join(hex(val)[2:].upper() for val in unicode_values)
    return unicode_str

def unicode_to_chars(unicode_str):
    unicode_values = [int(val, 16) for val in unicode_str.split('\n')]
    chars = ''.join(chr(val) for val in unicode_values)
    return chars

def update_unicode(event):
    hanzi_text = hanzi_entry.get()
    unicode_str = chars_to_unicode(hanzi_text)
    unicode_display.config(state=tk.NORMAL)
    unicode_display.delete(1.0, tk.END)
    unicode_display.insert(tk.END, unicode_str)
    #unicode_display.config(state=tk.DISABLED)
    # 複製Unicode數值到剪貼簿
    pyperclip.copy(unicode_str)

def update_hanzi(event):
    unicode_str = unicode_display.get(1.0, tk.END).strip()
    hanzi_entry.delete(0, tk.END)
    hanzi_entry.insert(0, unicode_to_chars(unicode_str))
    # 複製漢字到剪貼簿
    pyperclip.copy(unicode_to_chars(unicode_str))

# 建立主視窗
root = tk.Tk()
root.title("漢字和Unicode轉換工具")

# 第一個輸入框（漢字）
tk.Label(root, text="漢字：").grid(row=0, column=0)
hanzi_entry = tk.Entry(root)
hanzi_entry.grid(row=0, column=1, columnspan=2, sticky="ew")
hanzi_entry.bind('<Return>', update_unicode)

# 第二個輸入框（Unicode）帶有卷軸
tk.Label(root, text="Unicode：").grid(row=1, column=0)
unicode_display = tk.Text(root, height=5, width=30, wrap=tk.WORD)
unicode_display.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
#unicode_display.config(state=tk.DISABLED)

# 卷軸
scrollbar = tk.Scrollbar(root, command=unicode_display.yview)
scrollbar.grid(row=1, column=2, sticky='nsew')
unicode_display['yscrollcommand'] = scrollbar.set

# 視窗大小改變時輸入框跟著縮放
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# 在第二輸入框輸入Unicode後，更新第一輸入框
unicode_display.bind('<Return>', update_hanzi)

# 啟動主迴圈
root.mainloop()
