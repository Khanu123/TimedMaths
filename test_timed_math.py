import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("timed math quiz.py")


def load_module():
    spec = importlib.util.spec_from_file_location("timed_math_quiz", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TimedMathTests(unittest.TestCase):
    def test_generate_problem_returns_safe_expression_and_answer(self):
        module = load_module()
        expression, answer = module.generate_problem(3, 3)
        self.assertIn(expression, {"3 + 3", "3 - 3", "3 * 3"})
        self.assertIn(answer, {6, 0, 9})


if __name__ == "__main__":
    unittest.main()
