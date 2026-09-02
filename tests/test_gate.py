import json, unittest
from src.gate import evaluate

class GateTests(unittest.TestCase):
    def test_prod(self):
        with open("examples/production.json") as f:
            result = evaluate(json.load(f))
        self.assertTrue(result["allowed"])
        self.assertEqual(result["findings"], [])

    def test_unsafe(self):
        with open("examples/unsafe.json") as f:
            result = evaluate(json.load(f))
        self.assertFalse(result["allowed"])
        self.assertGreaterEqual(len(result["findings"]), 60)
