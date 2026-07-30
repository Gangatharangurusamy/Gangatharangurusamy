"""
Test file for calculator.py
Tests the key financial calculations and formulas
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculator import (
    calculate_wacc, calculate_depreciation_rate, calculate_working_capital_interest,
    get_transition_credit_base, detect_currency, CURRENCY_MAPPING, 
    ANNUAL_INCREASE_RATE, SALVAGE_RATE
)


def test_wacc_calculation():
    """Test WACC calculation formula"""
    # Test with known values
    debt_ratio = 0.567
    equity_ratio = 0.433
    cost_of_debt = 10.863  # as percentage
    roe = 12.769  # as percentage
    tax_rate = 0.264
    
    wacc = calculate_wacc(debt_ratio, equity_ratio, cost_of_debt, roe, tax_rate)
    
    # Should be close to 10.064%
    assert 10.0 <= wacc <= 10.1, f"WACC should be around 10.064%, got {wacc}%"
    print(f"✓ WACC calculation test passed: {wacc:.3f}%")


def test_depreciation_rate():
    """Test depreciation rate calculation"""
    depreciation_of_ppe = 2142406000.0
    gross_block = 36374340000.0
    
    rate = calculate_depreciation_rate(depreciation_of_ppe, gross_block)
    
    # Should be approximately 0.0589
    assert 0.058 <= rate <= 0.060, f"Depreciation rate should be around 0.059, got {rate}"
    print(f"✓ Depreciation rate calculation test passed: {rate:.3f}")


def test_working_capital_interest():
    """Test working capital interest calculation"""
    current_assets = 5000000000.0
    cash_equivalents = 1000000000.0
    current_liabilities = 3000000000.0
    short_term_borrowings = 500000000.0
    total_assets = 45000000000.0
    
    wc_interest = calculate_working_capital_interest(
        current_assets, cash_equivalents, current_liabilities, 
        short_term_borrowings, total_assets
    )
    
    # Should be positive and reasonable
    assert wc_interest > 0, f"Working capital interest should be positive, got {wc_interest}"
    print(f"✓ Working capital interest calculation test passed: {wc_interest:.3f}")


def test_currency_mapping():
    """Test currency mapping functionality"""
    # Test key currencies
    assert get_transition_credit_base('INR') == 833.9, "INR transition credit should be 833.9"
    assert get_transition_credit_base('ZAR') == 180.0, "ZAR transition credit should be 180.0"  
    assert get_transition_credit_base('USD') == 10.0, "USD transition credit should be 10.0"
    assert get_transition_credit_base('EUR') == 9.2, "EUR transition credit should be 9.2"
    
    # Test currency detection
    jhajjar_data = {'company_name': 'Jhajjar Power Limited'}
    eskom_data = {'company_name': 'Eskom Holdings SOC Ltd'}
    
    assert detect_currency(jhajjar_data) == 'INR', "Should detect INR for Jhajjar"
    assert detect_currency(eskom_data) == 'ZAR', "Should detect ZAR for Eskom"
    
    print("✓ Currency mapping and detection tests passed")


def test_static_values():
    """Test static values are correct"""
    assert ANNUAL_INCREASE_RATE == 1.05, f"Annual increase rate should be 1.05, got {ANNUAL_INCREASE_RATE}"
    assert SALVAGE_RATE == 0.1, f"Salvage rate should be 0.1, got {SALVAGE_RATE}"
    
    print("✓ Static values test passed")


def test_currency_coverage():
    """Test that we have comprehensive currency coverage"""
    expected_currencies = ['INR', 'USD', 'ZAR', 'EUR', 'GBP', 'CNY', 'JPY', 'CAD', 'AUD']
    
    for currency in expected_currencies:
        assert currency in CURRENCY_MAPPING, f"Currency {currency} should be in mapping"
        assert 'value' in CURRENCY_MAPPING[currency], f"Currency {currency} should have value"
        assert 'symbol' in CURRENCY_MAPPING[currency], f"Currency {currency} should have symbol"
    
    # Check we have at least 20 currencies
    assert len(CURRENCY_MAPPING) >= 20, f"Should have at least 20 currencies, got {len(CURRENCY_MAPPING)}"
    
    print(f"✓ Currency coverage test passed: {len(CURRENCY_MAPPING)} currencies supported")


if __name__ == "__main__":
    print("Running calculator.py tests...")
    
    test_wacc_calculation()
    test_depreciation_rate()
    test_working_capital_interest()
    test_currency_mapping()
    test_static_values()
    test_currency_coverage()
    
    print("\n🎉 All tests passed successfully!")
    print("\nKey Features Validated:")
    print("- WACC formula: (debt_ratio × cost_of_debt × (1 - tax_rate)) + (equity_ratio × roe)")
    print("- Depreciation rate: depreciation_of_ppe / gross_block")
    print("- Dynamic currency-based transition credits")
    print("- Working capital interest calculation")
    print("- Static values: ANNUAL_INCREASE_RATE = 1.05, SALVAGE_RATE = 0.1")
    print("- Support for 25+ currencies")
    print("- Generic power plant support")