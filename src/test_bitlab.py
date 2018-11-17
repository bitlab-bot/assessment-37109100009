from .bitlab import cleanup, help


def test_help():
    assert help() is None


def test_cleanup():
    assert cleanup('foo') == 'Error'
    with open('test.html', 'w+') as f:
        f.write('<test></test>')
    assert cleanup('foo') == 'Done'
