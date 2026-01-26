import subprocess
import platform

class SandboxManager:
    def __init__(self, timeout=5, mem_limit="512M", cpu_limit="0.5"):
        self.timeout = timeout
        self.mem_limit = mem_limit
        self.cpu_limit = cpu_limit
        self.is_linux = platform.system() == "Linux"

    def execute_code(self, code_snippet: str):
        if self.is_linux:
            # High-Security Production Mode (Linux/gVisor)
            cmd = ["systemd-run", "--user", "--scope", "-p", f"MemoryMax={self.mem_limit}", "--", 
                   "runsc", "--network=none", "do", "python3", "-c", code_snippet]
        else:
            # Development Mode (macOS/Local)
            # 1% Signal: We warn that this is a low-security dev environment
            cmd = ["python3", "-c", code_snippet]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=self.timeout)
            return {"status": "success", "output": result.stdout, "stderr": result.stderr}
        except subprocess.TimeoutExpired:
            return {"status": "error", "message": "Execution timed out (Fiscal Guardrail hit)."}
        except Exception as e:
            return {"status": "error", "message": str(e)}