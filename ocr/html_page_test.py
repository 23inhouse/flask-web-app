import unittest
from html_page import HtmlPage

class TestHtmlPage(unittest.TestCase):

    def test_default(self):
        html_page = HtmlPage()
        rendered = html_page.render()
        self.assertEqual(rendered, "<p></p><p><img src=\"\"/></p><p></p>")

    def test_with_content(self):
        html_page = HtmlPage()
        rendered = html_page.render("title", "img_url", "text")
        self.assertEqual(rendered, "<p>title</p><p><img src=\"img_url\"/></p><p>text</p>")

if __name__ == "__main__":
     unittest.main()
