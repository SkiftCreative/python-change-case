import os
import re

_underscorer1 = re.compile(r'(.)([A-Z][a-z]+)')
_underscorer2 = re.compile('([a-z0-9])([A-Z])')



def _get_camel_parts(subject: str) -> str:
    return ChangeCase.camel_to_snake(subject).split("_")

class ChangeCase(object):
    """
    Converts one type of string casing, to another. Easily convert to and from
    any of these types:
    - camelCase (lower camel case)
    - PascalCase (upper camel case)
    - WikiCase (PascalCase minus 1 letter words)
    - snake_case
    - param-case
    """

    #
    # camelCasing
    #

    @staticmethod
    def camel_to_pascal(subject: str) -> str:
        return subject[0].upper() + subject[1:]

    @staticmethod
    def camel_to_upper_camel(subject: str) -> str:
        result = ChangeCase.camel_to_pascal(subject)
        return result

    @staticmethod
    def camel_to_wiki(subject: str) -> str:
        parts = _get_camel_parts(subject)
        words = [x.title() for x in parts if len(x) > 1]
        return "".join(words)

    @staticmethod
    def camel_to_snake(subject: str) -> str:
        subbed = _underscorer1.sub(r'\1_\2', subject)
        return _underscorer2.sub(r'\1_\2', subbed).lower()

    @staticmethod
    def camel_to_param(subject: str) -> str:
        parts = _get_camel_parts(subject)
        return "-".join(x for x in parts)

    #
    # END camelCasing
    #

    #
    # PascalCasing
    #

    @staticmethod
    def pascal_to_camel(subject: str) -> str:
        return subject[0].lower() + subject[1:]

    @staticmethod
    def pascal_to_upper_camel(subject: str) -> str:
        """
        Really?
        :param subject:
        :return:
        """
        return subject

    @staticmethod
    def pascal_to_wiki(subject: str) -> str:
        parts = _get_camel_parts(subject)
        words = [x.title() for x in parts if len(x) > 1]
        return "".join(words)

    @staticmethod
    def pascal_to_snake(subject: str) -> str:
        return ChangeCase.camel_to_snake(subject)

    @staticmethod
    def pascal_to_param(subject: str) -> str:
        parts = _get_camel_parts(subject)
        return "-".join(x for x in parts)

    #
    # END PascalCasing
    #

    #
    # WikiCasing
    #

    @staticmethod
    def wiki_to_camel(subject: str) -> str:
        return subject[0].lower() + subject[1:]

    @staticmethod
    def wiki_to_upper_camel(subject: str) -> str:
        """
        Really?
        :param subject:
        :return:
        """
        return subject

    @staticmethod
    def wiki_to_pascal(subject: str) -> str:
        return subject

    @staticmethod
    def wiki_to_snake(subject: str) -> str:
        return ChangeCase.camel_to_snake(subject)

    @staticmethod
    def wiki_to_param(subject: str) -> str:
        parts = _get_camel_parts(subject)
        return "-".join(x for x in parts)

    #
    # END WikiCasing
    #

    #
    # snake_casing
    #

    @staticmethod
    def snake_to_camel(subject: str) -> str:
        parts = subject.lower().split('_')
        return parts[0] + "".join(x.title() for x in parts[1:])

    @staticmethod
    def snake_to_pascal(subject: str) -> str:
        parts = subject.lower().split('_')
        return "".join(x.title() for x in parts)

    @staticmethod
    def snake_to_upper_camel(subject: str) -> str:
        return ChangeCase.snake_to_pascal(subject)

    @staticmethod
    def snake_to_wiki(subject: str) -> str:
        parts = subject.lower().split('_')
        wiki = [x.title() for x in parts if len(x) > 1]
        return "".join(x.title() for x in wiki)

    @staticmethod
    def snake_to_param(subject: str) -> str:
        return subject.lower().replace('_', '-')

    #
    # END snake_casing
    #

    #
    # param-casing
    #

    @staticmethod
    def param_to_camel(subject: str) -> str:
        parts = subject.lower().split('-')
        return parts[0] + "".join(x.title() for x in parts[1:])

    @staticmethod
    def param_to_upper_camel(subject: str) -> str:
        return ChangeCase.param_to_pascal(subject)

    @staticmethod
    def param_to_pascal(subject: str) -> str:
        parts = subject.lower().split('-')
        return "".join(x.title() for x in parts)

    @staticmethod
    def param_to_wiki(subject: str) -> str:
        parts = subject.lower().split('-')
        wiki = [x.title() for x in parts if len(x) > 1]
        return "".join(x.title() for x in wiki)

    @staticmethod
    def param_to_snake(subject: str) -> str:
        return subject.lower().replace('-', '_')

    #
    # END param-casing
    #

    #
    # Tests
    #

    @staticmethod
    def run_tests():
        #
        # Camel
        #

        assert ChangeCase.camel_to_upper_camel('snakesOnAPlane') == 'SnakesOnAPlane'
        assert ChangeCase.camel_to_upper_camel('SnakesOnAPlane') == 'SnakesOnAPlane'
        assert ChangeCase.camel_to_upper_camel('IPhoneHysteria') == 'IPhoneHysteria'
        assert ChangeCase.camel_to_upper_camel('iPhoneHysteria') == 'IPhoneHysteria'

        print('camel_to_upper_camel tests passed.')

        assert ChangeCase.camel_to_pascal('snakesOnAPlane') == 'SnakesOnAPlane'
        assert ChangeCase.camel_to_pascal('SnakesOnAPlane') == 'SnakesOnAPlane'
        assert ChangeCase.camel_to_pascal('IPhoneHysteria') == 'IPhoneHysteria'
        assert ChangeCase.camel_to_pascal('iPhoneHysteria') == 'IPhoneHysteria'

        print('camel_to_pascal tests passed.')

        assert ChangeCase.camel_to_wiki('snakesOnAPlane') == 'SnakesOnPlane'
        assert ChangeCase.camel_to_wiki('SnakesOnAPlane') == 'SnakesOnPlane'
        assert ChangeCase.camel_to_wiki('IPhoneHysteria') == 'PhoneHysteria'
        assert ChangeCase.camel_to_wiki('iPhoneHysteria') == 'PhoneHysteria'

        print('camel_to_wiki tests passed.')

        assert ChangeCase.camel_to_snake('snakesOnAPlane') == 'snakes_on_a_plane'
        assert ChangeCase.camel_to_snake('SnakesOnAPlane') == 'snakes_on_a_plane'
        assert ChangeCase.camel_to_snake('IPhoneHysteria') == 'i_phone_hysteria'
        assert ChangeCase.camel_to_snake('iPhoneHysteria') == 'i_phone_hysteria'

        print('camel_to_snake tests passed.')

        assert ChangeCase.camel_to_param('snakesOnAPlane') == 'snakes-on-a-plane'
        assert ChangeCase.camel_to_param('SnakesOnAPlane') == 'snakes-on-a-plane'
        assert ChangeCase.camel_to_param('IPhoneHysteria') == 'i-phone-hysteria'
        assert ChangeCase.camel_to_param('iPhoneHysteria') == 'i-phone-hysteria'

        print('camel_to_param tests passed.')

        #
        # PascalCase
        #

        assert ChangeCase.pascal_to_camel('snakesOnAPlane') == 'snakesOnAPlane'
        assert ChangeCase.pascal_to_camel('SnakesOnAPlane') == 'snakesOnAPlane'
        assert ChangeCase.pascal_to_camel('IPhoneHysteria') == 'iPhoneHysteria'
        assert ChangeCase.pascal_to_camel('iPhoneHysteria') == 'iPhoneHysteria'

        print('pascal_to_camel tests passed.')

        assert ChangeCase.pascal_to_upper_camel('SnakesOnAPlane') == 'SnakesOnAPlane'
        assert ChangeCase.pascal_to_upper_camel('SnakesOnAPlane') == 'SnakesOnAPlane'
        assert ChangeCase.pascal_to_upper_camel('IPhoneHysteria') == 'IPhoneHysteria'
        assert ChangeCase.pascal_to_upper_camel('IPhoneHysteria') == 'IPhoneHysteria'

        print('pascal_to_upper_camel tests passed.')

        assert ChangeCase.pascal_to_wiki('snakesOnAPlane') == 'SnakesOnPlane'
        assert ChangeCase.pascal_to_wiki('SnakesOnAPlane') == 'SnakesOnPlane'
        assert ChangeCase.pascal_to_wiki('IPhoneHysteria') == 'PhoneHysteria'
        assert ChangeCase.pascal_to_wiki('iPhoneHysteria') == 'PhoneHysteria'

        print('pascal_to_wiki tests passed.')

        assert ChangeCase.pascal_to_snake('snakesOnAPlane') == 'snakes_on_a_plane'
        assert ChangeCase.pascal_to_snake('SnakesOnAPlane') == 'snakes_on_a_plane'
        assert ChangeCase.pascal_to_snake('IPhoneHysteria') == 'i_phone_hysteria'
        assert ChangeCase.pascal_to_snake('iPhoneHysteria') == 'i_phone_hysteria'

        print('pascal_to_snake tests passed.')

        assert ChangeCase.pascal_to_param('snakesOnAPlane') == 'snakes-on-a-plane'
        assert ChangeCase.pascal_to_param('SnakesOnAPlane') == 'snakes-on-a-plane'
        assert ChangeCase.pascal_to_param('IPhoneHysteria') == 'i-phone-hysteria'
        assert ChangeCase.pascal_to_param('iPhoneHysteria') == 'i-phone-hysteria'

        print('pascal_to_param tests passed.')

        #
        # WikiCase
        #

        assert ChangeCase.wiki_to_camel('SnakesOnPlane') == 'snakesOnPlane'
        assert ChangeCase.wiki_to_camel('SnakesOnPlane') == 'snakesOnPlane'
        assert ChangeCase.wiki_to_camel('PhoneHysteria') == 'phoneHysteria'
        assert ChangeCase.wiki_to_camel('PhoneHysteria') == 'phoneHysteria'

        print('wiki_to_camel tests passed.')

        assert ChangeCase.wiki_to_upper_camel('SnakesOnPlane') == 'SnakesOnPlane'
        assert ChangeCase.wiki_to_upper_camel('SnakesOnPlane') == 'SnakesOnPlane'
        assert ChangeCase.wiki_to_upper_camel('PhoneHysteria') == 'PhoneHysteria'
        assert ChangeCase.wiki_to_upper_camel('PhoneHysteria') == 'PhoneHysteria'

        print('wiki_to_upper_camel tests passed.')

        assert ChangeCase.wiki_to_pascal('SnakesOnPlane') == 'SnakesOnPlane'
        assert ChangeCase.wiki_to_pascal('SnakesOnPlane') == 'SnakesOnPlane'
        assert ChangeCase.wiki_to_pascal('PhoneHysteria') == 'PhoneHysteria'
        assert ChangeCase.wiki_to_pascal('PhoneHysteria') == 'PhoneHysteria'

        print('wiki_to_pascal tests passed.')

        assert ChangeCase.wiki_to_snake('SnakesOnPlane') == 'snakes_on_plane'
        assert ChangeCase.wiki_to_snake('SnakesOnPlane') == 'snakes_on_plane'
        assert ChangeCase.wiki_to_snake('PhoneHysteria') == 'phone_hysteria'
        assert ChangeCase.wiki_to_snake('PhoneHysteria') == 'phone_hysteria'

        print('wiki_to_snake tests passed.')

        assert ChangeCase.wiki_to_param('SnakesOnAPlane') == 'snakes-on-a-plane'
        assert ChangeCase.wiki_to_param('SnakesOnAPlane') == 'snakes-on-a-plane'
        assert ChangeCase.wiki_to_param('IPhoneHysteria') == 'i-phone-hysteria'
        assert ChangeCase.wiki_to_param('IPhoneHysteria') == 'i-phone-hysteria'

        print('wiki_to_param tests passed.')

        #
        # snake_case
        #

        assert ChangeCase.snake_to_camel('snakes_on_a_plane') == 'snakesOnAPlane'
        assert ChangeCase.snake_to_camel('Snakes_On_A_Plane') == 'snakesOnAPlane'
        assert ChangeCase.snake_to_camel('snakes_On_a_Plane') == 'snakesOnAPlane'
        assert ChangeCase.snake_to_camel('snakes_on_A_plane') == 'snakesOnAPlane'
        assert ChangeCase.snake_to_camel('i_phone_hysteria') == 'iPhoneHysteria'
        assert ChangeCase.snake_to_camel('i_Phone_Hysteria') == 'iPhoneHysteria'

        print('snake_to_camel tests passed.')

        assert ChangeCase.snake_to_upper_camel('snakes_on_a_plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_upper_camel('Snakes_On_A_Plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_upper_camel('snakes_On_a_Plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_upper_camel('snakes_on_A_plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_upper_camel('i_phone_hysteria') == 'IPhoneHysteria'
        assert ChangeCase.snake_to_upper_camel('i_Phone_Hysteria') == 'IPhoneHysteria'

        print('snake_to_upper_camel tests passed.')

        assert ChangeCase.snake_to_pascal('snakes_on_a_plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_pascal('Snakes_On_A_Plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_pascal('snakes_On_a_Plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_pascal('snakes_on_A_plane') == 'SnakesOnAPlane'
        assert ChangeCase.snake_to_pascal('i_phone_hysteria') == 'IPhoneHysteria'
        assert ChangeCase.snake_to_pascal('i_Phone_Hysteria') == 'IPhoneHysteria'

        print('snake_to_pascal tests passed.')

        assert ChangeCase.snake_to_wiki('snakes_on_a_plane') == 'SnakesOnPlane'
        assert ChangeCase.snake_to_wiki('Snakes_On_A_Plane') == 'SnakesOnPlane'
        assert ChangeCase.snake_to_wiki('snakes_On_a_Plane') == 'SnakesOnPlane'
        assert ChangeCase.snake_to_wiki('snakes_on_A_plane') == 'SnakesOnPlane'
        assert ChangeCase.snake_to_wiki('i_phone_hysteria') == 'PhoneHysteria'
        assert ChangeCase.snake_to_wiki('i_Phone_Hysteria') == 'PhoneHysteria'

        print('snake_to_wiki tests passed.')

        assert ChangeCase.snake_to_param('snakes_on_a_plane') == 'snakes-on-a-plane'
        assert ChangeCase.snake_to_param('Snakes_On_A_Plane') == 'snakes-on-a-plane'
        assert ChangeCase.snake_to_param('snakes_On_a_Plane') == 'snakes-on-a-plane'
        assert ChangeCase.snake_to_param('snakes_on_A_plane') == 'snakes-on-a-plane'
        assert ChangeCase.snake_to_param('i_phone_hysteria') == 'i-phone-hysteria'
        assert ChangeCase.snake_to_param('i_Phone_Hysteria') == 'i-phone-hysteria'

        print('snake_to_param tests passed.')

        #
        # param-case
        #

        assert ChangeCase.param_to_camel('snakes-on-a-plane') == 'snakesOnAPlane'
        assert ChangeCase.param_to_camel('Snakes-On-A-Plane') == 'snakesOnAPlane'
        assert ChangeCase.param_to_camel('snakes-On-a-Plane') == 'snakesOnAPlane'
        assert ChangeCase.param_to_camel('snakes-on-A-plane') == 'snakesOnAPlane'
        assert ChangeCase.param_to_camel('i-phone-hysteria') == 'iPhoneHysteria'
        assert ChangeCase.param_to_camel('i-Phone-Hysteria') == 'iPhoneHysteria'

        print('param_to_camel tests passed.')

        assert ChangeCase.param_to_upper_camel('snakes-on-a-plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_upper_camel('Snakes-On-A-Plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_upper_camel('snakes-On-a-Plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_upper_camel('snakes-on-A-plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_upper_camel('i-phone-hysteria') == 'IPhoneHysteria'
        assert ChangeCase.param_to_upper_camel('i-Phone-Hysteria') == 'IPhoneHysteria'

        print('param_to_upper_camel tests passed.')

        assert ChangeCase.param_to_pascal('snakes-on-a-plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_pascal('Snakes-On-A-Plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_pascal('snakes-On-a-Plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_pascal('snakes-on-A-plane') == 'SnakesOnAPlane'
        assert ChangeCase.param_to_pascal('i-phone-hysteria') == 'IPhoneHysteria'
        assert ChangeCase.param_to_pascal('i-Phone-Hysteria') == 'IPhoneHysteria'

        print('param_to_pascal tests passed.')

        assert ChangeCase.param_to_wiki('snakes-on-a-plane') == 'SnakesOnPlane'
        assert ChangeCase.param_to_wiki('Snakes-On-A-Plane') == 'SnakesOnPlane'
        assert ChangeCase.param_to_wiki('snakes-On-a-Plane') == 'SnakesOnPlane'
        assert ChangeCase.param_to_wiki('snakes-on-A-plane') == 'SnakesOnPlane'
        assert ChangeCase.param_to_wiki('i-phone-hysteria') == 'PhoneHysteria'
        assert ChangeCase.param_to_wiki('i-Phone-Hysteria') == 'PhoneHysteria'

        print('param_to_wiki tests passed.')

        assert ChangeCase.param_to_snake('snakes-on-a-plane') == 'snakes_on_a_plane'
        assert ChangeCase.param_to_snake('Snakes-On-A-Plane') == 'snakes_on_a_plane'
        assert ChangeCase.param_to_snake('snakes-On-a-Plane') == 'snakes_on_a_plane'
        assert ChangeCase.param_to_snake('snakes-on-A-plane') == 'snakes_on_a_plane'
        assert ChangeCase.param_to_snake('i-phone-hysteria') == 'i_phone_hysteria'
        assert ChangeCase.param_to_snake('i-Phone-Hysteria') == 'i_phone_hysteria'

        print('param_to_snake tests passed.')

if __name__ == '__main__':
    ChangeCase.run_tests()