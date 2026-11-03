import tkinter as tk

root = tk.Tk()
root.title("生日快乐✨")
root.geometry("520x260")
# 背景色
root.configure(bg="#FFF0F5")

msg = tk.Label(
    root,
    text="🎂 生日快乐！\n愿平安喜乐，万事顺意\n岁岁无忧，年年有我❤️",
    font=("微软雅黑", 20),
    bg="#FFF0F5",
    fg="#c84275"
)
msg.pack(expand=True)

root.mainloop()