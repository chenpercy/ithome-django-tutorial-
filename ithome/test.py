def clean_tile(self, *args, **kwargs):
    title = self.cleand_data.get("title")
    if not "CFE" in title:
        return title
