import os
import openai
import requests
from fpdf import FPDF
import fpdf as pdf
from fpdf import Template
import aspose.words as aw
from twilio.rest import Client
import pyshorteners

def make_pdf():
    api_key = "tkn"
    openai.api_key = api_key

    def generate_and_save_images(save_folder_name, prompt, num_images=4, size="1024x1024"):
        """
        generate and save images into a specified folder. Images
        are generated with the specified primpt
        """
        
        generations = openai.Image.create(
            prompt=prompt,
            n=num_images,
            size=size,
        )
        
        urls = []
        for generation in generations['data']:
            urls.append(generation['url'])
        
        os.mkdir(save_folder_name)
        paths = []
        for index, url in enumerate(urls):
            image = requests.get(url)
            path = os.path.join(save_folder_name, str(index) + '.png')
            paths.append(path)
            with open(path, 'wb') as f:
                f.write(image.content)
        return paths
            
        
    def generate_news_article(info):
        """
        take in a promt as input, and return the generated text.
        The return format is as a dictionary with entries 
        full_text: full text that was generated,
        split_text: list, where each index is one paragraph of the full article
        title: generated title of the article
        """
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt="write a detailed an emotionally charged news article about the following info. Make sure to use lots of star wars references. " + info,
                temperature=0,
                max_tokens=2000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
                )
        full_text = response['choices'][0]['text']
        split_text = full_text.split('\n\n')
        
        while('' in split_text):
            split_text.remove('')
            
        title_response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"generate a short title for the following news article: {full_text}",
                temperature=0,
                max_tokens=100,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
                )
        title = title_response['choices'][0]['text'].strip()
        
        
        image_prompt = title_response['choices'][0]['text']
        
        return {'full_text': full_text,
                'split_text': split_text,
                'title':title,
                'image_prompt': image_prompt
            }

    def generate_pdf_fom_images_and_text(title, text_list, image_paths, pdf_path=None):
        """
        generate a pdf that is a news article from a specified title,
        a lits of paragaphs, and a list of images.
        save the pdf to a specified path
        """
        doc = aw.Document()
    # sectionToAdd = aw.Section(doc)
    # section = doc.sections.add(sectionToAdd)
    # page_setup = section.page_setup
    # page_setup.top_margin = aw.ConvertUtil.inch_to_point(1)
    #  page_setup.bottom_margin = aw.ConvertUtil.inch_to_point(1)
    # page_setup.left_margin = aw.ConvertUtil.inch_to_point(0.75)
    # page_setup.right_margin = aw.ConvertUtil.inch_to_point(0.75)
    # page_setup.orientation = aw.Orientation.LANDSCAPE
    # page_setup.text_columns.set_count(3)
        # pdf.set_fill_color(0, 0, 0)
        # pdf.set_text_color(225, 225, 225)

        # pdf.rect(x = 0, y = 0, w = 9_999, h = 9_999, style = 'DF')


        builder = aw.DocumentBuilder(doc)
        
        
        
        
        builder.writeln("")
        builder.bold = True
        builder.font.size = 24
        builder.write(title)
        builder.bold = False
        builder.font.size = 12
        builder.writeln("  |  April 2nd, 2023")


        
        for i in range(len(text_list)):
            if(i!=0):
                builder.insert_break(aw.BreakType.COLUMN_BREAK)
            builder.font.size = 18
            builder.bold = True
            builder.write("Section " + str(i+1))
            builder.insert_paragraph()
            builder.font.size = 12
            builder.bold = False
            builder.write(text_list[i])
            builder.insert_break(aw.BreakType.LINE_BREAK)
            builder.insert_image(image_paths[i])
            builder.insert_paragraph()
        

        doc.save(pdf_path)

    def make_pdf_from_info(prompt, path):
        news_article = generate_news_article(prompt)
        
        paths = generate_and_save_images(path, " ' hyper realistic ' " + news_article['image_prompt'], num_images = len(news_article['split_text']))
        generate_pdf_fom_images_and_text(news_article['title'], news_article['split_text'], paths, path + '.pdf')

    import random


    # listOfTopics = [" #star wars# Rebellion forces make daring raid on Imperial research facility on planet Ilum - In this story, rebel forces have attacked an Imperial research facility on the frozen planet of Ilum, stealing valuable information and sabotaging key equipment.",

    #     "#star wars# Jedi Council announces new initiative to train young Force-sensitive children - The Jedi Council has announced a new initiative to identify and train young children who show signs of Force sensitivity, with the goal of rebuilding the Jedi Order.",

    #     "#star wars# Smuggler's Guild denies involvement in spice smuggling ring busted by Coruscant authorities - The Smuggler's Guild has issued a statement denying any involvement in a large-scale spice smuggling operation that was recently busted by Coruscant authorities.",

    #     "#star wars# Separatist forces attack Republic outpost on remote planet - Separatist forces have attacked a Republic outpost on a remote planet, sparking a fierce battle that has left many dead or injured on both sides.",

    #     "#star wars# Mandalorian bounty hunter captures notorious gang leader on planet Tatooine - A Mandalorian bounty hunter has captured a notorious gang leader on the desert planet of Tatooine, collecting a substantial bounty in the process.",


    #     "#star wars# Imperial stormtroopers clash with rebel fighters in space battle above planet Dantooine - A space battle has erupted above the planet Dantooine, as Imperial stormtroopers engage in combat with rebel fighters in a bid to gain control of the planet.",

    #     "#star wars# Jedi Master to lead diplomatic mission to negotiate peace treaty between warring factions on planet Onderon - A Jedi Master has been chosen to lead a diplomatic mission to the war-torn planet of Onderon, in an attempt to negotiate a lasting peace between rival factions.",

    #     "#star wars# Massive creature spotted in the depths of the oceans of Mon Calamari - Reports are emerging of a massive, previously unknown creature that has been sighted in the depths of the oceans surrounding the planet Mon Calamari.",

    #     "#star wars# Sith Lord rumored to have acquired ancient artifact of immense power - Rumors are circulating that a powerful Sith Lord has acquired an ancient artifact of immense power, and is using it to increase their strength and influence in the galaxy."]

    index = len(os.listdir())

    generated_prompt = title_response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"#star wars# generate a short summary of a battle between the evil galactic empire and the heroic rebelion. Include details like the location, the kind of fight (space fight, lightsaber battle, shootout, etc), and which important people were there",
                temperature=0.8,
                max_tokens=100,
                frequency_penalty=0.0,
                presence_penalty=0.0
                )
    gp = generated_prompt['choices'][0]['text']

    # make_pdf_from_info(listOfTopics[random.randint(0,len(listOfTopics)-1)], str(index))
    make_pdf_from_info(gp, str(index))

    return index


def send_mms(url):
    account_sid = "tkn"
    auth_token = "tkn"
    client = Client(account_sid, auth_token)
    long_url = url
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    msg = "The newest edition of our newletter is out check it out on our Galaxy-box!"
    #msg = "helloworld"
    message = client.messages \
        .create(
            body= msg,
            from_="+18446510644",
            to="+19187101434"
    )
    print(message.sid)

from aifc import Error
import sys
import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Access token
TOKEN = 'tkn'

# LOCALFILE = '/home/nima-n/Documents/code/codez/Hacklahoma Project/Python Attempt/t.pdf'
# BACKUPPATH = '/Star-News-Express.pdf' # Keep the forward slash before destination filename


# Uploads contents of LOCALFILE to Dropbox
def backup(dbx, localfile, backup_path):
    with open(localfile, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + localfile + " to Dropbox as " + backup_path + "...")
        try:
            dbx.files_upload(f.read(), backup_path, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


# Adding few functions to check file details
def checkFileDetails(dbx):
    print("Checking file details")

    for entry in dbx.files_list_folder('').entries:
        print("File list is : ")
        print(entry.name)


# Run this script independently
def dropbox_upload(index):
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    try:
        checkFileDetails(dbx)
    except Error as err:
        sys.exit("Error while checking file details")

    print("Creating backup...")
    # Create a backup of the current settings file
    main_dir = r"C:\Users\noaha\OneDrive - University of Oklahoma\Spring 2023\Hacklahoma\Hacklahoma Project" 
    file_path = os.path.join(main_dir, str(index) + ".pdf")
    backup_path = "/Star-News-Express" + str(index) + ".pdf"

    backup(dbx, file_path, backup_path)
    result = dbx.files_get_temporary_link(backup_path)
    send_mms(result.link)
    #print (result.link)
    print("Done!")

