from tkinter import *
import speedtest 



def main():
    def speedcheck():
        sp= speedtest.Speedtest()
        sp.get_servers()
        down= str(round(sp.download()/(10**6),3))+"Mbps"
        up= str(round(sp.upload()/(10**6),3))+"Mbps"
        lab_down.config(text=down)
        lab_up.config(text=up)



    sp =Tk()
    sp.title("Internet Speed Test")
    sp.geometry("500x650")
    sp.config(bg="Blue")

    lab= Label(sp,text="Internet Speed Test",font=("Times New Roman",30,"bold"),bg="blue",fg="white")
    lab.place(x=60,y=40,height=50,width=380)

    lab= Label(sp,text="Download Speed",font=("Times New Roman",30,"bold"))
    lab.place(x=60,y=130,height=50,width=380)
    
    lab_down= Label(sp,text=" 00 ",font=("Times New Roman",30,"bold"))
    lab_down.place(x=60,y=200,height=50,width=380)
    lab= Label(sp,text=" Upload Speed ",font=("Times New Roman",30,"bold"))
    lab.place(x=60,y=290,height=50,width=380)
    lab_up= Label(sp,text=" 00 ",font=("Times New Roman",30,"bold"))
    lab_up.place(x=60,y=360,height=50,width=380)
    # Button
    button= Button(sp,text="Check Speed",font=("Times New Roman",30,"bold"),relief=RAISED,bg="pink",command=speedcheck)
    
    button.pack(ipadx=105, ipady=15, fill="both", expand=True)
    button.place(x=120,y=460,height=50,width=250)

    sp.mainloop()
main()