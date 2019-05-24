# Pyforms custom forms

The library implements the functionality to add dynamic extra fields to the Pyforms Web
applications.

&nbsp;

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

### Forms configuration

The next steps demonstrates how to configure extra custom fields.

First select the application **Custom forms** on the user menu.

![Menu](https://raw.githubusercontent.com/fchampalimaud/pyforms-custom-forms/master/docs/images/user-menu.png)

Create the forms you need and associate them to a Content Type.\
These forms will be available when editing an object from the selected content type.

![Add custom form](https://raw.githubusercontent.com/fchampalimaud/pyforms-custom-forms/master/docs/images/add-custom-form.png)

The **Formset** field configures the organization of the configured extra fields, ala Pyforms.

![Edit the custom form](https://raw.githubusercontent.com/fchampalimaud/pyforms-custom-forms/master/docs/images/edit-custom-form.png)

To each custom form you can associate several fields from diferent types.\
These fields can be customized as it is show in the image bellow.

![Edit a field](https://raw.githubusercontent.com/fchampalimaud/pyforms-custom-forms/master/docs/images/edit-field.png)


### Result

First ExpenseForm app inherit from the ModelFormWidget class.

![ModelFormWidget](https://raw.githubusercontent.com/fchampalimaud/pyforms-custom-forms/master/docs/images/model_form_widget.png)


Second ExpenseForm app inherit from the CustomModelForm class.
On this app it is possible to visualise the [Extra information] control which allow the user to select the form with the extra fields he wiches to complete.

![CustomModelForm](https://raw.githubusercontent.com/fchampalimaud/pyforms-custom-forms/master/docs/images/custom_model_form.png)

&nbsp;

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