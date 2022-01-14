# name=input("Name:")
# age=int(input("Age:"))
# Education=input("Education:")
# if(age>=18):
#     if(Education=="highschool") or (Education=="college"):
#         print(f"Sayın {name}, ehliyet alabilirsiniz. ")

#     else:
#         print(f"Sayın{name}, eğitim durumunuz ehliyet almak için yeterli değil. ")
# else:
#     print(f"Sayın {name}, yaşınız ehliyet almak için yeterli değil.")






yazili1=int(input("İlk yazılı puanınızı giriniz:"))
yazili2=int(input("İkinci yazılı puanınızı giriniz:"))
sozlu=int(input("Sözlu puanınızı giriniz:"))
ortPuan=(yazili1+yazili2+sozlu)/3

if ( ortPuan > 0 and ortPuan <25):
    print(f"Puan ortalamanız {ortPuan}'dır. Notunuz:0 ")
else:
    if ( ortPuan > 24 and ortPuan <45):
         print(f"Puan ortalamanız {ortPuan}'dır. Notunuz:1 ")
    else:
        if ( ortPuan > 44 and ortPuan <55):
         print(f"Puan ortalamanız {ortPuan}'dır. Notunuz:2 ")
        else:
            if ( ortPuan > 54 and ortPuan <70):
                print(f"Puan ortalamanız {ortPuan}'dır. Notunuz:3 ")
            else:
                if ( ortPuan > 69 and ortPuan <85):
                    print(f"Puan ortalamanız {ortPuan}'dır. Notunuz:4 ")    
                else:
                    if ( ortPuan > 85 and ortPuan <101):
                        print(f"Puan ortalamanız {ortPuan}'dır. Notunuz:5 ")
                    else:
                        print(f"Hatalı giriş yaptınız. Sonuç maksimum puanın üstünde.")





# import datetime
# tarih=input("Aracınızın trafiğe giriş şeklini yıl/ay/gün şeklinde ','işareti ile ayırarak girinizör(2021,01,21):")
# tarih=tarih.split(",")

# trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
# simdi= datetime.datetime.now()
# fark=simdi-trafigeCikis
# fark=fark.days

# print(f"Aracınız {fark} gündür trafikte.")

# if (fark <= 365):
#     print("Aracınız 1. servis aralığındadır.")
# elif (364<fark<365*2):
#     print("Aracınız 2. servis aralığındadır.")
# elif (((365*2)-1)<fark<365*3):
#     print("Aracınız 3. servis aralığındadır.")
# else:
#     print("Aracınız 4. ya da üstü servis aralığındadır. Hizmet verememekteyiz.")


