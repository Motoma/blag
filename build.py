#!/usr/bin/env python
from config import *

import os
import sys
import time

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader(__name__, TEMPLATE_DIR))

t_about = env.get_template('about.html')
t_index = env.get_template('index.html')
t_post = env.get_template('post.html')

about = None
posts = {}
projects = []
tags = {}

def rmrf(path): os.system('rm -rf %s' % path)
def mkdirp(path): os.system('mkdir -p %s' % path)
def cp(src, dest): os.system('cp %s %s' % (src, dest))
def cpr(src, dest): os.system('cp -R %s %s' % (src, dest))

# round up division: 1/2=1 2/2=1 3/2=2
def cdiv(num, denom):
    if num % denom == 0: return num / denom
    else: return num / denom + 1

# Iterate over Python moduels in data directory and load them
sys.path.append('./%s' % (DATA_DIR))
modules = [mod[:-3] for mod in os.listdir(DATA_DIR) if mod[-3:] == '.py']
modules.sort()
for module in modules:
    if module == 'about':
        about = __import__(module)
        
    elif module[:4] == 'post':
        post = __import__(module)
        
        if hasattr(post, 'tags'):
            post.tags = [tag.strip() for tag in post.tags.split(',')]
            for tag in post.tags:
                tag = tag.lower()
                if not tags.has_key(tag):
                    tags[tag] = []
                tags[tag].insert(0, module)
                    
        posts[module] = post

    elif module[:7] == 'project':
        projects.insert(0, __import__(module))

    elif module[:5] == 'quote':
        quote = __import__(module)


# Build up globals
env.globals['about'] = about
env.globals['projects']=projects[:PROJECTS_ON_PAGE]
env.globals['year'] = time.strftime('%Y')
env.globals['quote'] = quote.text
        
# Begin rendering pages
rmrf(WWW_DIR)
mkdirp(WWW_DIR)
cpr(WWW_STATIC, WWW_DIR)
cp(WWW_ROOT_ASSETS, WWW_DIR)

# Render About page
mkdirp('%s/about' % (WWW_DIR))
fhandle = open('%s/about/index.html' % (WWW_DIR), 'wb')
fhandle.write(t_about.render().encode('utf-8'))
fhandle.close()

# Render individual posts
for post in posts.values():
    mkdirp('%s/%s' % (WWW_DIR, post.url))
    fhandle = open('%s/%s/index.html' % (WWW_DIR, post.url), 'wb')
    fhandle.write(t_post.render(post=post).encode('utf-8'))
    fhandle.close()

# Render index pages
rmrf('%s/index.html' % (WWW_DIR))
sorted_keys = sorted(posts, key=lambda x: posts[x].date, reverse=True)
last_index = cdiv(len(posts), ITEMS_PER_PAGE)
for i in range(last_index):
    rmrf('%s/%i' % (WWW_DIR, i))
    mkdirp('%s/%i' % (WWW_DIR, i))
    first = i * ITEMS_PER_PAGE
    last = first + ITEMS_PER_PAGE
    index_posts = [posts[post] for post in sorted_keys[first:last]]
    
    fhandle = open('%s/%i/index.html' % (WWW_DIR, i), 'wb')
    fhandle.write(t_index.render(posts=index_posts,
                                 current_page=i,
                                 last_page=last_index - 1).encode('utf-8'))
    fhandle.close()
cp('%s/0/index.html' % (WWW_DIR), '%s/index.html' % (WWW_DIR))
rmrf('%s/0/index.html' % (WWW_DIR))

# Render tag pages
rmrf('%s/tags' % (WWW_DIR))
mkdirp('%s/tags' % (WWW_DIR))
for tag, items in tags.items():
    tag = tag.replace(' ', '-')
    mkdirp('%s/tags/%s' % (WWW_DIR, tag))

    tag_posts = {}
    for item in items:
        tag_posts[item] = posts[item]

    sorted_keys = sorted(tag_posts, key=lambda x: tag_posts[x].date,
                         reverse=True)

    last_index = cdiv(len(sorted_keys), ITEMS_PER_PAGE)
    for i in range(last_index):
        rmrf('%s/tags/%s/%i' % (WWW_DIR, tag, i))
        mkdirp('%s/tags/%s/%i' % (WWW_DIR, tag, i))
        
        first = i * ITEMS_PER_PAGE
        last = first + ITEMS_PER_PAGE
        index_posts = [posts[post] for post in sorted_keys[first:last]]
        
        fhandle = open('%s/tags/%s/%i/index.html' % (WWW_DIR, tag, i), 'wb')
        fhandle.write(t_index.render(posts=index_posts,
                                     current_page=i,
                                     last_page=last_index - 1,
                                     tag_page=tag).encode('utf-8'))
        fhandle.close()
    cp('%s/tags/%s/0/index.html' % (WWW_DIR, tag),
       '%s/tags/%s/index.html' % (WWW_DIR, tag))
    rmrf('%s/tags/%s/0/' % (WWW_DIR, tag))
