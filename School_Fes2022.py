import tkinter as tk


# サブウィンドウの設定

def sub_window():
    global sub_win
    if sub_win is None or not sub_win.winfo_exists():
        sub_win = tk.Toplevel()
        sub_win.geometry("400x250")
        sub_win.title("バージョン")
        label_sub = tk.Label(sub_win, text="バージョン:0.11.829B\nベータ:はい\nLicence:MIT\n 2022_C-Dioxide")
        label_sub.pack()
        sub_win = tk.PhotoImage(file="game_logo.png")
        canvas = tk.Canvas(bg="black", width=240, height=60)
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, anchor=tk.NW)


# licence

def licence_window():
    global licence_win
    if licence_win is None or not licence_win.winfo_exists():
        licence_win = tk.Toplevel()
        licence_win.geometry("400x250")
        licence_win.title("ライセンス")
        label_sub = tk.Label(licence_win, text="バージョン:0.11.829B\nベータ:はい\nLicence:MIT\n 2022_C-Dioxide")
        label_sub.pack()


# メインウィンドウの設定

root = tk.Tk()
root.title("箱入り娘-2022ver")
root.geometry("640x480")

# 定義
sub_win = None
licence_win = None


# プルダウンメニュー
# メニューから呼び出される関数
def close_disp():
    pass


def help_file():
    pass


# menubarの大元（コンテナ）の作成と設置
menubar = tk.Menu(root)
root.config(menu=menubar)

# メニューに親メニュー（ファイル）を作成する
menu_file = tk.Menu(root, tearoff=False)
menubar.add_cascade(label='ファイル', menu=menu_file)

# menubarを親としてヘルプメニューを作成と表示
help_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label='情報', menu=help_menu)

# 親メニューに子メニューを追加する
menu_file.add_command(label='終了', command=close_disp)
help_menu.add_command(label='ヘルプ', command=help_file)
help_menu.add_command(label='バージョン', command=sub_window)
help_menu.add_command(label='ライセンス', command=licence_window)

# 画面の表示
root.mainloop()
