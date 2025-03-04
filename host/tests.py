from hypothesis import given
from hypothesis.extra.django import TestCase, from_model
import hypothesis.strategies as st

from host.models import Game, Studio

class TestStudioAddNew(TestCase):

    @given(test_name=st.text())
    def tests_basic_add_studio(self, test_name):
        Studio.objects.create(name=test_name)
        check_item = Studio.objects.get(name=test_name)
        assert check_item.name == test_name

# class TestGameAddNew(TestCase):
#
#     @given(test_studio=from_model(Studio), test_name=st.text())
#     def tests_basic_add_studio(self, test_studio, test_name):
#         Game.objects.create(
#             studio=test_studio,
#             name=test_name,
#         )
#         check_item = Studio.objects.get(name=test_name)
#         assert check_item.name == test_name
