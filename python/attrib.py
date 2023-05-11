import dataclasses
import logging

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


@dataclasses.dataclass
class DictAttrib:
    # class attribute
    name:  str
    # runtime user defined attributes  
    data:  dict = dataclasses.field(default_factory=dict)

    def __str__(self):
        return f'{self.name}| {self.data}'

    def __getattr__(self, name):
        """called when attribute not found after __getattribute__"""
        try:
            # check if in dict
            return self.data[name]
        except KeyError:
            # to avoid nested exception error
            pass
        raise AttributeError(name)


if __name__ == '__main__':
    foo = DictAttrib('foo')
    bar = DictAttrib('bar', data={'bar': 'hello'})
    try:
        logger.info(f'{foo}')
        logger.info(f'{foo.bar}')
    except AttributeError:
        logger.exception('failure')

    try:
        logger.info(f'{bar}')
        logger.info(f'{bar.bar}')
        logger.info(f'{bar.a}')
    except AttributeError:
        logger.exception('failure')
