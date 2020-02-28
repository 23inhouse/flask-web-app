class HtmlPage:

    def render(self, title = '', img_url = '', text = ''):
        template = '<p>{}</p><p><img src="{}"/></p><p>{}</p>'
        html = template.format(title, img_url, text)
        return html
