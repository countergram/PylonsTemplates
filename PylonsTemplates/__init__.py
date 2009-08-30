import pylons.configuration
from paste.deploy.converters import asbool
from paste.script.templates import Template, var
from tempita import paste_script_template_renderer

class PylonsRepozeWhat(Template):
    _template_dir = ('PylonsTemplates', 'pylons_repoze_what')
    template_renderer = staticmethod(paste_script_template_renderer)
    summary = 'Pylons application template with SQL-based repoze.what authorization'
    egg_plugins = ['PasteScript', 'Pylons']
    vars = [
        var('template_engine', 'mako/genshi/jinja2/etc: Template language', 
            default='mako'),
    ]
    ensure_names = ['description', 'author', 'author_email', 'url']
    
    def pre(self, command, output_dir, vars):
        """Called before template is applied."""
        package_logger = vars['package']
        if package_logger == 'root':
            # Rename the app logger in the rare case a project is named 'root'
            package_logger = 'app'
        vars['package_logger'] = package_logger

        template_engine = \
            vars.setdefault('template_engine',
                            pylons.configuration.default_template_engine)

        if template_engine == 'mako':
            # Support a Babel extractor default for Mako
            vars['babel_templates_extractor'] = \
                ("('templates/**.mako', 'mako', {'input_encoding': 'utf-8'})"
                 ",\n%s#%s" % (' ' * 4, ' ' * 8))
        else:
            vars['babel_templates_extractor'] = ''

        # Ensure these exist in the namespace
        for name in self.ensure_names:
            vars.setdefault(name, '')

        vars['version'] = vars.get('version', '0.1')
        vars['zip_safe'] = asbool(vars.get('zip_safe', 'false'))
        vars['sqlalchemy'] = True
    