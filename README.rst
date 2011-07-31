a basic software package for hackerspaces and similiar organizations.

based on django and python, it allows you to

 * manage and announce events (basic calendaring)
 * manage members and their payments
 * publish information about current projects
 * have a nice-looking website, which allows easy access (and edit functionality) to all that information 


TODO
-------------------
 * migrate to Django 1.3
 * cleanup



Install
=======

#. Checkout hackerspace-os
    
   ``git clone git@github.com:fhahn/hackerspace-os.git``

#. Install Requirements

   ``pip install -r hackerspace-os/requirements.txt``


Setup
=====

#. Add your local settings (database,...)

   ``create hackerspace-os/hos/settings_local.py``

#. Sync database

   ``cd hackerspace-os/hos/``
   
   ``python manage.py syncdb``
