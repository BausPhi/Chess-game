if __name__ == "__main__":
    import unittest
    from tests import test_figures_update_possible_moves
    from tests import test_figures_get_possible_moves
    from tests import test_game_logic
    from tests import test_field_functions

    suite_update_possible_moves = unittest.TestLoader().loadTestsFromModule(test_figures_update_possible_moves)
    suite_game_logic = unittest.TestLoader().loadTestsFromModule(test_game_logic)
    suite_get_possible_moves = unittest.TestLoader().loadTestsFromModule(test_figures_get_possible_moves)
    suite_test_field_functions = unittest.TestLoader().loadTestsFromModule(test_field_functions)
    suite = unittest.TestSuite([suite_update_possible_moves, suite_game_logic, suite_get_possible_moves,
                                suite_test_field_functions])
    unittest.TextTestRunner(verbosity=2).run(suite)
