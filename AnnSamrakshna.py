from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout, MDNavigationDrawerMenu, MDNavigationDrawerHeader, MDNavigationDrawerItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
import webbrowser
import firebase_admin
from firebase_admin import credentials, db
from functools import partial
from kivymd.toast import toast
import bcrypt
from kivy.clock import Clock
import time
from kivy.clock import mainthread
from kivymd.uix.list import ThreeLineIconListItem, MDList, IconLeftWidget

cred = credentials.Certificate(r"")
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
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
        DonateFoodScreen:
        ViewDonationsScreen:
        ViewNGOsScreen:
        ViewDetailNgoScreen:
        
        HomeNGOScreen:
        ViewDonationsNgoScreen:
        ViewDetailDonationNgoScreen:
        ViewNGOsNgoScreen:
   


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
                on_release: app.register_ngo(); 

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
                    on_release: app.change_screen('donate_food'); nav_drawer_donor.set_state("close")

                MDRaisedButton:
                    text: "View Donations"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    on_release: app.change_screen('view_donations'); nav_drawer_donor.set_state("close")
                MDRaisedButton:
                    text: "View NGOs"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    on_release: app.change_screen('view_ngos'); nav_drawer_donor.set_state("close")
                    
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
                on_release: app.change_screen('donate_food'); nav_drawer_donor.set_state("close")

            MDNavigationDrawerItem:
                text: "View Donations"
                icon: "gift"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.change_screen('view_donations'); nav_drawer_donor.set_state("close")

            MDNavigationDrawerItem:
                text: "View NGO's"
                icon: "account-group"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.change_screen('view_ngos'); nav_drawer_donor.set_state("close")
            MDNavigationDrawerItem:
                text: "Settings"
                icon: "wrench"
                md_bg_color: 235/255, 220/255, 199/255, 1
            
            MDNavigationDrawerItem:
                text: "Log-Out"
                icon: "logout"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: root.logout(); 


          
<DonateFoodScreen>:
    name: 'donate_food'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Donate Food"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home_donor')]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: [40, 50, 40, 200]
            md_bg_color: 235/255, 220/255, 199/255, 1
            MDTextField:
                id: donor_name
                hint_text: "Donor Name"
            MDTextField:
                id: food_type
                hint_text: "Food Type"
            MDTextField:
                id: quantity
                hint_text: "Quantity "
            MDTextField:
                id: location
                hint_text: "Pickup Location"
            MDRaisedButton:
                text: "Submit"
                size_hint: (1, None) 
                md_bg_color: 205/255, 133/255, 63/255,              
                on_release: root.submit_donation()

<ViewDonationsScreen>:
    name: 'view_donations'
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "View Donations"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home_donor')]]
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: 235/255, 220/255, 199/255, 1
            ScrollView:
                MDList:
                    id: donation_list
                
<ViewNGOsScreen>:
    name: 'view_ngos'
    BoxLayout:
        orientation: 'vertical'
        md_bg_color: 235/255, 220/255, 199/255, 1
        MDTopAppBar:
            title: "View NGOs"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home_donor')]]
        
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: 235/255, 220/255, 199/255, 1
            ScrollView:
                MDList:
                    id: ngo_list 

                    
<ViewDetailNgoScreen>:
    name: "view_detail_ngo"
    md_bg_color: 235/255, 220/255, 199/255, 1

    BoxLayout:
        orientation: "vertical"
        md_bg_color: 235/255, 220/255, 199/255, 1

        MDTopAppBar:
            title: "NGO Details"
            md_bg_color: 205/255, 133/255, 63/255
            left_action_items: [["arrow-left", lambda x: app.change_screen("view_ngos")]]  # Back button

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(20)
                spacing: dp(20)
                md_bg_color: 235/255, 220/255, 199/255, 1


                MDCard:
                    orientation: "vertical"
                    padding: dp(45)
                    size_hint: None, None
                    size: dp(320), dp(536)
                    md_bg_color: 1, 1, 1, 1
                    elevation: 4
                    radius: dp(12)

                    MDLabel:
                        id: ngo_name
                        text: "NGO Name"
                        font_style: "H5"
                        theme_text_color: "Primary"
                        bold: True

                    MDLabel:
                        id: ngo_type
                        text: "NGO Type"
                        theme_text_color: "Secondary"

                    MDLabel:
                        id: ngo_address
                        text: "Address"
                        theme_text_color: "Hint"

                    MDLabel:
                        id: ngo_phone
                        text: "Phone"
                        theme_text_color: "Secondary"

                    MDLabel:
                        id: ngo_email
                        text: "Email"
                        theme_text_color: "Secondary"
 

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
                    on_release: app.change_screen('view_donations_ngo');nav_drawer_ngo.set_state("close")

                MDRaisedButton:
                    text: "View NGOs"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    on_release: app.change_screen('view_ngos_ngo'); nav_drawer_ngo.set_state("close")
                    

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
                on_release: app.change_screen('view_donations'); nav_drawer_ngo.set_state("close")

            MDNavigationDrawerItem:
                text: "View NGO's"
                icon: "account-group"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.chane_screen('view_ngos_ngo'); nav_drawer_ngo.set_state("close")
            MDNavigationDrawerItem:
                text: "Settings"
                icon: "wrench"
                md_bg_color: 235/255, 220/255, 199/255, 1
            
            MDNavigationDrawerItem:
                text: "Log-Out"
                icon: "logout"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: root.logout();


<ViewDonationsNgoScreen>:
    name: 'view_donations_ngo'
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "View Donations"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home_ngo')]]
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: 235/255, 220/255, 199/255, 1
            ScrollView:
                MDList:
                    id: donation_list

<ViewDetailDonationNgoScreen>:
    name: 'donation_detail'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Donation Details"
            md_bg_color: 205/255, 133/255, 63/255
            left_action_items: [["arrow-left", lambda x: app.change_screen('home_ngo')]]
        MDBoxLayout:
            orientation: 'vertical'
            padding: '20dp'
            spacing: '10dp'
            md_bg_color: 235/255, 220/255, 199/255, 1

            MDLabel:
                id: donor_name
                text: "Donor: "
                halign: 'center'

            MDLabel:
                id: food_type
                text: "Food Type: "
                halign: 'center'

            MDLabel:
                id: quantity
                text: "Quantity: "
                halign: 'center'
            MDLabel:
                id: location
                text: "Location: "
                halign: 'center'

            MDRectangleFlatButton:
                text: 'Open Location in Google Maps'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}
                md_bg_color: 205/255, 133/255, 63/255
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1 
                on_release: root.open_location_in_maps()

            MDRectangleFlatButton:
                id: claim_donation_btn  
                text: 'Claim Donation'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}
                md_bg_color: 205/255, 133/255, 63/255
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1 

<ViewNGOsNgoScreen>:
    name: 'view_ngos_ngo'
    BoxLayout:
        orientation: 'vertical'
        md_bg_color: 235/255, 220/255, 199/255, 1
        MDTopAppBar:
            title: "View NGOs"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home_donor')]]
        
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: 235/255, 220/255, 199/255, 1
            ScrollView:
                MDList:
                    id: ngo_list 
                         
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
    def logout(self):
        self.ids.nav_drawer_donor.set_state("close")

        print("User logged out")
        
      
        self.manager.current = 'login'

class DonateFoodScreen(Screen):
    def submit_donation(self):
        donor_name = self.ids.donor_name.text.strip()
        food_type = self.ids.food_type.text.strip()
        quantity = self.ids.quantity.text.strip()
        location = self.ids.location.text.strip()

        if not donor_name or not food_type or not quantity or not location:
            toast("All fields are required")
            print("All fields are required!")
            return

       
        donation_key = f"donation_{int(time.time())}"


        donation_data = {
            "donor_name": donor_name,
            "food_type": food_type,
            "quantity": quantity,
            "location": location,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S") 
        }

 
        db.reference("donations").child(donation_key).set(donation_data)

        print("Donation submitted successfully!")
        toast("Donation Submitted successfully!!")
     
        Clock.schedule_once(self.clear_fields, 0.5)

    def clear_fields(self, dt):
        self.ids.donor_name.text = ""
        self.ids.food_type.text = ""
        self.ids.quantity.text = ""
        self.ids.location.text = ""


class ViewDonationsScreen(Screen):
    def on_enter(self):
        """Fetch and display only unclaimed donations when the screen is opened."""
        self.load_donations()

    def load_donations(self):
        """Retrieve and display only unclaimed donations from Firebase."""
        donation_ref = db.reference("donations")
        donations = donation_ref.get()

       
        self.ids.donation_list.clear_widgets()

        if donations:
            has_unclaimed = False  
            for key, donation in donations.items():
                if donation.get("status") != "claimed": 
                    donation_text = f"{donation['donor_name']} - {donation['food_type']} ({donation['quantity']}) at {donation['location']}"
                    self.ids.donation_list.add_widget(OneLineListItem(text=donation_text))
                    has_unclaimed = True  
            
       
            if not has_unclaimed:
                self.ids.donation_list.add_widget(OneLineListItem(text="No unclaimed donations available."))
        else:
            self.ids.donation_list.add_widget(OneLineListItem(text="No donations available."))

class ViewNGOsScreen(Screen):
    def on_pre_enter(self):
        """Clear and reload NGOs every time the screen is entered."""
        self.fetch_ngos()

    def fetch_ngos(self):
        """Fetch NGOs from Firebase and update the list."""
        ref = db.reference('ngos')  # Adjust if needed
        ngos = ref.get()

        if ngos:
            self.update_list(ngos)
        else:
            self.update_list({})  # If no data, show an empty list

    @mainthread
    def update_list(self, ngos):
        """Update the UI with fetched NGOs."""
        self.ids.ngo_list.clear_widgets()  # Clear old list

        if ngos:
            for ngo_id, ngo_data in ngos.items():
                ngo_name = ngo_data.get("ngo_name", "Unknown NGO")
                ngo_type = ngo_data.get("ngo_type", "No Type Provided")
                address = ngo_data.get("address", "No Address")
                phone = ngo_data.get("phone", "No Contact")
                email = ngo_data.get("email", "No Email")

                # Create list item with tap action
                item = ThreeLineIconListItem(
                    text=f"{ngo_name} ({ngo_type})",
                    secondary_text=f"Address: {address}",
                    tertiary_text=f"Phone: {phone} \nEmail: {email}",
                    on_release=lambda x, data=ngo_data: self.view_ngo_details(data)
                )

                # Add NGO icon
                item.add_widget(IconLeftWidget(icon="charity"))

                self.ids.ngo_list.add_widget(item)
        else:
            self.ids.ngo_list.add_widget(ThreeLineIconListItem(text="No NGOs registered."))

    def view_ngo_details(self, ngo_data):
        """Navigate to ViewDetailNgoScreen and set NGO details."""
        detail_screen = self.manager.get_screen("view_detail_ngo")
        detail_screen.update_details(ngo_data)
        self.manager.current = "view_detail_ngo"


class ViewDetailNgoScreen(Screen):
    def update_details(self, ngo_data):
        """Update UI elements with NGO details."""
        self.ids.ngo_name.text = f"NGO: {ngo_data.get('ngo_name', 'Unknown')}"
        self.ids.ngo_type.text = f"Type: {ngo_data.get('ngo_type', 'N/A')}"
        self.ids.ngo_address.text = f"Address: {ngo_data.get('address', 'N/A')}"
        self.ids.ngo_phone.text = f"Phone: {ngo_data.get('phone', 'N/A')}"
        self.ids.ngo_email.text = f"Email: {ngo_data.get('email', 'N/A')}"


class HomeNGOScreen(Screen):
    def logout(self):
        self.ids.nav_drawer_ngo.set_state("close")
        
        print("User logged out")
        
       
        self.manager.current = 'login'

class ViewDonationsNgoScreen(Screen):
    def on_enter(self):
        """Fetch and display donations when the screen is opened."""
        self.load_donations()

    def load_donations(self):
        """Retrieve and display only unclaimed donations from Firebase."""
        donation_ref = db.reference("donations")
        donations = donation_ref.get()


        self.ids.donation_list.clear_widgets()

        if donations:
            for key, donation in donations.items():
                if donation.get("status") != "claimed":  
                    donation_text = f"{donation['food_type']} ({donation['quantity']}) from {donation['donor_name']}"
                    item = OneLineListItem(text=donation_text, on_release=lambda x, k=key: self.view_details(k))
                    self.ids.donation_list.add_widget(item)
        else:
            self.ids.donation_list.add_widget(OneLineListItem(text="No available donations."))

    def view_details(self, donation_id):
        """Navigate to the donation detail screen and pass the donation ID."""
        detail_screen = self.manager.get_screen('donation_detail')
        detail_screen.load_donation_details(donation_id)
        self.manager.current = 'donation_detail'

class ViewDetailDonationNgoScreen(Screen):
    def load_donation_details(self, donation_id):
        """Fetch detailed donation information from Firebase."""
        donation_ref = db.reference(f"donations/{donation_id}")
        donation = donation_ref.get()

        if donation:
            self.ids.donor_name.text = f"Donor: {donation['donor_name']}"
            self.ids.food_type.text = f"Food Type: {donation['food_type']}"
            self.ids.quantity.text = f"Quantity: {donation['quantity']}"
            self.ids.location.text = f"Location: {donation['location']}"

           
            self.ids.claim_donation_btn.on_release = lambda: self.claim_donation(donation_id)

    def open_location_in_maps(self):
        """Open the pickup location in Google Maps."""
        location = self.ids.location.text.replace("Location: ", "").strip()
        url = f"https://www.google.com/maps/search/?api=1&query={location.replace(' ', '+')}"
        webbrowser.open(url)

    def claim_donation(self, donation_id):
        """Mark the donation as claimed in Firebase and refresh the list."""
        donation_ref = db.reference(f"donations/{donation_id}")
        donation_ref.update({"status": "claimed"}) 

   
        toast(f"Donation {donation_id} claimed!")
        print(f"Donation {donation_id} claimed!")

        self.manager.current = 'view_donations_ngo'


        self.manager.get_screen('view_donations_ngo').load_donations()

class ViewNGOsNgoScreen(Screen):
    def on_pre_enter(self):
        """Clear and reload NGOs every time the screen is entered."""
        self.fetch_ngos()

    def fetch_ngos(self):
        """Fetch NGOs from Firebase and update the list."""
        ref = db.reference('ngos')  
        ngos = ref.get()

        if ngos:
            self.update_list(ngos)
        else:
            self.update_list({})  

    @mainthread
    def update_list(self, ngos):
        """Update the UI with fetched NGOs."""
        self.ids.ngo_list.clear_widgets()  

        if ngos:
            for ngo_id, ngo_data in ngos.items():
                ngo_name = ngo_data.get("ngo_name", "Unknown NGO")
                ngo_type = ngo_data.get("ngo_type", "No Type Provided")
                address = ngo_data.get("address", "No Address")
                phone = ngo_data.get("phone", "No Contact")
                email = ngo_data.get("email", "No Email")

                
                item = ThreeLineIconListItem(
                    text=f"{ngo_name} ({ngo_type})",
                    secondary_text=f"Address: {address}",
                    tertiary_text=f"Phone: {phone}\n|Email: {email}",
                )

               
                item.add_widget(IconLeftWidget(icon="charity"))  

                self.ids.ngo_list.add_widget(item)
        else:
            self.ids.ngo_list.add_widget(ThreeLineIconListItem(text="No NGOs registered."))

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
