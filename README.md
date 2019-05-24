# Pyforms custom forms

The library offers the functionality to add dynamic extra fields to the Pyforms applications.


## Install & configure

Clone the repository
```python
> git clone git@github.com:fchampalimaud/pyforms-custom-forms.git
```

Install the library
```python
> pip install ./pyforms-custom-form
```

Add the app to the django settings.py
```python
INSTALLED_APPS = [
    ...
    'model_extra_fields',
    ...
]
```

Execute the django migrations
```shell
> python manage.py migrate model_extra_fields
```

## Usage

For this explanation we are going to use the next pyforms application as example.
This application is used to manage the django **Expense** model.

```python
from reimbursements.models import Expense
from pyforms_web.widgets.django import ModelFormWidget

class ExpenseForm(ModelFormWidget):

    MODEL = Expense
    
    FIELDSETS = [
        ('document_number', "requisition_number", 'is_social'),
        ' ',
        ('_costcenter', '_financeprj', 'expensecode'),
        ('eur_value', "value", "value_currency"),
        ' ',
        ('receipt_date', ' ', ' '),
        'receipt',
        ' ',
        'description'
    ]
```

To add extra custom fields to this application we should inherit it from **CustomModelForm**.
This class adds 2 fields, the **select_form** for the user to select the extra fields, 
and the **customized_form** used to render the extra fields.

```python
...
from model_extra_fields.widgets.custom_model_form import CustomModelForm

class ExpenseForm(CustomModelForm):
    ...
    
    FIELDSETS = [
        ...
        'select_form',
        'customized_form',
        ...
    ]
```

### Print screen examples

