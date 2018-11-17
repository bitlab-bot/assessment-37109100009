from bitlab_assessment.bitlab import cleanup, help, RickAndMortyHtmlFile


def test_help():
    assert help() is None


def test_file_creation():
    with open('tests/data/results.html', 'r') as f:
        correct_results = f.read()

    test_file = './test_file.html'

    try:
        RickAndMortyHtmlFile.create(test_file)
        with open(test_file, 'r') as f:
            created_contents = f.read()
        assert created_contents == correct_results
    finally:
        cleanup(test_file)
    

def test_cleanup():
    assert cleanup('foo') == 'Error'
    with open('test.html', 'w+') as f:
        f.write('<test></test>')
    assert cleanup('test.html') == 'Done'
