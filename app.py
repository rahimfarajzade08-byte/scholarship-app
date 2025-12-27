qrup_1_RI = [250104, 250108, 250107, 250103, 250110]
qrup_1_RK = [250101, 250102]
qrup_2 = [250109, 250111]

class Student:
    def __init__(self, ixtisas_id, name, surname, semester, english_point):
        self.ixtisas_id = int(ixtisas_id)
        self.name = name
        self.surname = surname
        self.semester = str(semester)
        self.english_point = english_point
        self.adiak_point = 0
        self.history_point = 0

    def bal_melumatlarini_al(self):
        # Ixtisas və semestrə görə yalnız birini soruşur
        if self.ixtisas_id in qrup_1_RI:
            if self.semester == '1':
                self.adiak_point = float(input(f"{self.name} üçün ADİAK balını daxil edin: "))
            else:
                self.history_point = float(input(f"{self.name} üçün Tarix balını daxil edin: "))
        elif self.ixtisas_id in qrup_1_RK or self.ixtisas_id in qrup_2:
            if self.semester == '1':
                self.history_point = float(input(f"{self.name} üçün Tarix balını daxil edin: "))
            else:
                self.adiak_point = float(input(f"{self.name} üçün ADİAK balını daxil edin: "))

    def neticeleri_goster(self):
        # Bu hissə yalnız dəyəri olan balı göstərir
        print(f"\n--- Məlumat Paneli ---")
        print(f"Tələbə: {self.name} {self.surname}")
        print(f"İngilis dili: {self.english_point}")
        
        if self.adiak_point > 0:
            print(f"ADİAK balı: {self.adiak_point}")
        
        if self.history_point > 0:
            print(f"Tarix balı: {self.history_point}")

# --- İSTİFADƏ ---
telebe1 = Student(input("ID: "), input("Ad: "), input("Soyad: "), input("Semestr: "), input("Ingilis dili:"))
telebe1.bal_melumatlarini_al() # Lazım olan balı soruşur
telebe1.neticeleri_goster()     # Yalnız o balı göstərir