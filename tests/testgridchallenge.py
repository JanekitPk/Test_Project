from codes.gridchallenge import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_give_eabcd_fghij_olkmn_trpqs_xywuv_is_YES(self):
        grid = ['eabcd','fghij','olkmn','trpqs','xywuv']
        expected_result = 'YES'
        result = gridChallenge(grid)
        self.assertEqual(result, expected_result)

    def test_give_abc_lmp_qrt_is_YES(self):
        grid = ['abc', 'lmp', 'qrt']
        expected_result = 'YES'
        result = gridChallenge(grid)
        self.assertEqual(result, expected_result)

    def test_give_mpxz_abcd_wlmf_is_NO(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        expected_result = 'NO'
        result = gridChallenge(grid)
        self.assertEqual(result, expected_result)

    def test_give_abc_hjk_mpq_rtv_is_YES(self):
        grid = ['abc', 'hjk', 'mpq', 'rtv']
        expected_result = 'YES'
        result = gridChallenge(grid)
        self.assertEqual(result, expected_result)

    def test_give_p_is_YES(self):
        grid = ['p']
        expected_result = 'YES'
        result = gridChallenge(grid)
        self.assertEqual(result, expected_result)

    def test_give_rpb_hot_qra_is_NO(self):
        grid = ['rpb', 'hot', 'qra']
        expected_result = 'NO'
        result = gridChallenge(grid)
        self.assertEqual(result, expected_result)