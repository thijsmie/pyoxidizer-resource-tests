import pkgutil
import pkg_resources
import importlib.resources


def test_pkgutil():
    try:
        print('pkgutil.get_data', pkgutil.get_data('resource_tests', 'test.txt').decode())
    except:
        print('pkgutil.get_data', 'FAILURE')


def test_pkg_resources():
    try:
        print('pkg_resources.resource_string', pkg_resources.resource_string('resource_tests', 'test.txt').decode())
    except:
        print('pkg_resources.resource_string', "FAILURE")


def test_importlib_resources():
    try:
        print('importlib.resources.open_text', importlib.resources.open_text('resource_tests', 'test.txt').read())
    except:
        print('importlib.resources.open_text', 'FAILURE')

    try:
        print('importlib.resources.files', importlib.resources.files('resource_tests').joinpath('test.txt').read_text())
    except:
        print('importlib.resources.files', 'FAILURE')

    try:
        print('importlib.resources.read_text', importlib.resources.read_text('resource_tests', 'test.txt'))
    except:
        print('importlib.resources.read_text', 'FAILURE')

    try:
        print('importlib.resources.read_binary', importlib.resources.read_binary('resource_tests', 'test.txt').decode())
    except:
        print('importlib.resources.read_binary', 'FAILURE')

    print('importlib.resources.contents', 'SUCCESS' if 'test.txt' in importlib.resources.contents('resource_tests') else 'FAILURE')


def test_subdir_pkgutil():
    try:
        print('pkgutil.get_data', pkgutil.get_data('resource_tests', 'subdir/test.txt').decode())
    except:
        print('pkgutil.get_data', 'FAILURE')


def test_subdir_pkg_resources():
    try:
        print('pkg_resources.resource_string', pkg_resources.resource_string('resource_tests', 'subdir/test.txt').decode())
    except:
        print('pkg_resources.resource_string', "FAILURE")


def test_subdir_importlib_resources():
    print('importlib.resources.open_text', 'CANT_USE')

    try:
        print('importlib.resources.files', importlib.resources.files('resource_tests').joinpath('subdir/test.txt').read_text())
    except:
        print('importlib.resources.files', 'FAILURE')

    print('importlib.resources.read_text', 'CANT_USE')

    print('importlib.resources.read_binary', 'CANT_USE')

    print('importlib.resources.contents', 'SUCCESS' if 'subdir/test.txt' in importlib.resources.contents('resource_tests') else 'FAILURE')



def test():
    print("Resource in main directory of module")
    test_pkgutil()
    test_pkg_resources()
    test_importlib_resources()
    print("Resource in subdirectory of module")
    test_subdir_pkgutil()
    test_subdir_pkg_resources()
    test_subdir_importlib_resources()

