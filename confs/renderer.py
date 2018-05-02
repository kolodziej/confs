import jinja2

class Renderer(object):
    def __init__(self, repo, endpoint):
        self.repo = repo
        self.endpoint = endpoint

        self.loader = jinja2.FileSystemLoader(
            repo.get_path()
        )

        self.env = jinja2.Environment(
            loader=self.loader
        )

    def render(self, src_path, dst_path, context):
        src_path = self.repo.get_file_relpath(src_path)
        template = self.env.get_template(src_path)
        rendered = template.render(context)

        dst_path = self.endpoint.get_file_path(dst_path)
        with open(dst_path, 'w') as f:
            f.write(rendered)
