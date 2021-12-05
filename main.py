from tkinter import *
#---- color variables -------
WINDOW_BG_COLOR = "#1eb2a6"
BTN_BG_COLOR = "#00c853"
F_BTN_COLOR="#e8f5e9"
#---- fonts variables -------
HEADER_FONT = ('Traditional Arabic', 22, 'bold')
SUBHEADER_FONT = ('Traditional Arabic', 18, 'bold')
BTN_FONT_FMLY = ('Traditional Arabic', 16, 'bold')
#---- width variable -------
BTN_WIDTH_4C = 12
BTN_WIDTH_3C = 16

root = Tk()
root['background'] = WINDOW_BG_COLOR
root.maxsize(width=800,height=1000)
root.minsize(width=800,height=900)


# **************************
# ********* العنوان *******
# **************************
header = Label(root, text="الفرقة الإقليمية للدرك الوطني بتماسين",font=HEADER_FONT,padx=20,pady=5)
header.pack()


# **************************
# ******* عنوان فرعي ******
# **************************

header = Label(root, text="معلومات عن الفرقة", font=HEADER_FONT, bg=WINDOW_BG_COLOR)
header.place(x=600,y=80)



# **************************
# ********* الأزرار *********
# **************************

users_list_btn=Button(root, text="الأفراد", bg=BTN_BG_COLOR, pady=10, font=BTN_FONT_FMLY, width=BTN_WIDTH_4C, fg=F_BTN_COLOR)
users_list_btn.place(x=630,y=140)


cars_list_btn=Button(root, text="السيارات ع", bg=BTN_BG_COLOR, width=BTN_WIDTH_4C, pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
cars_list_btn.place(x=430,y=140)


weapens_list_btn=Button(root, text="الأسلحة", bg=BTN_BG_COLOR, width=BTN_WIDTH_4C, pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
weapens_list_btn.place(x=230,y=140)


trans_mat_list_btn=Button(root, text="عتاد الإشارة", bg=BTN_BG_COLOR, width=BTN_WIDTH_4C, pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
trans_mat_list_btn.place(x=10,y=140)

# **************************
# ******* عنوان فرعي ******
# **************************

header = Label(root, text="معلومات عن الأفراد", font=HEADER_FONT, bg=WINDOW_BG_COLOR)
header.place(x=600,y=580)

leader_btn=Button(root, text="قائد الفرقة", bg=BTN_BG_COLOR, pady=10, font=BTN_FONT_FMLY, width=BTN_WIDTH_4C, fg=F_BTN_COLOR)
leader_btn.place(x=630,y=630)

deputy_btn=Button(root, text="نائب قائد الفرقة", bg=BTN_BG_COLOR, width=BTN_WIDTH_4C, pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
deputy_btn.place(x=430,y=630)

plice_officer_btn=Button(root, text="ضباط الشرطة القضائية", bg=BTN_BG_COLOR, width=BTN_WIDTH_4C, pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
plice_officer_btn.place(x=230,y=630)

staff_sergeant_btn=Button(root, text="الرقباء الأوائل", bg=BTN_BG_COLOR, pady=10, font=BTN_FONT_FMLY, width=BTN_WIDTH_4C, fg=F_BTN_COLOR)
staff_sergeant_btn.place(x=10,y=630)

sergeant_active_btn=Button(root, text="الرقباء العاملين", bg=BTN_BG_COLOR, width=BTN_WIDTH_4C, pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
sergeant_active_btn.place(x=630,y=710)

sergeant_contract_btn=Button(root, text="الرقباء المتعاقدين", bg=BTN_BG_COLOR, width=BTN_WIDTH_4C, pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
sergeant_contract_btn.place(x=430,y=710)
all_users=Button(root, text=" جميع الأفراد", bg=BTN_BG_COLOR, width=(BTN_WIDTH_4C*2+5), pady=10, font=BTN_FONT_FMLY, fg=F_BTN_COLOR)
all_users.place(x=10,y=710)


root.mainloop()


