from bitlab_assessment.bitlab import cleanup, help, RickAndMortyHtmlFile
import vcr



def test_help(capsys):
    assert help() is None
    out, err = capsys.readouterr()
    assert 'Virtualenv Setup:' in out
    assert '1. Ensure virtualenv' in out
    assert '2. Create a virtualenv' in out
    assert '. Activate the environment:' in out
    assert '- (optional) when' in out


def test_file_creation():
    with open('tests/data/results.html', 'r') as f:
        correct_results = f.read()
    test_file = './test_file.html'

    with vcr.use_cassette('fixtures/vcr_cassettes/rick_and_morty_episodes.yaml'):

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
