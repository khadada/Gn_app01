from tkinter import *
#---- color variables -------
BG_COLOR = "#1eb2a6"
BTN_COLOR = "#00c853"
F_BTN_COLOR="#e8f5e9"
#---- fonts variables -------
HEADER_FONT = ('Traditional Arabic', 22, 'bold')
SUBHEADER_FONT = ('Traditional Arabic', 18, 'bold')
BTN_FONT_FMLY = ('Traditional Arabic', 16, 'bold')
#---- width variable -------
BTN_WIDTH = 12
root = Tk()
root['background'] = BG_COLOR
root.maxsize(width=800,height=900)
root.minsize(width=800,height=900)


# **************************
# ********* العنوان *******
# **************************
header = Label(root, text="الفرقة الإقليمية للدرك الوطني بتماسين",font=HEADER_FONT,padx=20,pady=5)
header.pack()


# **************************
# ******* عنوان فرعي ******
# **************************

header = Label(root, text="معلومات عن الفرقة",font=HEADER_FONT,bg=BG_COLOR)
header.place(x=600,y=80)



# **************************
# ********* الأزرار *********
# **************************

users_list_btn=Button(root,text="الأفراد",bg=BTN_COLOR,pady=10,font=BTN_FONT_FMLY,width=BTN_WIDTH,fg=F_BTN_COLOR)
users_list_btn.place(x=630,y=140)


users_list_btn=Button(root,text="السيارات",bg=BTN_COLOR,width=BTN_WIDTH, pady=10,font=BTN_FONT_FMLY,fg=F_BTN_COLOR)
users_list_btn.place(x=430,y=140)


users_list_btn=Button(root,text="الأسلحة",bg=BTN_COLOR,width=BTN_WIDTH, pady=10,font=BTN_FONT_FMLY,fg=F_BTN_COLOR)
users_list_btn.place(x=230,y=140)


users_list_btn=Button(root,text="عتاد الإشارة",bg=BTN_COLOR,width=BTN_WIDTH, pady=10,font=BTN_FONT_FMLY,fg=F_BTN_COLOR)
users_list_btn.place(x=10,y=140)

# **************************
# ******* عنوان فرعي ******
# **************************

header = Label(root, text="معلومات عن البلدية",font=HEADER_FONT,bg=BG_COLOR)
header.place(x=600,y=280)

users_list_btn=Button(root,text="السلطات المدنية",bg=BTN_COLOR,pady=10,font=BTN_FONT_FMLY,width=BTN_WIDTH,fg=F_BTN_COLOR)
users_list_btn.place(x=630,y=340)

users_list_btn=Button(root,text="الأئمة",bg=BTN_COLOR,width=BTN_WIDTH, pady=10,font=BTN_FONT_FMLY,fg=F_BTN_COLOR)
users_list_btn.place(x=430,y=340)

users_list_btn=Button(root,text="الشركات",bg=BTN_COLOR,width=BTN_WIDTH, pady=10,font=BTN_FONT_FMLY,fg=F_BTN_COLOR)
users_list_btn.place(x=230,y=340)

users_list_btn=Button(root,text="المساجد",bg=BTN_COLOR,width=BTN_WIDTH, pady=10,font=BTN_FONT_FMLY,fg=F_BTN_COLOR)
users_list_btn.place(x=10,y=340)

root.mainloop()