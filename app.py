#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import Flask


# Добавление модели в админ-панель
# admin.add_view(ModelView(User, db.session))


app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Worl d!"
if __name__ == "__main__":
    app.run()
    
# admin = Admin(app, name='Admin', template_mode='bootstrap3')
# # Добавление модели в админ-панель
# admin.add_view(ModelView(User, db.session))


# In[6]:


# !pip install Flask-Admin


# In[5]:


# !pip install Flask-MySQL


# In[18]:


# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView

# admin = Admin(app, name='Admin', template_mode='bootstrap3')

# Добавление модели в админ-панель
# admin.add_view(ModelView(User, db.session))


# In[11]:


# !pip install --upgrade Flask


# In[ ]:




