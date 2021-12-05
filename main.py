from tkinter import *
BG_COLOR = "#1eb2a6"
BTN_COLOR = "#f5f5f5"
root = Tk()
root['background'] = BG_COLOR
root.minsize(800,600)
HEADER_FONT = ('Arial', 22, 'bold')
SUBHEADER_FONT = ('Arial', 18, 'bold')
BTN_FONT = ('Arial', 12, 'bold')
# **************************
# ********* العنوان *******
# **************************
header = Label(root, text="الفرقة الإقليمية للدرك الوطني بتماسين",font=HEADER_FONT)
header.pack()


# **************************
# ******* عنوان فرعي ******
# **************************

header = Label(root, text="معلومات عن الفرقة",font=HEADER_FONT,bg=BG_COLOR)
header.place(x=600,y=80)



# **************************
# ********* الأزرار *********
# **************************

users_list_btn=Button(root,text="الأفراد",bg=BTN_COLOR,pady=10,font=BTN_FONT,width=15)
users_list_btn.place(x=630,y=140)


users_list_btn=Button(root,text="السيارات",bg=BTN_COLOR,width=15, pady=10,font=BTN_FONT)
users_list_btn.place(x=430,y=140)


users_list_btn=Button(root,text="الأسلحة",bg=BTN_COLOR,width=15, pady=10,font=BTN_FONT)
users_list_btn.place(x=230,y=140)


users_list_btn=Button(root,text="عتاد الإشارة",bg=BTN_COLOR,width=15, pady=10,font=BTN_FONT)
users_list_btn.place(x=10,y=140)

# **************************
# ******* عنوان فرعي ******
# **************************

header = Label(root, text="معلومات عن البلدية",font=HEADER_FONT,bg=BG_COLOR)
header.place(x=600,y=280)

users_list_btn=Button(root,text="السلطات المدنية",bg=BTN_COLOR,pady=10,font=BTN_FONT,width=15)
users_list_btn.place(x=630,y=340)

users_list_btn=Button(root,text="الأئمة",bg=BTN_COLOR,width=15, pady=10,font=BTN_FONT)
users_list_btn.place(x=430,y=340)

users_list_btn=Button(root,text="الشركات",bg=BTN_COLOR,width=15, pady=10,font=BTN_FONT)
users_list_btn.place(x=230,y=340)

users_list_btn=Button(root,text="المساجد",bg=BTN_COLOR,width=15, pady=10,font=BTN_FONT)
users_list_btn.place(x=10,y=340)

root.mainloop()