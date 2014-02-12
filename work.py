# This file is part of the project_waiting module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelView
from trytond.pool import PoolMeta
from trytond.pyson import Eval
__all__ = ['Work']

__metaclass__ = PoolMeta


class Work:
    __name__ = 'project.work'

    @classmethod
    def __setup__(cls):
        super(Work, cls).__setup__()
        value = ('waiting', 'Waiting')
        if not value in cls.state.selection:
            cls.state.selection.append(value)
        cls._buttons.update({
                'wait': {
                    'invisible': Eval('state') != 'opened',
                    },
                })

    @classmethod
    @ModelView.button
    def wait(cls, works):
        for work in works:
            work.state = 'waiting'
            work.save()
