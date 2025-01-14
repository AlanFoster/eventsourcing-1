from unittest import skip

from eventsourcing.application.popo import PopoApplication

from eventsourcing.tests.sequenced_item_tests.test_popo_record_manager import PopoTestCase
from eventsourcing.tests.test_process import TestProcessApplication


class TestProcessWithPopos(PopoTestCase, TestProcessApplication):
    process_class = PopoApplication

    @skip("Popo record manager doesn't support pipelines")
    def test_causal_dependencies(self):
        super(TestProcessWithPopos, self).test_causal_dependencies()


del TestProcessApplication
