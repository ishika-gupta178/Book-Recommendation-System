from flask import Flask,request,jsonify, render_template
import numpy as np
import pandas as pd
import pickle
#import collections as c

idlist = pickle.load(open('idlist.pkl','rb'))
df2 = pickle.load(open('df2.pkl','rb'))
idlist_new = pickle.load(open('idlist_new.pkl','rb'))
dataset = pickle.load(open('dataset.pkl','rb'))
book_titles = pickle.load(open('book_titles.pkl','rb'))
app = Flask(__name__) #flask object
book_title_list = []
for x in book_titles:
    book_title_list.append(x)
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#import time driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
dataset["description"].fillna("No description available", inplace=True)
dataset.awards.replace(to_replace ="[]",value ="awards not available", inplace=True)

@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('index.html', book_titles=book_title_list)

@app.route('/bookRecom', methods=['GET','POST'])
def bookRecom(bookTitle):

    book_list=[]
    book_id=dataset[dataset['title']==bookTitle].index
    #book_id=new_data[new_data['title']==bookTitle].index
    book_id=book_id[0]
    for new in idlist_new[book_id]:
        
        #book_list.append(new_data.loc[new].title)

        book_list.append(dataset.loc[new].title)
        
    return book_list

@app.route('/predict', methods=['GET','POST'])
def predict():

    bookTitle = request.form.get("bookTitle")
    # book_titles = request.form.get('book_titles')

    # driver.implicitly_wait(0.5)
    # driver.get("http://127.0.0.1:5000/")
    # # identify dropdown
    # s = Select(driver.find_element_by_id("book_titles"))
    # #get selected item with method first_selected_option
    # bookTitle= s.first_selected_option
    # #text method for selected option text
    # print("Selected option is: "+ bookTitle.text)
    # driver.close()


    Book_names = bookRecom(bookTitle)
    # Book_names = bookRecom(request.form.get('book_titles'))
    result = Book_names
    #return render_template('index.html', prediction_text='book recommendations are :{}'.format(result))
    return render_template('index.html', prediction_text=result)

@app.route('/descPage')
def descPage():
    return render_template('description.html')

@app.route('/description', methods=['GET'])
def description():
    title = request.form.get("title")
    #bookID=dataset[dataset['title']==title].index
    book_id=new_data[new_data['title']==bookTitle].index
    bookID=bookID[0]
    #desc = dataset.loc[bookID].description
    desc = new_data.loc[bookID].description
    return render_template('description.html', description_text=desc)

    # desc = dataset.loc[book_id].description
    # return render_template('description.html', description_text=desc)
@app.route('/infoPage/<bookName>', methods=['GET'])
def infoPage(bookName):
    

    # bookID=new_data[new_data['title']==bookName].index
    # bookID=bookID[0]
    # desc = new_data.loc[bookID].description
    # author = new_data.loc[bookID].author
    # rating = new_data.loc[bookID].rating
    # awards = new_data.loc[bookID].awards

    bookID=dataset[dataset['title']==bookName].index
    bookID=bookID[0]
    desc = dataset.loc[bookID].description
    author = dataset.loc[bookID].author
    genres = dataset.loc[bookID].genres
    rating = dataset.loc[bookID].rating
    awards = dataset.loc[bookID].awards
    
    return render_template('description.html', title_text= bookName ,description_text=desc, author_text=author, genres_text=genres, rating_text=rating, awards_text=awards)

@app.route('/graphpage')
def graphpage():
    return render_template('graph.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/homepage')
def homepage():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html', book_titles=book_title_list)


if __name__ == '__main__':
    app.run(debug=True)
