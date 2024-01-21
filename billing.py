from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
import random,os
from tkinter import messagebox
import tempfile
from time import strftime



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("RJN STORE")

        lbl_title=Label(self.root, text="RJN STORE" , font = ("times new romen",35,"bold"),bg="white",fg="red")
        lbl_title.place(x = 0,y=120,width=1920,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1923,height=840)


        # ======================Variables======================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.seacrh_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        


        # product category list 
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Nike","Addidas","Puma","Levis"]
        self.price_pant_Nike=7000
        self.price_pant_Addidas=4000
        self.price_pant_Puma=4500
        self.price_pant_Levis=2500

        self.Tshirt=["Nike","Addidas","Puma","Levis"]
        self.price_Tshirt_Nike=4000
        self.price_Tshirt_Addidas=3500
        self.price_Tshirt_Puma=2500
        self.price_Tshirt_Levis=2000

        self.Shirt=["Nike","Addidas","Puma","Levis"]
        self.price_Shirt_Nike=3600
        self.price_Shirt_Addidas=3000
        self.price_Shirt_Puma=2500
        self.price_Shirt_Levis=1500

        #subcategory
        self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
        self.BathSoap=["Life Boy","Lux","Santoor","Pearl"]
        self.price_LifeBoy=150
        self.price_Lux=70
        self.price_Santoor=60
        self.price_Pearl=200

        self.FaceCream=["CeraVe","Caudalie","NIVEA","Aqua"]
        self.price_CeraVe=1500
        self.price_Caudalie=1000
        self.price_NIVEA=700
        self.price_Aqua=1300

        self.HairOil=["Luxury","Essential","Mane","Velvet"]
        self.price_Luxury=2000
        self.price_Essential=1500
        self.price_Mane=3500
        self.price_Velvet=900
        
        #subcategory
        self.SubCatMobiles=["Iphone","Samsung","Xiaomi","RealMe","One+"]

        self.Iphone=["Iphone 11","Iphone 12","Iphone 13","Iphone 14","Iphone 15"]
        self.price_i11=112999
        self.price_i12=155000
        self.price_i13=185999
        self.price_i14=225999
        self.price_i15=255000

        self.Samsung=["A20","M30s","M50","A50"]
        self.price_A20=20000
        self.price_M30s=27999
        self.price_M50=36999
        self.price_A50=42999

        self.Xiaomi=["Xiaomi 12","Xiaomi 12 pro","Xiaomi 13","Xiaomi 14"]
        self.price_x12=76000
        self.price_x12pro=83000
        self.price_x13=96999
        self.price_x14=104999

        self.Realme=["C35","C55","C65","C55s"]
        self.price_C35=21999
        self.price_C55=36999
        self.price_C65=44000
        self.price_C55s=41999

        self.Oneplus=["One Plus 8","One Plus 10 pro","One Plus 11","One Plus 12"]
        self.price_8=110000
        self.price_10pro=140000
        self.price_11=155000
        self.price_12=170000





        #image
        img = Image.open("C:/allcode/billing project/img/banner2.jpg")
        img = img.resize((1920, 120)) 
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root, image=self.photoimg) 
        lbl_img.place(x=0, y=0, width=1920, height=120)

        
        def time():
            string=strftime("%H:%M:%S %p") 
            lbl.config(text = string)
            lbl.after(1000, time)

            lbl= Label(lbl_title, font = ('times new roman', 16, 'bold'), background = 'white',foreground='blue')
            lbl.place(x=0,y=0, width=120,height=45)
            time()


        # customer Label Frame
        cust_Frame=LabelFrame(Main_Frame,text="customer",font = ("times new romen",12,"bold"),bg="white",fg="red")
        cust_Frame.place(x=10,y=5,width=380,height=140)

        #mobile no
        self.lbl_mob=Label(cust_Frame,text="Mobile No.",font = ("times new romen",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_Frame, textvariable=self.c_phone, font = ("times new romen",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        #customer name
        self.lblCustName=Label(cust_Frame,text="Customer Name",font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(cust_Frame,textvariable=self.c_name, font = ("arial",12,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        #Email
        self.lblEmail=Label(cust_Frame,text="Email", font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(cust_Frame,textvariable=self.c_email, font = ("arial",12,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        # Product Label Frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font = ("times new romen",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=400,y=5,width=650,height=140)

        #category
        self.lblcategory=Label(Product_Frame,text="Select Categories",font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font = ("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #subcategory
        self.lblSubcategory=Label(Product_Frame,text="Select SubCategories",font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblSubcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font = ("arial",10,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #product
        self.lblproduct=Label(Product_Frame,text="Product Name",font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.Comboproduct=ttk.Combobox(Product_Frame, textvariable=self.product, font = ("arial",10,"bold"),width=24,state="readonly")
        self.Comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.Comboproduct.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lblPrice=Label(Product_Frame,text="Price",font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font = ("arial",10,"bold"),width=24,state="readonly")
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(Product_Frame,text="Qty",font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame, textvariable=self.qty,font = ("arial",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        #middle frame
        MiddleFrame=Frame(Main_Frame,bg="orangered", bd=10)
        MiddleFrame.place(x=10,y=160,width=1040,height=530)

        


        #Image1
        img1 = Image.open("C:/allcode/billing project/img/good.jpg")
        img1 = img1.resize((500, 500)) 
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(MiddleFrame, image=self.photoimg1) 
        lbl_img1.place(x=0, y=0, width=500, height=500)


        # Image2
        img2=Image.open("C:/allcode/billing project/img/mall.jpg") 
        img2=img2.resize((510,500)) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(MiddleFrame, image=self.photoimg2) 
        lbl_img2.place(x=510, y=0, width=510, height=500)





        #search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1090,y=70,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font = ("arial",13,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry (Search_Frame, textvariable=self.seacrh_bill, font=('arial', 13, 'bold'), width=24)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.btnSearch=Button(Search_Frame,command=self.find_bill,text="Search", font = ('arial', 9, 'bold'),bg="Orangered",fg="white", width=20, cursor="hand2")
        self.btnSearch.grid(row=0,column=2)


        # rightframe Bill aria
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font = ("times new romen",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1070,y=105,width=825,height=560)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,font = ("times new romen",12,"bold"),bg="white",fg="blue")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill Counter Label Frame
        bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font = ("times new romen",12,"bold"),bg="white",fg="red")
        bottom_Frame.place(x=0,y=680,width=1905,height=140)

        #sub total
        self.lblSubTotal=Label(bottom_Frame, text="Sub Total",font = ("arial",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubTotal=ttk.Entry(bottom_Frame,textvariable=self.sub_total,font = ("arial",10,"bold"),width=24)
        self.ComboSubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #tax
        self.lbl_tax=Label (bottom_Frame,text="Gov Tax", font=('arial', 12, 'bold'), bg="white",bd=4) 
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5,pady=2)

        self.txt_tax=ttk.Entry (bottom_Frame,textvariable=self.tax_input, font=('arial', 10, 'bold'), width=24)
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #amount
        self.lblAmountTotal=Label (bottom_Frame, font=('arial', 12, 'bold'), bg="white", text="Total",bd=4) 
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=5,pady=2)

        self.txtAmountTotal=ttk. Entry (bottom_Frame,textvariable=self.total, font = ('arial', 10, 'bold'),width=24)
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.btnAddToCart=Button(Btn_Frame,command=self.ADDItem, text="Add To Cart",height=2, font = ('arial', 15, 'bold'),bg="Orangered",fg="white", width=20, cursor="hand2")
        self.btnAddToCart.grid(row=0,column=0)

        self.btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",height=2, font = ('arial', 15, 'bold'),bg="Orangered",fg="white", width=20, cursor="hand2")
        self.btngenerate_bill.grid(row=0,column=1)

        self.btnSave=Button(Btn_Frame,command=self.save_bill,text="Save Bill",height=2, font = ('arial', 15, 'bold'),bg="Orangered",fg="white", width=20, cursor="hand2")
        self.btnSave.grid(row=0,column=2)

        self.btnPrint=Button(Btn_Frame,command=self.iprint,text="Print",height=2, font = ('arial', 15, 'bold'),bg="Orangered",fg="white", width=20, cursor="hand2")
        self.btnPrint.grid(row=0,column=3)

        self.btnClear=Button(Btn_Frame,command=self.clear,text="clear",height=2, font = ('arial', 15, 'bold'),bg="Orangered",fg="white", width=20, cursor="hand2")
        self.btnClear.grid(row=0,column=4)

        self.btnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",height=2, font = ('arial', 15, 'bold'),bg="Orangered",fg="white", width=20, cursor="hand2")
        self.btnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
    #========================Function Decleration================================
    def ADDItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n 
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the product Name")
        else:
            self.textarea.insert(END,f"\n  {self.product.get()}\t\t\t\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'% (sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Card Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n========================================================================================")
            self.textarea.insert(END,f"\n Sub Ammount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Ammount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Ammount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n========================================================================================")
    

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.seacrh_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.seacrh_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome to RJN Store")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n========================================================================================")
        self.textarea.insert(END,f"\n Products\t\t\t\t\t\tQTY\t\t\tPrice")
        self.textarea.insert(END,"\n========================================================================================\n")




    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)

    
    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.Comboproduct.config(value=self.pant)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.Comboproduct.config(value=self.Tshirt)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.Comboproduct.config(value=self.Shirt)
            self.Comboproduct.current(0)


        #life style
        if self.ComboSubCategory.get()=="Bath Soap":
            self.Comboproduct.config(value=self.BathSoap)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Face Cream":
            self.Comboproduct.config(value=self.FaceCream)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.Comboproduct.config(value=self.HairOil)
            self.Comboproduct.current(0)

        #mobile
        if self.ComboSubCategory.get()=="Iphone":
            self.Comboproduct.config(value=self.Iphone)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.Comboproduct.config(value=self.Samsung)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Xiaomi":
            self.Comboproduct.config(value=self.Xiaomi)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="RealMe":
            self.Comboproduct.config(value=self.Realme)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="One+":
            self.Comboproduct.config(value=self.Oneplus)
            self.Comboproduct.current(0)


    def price(self, event=""):
        #pant
        if self.Comboproduct.get()=="Nike":
            self.ComboPrice.config(value=self.price_pant_Nike)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Addidas":
            self.ComboPrice.config(value=self.price_pant_Addidas)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Puma":
            self.ComboPrice.config(value=self.price_pant_Puma)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_pant_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #T-shirt
        if self.Comboproduct.get()=="Nike":
            self.ComboPrice.config(value=self.price_Tshirt_Nike)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Addidas":
            self.ComboPrice.config(value=self.price_Tshirt_Addidas)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Puma":
            self.ComboPrice.config(value=self.price_Tshirt_Puma)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_Tshirt_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Shirt
        if self.Comboproduct.get()=="Nike":
            self.ComboPrice.config(value=self.price_Shirt_Nike)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Addidas":
            self.ComboPrice.config(value=self.price_Shirt_Addidas)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Puma":
            self.ComboPrice.config(value=self.price_Shirt_Puma)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_Shirt_Levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Bath soap
        if self.Comboproduct.get()=="Life Boy":
            self.ComboPrice.config(value=self.price_LifeBoy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_Lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_Santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Pearl":
            self.ComboPrice.config(value=self.price_Pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Face Cream
        if self.Comboproduct.get()=="CeraVe":
            self.ComboPrice.config(value=self.price_CeraVe)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Caudalie":
            self.ComboPrice.config(value=self.price_Caudalie)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="NIVEA":
            self.ComboPrice.config(value=self.price_NIVEA)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Aqua":
            self.ComboPrice.config(value=self.price_Aqua)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #Face Cream
        if self.Comboproduct.get()=="Luxury":
            self.ComboPrice.config(value=self.price_Luxury)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Essential":
            self.ComboPrice.config(value=self.price_Essential)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Mane":
            self.ComboPrice.config(value=self.price_Mane)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Velvet":
            self.ComboPrice.config(value=self.price_Velvet)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Iphone
        if self.Comboproduct.get()=="Iphone 11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Iphone 12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Iphone 13":
            self.ComboPrice.config(value=self.price_i13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Iphone 14":
            self.ComboPrice.config(value=self.price_i14)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Iphone 15":
            self.ComboPrice.config(value=self.price_i15)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Samsung
        if self.Comboproduct.get()=="A20":
            self.ComboPrice.config(value=self.price_A20)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="M30s":
            self.ComboPrice.config(value=self.price_M30s)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="M50":
            self.ComboPrice.config(value=self.price_M50)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="A50":
            self.ComboPrice.config(value=self.price_A50)
            self.ComboPrice.current(0)
            self.qty.set(1)


        #Xiaomi
        if self.Comboproduct.get()=="Xiaomi 12":
            self.ComboPrice.config(value=self.price_x12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Xiaomi 12 pro":
            self.ComboPrice.config(value=self.price_x12pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Xiaomi 13":
            self.ComboPrice.config(value=self.price_x13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Xiaomi 14":
            self.ComboPrice.config(value=self.price_x14)
            self.ComboPrice.current(0)
            self.qty.set(1)



        #Realme
        if self.Comboproduct.get()=="C35":
            self.ComboPrice.config(value=self.price_C35)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="C55":
            self.ComboPrice.config(value=self.price_C55)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="C65":
            self.ComboPrice.config(value=self.price_C65)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="C55s":
            self.ComboPrice.config(value=self.price_C55s)
            self.ComboPrice.current(0)
            self.qty.set(1)



        #OnePlus
        if self.Comboproduct.get()=="One Plus 8":
            self.ComboPrice.config(value=self.price_8)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="One Plus 10 pro":
            self.ComboPrice.config(value=self.price_10pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="One Plus 11":
            self.ComboPrice.config(value=self.price_11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="One Plus 12":
            self.ComboPrice.config(value=self.price_12)
            self.ComboPrice.current(0)
            self.qty.set(1)


        






if __name__=="__main__":
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()


