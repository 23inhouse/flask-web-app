import unittest
from ocr import OCR

class TestOCR(unittest.TestCase):

    def test_default(self):
        subject = OCR()
        text = subject.text()
        self.assertEqual(text, "")

    # In a real app this would need to be tested with a local file
    # but that's beyond the scope of this example app
    # something like this: https://github.com/dashea/requests-file
    def test_with_url(self):
        subject = OCR("https://i.stack.imgur.com/vrkIj.png")
        text = subject.text()
        self.assertEqual(text, "lam curious about\narea-filling text\nrendering options")

    def test_with_invalid_url(self):
        subject = OCR("https://not.gunna.work/any.png")
        text = subject.text()
        self.assertEqual(text, "Couldn't process the image")

if __name__ == "__main__":
     unittest.main()
