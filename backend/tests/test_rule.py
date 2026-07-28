from backend.services.rule_engine import evaluate_rules

risk, reasons = evaluate_rules(
    age=60,
    bmi=33,
    glucose=180,
    hba1c=7.2
)

print("Risk:", risk)

print("\nReasons:")

for reason in reasons:
    print("-", reason)