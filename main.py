from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout, MDNavigationDrawerMenu, MDNavigationDrawerHeader, MDNavigationDrawerItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
import webbrowser
import firebase_admin
from firebase_admin import credentials, db
from functools import partial
from kivymd.toast import toast
import bcrypt


# Initialize Firebase
cred = credentials.Certificate(r"") 
firebase_admin.initialize_app(cred, {
    'databaseURL': ' '
})

Window.size = (360, 640)

KV = """
MDNavigationLayout:
    ScreenManager:
        id: screen_manager
        LoginScreen:
        RegisterScreen:
        RegisterDonorScreen:
        RegisterNGOScreen:
        HomeDonorScreen:
        HomeNGOScreen:

   


<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "10dp"
            md_bg_color: 235/255, 220/255, 199/255, 1
            Image:
                source: 'D:/Annsamrakshna/assets/logo/Annsamrakshna.png'
                size_hint: (0.8, 0.7)
                pos_hint: {"center_x": 0.5}
                keep_ratio: True
                allow_stretch: True
            MDBoxLayout:
                orientation: 'vertical'
                padding: [50,100]
                spacing: dp(20)

                MDTextField:
                    id: username
                    hint_text: "Username"
                    size_hint: (1, None)
                    icon_right: 'account'
                    height: "40dp"
                MDTextField:
                    id: password
                    hint_text: "Password"
                    size_hint: (1, None)
                    icon_right: 'eye-off'
                    height: "40dp"
                    password: True
                MDRaisedButton:
                    text: "Login"
                    size_hint: (1, None)
                    height: "50dp"
                    md_bg_color: 205/255, 133/255, 63/255,
                    on_release: app.login()
                MDRaisedButton:
                    text: "Sign Up"
                    size_hint: (1, None)
                    height: "50dp"
                    md_bg_color: 205/255, 133/255, 63/255,
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1 
                    on_release: app.change_screen('register')

<RegisterScreen>:
    name: 'register'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Register"
            md_bg_color: 205/255, 133/255, 63/255
            left_action_items: [["arrow-left", lambda x: app.change_screen('login')]]

        MDBoxLayout:
            orientation: 'vertical'
            padding: [40, 50, 40,350]
            spacing: 40
            md_bg_color: 235/255, 220/255, 199/255, 1

            MDRaisedButton:
                text: "Register as Donor"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                md_bg_color: 205/255, 133/255, 63/255,
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1 
                on_release: app.change_screen('register_donor')
            MDRaisedButton:
                text: "Register as NGO"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                md_bg_color: 205/255, 133/255, 63/255,
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1 
                on_release: app.change_screen('register_ngo')
        
                
<RegisterDonorScreen>:
    name: "register_donor"
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Register as Donor"
            md_bg_color: 205/255, 133/255, 63/255
            left_action_items: [["arrow-left", lambda x: app.change_screen('register')]]
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: [40, 50, 40, 100]
            spacing: 20
            md_bg_color: 235/255, 220/255, 199/255, 1

            MDTextField:
                id: full_name
                hint_text: "Full Name"
                mode: "rectangle"
            
            MDTextField:
                id: user_name
                hint_text: "User Name"
                mode: "rectangle"
            
            MDTextField:
                id: email
                hint_text: "Email Address"
                mode: "rectangle"
                input_type: "mail"

            MDTextField:
                id: phone
                hint_text: "Phone Number"
                mode: "rectangle"
                input_type: "number"
                max_text_length: 10

            MDTextField:
                id: address
                hint_text: "Address / Location"
                mode: "rectangle"

            MDTextField:
                id: password
                hint_text: "Password"
                mode: "rectangle"
                password: True

            MDRaisedButton:
                text: "Register"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                md_bg_color: 205/255, 133/255, 63/255,
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1 
                on_release: app.register_donor()
      
                    
<RegisterNGOScreen>:
    name: "register_ngo"
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Register as NGO"
            md_bg_color: 205/255, 133/255, 63/255
            left_action_items: [["arrow-left", lambda x: app.change_screen('register')]]
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: [40, 20, 40, 50]
            spacing: 15
            md_bg_color: 235/255, 220/255, 199/255, 1

            MDTextField:
                id: ngo_name
                hint_text: "NGO Name"
                mode: "rectangle"

            MDTextField:
                id: registration_number
                hint_text: "Registration Number"
                mode: "rectangle"

            MDTextField:
                id: email
                hint_text: "Email Address"
                mode: "rectangle"
                input_type: "mail"

            MDTextField:
                id: phone
                hint_text: "Phone Number"
                mode: "rectangle"
                input_type: "tel"
                max_text_length: 10

            MDTextField:
                id: address
                hint_text: "Office Address, City, State"
                mode: "rectangle"

            MDTextField:
                id: ngo_type
                hint_text: "Type of NGO (Food Relief, Homeless Support, etc.)"
                mode: "rectangle"
            
            MDTextField:
                id: password
                hint_text: "Password"
                mode: "rectangle"
                password: True

            MDRaisedButton:
                text: "Register"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                md_bg_color: 205/255, 133/255, 63/255,
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1 
                on_release: app.register_ngo()

<HomeDonorScreen>:
    name: 'home_donor'
    BoxLayout:
        orientation: 'vertical'
    
        MDTopAppBar:
            title: "Annasamrakshna"
            left_action_items: [["menu", lambda x: root.ids.nav_drawer_donor.set_state("open")]]
            md_bg_color: 205/255, 133/255, 63/255,
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            md_bg_color: 235/255, 220/255, 199/255, 1
            Image:
                source: 'D:/Annsamrakshna/assets/logo/Annsamrakshna.png'
                size_hint: (0.5, 0.5)
                pos_hint: {"center_x": 0.5}
                keep_ratio: True
                allow_stretch: True
            MDBoxLayout:
                orientation: 'vertical'
                padding: [20,80]
                spacing: dp(30)
                MDRaisedButton:
                    text: "Donate Food"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0)
                    md_bg_color: 205/255, 133/255, 63/255,  
                    
                MDRaisedButton:
                    text: "View Donations"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    
                MDRaisedButton:
                    text: "View NGOs"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
        
    MDNavigationDrawer:
        id: nav_drawer_donor
        md_bg_color: 235/255, 220/255, 199/255, 1

        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "Menu"
                spacing: "18dp"
                md_bg_color: 235/255, 220/255, 199/255, 1
                
            MDNavigationDrawerItem:
                text: "Profile"
                icon: "face-man-profile"
                md_bg_color: 235/255, 220/255, 199/255, 1
            
            MDNavigationDrawerItem:
                text: "Donate Food"
                icon: "food"
                md_bg_color: 235/255, 220/255, 199/255, 1
            
            MDNavigationDrawerItem:
                text: "View Donations"
                icon: "gift"
                md_bg_color: 235/255, 220/255, 199/255, 1

            MDNavigationDrawerItem:
                text: "View NGO's"
                icon: "account-group"
                md_bg_color: 235/255, 220/255, 199/255, 1

            MDNavigationDrawerItem:
                text: "Settings"
                icon: "wrench"
                md_bg_color: 235/255, 220/255, 199/255, 1
            
            MDNavigationDrawerItem:
                text: "Log-Out"
                icon: "logout"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.logout(); nav_drawer.set_state("close")
            
                
                

<HomeNGOScreen>:
    name: 'home_ngo'
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "Annasamrakshna"
            left_action_items: [["menu", lambda x: root.ids.nav_drawer_ngo.set_state("open")]]
            md_bg_color: 205/255, 133/255, 63/255,
        
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            md_bg_color: 235/255, 220/255, 199/255, 1
            Image:
                source: 'D:/Annsamrakshna/assets/logo/Annsamrakshna.png'
                size_hint: (0.5, 0.5)
                pos_hint: {"center_x": 0.5}
                keep_ratio: True
                allow_stretch: True
            MDBoxLayout:
                orientation: 'vertical'
                padding: [20,80]
                spacing: dp(50)
                
            
                MDRaisedButton:
                    text: "View Donations"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    
                MDRaisedButton:
                    text: "View NGOs"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
        
    MDNavigationDrawer:
        id: nav_drawer_ngo
        md_bg_color: 235/255, 220/255, 199/255, 1

        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "Menu"
                spacing: "18dp"
                md_bg_color: 235/255, 220/255, 199/255, 1
                
            MDNavigationDrawerItem:
                text: "Profile"
                icon: "face-man-profile"
                md_bg_color: 235/255, 220/255, 199/255, 1
            
            
            MDNavigationDrawerItem:
                text: "View Donations"
                icon: "gift"
                md_bg_color: 235/255, 220/255, 199/255, 1

            MDNavigationDrawerItem:
                text: "View NGO's"
                icon: "account-group"
                md_bg_color: 235/255, 220/255, 199/255, 1

            MDNavigationDrawerItem:
                text: "Settings"
                icon: "wrench"
                md_bg_color: 235/255, 220/255, 199/255, 1
            
            MDNavigationDrawerItem:
                text: "Log-Out"
                icon: "logout"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.logout(); nav_drawer.set_state("close")
""" 

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class RegisterDonorScreen(Screen):
    pass

class RegisterNGOScreen(Screen):
    pass

class HomeDonorScreen(Screen):
    pass

class HomeNGOScreen(Screen):
    pass

class FoodWasteApp(MDApp):
    def build(self):
        self.title = "Annasamrakshna"
        self.theme_cls.primary_palette = "DeepOrange"
        self.screen_manager = Builder.load_string(KV)
        self.donations = []
        self.ngos = []
        self.is_donor = False  
        return self.screen_manager

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def login(self):
        username = self.root.ids.screen_manager.get_screen('login').ids.username.text
        password = self.root.ids.screen_manager.get_screen('login').ids.password.text

        if not username or not password:
            toast("Please enter username and password")
            return

 
        donor_ref = db.reference("donors")
        donor_data = donor_ref.child(username).get()

        if donor_data and bcrypt.checkpw(password.encode('utf-8'), donor_data["password"].encode('utf-8')):
            self.is_donor = True
            self.change_screen('home_donor')
            toast("Login successful!")
            return

        ngo_ref = db.reference("ngos")
        ngo_data = ngo_ref.child(username).get()

        if ngo_data and bcrypt.checkpw(password.encode('utf-8'), ngo_data["password"].encode('utf-8')):
            self.is_donor = False
            self.change_screen('home_ngo')
            toast("Login successful!")
            return

        toast("Invalid credentials")
    
    def logout(self):
        self.is_donor = False 
        self.root.ids.screen_manager.current = "login"  
        self.root.ids.nav_drawer.set_state("close") 
        print("User logged out successfully")

    def register_donor(self):
        full_name = self.root.ids.screen_manager.get_screen('register_donor').ids.full_name.text
        user_name = self.root.ids.screen_manager.get_screen('register_donor').ids.user_name.text
        email = self.root.ids.screen_manager.get_screen('register_donor').ids.email.text
        phone = self.root.ids.screen_manager.get_screen('register_donor').ids.phone.text
        address = self.root.ids.screen_manager.get_screen('register_donor').ids.address.text
        password = self.root.ids.screen_manager.get_screen('register_donor').ids.password.text

        if not full_name or not user_name or not email or not phone or not address or not password:
            toast("Please fill all fields")
            return

        donor_ref = db.reference("donors")

   
        if donor_ref.child(user_name).get():
            toast("Username already exists")
            return

 
        existing_donors = donor_ref.get()
        if existing_donors:
            for donor_info in existing_donors.values():
                if donor_info.get("email") == email:
                    toast("Email is already registered")
                    return
                if donor_info.get("phone") == phone:
                    toast("Phone number is already registered")
                    return


        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        donor_data = {
        "full_name": full_name,
        "user_name": user_name,
        "email": email,
        "phone": phone,
        "address": address,
        "password": hashed_password 
    }

        donor_ref.child(user_name).set(donor_data)
        toast("Registration successful!")
        self.change_screen('login')


    def register_ngo(self):
        ngo_name = self.root.ids.screen_manager.get_screen('register_ngo').ids.ngo_name.text
        registration_number = self.root.ids.screen_manager.get_screen('register_ngo').ids.registration_number.text
        email = self.root.ids.screen_manager.get_screen('register_ngo').ids.email.text
        phone = self.root.ids.screen_manager.get_screen('register_ngo').ids.phone.text
        address = self.root.ids.screen_manager.get_screen('register_ngo').ids.address.text
        ngo_type = self.root.ids.screen_manager.get_screen('register_ngo').ids.ngo_type.text
        password = self.root.ids.screen_manager.get_screen('register_ngo').ids.password.text

        if not ngo_name or not registration_number or not email or not phone or not address or not ngo_type or not password:
            toast("Please fill all fields")
            return

        ngo_ref = db.reference("ngos")


        if ngo_ref.child(registration_number).get():
            toast("Registration number already exists")
            return

        existing_ngos = ngo_ref.get()
        if existing_ngos:
            for ngo_info in existing_ngos.values():
                if ngo_info.get("email") == email:
                    toast("Email is already registered")
                    return
                if ngo_info.get("phone") == phone:
                    toast("Phone number is already registered")
                    return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        ngo_data = {
        "ngo_name": ngo_name,
        "registration_number": registration_number,
        "email": email,
        "phone": phone,
        "address": address,
        "ngo_type": ngo_type,
        "password": hashed_password  
    }

        ngo_ref.child(registration_number).set(ngo_data)
        toast("NGO registered successfully!")
        self.change_screen('login')
        



if __name__ == '__main__':
    FoodWasteApp().run()
