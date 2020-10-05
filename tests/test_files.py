"""
test_files.py.

Operace se soubory.
"""
import os
import filecmp
import difflib
outfile = 'tests/output.txt'
expfile = 'tests/expected.txt'
'''
def teardown_function(function):
    """Uklidí na konci testu."""
    if os.path.exists('output.txt'):
        os.remove('output.txt')
'''
def test_file_output():
    """Otestuje vytvoření a zápis do souboru."""
    open(outfile, 'w').write('Hello World!')   # the code being tested
    assert os.path.exists(outfile)

def test_compare_files():
    """Porovná výstupní soubor (nejen jméno, ale i obsah souboru) se vzorovým souborem."""
    open(outfile,'w').write('Hello World!')      # zápis do souboru
    assert filecmp.cmp(outfile, expfile)

def test_compare_files2():
    """Porovná výstupní soubor (nejen jméno, ale i obsah souboru) se vzorovým souborem. Navíc vypíše rozdíly."""
    open(outfile,'w').write('Hello World!')      # zápis do souboru
    lines_result = open(outfile).readlines()
    lines_expected = open(expfile).readlines()
    print('\n'.join(difflib.ndiff(lines_result, lines_expected)))
    assert filecmp.cmp(outfile, expfile)
    
