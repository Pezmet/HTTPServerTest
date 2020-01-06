class DisplayPage:
    def __init__(self, body='server is running', title='http server'):
        self.title = title
        self.body = body

    @staticmethod
    def startPageHtml():
        return bytes('<html>', 'UTF-8')

    @staticmethod
    def startPageHead():
        return bytes('<head>', 'UTF-8')

    def setPageTitle(self):
        return bytes(f'<title> {self.title} </title>', 'UTF-8')

    @staticmethod
    def endPageHead():
        return bytes('</head>', 'UTF-8')

    def setPageBody(self):
        return bytes(f'<body> {self.body} </body>', 'UTF-8')

    @staticmethod
    def endPageHtml():
        return bytes('</html>', 'UTF-8')

    def setBodyMessageNotificationCount(self, notification_count='value N/A'):
        self.body = (f'The total number of received notifications is: '
                     f'{notification_count}')
