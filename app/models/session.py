class Session:
    def __init__(self, title, description, user_id, created_date, website_url, screen_record_url, webcam_record_url, heatmap_url, callib_url):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.created_date = created_date
        self.website_url = website_url
        self.screen_record_url = screen_record_url
        self.webcam_record_url = webcam_record_url
        self.heatmap_url = heatmap_url
        self.callib_url = callib_url

    def to_dict(self):
        return {
            u'title': self.title,
            u'description': self.description,
            u'user_id': self.user_id,
            u'created_date': self.created_date,
            u'website_url': self.website_url,
            u'screen_record_url': self.screen_record_url,
            u'webcam_record_url': self.webcam_record_url,
            u'heatmap_url': self.heatmap_url,
            u'callib_url': self.callib_url
        }