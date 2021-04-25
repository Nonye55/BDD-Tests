"""
this  fill will be responsible for the strorage of urls,
passwords,username,element locators,and all string literals.
"""
# ++++++++++++++++++++++++++++++++++++#
#  For All urls
# ++++++++++++++++++++++++++++++++++++#

lamp_page = "https://lamp-frontend.herokuapp.com/"

# +++++++++++++++++++++++++++++++++++++#
# Landing page and login#
# +++++++++++++++++++++++++++++++++++++#

landing_login = "//div[@id='app']/div[@class='v-application--wrap']/div[2]/div[1]/header/div/div/div[@class='justify-lg-space-between']/div[@class='d-flex']/button[1]/span[@class='v-btn__content']"
email_field = "/html//div[@id='app']/div[@role='document']/div//form/span[1]/div//input[@placeholder='Email Address']"
login_email = "uka29c@gmail.com"
password_field = "/html//div[@id='app']/div[@role='document']/div//form/span[2]/div//input[@placeholder='Password']"
Login_password = "123pass321"
login_button = "//div[@id='app']/div[@role='document']//form/div[2]/button[@type='submit']/span[@class='v-btn__content']"

# +++++++++++++++++++++++++++++++++++++++#
# Invite Employee
# ++++++++++++++++++++++++++++++++++++++++#

Invite_Trainees = "//div[@id='app']//main[@class='v-main']/div/div/div/div[2]/div[1]/div[1]/div//div[@class='mt-2']/button[@role='button']/span/button[@type='button']"
Invite_Trainees_text = "Invite Trainees"
invite_button = "//div[@id='app']//main[@class='v-main']/div/div/div/div[2]/div[1]/div[1]/div//div[@class='mt-2']/button[@role='button']/span/button[@type='button']"
email_field2 = "//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div//input[@type='text']"
employees_email = "tennie@yopmail.com"
add_button = "//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div/div[1]/div[2]/button[@type='button']/span[@class='v-btn__content']"
send_invite_button = "//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div/div[3]/button[2]/span[@class='v-btn__content']"
close_button = "//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div/div[3]/button[2]/span[@class='v-btn__content']"

# add_employees_button = "/html//div[@id='app']/div[@role='document']/div/div/div/div/div[2]/div//input[@type='text']"


# +++++++++++++++++++++++++++++++++++++++++++++#
# Create group
# +++++++++++++++++++++++++++++++++++++++++++++++#

Trainees_tab = "/html//div[@id='app']//nav/div[@class='v-navigation-drawer__content']/div/div/div[@role='tablist']//div[@class='v-slide-group__content v-tabs-bar__content']/a[2]"
groups_tab = "//div[@id='app']//main[@class='v-main']/div/div/div/div[1]/div/div/div[@role='tablist']//div[@class='v-slide-group__content v-tabs-bar__content']/a[2]"
groups_tab_text = "Groups"
create_button = "/html//div[@id='app']//main[@class='v-main']/div/div/div/div[2]/div/div[1]/div[3]/button[@role='button']/span[@class='v-btn__content']"
group_field = "/html//div[@id='app']/div[@role='document']/div//div[@class='mx-16']/div[1]/div[@class='v-input__control']/div[@role='button']//div[@class='v-select__selections']"
others = "//div[@id='app']//div[@role='listbox']/div[1]//div[@class='v-list-item__title']"
groups_name_field = "/html//div[@id='app']/div[@role='document']/div/div//div[@class='v-text-field__slot']/input[@type='text']"
groups_name = "Umu-Nma"
assign_course_field = "/html//div[@id='app']/div[@role='document']/div//div[@class='mx-16']/div[3]/div[@class='v-input__control']/div[@role='button']//div[@class='v-select__selections']"
course_name = "//div[@id='app']/div[5]/div[@role='listbox']/div[1]//div[@class='v-list-item__title']"
create_group_button = "//div[@id='app']/div[@role='document']/div/div"

