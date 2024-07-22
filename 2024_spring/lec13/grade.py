import unittest, pathlib, json
from contextlib import contextmanager,redirect_stderr,redirect_stdout
from os import devnull

@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)


# TestSequence
class Test(unittest.TestCase):
    def import_homework13(self):
        try:
            import homework13
            self.homework13 = homework13
        except:
            self.fail("You did not upload a text file called homework13.py!")

    def extract_stories_from_NPR_text(self, webpage_text):
        try:
            stories = self.homework13.extract_stories_from_NPR_text(webpage_text)
            return stories
        except AttributeError:
            self.fail("homework13.py does not have a method called extract_stories_from_NPR_text!")
    
    def read_nth_story(self, stories, n, filename):
        try:
            self.homework13.read_nth_story(stories, n, filename)
        except AttributeError:
            self.fail("homework13.py does not have a method called read_nth_story!")
    
    def assertIsFile(self, path):
        if not pathlib.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_extract_stories_from_NPR_text_exists(self):
        self.import_homework13()
        with open('npr_webpage.html') as f:
            webpage_text = f.read()
        self.extract_stories_from_NPR_text(webpage_text)
        self.assertTrue("homework13.py contains a method called 'extract_stories_from_NPR_text'")
       
    def test_read_nth_story_exists(self):
        self.import_homework13()
        with open('stories.json') as f:
            stories = json.load(f)
        self.read_nth_story(stories, 3, 'test.mp3')
        self.assertTrue("homework13.py contains a method called 'read_nth_story'")
    
