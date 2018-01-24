import sys
from flask_script import Shell, Manager, Server
from core import create_app

CONFIG_NAME = "develop"  # 先默认develop


def main():
    app = create_app(CONFIG_NAME)
    manager = Manager(app)

    def make_shell_context():
        """Run Python Shell"""
        return dict(app=app)

    manager.add_command('shell', Shell(make_context=make_shell_context))
    manager.add_command('runserver', Server(host='0.0.0.0', port=5000))

    @manager.command
    def test():
        """
        Run unittest.
        """
        pass

    return manager


if __name__ == '__main__':
    args = sys.argv
    manager = main()

    if manager:
        manager.run()
