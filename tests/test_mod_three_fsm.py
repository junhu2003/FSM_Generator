import pytest

def test_fsm_modThree_is_fully_trained(fsm_modThree):
    """test fsm modThree is fully trained"""
    assert fsm_modThree.check_coverage()

def test_binary_num_str_1101(mod_three_fsm):
    """test binary num str 1101"""
    binary_num_str = "1101"

    result = mod_three_fsm.mod_by_three(binary_num_str)

    assert result == int(binary_num_str, 2) % 3

def test_binary_num_str_110(mod_three_fsm):
    """test binary num str 110"""
    binary_num_str = "110"

    result = mod_three_fsm.mod_by_three(binary_num_str)

    assert result == int(binary_num_str, 2) % 3    

def test_binary_num_str_1010(mod_three_fsm):
    """test binary num str 1010"""
    binary_num_str = "1010"

    result = mod_three_fsm.mod_by_three(binary_num_str)

    assert result == int(binary_num_str, 2) % 3        

def test_binary_num_str_1111(mod_three_fsm):
    """test binary num str 1111"""
    binary_num_str = "1111"

    result = mod_three_fsm.mod_by_three(binary_num_str)

    assert result == int(binary_num_str, 2) % 3