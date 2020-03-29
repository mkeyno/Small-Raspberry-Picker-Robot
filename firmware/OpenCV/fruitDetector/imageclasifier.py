#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
import cv2
import os
import numpy as np
from sys import exit as exit
from PIL import Image
Width=540
Height=500
WidthB=50
HeightB=50
# Get the folder containing the images from the user
folder = sg.PopupGetFolder('Image folder to open')
if folder is None:
    sg.PopupCancel('Cancelling')
    exit(0)

# get list of PNG files in folder
png_files = [folder + '\\' + f for f in os.listdir(folder) if '.png' in f]
filenames_only = [f for f in os.listdir(folder) if '.png' in f]
#print(png_files,'\n',filenames_only)
#['C:/Users/Mehrdad/Documents\\1.png', 'C:/Users/Mehrdad/Documents\\image.png']
# ['1.png', 'image.png']
if len(png_files) == 0:
    sg.Popup('No PNG images in folder')
    exit(0)

# resizedAnddrayImages=[]
# for file in png_files:
    # im=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    # im=cv2.resize(im ,(Width,Height))
    # resizedAnddrayImages.append(im)
    
mask_image_s = np.zeros((Height,Width), np.uint8)

def file2byteImage(file,type=1):
    if type:
        im=cv2.imread(file)
    else:
        im=cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    im=cv2.resize(im ,(Width,Height))
    img =cv2.imencode('.png', im)[1].tobytes()
    return img
    

#imgbytes = resizedAnddrayImages[0].tobytes() #144000 (360, 400)
imgbytes =cv2.imencode('.png', mask_image_s)[1].tobytes() #59807 (360, 400)
#imgbytes =Image.fromarray(resizedAnddrayImages[0])
#print(len(imgbytes),resizedAnddrayImages[0].shape)
#cv2.imshow('resizedAnddrayImages[0]',resizedAnddrayImages[0])

#-------------------------------------------------------------------------
menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About',]]]
col_files = [
              [sg.Listbox(values=filenames_only, size=(20,40), key='listbox')],
              [sg.Button('Read')]
            ]
col = [#window['image'](data=cv2.imencode('.png'   , template)[1].tobytes()          )
          [
              sg.T('Width:'), sg.In(size=(10, 10),default_text ='540',key='Width'),
              sg.T('Height:'), sg.In(size=(10, 10),default_text ='500',key='Height'),sg.ReadButton('Set Size'),
              sg.T('Width Box:'), sg.In(size=(10, 10),default_text ='50',key='WidthB'),
              sg.T('Height Box:'), sg.In(size=(10, 10),default_text ='50',key='HeightB'),sg.ReadButton('Set Box Size'),
              
           ],
          [
             sg.T('File Name:'),
             sg.Text(png_files[0], key='filename'),
             sg.T('Number of Object:'),
             sg.In(size=(10, 10),default_text ='0',key='NumOFD'),
             sg.ReadButton('Save Image'),
          ],
          [
            sg.Image(filename='',data=mask_image_s,  key='imageO'),
            #sg.Image(filename='',data=mask_image_s,  key='imageG'),
            sg.Graph(
            canvas_size=(Width, Height),
            graph_bottom_left=(0, 0),
            graph_top_right=(Width, Height),
            change_submits=True,
            drag_submits=False,
            key="graph"
        )
            ],
          #[sg.Text(png_files[0], size=(80, 3), key='filename')],
          #[sg.Image(filename='',data=Image.fromarray(mask_image_s, 'P'),  key='imagexx')],
          #[sg.Text('==================================================================', size=(80, 3) )],
          #[sg.Image(filename='',data= imgbytes , key='image')],          
          [sg.Button('Prev', size=(8,2)), sg.Button('Next', size=(8,2)),  sg.Text('File 1 of {}'.format(len(png_files)), size=(15,1), key='filenum')]
      ]
layout = [[sg.Menu(menu)], [sg.Column(col_files), sg.Column(col)]]
#-------------------------------------------------------------------------
window = sg.Window('Image Dtatset creator', 
                    return_keyboard_events=True, 
                    resizable=True,
                    #text_justification='c',
                    auto_size_text=True,
                    auto_size_buttons=True,
                    no_titlebar=False,
                    location=(0,0), 
                    use_default_focus=False 
                    ).Layout(layout)

# loop reading the user input and displaying image, filename
i=0
top_left=(0,0)
bottom_right=(50,50)
while True:

    event, values = window.Read()
    # --------------------- Button & Keyboard ---------------------
    if event is None:
        break
    elif event in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34') and i < len(png_files)-1:
        i += 1
        NumOFD=0
        window.FindElement('NumOFD').Update(NumOFD)
    elif event in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33') and i > 0:
        i -= 1
        NumOFD=0
        window.FindElement('NumOFD').Update(NumOFD)
    elif event == 'graph':
        mouse =values['graph']
        if mouse == (None, None):
            continue
        print(mouse)
        x = mouse[0]
        y = mouse[1]
        top_left=(x-WidthB,y-HeightB)
        bottom_right=(x+WidthB,y+HeightB)
        #letter_location = (box_x * 200 + 18, box_y * 200 + 17)
        #graph.DrawRectangle((200, 200), (250, 300), line_color="red")
        #DrawRectangle(top_left,bottom_right,       fill_color=None,        line_color=None,        line_width=None)
        #print(box_x, box_y)
        
    elif event == 'Set Size':
        #print(int(values['Width']),int(values['Height']))
        Width =int(values['Width'])
        Height=int(values['Height'])
        print(Width,Height)
    elif event == 'Set Box Size':
        #print(int(values['Width']),int(values['Height']))
        WidthB =int(values['WidthB'])
        HeightB=int(values['HeightB'])
        print(WidthB,HeightB)
        
    elif event == 'Exit':
        exit(69)

    filename = folder + '/' + values['listbox'][0] if event == 'Read' else png_files[i]
    print(event)

    # ----------------- Menu choices -----------------
    if event == 'Open Folder':
        newfolder = sg.PopupGetFolder('New folder', no_window=True)
        if newfolder is None:
            continue
        folder = newfolder
        png_files = [folder + '/' + f for f in os.listdir(folder) if '.png' in f]
        filenames_only = [f for f in os.listdir(folder) if '.png' in f]
        window.FindElement('listbox').Update(values=filenames_only)
        window.Refresh()
        i = 0
    elif event == 'About':
        sg.Popup('Image Dataset creator', 'github.com')

    # update window with new image
    window.FindElement('imageO').Update(data=file2byteImage(filename))
    #window.FindElement('imageG').Update(data=file2byteImage(filename,type=0))
    graph = window.Element("graph")
    graph.DrawImage(data=file2byteImage(filename,type=0), location=(0, Height))
    if event=='graph':
        graph.DrawRectangle(top_left,bottom_right,fill_color=None,line_color='red',line_width=5)
        NumOFD+=1
        window.FindElement('NumOFD').Update(NumOFD)
    
    #graph.DrawText('test', letter_location, font='Courier 25')
    # update window with filename
    window.FindElement('filename').Update(filename)
    # update page display
    window.FindElement('filenum').Update('File {} of {}'.format(i+1, len(png_files)))
#window['image'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
