import numpy as np
import unittest
from pathlib import Path
import sys

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from hurricane_resilience.data import load_event_node_data
from hurricane_resilience.evaluation import weighted_cvar
from hurricane_resilience.scenarios import validate_scenario_weights


class CoreResearchTests(unittest.TestCase):
    def test_event_node_data_loads(self):
        df = load_event_node_data()
        self.assertFalse(df.empty)
        self.assertIn("node_id", df.columns)
        self.assertTrue({"SID", "storm_id"}.intersection(df.columns))

    def test_weighted_cvar_matches_manual_tail_case(self):
        value, eta = weighted_cvar([0.0, 10.0], [0.9, 0.1], alpha=0.9)
        self.assertAlmostEqual(value, 10.0)
        self.assertIn(eta, {0.0, 10.0})

    def test_scenario_weights_are_validated(self):
        self.assertTrue(np.array_equal(validate_scenario_weights([0.25, 0.75]), [0.25, 0.75]))
        with self.assertRaises(ValueError):
            validate_scenario_weights([0.2, 0.7])
        with self.assertRaises(ValueError):
            validate_scenario_weights([1.1, -0.1])


if __name__ == "__main__":
    unittest.main()
