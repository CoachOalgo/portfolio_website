File Structure
- var/www/jonahorlovsky.com
    |- index.html (basic portfolio site)
    |- dag_vis.html (html for the line_logic django app)
    |- line_logic.sock (sock file for line_logic app)
    |- manage.py (manage file for the line_logic app)
    |- db.sqlite3 (database for the line_logic app)
    |- README.md
    |- line_logic (directory)
        |- __init__.py (empty)
        |- asgi.py
        |- settings.py
        |- urls.py
        |- wsgi.py
        |__pycache__ (directory)
    |- line_logic_app (directory)
        |- __init__.py (empty)
        |- admin.py
        |- apps.py
        |- forms.py
        |- models.py
        |- tests.py
        |- urls.py
        |- views.py
        |- __pycache__ (directory)
        |- migrations (directory)
            |- __init__.py
            |- 0001_initial.py
    |- media (directory)
    |- staticfiles (directory)
        |- css (directory)
        |- img (directory)
        |- js (directory)
    |- venv (directory)
        |- bin (directory)
        |- include (directory)
        |- lib (directory)
        |- lib64 (directory)
        |- pyenv.cfg


File Contents
var/www/jonahorlovsky.com
    |- index.html (basic portfolio site)
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Jonah Orlovsky - Portfolio</title>

	<style>
		body {
			font-family: Arial, sans-serif;
			line-height: 1.6;
			max-width: 800px;
			margin: 0 auto;
			padding: 20px;
			color: #333;
		}
		header {
			text-align: center;
			margin-bottom: 40px;
		}
		h1 {
			color: #2c3e50;
		}
		section {
			margin-bottom: 40px;
		}
		.about {
			margin-bottom: 20px;
			padding-bottom: 20px;
			border-bottom: 1px solid #eee;
		}
		.project {
			margin-bottom: 20px;
			padding-bottom: 20px;
			border-bottom: 1px solid #eee;
		}
		.contact {
			margin-bottom: 20px;
			padding-bottom: 20px;
			border-bottom: 1px solid #eee;
		}
	</style>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
	<header>
		<h1>Jonah Orlovsky</h1>
		<p>AI/ML Engineer | Researcher | Rowing Coach</p>
		<p>Cognitive Space | Ex-Boeing</p>
	</header>

	<section id="about">
		<h2>About Me</h2>
		<div class="about">
			<p>Hello! I'm Jonah, I'm just a guy who likes to read research paper and implement them in code, I love rowing, and I just like to go outside!</p>
			<p>
				Professionaly, I would consider myself a data scientist with a deep fascination with dynamic systems.
				I have a track record of solving complex engineering problems with novel methods.
				I excel at developing and implementing innovative solutions that drive efficiency and optimize operations.
			</p>
		</div>
	</section>

	<section id="projects">
		<h2>My Projects</h2>
		<div class="project">
			<h3>Line-Logic</h3>
			<p>RL-Based Production Line Resource Allocation Optimization</p>
		</div>
	</section>
	
	<section id="contact">
		<h2>Let's talk!</h2>
		<div class="contact">
			<h3>Contact Info</h3>
			<ul>
				<li>Email: Jonah.Orlovsky@gmail.com</li>
				<li>Phone: (206) 670-7650</li>
			</ul>

			<h3>Socials</h3>
			<ul>
				<li><a href="https://www.linkedin.com/in/jonah-orlovsky-32903a164/"><i class="fab fa-linkedin"></i>LinkedIn</a></li>
			</ul>

			<h3>Development</h3>
			<ul>
				<li><a href="https://github.com/CoachOalgo"><i class="fab fa-github"></i>Github</a></li>
			</ul>
		</div>
	</section>

	<footer>
		<p>&copy; 2025 Jonah Orlovsky. All rights reserved.</p>
	</footer>
</body>
</html>

- var/www/jonahorlovsky.com
    |- dag_vis.html (html for the line_logic django app)
<!-- dag_app/templates/dag_app/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DAG Visualizer</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    {% block extra_head %}{% endblock %}
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'home' %}">DAG Visualizer</a>
        </div>
    </nav>
    
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_scripts %}{% endblock %}
</body>
</html>

<!-- dag_app/templates/dag_app/home.html -->
{% extends 'dag_app/base.html' %}

{% block content %}
<div class="row">
    <div class="col-md-6 offset-md-3">
        <div class="card">
            <div class="card-header">
                <h3>Upload DAG Data</h3>
            </div>
            <div class="card-body">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="{{ form.title.id_for_label }}" class="form-label">Title</label>
                        {{ form.title }}
                    </div>
                    <div class="mb-3">
                        <label for="{{ form.description.id_for_label }}" class="form-label">Description (Optional)</label>
                        {{ form.description }}
                    </div>
                    <div class="mb-3">
                        <label for="{{ form.csv_file.id_for_label }}" class="form-label">CSV File</label>
                        {{ form.csv_file }}
                        <div class="form-text">CSV should have columns: source, target, average, standard_deviation, resource_type</div>
                    </div>
                    <button type="submit" class="btn btn-primary">Upload & Visualize</button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}

<!-- dag_app/templates/dag_app/visualize.html -->
{% extends 'dag_app/base.html' %}

{% block extra_head %}
<link href="https://cdn.jsdelivr.net/npm/vis-network@9.1.2/dist/dist/vis-network.min.css" rel="stylesheet">
<style>
    #network {
        width: 100%;
        height: 600px;
        border: 1px solid #ddd;
    }
    .card-body {
        overflow: auto;
    }
</style>
{% endblock %}

{% block content %}
<div class="row">
    <div class="col-12">
        <h2>{{ dag_data.title }}</h2>
        {% if dag_data.description %}
            <p>{{ dag_data.description }}</p>
        {% endif %}
    </div>
</div>

<div class="row mt-3">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h4>DAG Visualization</h4>
            </div>
            <div class="card-body">
                <div id="network"></div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_scripts %}
<script src="https://cdn.jsdelivr.net/npm/vis-network@9.1.2/dist/dist/vis-network.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Fetch the graph data
        fetch('/dag/api/graph/{{ dag_data.id }}/')
            .then(response => response.json())
            .then(data => {
                // Create a network visualization
                const container = document.getElementById('network');
                
                const options = {
                    nodes: {
                        shape: 'box',
                        font: {
                            size: 16
                        },
                        borderWidth: 2
                    },
                    edges: {
                        width: 2,
                        arrows: {
                            to: { enabled: true, scaleFactor: 1 }
                        },
                        font: {
                            size: 12
                        }
                    },
                    physics: {
                        stabilization: true,
                        hierarchicalRepulsion: {
                            nodeDistance: 150
                        }
                    },
                    layout: {
                        hierarchical: {
                            direction: 'LR',
                            sortMethod: 'directed'
                        }
                    }
                };
                
                const network = new vis.Network(container, data, options);
                
                // Add event listeners for interaction
                network.on('click', function(params) {
                    if (params.nodes.length > 0) {
                        console.log('Node clicked:', params.nodes[0]);
                    } else if (params.edges.length > 0) {
                        console.log('Edge clicked:', params.edges[0]);
                    }
                });
            })
            .catch(error => console.error('Error fetching graph data:', error));
    });
</script>
{% endblock %}

- var/www/jonahorlovsky.com
    |- manage.py (manage file for the line_logic app)
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'line_logic.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

- var/www/jonahorlovsky.com
    |- line_logic (directory)
        |- asgi.py
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'line_logic.settings')

application = get_asgi_application()

- var/www/jonahorlovsky.com
    |- line_logic (directory)
        |- settings.py
# line_logic/settings.py
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-change-this-key-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['jonahorlovsky.com', 'www.jonahorlovsky.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'line_logic_app',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'line_logic.urls'

# line_logic/settings.py - Update TEMPLATES section
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '')],  # Look in the project root for templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'line_logic.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/jonahorlovsky.com/staticfiles/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

- var/www/jonahorlovsky.com
    |- line_logic (directory)
        |- urls.py
# line_logic/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('line_logic/', include('line_logic_app.urls')),
]

# Add this at the bottom to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

- var/www/jonahorlovsky.com
    |- line_logic (directory)
        |- wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'line_logic.settings')

application = get_wsgi_application()

- var/www/jonahorlovsky.com
    |- line_logic_app (directory)
        |- admin.py
from django.contrib import admin

# Register your models here.

- var/www/jonahorlovsky.com
    |- line_logic_app (directory)
        |- apps.py
from django.apps import AppConfig


class LineLogicAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'line_logic_app'

- var/www/jonahorlovsky.com
    |- line_logic_app (directory)
        |- forms.py
from django import forms
from .models import DagData

class DagDataForm(forms.ModelForm):
    class Meta:
        model = DagData
        fields = ['title', 'description', 'csv_file']

- var/www/jonahorlovsky.com
    |- line_logic_app (directory)
        |- models.py
from django.db import models

# Create your models here.
class DagData(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank = True, null = True)
    csv_file = models.FileField(upload_to='dag_data/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

- var/www/jonahorlovsky.com
    |- line_logic_app (directory)
        |- tests.py
from django.test import TestCase

# Create your tests here.

- var/www/jonahorlovsky.com
    |- line_logic_app (directory)
        |- urls.py
# line_logic_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visualize/<int:pk>/', views.visualize, name='visualize'),
    path('api/graph/<int:pk>/', views.get_graph_data, name='get_graph_data'),
]

- var/www/jonahorlovsky.com
    |- line_logic_app (directory)
        |- views.py
import json
import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DagData
from .forms import DagDataForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DagDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('visualize', pk=form.instance.pk)
    else:
        form = DagDataForm()

    return render(request, 'line_logic_app/home.html', {'form': form})

# line_logic_app/views.py - Adjust template path
def visualize(request, pk):
    dag_data = DagData.objects.get(pk=pk)
    return render(request, 'dag_vis.html', {'dag_data': dag_data})

@csrf_exempt
def get_graph_data(request, pk):
    dag_data = DagData.objects.get(pk=pk)
    file_path = dag_data.csv_file.path
    df = pd.read_csv(file_path)

    nodes = set()
    for _, row in df.iterrows():
        nodes.add(row['source'])
        nodes.add(row['target'])
    
    node_list = [{"id": node, "label": node} for node in nodes]

    edges_list = []
    for _, row in df.iterrows():
        edges_list.append({
            "from": row['source'],
            "to": row['target'],
            "label": f"Avg: {row['average']}\nStd: {row['standard_deviation']}",
            "title": f"Type: {row['resource_type']}",
            "value": float(row['average'])
        })

    graph_data = {
        "nodes": node_list,
        "edges": edges_list
    }
    return JsonResponse(graph_data)

Configurations Files
- /etc/systemd/system/
    |- gunicorn_line_logic.service
[Unit]
Description=Gunicorn daemon for Line Logic Visualizer
After=network.target

[Service]
User=jonah-orlovsky
Group=www-data
WorkingDirectory=/var/www/jonahorlovsky.com
ExecStart=/var/www/jonahorlovsky.com/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/jonahorlovsky.com/line_logic.sock --chdir=/var/www/jonahorlovsky.com line_logic.wsgi:application

[Install]
WantedBy=multi-user.target

- /etc/nginx/sites-available/
    |- jonahorlovsky.com
 HTTPS server block
server {
    root /var/www/jonahorlovsky.com;
    index index.html;
    server_name jonahorlovsky.com www.jonahorlovsky.com;

    # Django application for Line Logic
    location /line_logic/ {
        include proxy_params;
        proxy_pass http://unix:/var/www/jonahorlovsky.com/line_logic.sock;
    }

    # Static files for Line Logic
    location /static/ {
        alias /var/www/jonahorlovsky.com/staticfiles/;
    }

    # Media files for Line Logic
    location /media/ {
        alias /var/www/jonahorlovsky.com/media/;
    }

    # Your original portfolio site
    location / {
        try_files $uri $uri/ =404;
    }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/jonahorlovsky.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/jonahorlovsky.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

# HTTP to HTTPS redirect (keep this as is - managed by Certbot)
server {
    if ($host = www.jonahorlovsky.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
    if ($host = jonahorlovsky.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot
    listen 80;
    listen [::]:80;
    server_name jonahorlovsky.com www.jonahorlovsky.com;
    return 404; # managed by Certbot
}