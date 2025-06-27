import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from clean_emails import clean_email

def test_clean_email_simple():
    assert clean_email('contact@example.com') == 'contact@example.com'

def test_clean_email_prefix_suffix():
    assert clean_email('02.33contact@example.comNos') == 'contact@example.com'

def test_clean_email_hyphen():
    assert clean_email('03info@my-domain.frDu') == 'info@my-domain.fr'

def test_clean_email_complex():
    assert clean_email('Etigny03.86.97.10.45contact@pyrrhus.fr') == 'contact@pyrrhus.fr'
