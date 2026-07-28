def evaluate_rules(age, bmi, glucose, hba1c):
    """
    Evaluate medical rules for diabetes risk.
    Returns:
        risk_level (str)
        reasons (list)
    """

    reasons = []

    if hba1c >= 6.5:
        reasons.append("HbA1c is above the diabetes threshold (≥ 6.5%).")

    if glucose >= 126:
        reasons.append("Blood glucose is above the diabetes threshold (≥ 126 mg/dL).")

    if bmi >= 30:
        reasons.append("BMI indicates obesity (≥ 30).")

    if age >= 45:
        reasons.append("Age is 45 years or older, increasing diabetes risk.")

    # Determine risk level
    if len(reasons) >= 3:
        risk = "High"

    elif len(reasons) == 2:
        risk = "Moderate"

    elif len(reasons) == 1:
        risk = "Low"

    else:
        risk = "Minimal"

    return risk, reasons