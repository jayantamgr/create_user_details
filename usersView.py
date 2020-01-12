import re
import random
import string
import os
from datetime import datetime 

class AddUsers(object):

    def __init__(self):
        self.number_of_users = 0
        self.user_filename = 'user_details.txt'
        self.users_data = {}
        self.save_user_details = 'userDetails.txt'

    def clear_content(self):
        """Removes the details created for the previous users
        :return: None
        """
        open(self.save_user_details, 'w').close()

    def create_user_form_details(self, delimiter):
        """Creates the user data for each of the users to be filled in for creating the clients and appends it to a
        dictionary.
        :param delimiter: Choose the delimiter which separates the data in each line in the .csv file.
        :return: None
        """
        with open(self.user_filename, 'r') as user_file:
            for i, lines in enumerate(user_file):
                if i > 0:
                    if any(line.strip() for line in lines):
                        # if any(line.strip() for line in lines):
                        line_fields = lines.split(delimiter)
                        self.users_data[
                            ''.join([str(self.number_of_users), '_', line_fields[1], '_', line_fields[0]])] = [
                            line_fields[4].split('@')[0],
                            line_fields[0], line_fields[1], line_fields[4],
                            ''.join(['Firma', ' ', line_fields[1].upper(), ' ', line_fields[0].upper()]),
                            ''.join(
                                random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(8))]
                        self.number_of_users += 1

    def print_number_of_users(self):
        """Prints the number of users in the .csv file.
        :return: None
        """
        print("Number of users from this list are: ", self.number_of_users)

    def append_data(self, data):
        """Appends the created user details for each user into a .txt file.
        :param data: Which is to be appended.
        :return: None
        """
        file_name = open(self.save_user_details, 'a')
        file_name.write(data + '\n')
        file_name.close()

    def rearrange_data(self):
        """Arranges for each other user data according to the form and also appends the same into file.
        :return: None
        """
        for key, user_detail in self.users_data.items():
            mandaten_user = user_detail[0]
            email_user = user_detail[3]
            password_user = user_detail[5]
            vorname_user = user_detail[1]
            nachname_user = user_detail[2]
            name_der_firma_user = user_detail[4]
            #self.trace_login_data()
            self.append_data(mandaten_user + ';' + email_user + ';' + password_user + ';' + vorname_user + ';' + nachname_user + ';' + name_der_firma_user)

    
####### Main ########


add_user_object = AddUsers()


prompt = input('Do you want to clear content in the file ? : ')

if prompt == 'y' or prompt == 'Y':
    add_user_object.clear_content()
elif prompt == 'n' or prompt == 'N':
    pass
else:
    print("Bad input, you have only two options, either Y or N (case insensitive) \n \n Please try Again")

ask_for_delimiter = input('Please specify delimiter: HINT: it could be comma(,) or semicolon(;) : ')

block_separator = "\n##############################################\n"

add_user_object.create_user_form_details(ask_for_delimiter)

add_user_object.print_number_of_users()

add_user_object.rearrange_data()


####### End of Main #####


