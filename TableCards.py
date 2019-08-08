from fpdf import FPDF
from pprint import pprint
import os
from math import ceil
import  config

class TableCards:
    # 24 cards in the game
    # width : 32mm
    # height : 35mm
    # margin : 3mm
    # between image and text : 2mm
    # image height:20mm
    # image width: 25mm
    # text height:7mm
    def __init__(self, pdf ,files, names):
        self.pdf = pdf
        self.files = files
        self.names = names
        self.card_height = 35
        self.card_width = 32
        self.image_width = 26
        self.image_height = 20
        self.card_padding = 3
        self.blank_between_cards = 3
        self.blank_between_image_and_text = 2
        self.text_height = 7
        self.text_width = self.card_width - 2*self.card_padding
        self.nb_cards_by_line = 5


    def generate_page_recto(self):
        # https://pyfpdfbook.wordpress.com/2016/03/30/a-pdf-with-images-in-a-folder/
        # http: // www.fpdf.org / en / doc / image.htm
        # https://pyfpdf.readthedocs.io/en/latest/reference/image/index.html
        # https://pyfpdfbook.wordpress.com/2015/03/22/images-with-borders/


        self.pdf.add_page()

        index_current_card = 0

        while index_current_card < config.NB_CARDS:

            image_path = self.save_image(index_current_card)
            self.generate_card_recto(image_path, self.names.get('perso-'+str(index_current_card),'vide'),index_current_card)
            index_current_card = index_current_card + 1

        return self.pdf

    def save_image(self,index_current_card):
        image = self.files.get('file-' + str(index_current_card))
        # check if an image is present in files
        if image:
            # file upload : https://pythonise.com/feed/flask/flask-uploading-files
            # Split the extension from the filename
            ext = image.filename.rsplit(".", 1)[1]

            current_image_name = 'test-'+str(index_current_card)+'.'+ext
            image_storage_path = os.path.join(config.IMAGE_DIRECTORY, current_image_name)
            image.save(image_storage_path)
        else: #use default
            image_storage_path = config.DEFAULT_IMAGE_PATH
        return image_storage_path

    def generate_card_recto(self, my_image, my_text,index_current_card):
        shift_x = (index_current_card%self.nb_cards_by_line) * (self.blank_between_cards + self.card_width)
        #shift_y means a new line, we set 5 card by ine
        shift_y = ceil(index_current_card/self.nb_cards_by_line) * (self.blank_between_cards + self.card_height)

        #set x and y
        self.pdf.set_xy(config.PAGE_MARGIN + shift_x,config.PAGE_MARGIN + shift_y)

        #set card background
        self.pdf.set_fill_color(r=22, g=29, b=67)
        #draw card border
        self.pdf.cell(self.card_width, self.card_height, '', 1,0,'C',True)
        #add image

        try:
            self.pdf.image(my_image, config.PAGE_MARGIN + self.card_padding + shift_x, config.PAGE_MARGIN + self.card_padding +shift_y, w=self.image_width,
                  h=self.image_height)
            #draw image border
            self.pdf.set_xy(config.PAGE_MARGIN + self.card_padding + shift_x, config.PAGE_MARGIN + self.card_padding +shift_y)
            self.pdf.cell(self.image_width, self.image_height, '', 1, 0, 'C', fill=False)
        except:
            print('error with image')

        #add text under image
        self.pdf.set_xy(config.PAGE_MARGIN + self.card_padding + shift_x, config.PAGE_MARGIN + self.card_padding + self.image_height + self.blank_between_image_and_text + shift_y)

        # set car background
        self.pdf.set_fill_color(r=255, g=255, b=255)
        self.pdf.set_text_color(r=22, g=29, b=67)
        self.pdf.cell(self.text_width, self.text_height,my_text, 1,0,'C',True)




    def generate_page_verso(self):
        # https://pyfpdfbook.wordpress.com/2016/03/30/a-pdf-with-images-in-a-folder/
        # http: // www.fpdf.org / en / doc / image.htm
        # https://pyfpdf.readthedocs.io/en/latest/reference/image/index.html
        # https://pyfpdfbook.wordpress.com/2015/03/22/images-with-borders/


        self.pdf.add_page()

        self.pdf.set_fill_color(r= 65, g= 105,b= 225)

        index_current_card = 0

        while index_current_card < config.NB_CARDS:

            self.generate_card_verso(index_current_card)
            index_current_card = index_current_card + 1
        return self.pdf


    def generate_card_verso(self,index_current_card):
        #shift_x_for_verso is need for printer verso on large side
        shift_x_for_verso = 210 - (2*config.PAGE_MARGIN +self.nb_cards_by_line*self.card_width + (self.nb_cards_by_line-1)*self.blank_between_cards)

        shift_x = shift_x_for_verso + (index_current_card%self.nb_cards_by_line) * (self.blank_between_cards + self.card_width)
        #shift_y means a new line, we set 5 card by ine
        shift_y = ceil(index_current_card/self.nb_cards_by_line) * (self.blank_between_cards + self.card_height)

        #set x and y
        self.pdf.set_xy(config.PAGE_MARGIN + shift_x,config.PAGE_MARGIN + shift_y)

        #draw card border
        #self.pdf.cell(self.card_width, self.card_height, '', 1,0,'C',True)
        try:
            self.pdf.image(config.TABLE_CARD_VERSO, config.PAGE_MARGIN + shift_x, config.PAGE_MARGIN + shift_y, w=self.card_width,
                  h=self.card_height)
        except Exception as e:
            print(e)

            print('error with image')
