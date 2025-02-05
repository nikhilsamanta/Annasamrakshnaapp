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

Window.size = (360, 640)

KV = """
MDNavigationLayout:
    ScreenManager:
        id: screen_manager
        LoginScreen:
        HomeScreen:
        DonateScreen:
        NGORegisterScreen:
        ViewDonationsScreen:
        ViewNGOsScreen:
        DonationDetailScreen:

    MDNavigationDrawer:
        id: nav_drawer
        md_bg_color: 235/255, 220/255, 199/255, 1
        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "Menu"
                spacing: "12dp"
                md_bg_color: 235/255, 220/255, 199/255, 1
            MDNavigationDrawerItem:
                text: "Home"
                icon: "home"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.change_screen('home'); nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "Donate Food"
                icon: "food"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.change_screen('donate'); app.root.ids.nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "Register NGO"
                icon: "account-group"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.change_screen('ngo_register'); app.root.ids.nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "View Donations"
                icon: "clipboard-list"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.change_screen('view_donations'); nav_drawer.set_state("close")
            MDNavigationDrawerItem:
                text: "View NGOs"
                icon: "domain"
                md_bg_color: 235/255, 220/255, 199/255, 1
                on_release: app.change_screen('view_ngos'); nav_drawer.set_state("close")

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
        
<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Annasamrakshna"
            left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("open")]]
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
                    on_release: app.change_screen('donate')
                MDRaisedButton:
                    text: "Register as NGO"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    on_release: app.change_screen('ngo_register')
                MDRaisedButton:
                    text: "View Donations"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    on_release: app.change_screen('view_donations')
                MDRaisedButton:
                    text: "View NGOs"
                    pos_hint: {"center_x": 0.5}
                    size_hint: (0.8, 0) 
                    md_bg_color: 205/255, 133/255, 63/255,
                    on_release: app.change_screen('view_ngos')

<DonateScreen>:
    name: 'donate'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Donate Food"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
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
                on_release: app.add_donation()

<NGORegisterScreen>:
    name: 'ngo_register'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Register as NGO"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: 235/255, 220/255, 199/255, 1
            padding: [20, 0, 20, 150]
            spacing: dp(20) 
            MDTextField:
                id: ngo_name
                hint_text: "NGO Name"
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                size_hint_x: 0.8
            MDTextField:
                id: ngo_identification
                hint_text: "NGO ID"
                pos_hint: {"center_x": 0.5, "center_y": 0.8}
                size_hint_x: 0.8
            MDTextField:
                id: ngo_contact
                hint_text: "Contact"
                pos_hint: {"center_x": 0.5, "center_y": 0.7}
                size_hint_x: 0.8
            MDTextField:
                id: ngo_location
                hint_text: "Location"
                pos_hint: {"center_x": 0.5, "center_y": 0.6}
                size_hint_x: 0.8
            MDRaisedButton:
                text: "Submit"
                md_bg_color: 205/255, 133/255, 63/255,
                pos_hint: {"center_x": 0.5}
                size_hint: (0.8, None) 
                on_release: app.register_ngo()
                            

<ViewDonationsScreen>:
    name: 'view_donations'
    BoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            title: "View Donations"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
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
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
        
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color: 235/255, 220/255, 199/255, 1
            ScrollView:
                MDList:
                    id: ngo_list 

<DonationDetailScreen>:
    name: 'donation_detail'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Donation Details"
            md_bg_color: 205/255, 133/255, 63/255,
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]
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
                md_bg_color: 205/255, 133/255, 63/255,
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1 
                on_release: app.open_google_maps()
""" 

 

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class DonateScreen(Screen):
    pass

class NGORegisterScreen(Screen):
    pass

class ViewDonationsScreen(Screen):
    pass

class ViewNGOsScreen(Screen):
    pass

class DonationDetailScreen(Screen):
    pass

class FoodWasteApp(MDApp):
    def build(self):
        self.title = "Annasamrakshna"
        self.theme_cls.primary_palette = "DeepOrange"
        self.screen_manager = Builder.load_string(KV)
        self.donations = []
        self.ngos = []
        return self.screen_manager

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def login(self):
        screen_manager = self.root.ids.screen_manager
        login_screen = screen_manager.get_screen('login')

        username = login_screen.ids.username.text
        password = login_screen.ids.password.text

        # Simple authentication check 
        if username == "admin" and password == "admin":
            self.show_dialog("Success", "Login successful!")
            self.change_screen('home')
        else:
            self.show_dialog("Error", "Invalid credentials, please try again.")
    
    def add_donation(self):
        screen_manager = self.root.ids.screen_manager  
        donate_screen = screen_manager.get_screen('donate')  

        donor_name = donate_screen.ids.donor_name.text
        food_type = donate_screen.ids.food_type.text
        quantity = donate_screen.ids.quantity.text
        location = donate_screen.ids.location.text

        if donor_name and food_type and quantity and location:
            self.donations.append({
                "Donor": donor_name,
                "Food": food_type,
                "Quantity": quantity,
                "Location": location
            })

            donate_screen.ids.donor_name.text = ""
            donate_screen.ids.food_type.text = ""
            donate_screen.ids.quantity.text = ""
            donate_screen.ids.location.text = ""

            self.show_dialog("Success", "Donation added successfully!")
            self.update_donations()
            self.change_screen('home')
        else:
            self.show_dialog("Error", "Please fill out all fields!")

    def update_donations(self):
        screen_manager = self.root.ids.screen_manager  
        donation_list = screen_manager.get_screen('view_donations').ids.donation_list

        donation_list.clear_widgets() 

        for donation in self.donations:
            item_text = f"{donation['Donor']} donated {donation['Quantity']} of {donation['Food']} at {donation['Location']}"
            list_item = OneLineListItem(text=item_text, on_release=lambda x, donation=donation: self.show_donation_detail(donation))
            donation_list.add_widget(list_item)

    def show_donation_detail(self, donation):
        screen_manager = self.root.ids.screen_manager
        detail_screen = screen_manager.get_screen('donation_detail')

        detail_screen.ids.donor_name.text = f"Donor: {donation['Donor']}"
        detail_screen.ids.food_type.text = f"Food Type: {donation['Food']}"
        detail_screen.ids.quantity.text = f"Quantity: {donation['Quantity']}"
        detail_screen.ids.location.text = f"Location: {donation['Location']}"

        self.change_screen('donation_detail')
    def open_google_maps(self):
        screen_manager = self.root.ids.screen_manager
        donation_detail_screen = screen_manager.get_screen('donation_detail')
        
        location = donation_detail_screen.ids.location.text.replace("Location: ", "").strip()
        
        if location:
            query = location.replace(" ", "+")  # Convert spaces to `+` for URL encoding
            url = f"https://www.google.com/maps/search/?api=1&query={query}"
            webbrowser.open(url)
        else:
            self.show_dialog("Error", "No location provided.")


    def register_ngo(self):
        screen_manager = self.root.ids.screen_manager  
        ngo_screen = screen_manager.get_screen('ngo_register')  

        ngo_name = ngo_screen.ids.ngo_name.text
        ngo_contact = ngo_screen.ids.ngo_contact.text
        ngo_location = ngo_screen.ids.ngo_location.text

        if ngo_name and ngo_contact and ngo_location:
            self.ngos.append({
                "NGO": ngo_name,
                "Contact": ngo_contact,
                "Location": ngo_location
            })

            ngo_screen.ids.ngo_name.text = ""
            ngo_screen.ids.ngo_contact.text = ""
            ngo_screen.ids.ngo_location.text = ""

            self.show_dialog("Success", "NGO registered successfully!")
            self.update_ngos()
            self.change_screen('home')
        else:
            self.show_dialog("Error", "Please fill out all fields!")

    def update_ngos(self):
        screen_manager = self.root.ids.screen_manager  
        ngo_list = screen_manager.get_screen('view_ngos').ids.ngo_list  

        ngo_list.clear_widgets()  

        for ngo in self.ngos:
            item_text = f"{ngo['NGO']} | Contact: {ngo['Contact']} | Location: {ngo['Location']}"
            ngo_list.add_widget(OneLineListItem(text=item_text))
    

    def show_dialog(self, title, text):
        if not hasattr(self, 'dialog'):
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: self.dialog.dismiss())]
            )
        else:
            self.dialog.title = title
            self.dialog.text = text
        self.dialog.open()

if __name__ == '__main__':
    FoodWasteApp().run()
