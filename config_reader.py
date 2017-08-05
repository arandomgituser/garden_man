import ConfigParser


class ConfigReader(object):
    def __init__(self, config_file):
        try:
            self.config_parser = ConfigParser.ConfigParser()
            self.config_parser.read(config_file)
            self.config = self.get_env_config()
            self.config['environment'] = self.get_main_config()['environment']
        except Exception, e:
            print e

    def get_env_config(self):
        try:
            environments = ['DEV', 'TEST', 'PROD']
            config_env = str.upper(self.get_main_config()['environment'])
            return self._get_env_config(config_env)
        except Exception, err:
            print err

    def _get_env_config(self, env):
        return dict(self.config_parser.items(env))

    def get_main_config(self):
        d =  dict(self.config_parser.items('MAIN'))
        if d['environment'] == '':
            d['environment'] = 'DEV'
        return d

c = ConfigReader('settings.ini')
print c.get_env_config()
