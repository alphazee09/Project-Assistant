import os
import subprocess


def check_dependencies(project_path):
    os.chdir(project_path)

    # Check for missing dependencies
    print("Checking for missing dependencies...")
    missing_dependencies = subprocess.run(["pip", "check"], capture_output=True, text=True)
    if "No broken requirements found." in missing_dependencies.stdout:
        print("No missing dependencies found.")
    else:
        print("Missing dependencies found:")
        print(missing_dependencies.stdout)

    # Check for outdated dependencies
    print("Checking for outdated dependencies...")
    outdated_dependencies = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True)
    if outdated_dependencies.stdout == "":
        print("All dependencies are up to date.")
    else:
        print("Outdated dependencies found:")
        print(outdated_dependencies.stdout)


def perform_security_scan(project_path):
    os.chdir(project_path)

    # Run static code analysis using SonarQube
    print("Running static code analysis using SonarQube...")
    subprocess.run(["sonar-scanner"])

    # Run dependency check using OWASP Dependency Check
    print("Running dependency check using OWASP Dependency Check...")
    subprocess.run(["dependency-check", "--scan", "."])

    # Run security tests using OWASP ZAP
    print("Running security tests using OWASP ZAP...")
    subprocess.run(["zap-cli", "quick-scan", "--spider", "--ajaxSpider", "--activeScan", "--recursive", "--report",
                    "zap_report.html", "."])


def calculate_code_metrics(project_path):
    os.chdir(project_path)

    # Calculate cyclomatic complexity using radon
    print("Calculating cyclomatic complexity...")
    subprocess.run(["radon", "cc", "."])

    # Calculate code duplication using radon
    print("Calculating code duplication...")
    subprocess.run(["radon", "duplication", "."])

    # Calculate maintainability using radon
    print("Calculating maintainability...")
    subprocess.run(["radon", "mi", "."])


# Example usage
project_path = "path/to/your/project"

check_dependencies(project_path)
perform_security_scan(project_path)
calculate_code_metrics(project_path)