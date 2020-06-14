"""
test_files.py.

Operace se soubory.
"""
import os
import filecmp
import difflib

def teardown_function(function):
    """Uklidí na konci testu."""
    if os.path.exists('output.txt'):
        os.remove('output.txt')

def test_file_output():
    """Otestuje vytvoření a zápis do souboru."""
    open('output.txt', 'w').write('Hello World!')   # the code being tested
    assert os.path.exists('output.txt')

def test_compare_files():
    """Porovná výstupní soubor (nejen jméno, ale i obsah souboru) se vzorovým souborem."""
    open('output.txt','w').write('Hello World!')      # zápis do souboru
    assert filecmp.cmp('output.txt', 'expected.txt')

def test_compare_files2():
    """Porovná výstupní soubor (nejen jméno, ale i obsah souboru) se vzorovým souborem. Navíc vypíše rozdíly."""
    open('output.txt','w').write('Hello World!')      # zápis do souboru
    lines_result = open('output.txt').readlines()
    lines_expected = open('expected.txt').readlines()
    print('\n'.join(difflib.ndiff(lines_result, lines_expected)))
    assert filecmp.cmp('output.txt', 'expected.txt')
    
