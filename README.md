## djexp - Django Export

Application which exports Django models info to json, yaml and
xml file formats.
> WARNING: use this module on your own risk because of non-stable
> version.

### Installation
##### Using pip:
```bash
$ pip install djexp
```
> WARNING: this module has not been deployed yet.

##### Manual
```bash
# create and activate virtual environment (optional)
$ virtualenv -p python3 path/to/venv
$ source path/to/venv/bin/activate

# clone the repository
$ git clone https://github.com/Djangolify/djexp.git

# install djexp
$ cd djexp/
$ python setup.py install
```

### Requirements
- Django>=1.7
- PyYAML==4.2b4
- dicttoxml>=1.7.4

### Example
##### Djexp settings
```python
...

# setup ignorable models
DJEXP_IGNORE = {
    'MODELS': [
        'django.contrib.admin.models.LogEntry',
        'django.contrib.contenttypes.models.ContentType'
    ]
}
...
```
By default djexp ignores django's built-in models:
* `django.contrib.admin.models.LogEntry`
* `django.contrib.auth.models.Permission`
* `django.contrib.auth.models.Group`
* `django.contrib.contenttypes.models.ContentType`
* `django.contrib.sessions.models.Session`

Disable ignoring models:
```python
...

DJEXP_IGNORE = {
    'MODELS': []
}
...
```

The default export format is `json`. But `djexp` allows to set formats via
`DJEXP_FORMATS` project setting: 
```python
...

# setup export formats
DJEXP_FORMATS = [
    'yml',
    'xml'
]
...
```

##### Using as command line application:
```bash
# read usage
$ djexp -h

# export
$ djexp -r ./ -s ProjectName.settings --json
```

If you run the command without specifying format(s), djexp will use
them from `DJEXP_FORMATS` setting.

##### Using in Django project
Update `settings.py`:
```python
...

# add djexp to installed apps
INSTALLED_APPS = [
    ...
    'djexp.app'
]
...
```

Run the command from `djexp` application:
```bash
$ python manage.py project_info
```
This will create `django-project.json` (file format may vary
due to your choice) file with models' information in project
root directory.

### Authors
* [Orest Hopiak](https://github.com/OHopiak)
* [Yuriy Lisovskiy](https://github.com/YuriyLisovskiy)

### License
The project is licensed under the terms of the
[GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0),
see the [LICENSE](LICENSE) file for more information.
