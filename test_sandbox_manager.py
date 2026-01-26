import pytest
import platform
import time
from sandbox_manager import SandboxManager

# 1% Signal: Detect environment to apply relevant guardrail tests
is_linux = platform.system() == "Linux"

@pytest.fixture
def manager():
    return SandboxManager(timeout=3, mem_limit="128M", cpu_limit="0.2")

def test_successful_execution(manager):
    """Test 1: Basic logic execution (The 'Golden Path')"""
    code = "print(1 + 1)"
    result = manager.execute_code(code)
    assert result["status"] == "success"
    assert result["output"].strip() == "2"

def test_fiscal_guardrail_timeout(manager):
    """Test 2: Prevention of Infinite Loops (The 'AI Tax' Guardrail)"""
    code = "while True: pass"
    result = manager.execute_code(code)
    
    assert result["status"] == "error"
    # Improved robust check for the timeout message
    assert "timed out" in result["message"].lower()

@pytest.mark.skipif(not is_linux, reason="Isolation requires Linux gVisor/runsc")
def test_security_isolation_filesystem(manager):
    code = "print(open('/etc/passwd').read())"
    result = manager.execute_code(code)
    assert "root:" not in result.get("output", "")

@pytest.mark.skipif(not is_linux, reason="Resource governance requires Linux Cgroups")
def test_resource_governance_oom(manager):
    code = "x = bytearray(200 * 1024 * 1024)" 
    result = manager.execute_code(code)
    assert result["status"] == "error"

@pytest.mark.skipif(not is_linux, reason="Network isolation requires Linux namespaces")
def test_network_isolation(manager):
    code = "import urllib.request; urllib.request.urlopen('http://google.com')"
    result = manager.execute_code(code)
    assert result["status"] == "error"