"""
Capstone 72 — Requirement ID & RTM Automated Validator Script
"""

def validate_requirements():
    requirements = ["FR-01", "FR-02", "FR-03", "FR-04", "FR-05", "NFR-01", "NFR-02", "NFR-03"]
    rtm_mappings = {
        "FR-01": "TC-01",
        "FR-02": "TC-02",
        "FR-03": "TC-03",
        "FR-04": "TC-04",
        "FR-05": "TC-05",
        "NFR-01": "TC-06",
        "NFR-02": "TC-07",
        "NFR-03": "TC-08"
    }

    print("=== CAPSTONE 72 VALIDATION SCRIPT ===")
    
    if len(requirements) == len(set(requirements)):
        print(" SUCCESS: All Requirement IDs are unique.")
    else:
        print(" FAILED: Duplicate Requirement IDs detected!")

    unmapped = [req for req in requirements if req not in rtm_mappings]
    if not unmapped:
        print(" SUCCESS: All Requirements are mapped to valid Test Case IDs.")
    else:
        print(f" FAILED: Unmapped Requirements found: {unmapped}")

if __name__ == "__main__":
    validate_requirements()
