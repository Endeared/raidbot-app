import customtkinter
import tkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("ClanEye Client")
        self.iconbitmap('test_images\ClanEyeT.ico')
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ClanEyeT.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner.png")), size=(500, 150))
        self.banner2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner2.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "RaidEyeT.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "PracEyeT.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="ClanEye", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="RaidEye",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="PracEye",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")


        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="MANUAL RAID CHECK", corner_radius=5, font=('Calibri', 12))
        self.home_frame_button_1.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="ENABLE AUTO CHECK", corner_radius=5, font=('Calibri', 12))
        self.home_frame_button_2.grid(row=1, column=1, padx=90, pady=10, sticky="W")


        self.prac_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.prac_frame.grid_columnconfigure(0, weight=1)

        self.prac_frame_large_image_label = customtkinter.CTkLabel(self.prac_frame, text="", image=self.banner2)
        self.prac_frame_large_image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.prac_frame_button_1 = customtkinter.CTkButton(self.prac_frame, text="Manual raid check")
        self.prac_frame_button_1.grid(row=1, column=0, padx=10, pady=10, sticky="E")
        self.prac_frame_button_2 = customtkinter.CTkButton(self.prac_frame, text="Enable auto check")
        self.prac_frame_button_2.grid(row=1, column=1, padx=90, pady=10, sticky="W")


        self.select_frame_by_name("home")


    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "prac" else "transparent")

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "prac":
            self.prac_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.prac_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("prac")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()