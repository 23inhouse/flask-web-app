class HtmlPage:

    def render(self, img_url = '', text = ''):
        template = '<p>{}</p><p><img src="{}"/></p><p>{}</p>'
        title = self._title(img_url)
        html = template.format(title, img_url, text)
        return html

    def _title(self, img_url):
        if img_url == '':
            return ''

        return 'Your image url is {}'.format(img_url)
