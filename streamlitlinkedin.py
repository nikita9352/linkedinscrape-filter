# from msilib.schema import Font
import streamlit as st
import requests
import pandas as pd
import numpy as np 
# from bs4 import BeautifulSoup as bs
import re 
import contextlib
import time
from st_aggrid import AgGrid,JsCode, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
# from IPython.core.display import display, HTML
from IPython.display import display, HTML
from some.short import start_linkedin, search_job, save_the_jobs,dataframe_editor,browser #make_clickable
# HEroku deployment unseccessful
import time



browser.get("https://www.linkedin.com/")
print(browser.page_source)


# st.set_page_config(layout="wide")
# email = 'emrebasarr_@hotmail.com'
# password = 'linkedin19944'  

# st.title('Linkedin Job Scraper And Enhanced Filtering APP')

# with open('some/description.txt','r') as f:
#     st.write(f'{f.read()}')
# st.markdown("<h1>Search For Job Title and Location</h2>", unsafe_allow_html=True)
# # radial-gradient(circle, transparent 5%, #EEE8E8 5%)
# st.markdown(
#     """
# <style>
# .stMarkdown {
#     border-radius: 25px;
#     border-right:220px solid #EEE8E8 ;
#     border-top-right-radius: 100px !important;
#     border-bottom-right-radius: 100px;
#     border-left:240px solid #EEE8E8  ;
#     border-top-left-radius: 3px;
    
#     padding: 180px, 180px, 10px, 10px;
    
#     text-align: center;
#     background-color: #EF5B20;
# }


# </style>
# """,
#     unsafe_allow_html=True,
# )
# #style= 'border-right:50px solid #EEE8E8;border-left:50px solid #EEE8E8;'
# # with open('/style/style.css', 'r') as f:
# #     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# col1, col2 = st.columns([1, 1]) 
# search_tag = col1.text_input('', help='Enter the search string and skip the location do not enter or tab',placeholder='Enter the desired job')
# position = search_tag.replace(' ', "%20")

# location_tag = col2.text_input('', help='Enter the location and hit Enter/Return',placeholder='Enter the location')
# location_tag = location_tag.replace(' ', "%20")


# @st.cache
# def linkedin_complete(username,password):
#     start_linkedin(username,password)
#     results = search_job(position,location_tag)

#     return  save_the_jobs(results)


# # def searchbutton():

# #     if st.button('Search'):

# #         dataframe = linkedin_complete(email,password)
# #         return dataframe
#     # time.sleep(5)
# columnss = ['position name',
#         'workplace',
#         'number of employees',
#         'location',
#         'company name',
#         'working salary info',
#         'number of applicants',
#         'ad time',
#         'hiring status',
#         'corresponds name',
#         'connection is able',
#         'ad language',
#         'job link',
#         'easy apply']

        
# but = st.checkbox('Search Jobs',help='To see result check the box')
# st.write('if Search Jobs checked you will see the table otherways it will be blank table!')
# if but:
#     dataframe = linkedin_complete(email,password)
# else:
#     dataframe = pd.DataFrame(np.zeros((2, len(columnss))),columns= columnss)


# @st.cache
# def dataframe_finalizer(df):
#     zp = pd.DataFrame(df)
#     #  edit dataframe zp and ad education info, work experience info(senior junior)



#     z = zp.filter(columnss)

#     return dataframe_editor(z)

# z = dataframe_finalizer(dataframe)


# language = sorted(z['ad language'].unique())
# selected_language = st.sidebar.multiselect('Select the language', language, language)
# language_selected_z = z[z['ad language'].isin(selected_language)]

# try:
#     workplace = sorted(z['workplace'].unique())
# except:
#     workplace = []
# selected_workplace = st.sidebar.multiselect('Select the workplace', workplace, workplace)
# languge_workplace_selected_z = language_selected_z[language_selected_z['workplace'].isin(selected_workplace)]


# max = z['number of applicants'].max() if z['number of applicants'].max() >0 else 1
# Number_of_applications = st.sidebar.slider('Applicants ', help='setted number represenents smaller number of applicants',min_value=int(z['number of applicants'].min()), max_value=int(max), value = int(z['number of applicants'].max()))
# selected_zzz = languge_workplace_selected_z[languge_workplace_selected_z['number of applicants'] <= Number_of_applications]

# try:
#     hiring_s = selected_zzz['hiring status'].unique()
# except:
#     hiring_s = []


# hiring = st.sidebar.multiselect('Hiring Status',hiring_s,hiring_s)
# # hiring = str(hiring)


# selected_zzzz = selected_zzz[selected_zzz['hiring status'].isin(hiring)]

# easy_apply = str(st.checkbox('Easy Apply',value=False,help='Check the box and click the nested button to apply the job'))
# # activate the easy apply button if the checkbox is checked and easy apply button provide to apply the job
# if easy_apply == 'True':
#     st.button('Easy Apply',help='Apply now!')
# selected_zzzzz = selected_zzzz[selected_zzzz['easy apply'] == easy_apply]


# # this is working for streamlit but i need to work it for aggrid also
# # selected_zzzzz['job link'] = selected_zzzzz['job link'].apply(make_clickable)
# # st.write(selected_zzzzz.to_html(escape=False, index=False), unsafe_allow_html=True)


# st.header('Job Search Results',)


# # Grid options

# gd = GridOptionsBuilder.from_dataframe(selected_zzzzz)

# gd.configure_default_column(editable=False, groupable=True, sortable=True)



# # gd.configure_column('job link',cellRenderer=JsCode('''function(df['job link']){
# #         return '<a href="' + params.value + '" target="_blank">' + click the link + '</a>';))}'''))
# # gd.configure_column(selected_zzzz["job link"],
# #                             headerName="Link",
# #                             cellRenderer=JsCode('''function(params) {return '<a href=params>click the lins</a>'}'''),
# #                             width=300)

# gridoptions = gd.build()
# #still working on nested grids, hide columns and rows
# # column_defs = [{'headername':c,'field': c} for c in selected_zzzzz.columns]
# # grid_options = {
# #     'columndefs':column_defs,
# #     'enableSorting': True,
# #     'enableFilter': True,
# #     'enableColResize': True,
# #     'enableRangeSelection': True,
# #     'rowSelection': 'multiple',
# # }


# gd.configure_pagination()
# gd.configure_side_bar()
# grid_table = AgGrid(selected_zzzzz, gridoptions,
#                     enable_enterprise_modules=True,
#                     update_mode = GridUpdateMode.SELECTION_CHANGED,
#                     height = '500px',
#                     position = 'fixed',
#                     allow_unsafe_jscode=True,
#                     theme = 'streamlit',
#                     )
