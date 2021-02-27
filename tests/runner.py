if __name__ == "__main__":
    import unittest
    from tests import test_figures_update_possible_moves
    from tests import test_game_logic

    suite_possible_moves = unittest.TestLoader().loadTestsFromModule(test_figures_update_possible_moves)
    suite_game_logic = unittest.TestLoader().loadTestsFromModule(test_game_logic)
    suite = unittest.TestSuite([suite_possible_moves, suite_game_logic])
    unittest.TextTestRunner(verbosity=2).run(suite)